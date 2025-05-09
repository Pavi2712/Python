class TestData:
    BASE_URL = "https://reqres.in/api"

    class Credentials:
        EMAIL = "eve.holt@reqres.in"
        PASSWORD = "pistol"

    class Endpoints:
        LOGIN = "https://reqres.in/api/login"
        LIST_USERS = "https://reqres.in/api/users?page=2"
        SINGLE_USER = "https://reqres.in/api/users/2"
        SINGLE_USER_NOT_FOUND = "https://reqres.in/api/users/23"
