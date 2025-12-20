# DRF Authentication & Permissions — Cheat Sheet

## Authentication (Who are you?)

| Type            | Credentials            | Stateless | Use Case     | Notes               |
| --------------- | ---------------------- | --------- | ------------ | ------------------- |
| **BasicAuth**   | Username + Password    | ❌         | Testing      | Use only with HTTPS |
| **SessionAuth** | Session Cookie         | ❌         | Browsers     | Requires CSRF       |
| **TokenAuth**   | Token                  | ✅         | Mobile / API | One token per user  |
| **JWTAuth**     | Access / Refresh Token | ✅         | Modern APIs  | Scalable, fast      |

---

### Authentication Headers

```
Basic  <base64(username:password)>
Token  <token>
Bearer <jwt_token>
```

---

## Permissions (What can you do?)

| Permission                    | Read | Write | Who                     |
| ----------------------------- | ---- | ----- | ----------------------- |
| **AllowAny**                  | ✅    | ✅     | Everyone                |
| **IsAuthenticated**           | ✅    | ✅     | Logged-in users         |
| **IsAdminUser**               | ✅    | ✅     | Staff users             |
| **IsAuthenticatedOrReadOnly** | ✅    | ❌     | Public read, auth write |

---

## Common Permission Use Cases

| Endpoint        | Permission                |
| --------------- | ------------------------- |
| Login / Signup  | AllowAny                  |
| User Profile    | IsAuthenticated           |
| Admin Dashboard | IsAdminUser               |
| Blog / Products | IsAuthenticatedOrReadOnly |

---

## Settings.py (Quick Setup)

### Authentication

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

### Permissions

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

---

## View-Level Override

```python
from rest_framework.permissions import AllowAny

class PublicView(APIView):
    permission_classes = [AllowAny]
```

---

## Order of Execution

```
Request
   ↓
Authentication
   ↓
Permissions
   ↓
View Logic
```

---

## Quick Rules to Remember

* ❗ Authentication runs **before** permissions
* ❗ Permissions don’t identify users
* ❗ JWT ≠ built-in (needs extra package)
* ❗ SessionAuth needs CSRF

---

## One-Line Memory Hook

> **Auth proves identity, permissions grant authority.**