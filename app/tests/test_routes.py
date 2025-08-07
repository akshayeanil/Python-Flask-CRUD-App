def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mock Student" in response.data

def test_insert_route(client):
    response = client.post('/insert', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '1234567890'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Data Inserted Successfully!" in response.data

def test_update_route(client):
    response = client.post('/update', data={
        'id': '1',
        'name': 'Updated Name',
        'email': 'updated@example.com',
        'phone': '0000000000'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Data Updated Successfully" in response.data

def test_delete_route(client):
    response = client.get('/delete/1', follow_redirects=True)
    assert response.status_code == 200
    assert b"Data Deleted Successfully" in response.data
