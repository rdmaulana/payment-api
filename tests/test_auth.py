import json

def test_register_user(test_client):
    response = test_client.post(
        '/api/v1/auth/register',
        content_type='application/json',
        data = json.dumps(
            dict(
                first_name = 'Adrian',
                last_name = 'Arnold',
                phone_number = '087770135953',
                address = 'Jl. Tebet Raya No. 777',
                pin = "123456"
            )
        )
    )
    data = json.loads(response.data)

    assert response.content_type == 'application/json'
    assert response.status_code == 200
    assert data['status'] == 'SUCCESS'
    assert data['result']['first_name'] == 'Adrian'
    assert data['result']['last_name'] == 'Arnold'
    assert data['result']['phone_number'] == '087770135953'
    assert data['result']['address'] == 'Jl. Tebet Raya No. 777'

def test_register_phone_number_already_exist(test_client):
    response = test_client.post(
        '/api/v1/auth/register',
        content_type='application/json',
        data = json.dumps(
            dict(
                first_name = 'Adrian',
                last_name = 'Arnold',
                phone_number = '087770135953',
                address = 'Jl. Tebet Raya No. 777',
                pin = "123456"
            )
        )
    )
    data = json.loads(response.data)

    assert response.content_type == 'application/json'
    assert response.status_code == 400
    assert data['message'] == 'Phone number already registered'

def test_login(test_client):
    response = test_client.post(
        '/api/v1/auth/login',
        content_type='application/json',
        data = json.dumps(
            dict(
                phone_number = '087770135953',
                pin = "123456"
            )
        )
    )
    data = json.loads(response.data.decode())

    assert response.content_type == 'application/json'
    assert response.status_code == 200
    
    assert data['status'] == 'SUCCESS'
    assert data['result']['access_token']
    assert data['result']['refresh_token']

