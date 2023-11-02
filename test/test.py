import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import sys
import os
import json

src_dir = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.append(src_dir)

from main import Main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main()
        self.main._hub_connection = MagicMock()

    def test_take_action_turn_on_ac(self):
        # Test when the temperature is greater than or equal to T_MAX
        temperature = 11
        date = "2023-01-01"
        self.main.T_MAX = 10
        self.main.send_action_to_hvac = MagicMock()
        self.main.take_action(temperature, date)
        self.main.send_action_to_hvac.assert_called_with("TurnOnAc", date)

    def test_take_action_turn_on_heater(self):
        # Test when the temperature is less than or equal to T_MIN
        temperature = -1
        date = "2023-01-01"
        self.main.T_MIN = 0
        self.main.send_action_to_hvac = MagicMock()
        self.main.take_action(temperature, date)
        self.main.send_action_to_hvac.assert_called_with("TurnOnHeater", date)

    def test_take_action_do_nothing(self):
        # Test when the temperature is within the range [T_MIN, T_MAX]
        temperature = 5
        date = "2023-01-01"
        self.main.T_MIN = 0
        self.main.T_MAX = 10
        self.main.send_action_to_hvac = MagicMock()
        self.main.take_action(temperature, date)
        self.main.send_action_to_hvac.assert_not_called()

    @patch("requests.get")
    def test_send_action_to_hvac(self, mock_requests_get):
        action = "TurnOnAc"
        date = "2023-01-01"
        response_data = {"status": "success"}
        mock_response = MagicMock()
        mock_response.text = json.dumps(response_data)
        mock_requests_get.return_value = mock_response
        self.main.send_event_to_database = MagicMock()

        self.main.send_action_to_hvac(action, date)

        self.main.send_event_to_database.assert_called_with(action, date)
        mock_requests_get.assert_called_with(
            f"{self.main.HOST}/api/hvac/{self.main.TOKEN}/{action}/{self.main.TICKETS}"
        )

    @patch("psycopg2.connect")
    def test_send_temperature_to_database(self, mock_psycopg2_connect):
        temperature = 5
        date = "2023-01-01"
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_psycopg2_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        self.main.send_temperature_to_database(temperature, date)

        mock_psycopg2_connect.assert_called_with(**self.main.DATABASE)
        mock_cursor.execute.assert_called_with(
            "INSERT INTO Temperatures (temperature, time) VALUES (%s, %s);",
            (temperature, date),
        )
        mock_conn.commit.assert_called()
        mock_cursor.close.assert_called()
        mock_conn.close.assert_called()

    @patch("psycopg2.connect")
    def test_send_event_to_database(self, mock_psycopg2_connect):
        action = "TurnOnAc"
        date = "2023-01-01"
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_psycopg2_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        self.main.send_event_to_database(action, date)

        mock_psycopg2_connect.assert_called_with(**self.main.DATABASE)
        mock_cursor.execute.assert_called_with(
            "INSERT INTO Evenements (action, time) VALUES (%s, %s);", (action, date)
        )
        mock_conn.commit.assert_called()
        mock_cursor.close.assert_called()
        mock_conn.close.assert_called()


if __name__ == "__main__":
    unittest.main()
