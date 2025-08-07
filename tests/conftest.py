# tests/conftest.py
import pytest
from app import app
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app.config['TESTING'] = True

    # Patch mysql.connection.cursor to mock DB calls
    with patch('app.mysql') as mock_mysql:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        
        mock_conn.cursor.return_value = mock_cursor
        mock_mysql.connection = mock_conn

        with app.test_client() as client:
            yield client
