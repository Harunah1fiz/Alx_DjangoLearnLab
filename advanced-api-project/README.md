# Book API Views Documentation

This project uses Django REST Framework's **generic class-based views** to implement CRUD operations for the `Book` model.

---

## View Configurations

### 1. `BookListView`
- **Purpose**: Retrieve all books
- **Endpoint**: `GET /books/`
- **Permissions**: Public (no authentication required)
- **Notes**: Returns a serialized list of all books in the database.

---

### 2. `BookDetailView`
- **Purpose**: Retrieve a single book by ID
- **Endpoint**: `GET /books/<id>/`
- **Permissions**: Public
- **Notes**: Raises 404 if the book does not exist.

---

### 3. `BookCreateView`
- **Purpose**: Add a new book
- **Endpoint**: `POST /books/`
- **Permissions**: `IsAuthenticated` (only logged-in users can create)
- **Hooks**:
  - `perform_create(self, serializer)`:
    - Custom save logic.
    - Currently just calls `serializer.save()`.
    - Can be extended to attach the request user or perform additional validation.

---

### 4. `BookUpdateView`
- **Purpose**: Update an existing book
- **Endpoint**: `PUT/PATCH /books/<id>/`
- **Permissions**: `IsAuthenticated`
- **Hooks**:
  - `perform_update(self, serializer)`:
    - Custom save logic.
    - Currently just calls `serializer.save()`.

---

### 5. `BookDeleteView`
- **Purpose**: Delete an existing book
- **Endpoint**: `DELETE /books/<id>/`
- **Permissions**: `IsAuthenticated`

---

## Custom Settings & Hooks

- **Permissions**:
  - `BookListView` and `BookDetailView` are public.
  - Create, Update, Delete require authentication.
- **Hooks**:
  - `perform_create` and `perform_update` allow injecting custom logic into save operations.
  - Currently minimal, but can be extended.

---

## Example Usage (with Token Authentication)

1. **Obtain a token**:
   ```bash
   POST /api/token/
   {
     "username": "user",
     "password": "pass"
   }
