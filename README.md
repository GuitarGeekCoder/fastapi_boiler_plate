# fastapi_boiler_plate

## curls for the api's
```
curl -X 'POST'  'http://127.0.0.1:8000/users/create/'    -H 'Content-Type: application/json'   -d '{ "name": "John2 Doe", "email": "johndoe2@example.com"}'

curl -X 'GET'   'http://127.0.0.1:8000/users/get/3'

curl -X 'GET'   'http://127.0.0.1:8000/users/get_all/'

curl -X 'POST'  'http://127.0.0.1:8000/org/create/'      -H 'Content-Type: application/json'   -d '{ "name": "John_org", "user_id": 1}'

curl -X 'PATCH' 'http://127.0.0.1:8000/org/update/2'     -H 'Content-Type: application/json'   -d '{ "name": "John_org1" }'

curl -X 'GET'   'http://127.0.0.1:8000/users/get/3'

curl -X DELETE  'http://localhost:8000/org/delete/1'
```