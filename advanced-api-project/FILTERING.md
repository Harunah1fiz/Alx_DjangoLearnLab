
## Filtering, Searching, and Ordering in Book API

The `BookListView` supports **filtering**, **searching**, and **ordering** using
Django REST Framework’s `DjangoFilterBackend`, `SearchFilter`, and `OrderingFilter`.

### 1. Filtering
Filtering allows clients to retrieve books based on exact field values.
We enabled filtering on the following fields:

- `title`
- `author`
- `publication_year`

#### Example requests:
GET /api/books/?title=Django for Beginners
GET /api/books/?author=3
GET /api/books/?publication_year=2022

> Note: `author` is a foreign key, so filtering here uses the author’s ID.
If you want to filter by author name, use search (see below).

---

### 2. Searching
Searching allows case-insensitive, partial matches across text fields.
We enabled search on:

- `title`
- `author__name` (author’s name instead of ID)

#### Example requests:
GET /api/books/?search=django
GET /api/books/?search=john


This will return any books where the title contains "django" or the author’s name contains "john".

---

### 3. Ordering
Ordering allows clients to sort results by specific fields.
We enabled ordering on:

- `title`
- `publication_year`

#### Example requests:
GET /api/books/?ordering=title
GET /api/books/?ordering=-publication_year



- Prefix with `-` for descending order (e.g., newest books first).

---

### Summary
- **Filtering** → exact match (`?field=value`)  
- **Searching** → partial match, case-insensitive (`?search=query`)  
- **Ordering** → sort ascending or descending (`?ordering=field` or `?ordering=-field`)  

All three features are combined in `BookListView`, so you can mix them:
