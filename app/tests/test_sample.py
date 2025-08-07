from unittest.mock import patch, MagicMock
from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def mock_mysql():
    with patch('app.mysql') as mock_mysql:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        # Set up cursor behavior for SELECT * FROM students
        mock_cursor.fetchall.return_value = [(1, "Mock Student", "mock@example.com", "1234567890")]
        mock_conn.cursor.return_value = mock_cursor
        mock_mysql.connection = mock_conn
        yield
