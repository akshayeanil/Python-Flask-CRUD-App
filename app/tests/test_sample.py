# tests/test_sample.py

def test_homepage(client):
    """Test the homepage loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Student" in response.data  # Adjust based on your HTML content


def test_insert_route(client):
    """Test the insert route (mock data)."""
    response = client.post('/insert', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '1234567890'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Data Inserted Successfully!" in response.data


def test_update_route(client):
    """Mock update test (won’t really change anything without DB)"""
    response = client.post('/update', data={
        'id': '1',
        'name': 'Updated Name',
        'email': 'updated@example.com',
        'phone': '0000000000'
    }, follow_redirects=True)

    # This won't do real DB update unless record exists
    assert response.status_code == 200
    assert b"Data Updated Successfully" in response.data


def test_delete_route(client):
    """Mock delete test (won’t really delete without real ID)"""
    response = client.get('/delete/1', follow_redirects=True)
    assert response.status_code == 200
    assert b"Data Deleted Successfully" in response.data
