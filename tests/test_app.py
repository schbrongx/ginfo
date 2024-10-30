import unittest
from unittest.mock import patch, MagicMock
from app.app import app  # Importiere die Flask-App

class AppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Starte den Test-Client
        cls.client = app.test_client()
        cls.client.testing = True

    @patch('app.app.connect_db')
    def test_add_location(self, mock_connect_db):
        # Mock die Datenbankverbindung und das Cursor-Verhalten
        mock_conn = MagicMock()
        mock_connect_db.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value

        # Beispiel-JSON-Daten für den POST-Request
        data = {
            "name": "Test Location",
            "geom": "POINT(10 10)"
        }
        response = self.client.post('/locations', json=data)

        # Tests
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"message": "Location added!"})
        mock_cursor.execute.assert_called_once()  # Sicherstellen, dass ein Datenbank-Insert ausgeführt wurde

    @patch('app.app.connect_db')
    def test_get_locations(self, mock_connect_db):
        # Mock die Datenbankverbindung und Cursor
        mock_conn = MagicMock()
        mock_connect_db.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value

        # Definiere Rückgabewerte des Mock-Cursors
        mock_cursor.fetchall.return_value = [("Test Location", "POINT(10 10)")]

        # GET-Request
        response = self.client.get('/locations')

        # Tests
        self.assertEqual(response.status_code, 200)
        mock_cursor.execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()

