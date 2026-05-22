# FastAPI Todo App

## Opis projektu

Aplikacja REST API do zarządzania zadaniami Todo napisana w FastAPI.

Projekt zawiera:
- autoryzację JWT,
- role USER / ADMIN,
- CRUD Todo,
- architekturę warstwową,
- walidację danych,
- obsługę błędów,
- eventy,
- testy jednostkowe.

Administrator może moderować todo użytkowników i usuwać nieodpowiednie wpisy.

---

# Technologie

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Passlib + bcrypt
- Pydantic
- Pytest

---

# Architektura projektu

Projekt został zbudowany zgodnie z architekturą warstwową:

```text
Controller → Service → Repository → Database
```

## Struktura projektu

```text
app/
├── controllers/
├── services/
├── repositories/
├── models/
├── schemas/
├── core/
├── events/
├── tests/
├── database.py
├── seed.py
└── main.py
```

---

# Funkcjonalności

## Authentication
- rejestracja użytkownika,
- logowanie JWT,
- zabezpieczenie endpointów tokenem Bearer.

## Todo CRUD
- tworzenie todo,
- pobieranie todo,
- edycja todo,
- usuwanie todo.

## Role USER / ADMIN

### USER
- widzi tylko swoje todo,
- może tworzyć, edytować i usuwać swoje todo.

### ADMIN
- widzi wszystkie todo,
- może usuwać dowolne todo użytkowników.

## Eventy

Po usunięciu todo przez administratora wywoływany jest event:

```text
[EVENT] Admin {admin_id} deleted todo {todo_id}
```

---

# Instalacja projektu

## Virtualenv

```bash
python -m venv venv
```

## Aktywacja virtualenv

```powershell
.\venv\Scripts\Activate
```

## Instalacja zależności

```bash
pip install -r requirements.txt
```

## Uruchomienie aplikacji

```bash
python -m uvicorn app.main:app --reload
```

---

# Swagger

```text
http://127.0.0.1:8000/docs
```

---

# Testy

```bash
python -m pytest
```

---

# Domyślny administrator

```text
email: admin@test.com
password: admin123
```

---

# Endpointy API

## AUTH

```text
POST /auth/register
POST /auth/login
```

## TODOS

```text
GET /todos/
POST /todos/
GET /todos/{todo_id}
PUT /todos/{todo_id}
DELETE /todos/{todo_id}
```

## ADMIN

```text
GET /admin/todos
DELETE /admin/todos/{todo_id}
```
