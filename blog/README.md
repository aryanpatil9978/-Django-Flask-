# REST API Blog

This project now exposes a user profiles API built with Django REST Framework.

## Endpoints

- `GET /api/users/` - list user profiles
- `POST /api/users/` - create a user profile
- `GET /api/users/<id>/` - retrieve a user profile
- `PUT /api/users/<id>/` - replace a user profile
- `PATCH /api/users/<id>/` - partially update a user profile
- `DELETE /api/users/<id>/` - delete a user profile

## User Payload

```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "bio": "Short profile bio"
}
```

## How to Run

1. Create and activate a virtual environment.
2. Install the required packages:

```bash
pip install django djangorestframework
```

3. Run migrations:

```bash
python manage.py migrate
```

If you change the model later, run `python manage.py makemigrations users` before `migrate`.

4. Start the server:

```bash
python manage.py runserver
```

## Database Notes

This version uses a new `users` app and a custom `User` profile table, so the database must be migrated at least once before using the API. If you are starting from a fresh SQLite database, the `migrate` step is enough. No manual schema editing is needed.

login credential:
username: USER1
password: userlogin