
---

## 📄 `CRUD_operations.md`

```markdown
# Full CRUD Operations Summary

## Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
