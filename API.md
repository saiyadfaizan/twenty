# **APIs Details:**

**Base URL for all API endpoints : http://127.0.0.1:8000/api/**

Following API endpoints available in api app.

1. ## View all products:
   This API will list the data of all the products stored in the database. This API will be accessed by administrator/super users only.
   To hit this API, first login through: http://127.0.0.1:8000/admin-login/
    ```Json
    Methods: GET, HEAD, OPTIONS
    Endpoint: api/rest/product/
    Response:
    code: 200 OK
    data:
    [{
        "id": 5,
        "name": "The Alchemist",
        "price": 249.0,
        "description": "Novel by Paul Coelho",
        "digital": false,
        "image": "http://127.0.0.1:8000/images/alchemist.jpg",
        "category": 3
    }
    .
    .
    ]
    ```
2. ## Orders list:
    This API will return list of all the orders stored in the database.

    ```Json
    Methods: GET, HEAD, OPTIONS
    Endpoint: /api/rest/order/
    Response:
    code: 200 OK
    data:
    [{
        "id": 60,
        "emailAddress": "saliali@bestpeers.com",
        "date_ordered": "2021-01-11T10:41:05.612940Z",
        "complete": true,
        "transaction_id": "1610365589.97189",
        "status": "Order Processing",
        "customer": 1
    }
    .
    .
    ]
    ```

3. ## Admin-detail: 
   This API will return admin detail.

    ```Json
    Methods: GET, HEAD, OPTIONS
    Endpoint: /api/rest-auth/user/
    Success Response:
    code: 200 OK
    data:
    {
        "pk": 4,
        "username": "user1",
        "email": "user1@gmail.com",
        "first_name": "User",
        "last_name": "1"
    }
    Failure Response:  
    "detail": "Authentication credentials were not provided."
    ```