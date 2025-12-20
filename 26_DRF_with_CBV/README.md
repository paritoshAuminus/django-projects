# CRUD with APIView

- `@api_view` already works with function based views (FBVs)
- There are issues

### Difference between FBV and CBV as we use `@api_view` and `APIView`

| Feature        | Function-Based View `(@api_view)`        | Class-Based View `(APIView)`                  |
|---------------|----------------------------------------|---------------------------------------------|
| Style         | Working with functions                    | Working with classes                           |
| Reusability   | Code repeat hota hai                   | DRY (Don't Repeat Yourself)                 |
| Flexibility   | Perfect for smaller api            | Better for large projects                |
| Extensibility | Must write custom logic manually | Built-in methods like `get()`, `post()`, `put()`, `delete()` are available |
| Inheritance   | Not possible                           | APIView / GenericAPIView can be inherited |
| Readability   | Simple but messy when CRUD grows       | Clean and structured code                  |

<br/>

# `GenericAPIView` + `Mixins`

In **Django REST Framework (DRF)**, both `APIView` and `GenericAPIView` are base classes for building API views, but they serve different levels of abstraction and convenience.

---

## 1. `APIView` (low-level, explicit)

`APIView` is the **foundation** of DRF’s class-based views. It gives you:

* Request parsing (`request.data`)
* Response handling (`Response`)
* Authentication, permissions, throttling
* Method-based handlers (`get`, `post`, `put`, etc.)

### Key characteristics

* You **manually implement all logic**
* No built-in support for:

  * Querysets
  * Serializers
  * Object lookup
  * Pagination
  * Filtering

### Example

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

👉 **You control everything**, but you repeat common patterns often.

---

## 2. `GenericAPIView` (higher-level, reusable)

`GenericAPIView` **extends `APIView`** and adds common behavior for working with models and serializers.

### What `GenericAPIView` adds

* `queryset`
* `serializer_class`
* `get_queryset()`
* `get_serializer()`
* `get_object()`
* Pagination support
* Filtering support

It still **does not implement HTTP methods** itself—you combine it with *mixins*.

---

## 3. GenericAPIView + Mixins (the real power)

DRF provides mixins that implement common CRUD actions:

| Mixin                | Provides     |
| -------------------- | ------------ |
| `ListModelMixin`     | `list()`     |
| `CreateModelMixin`   | `create()`   |
| `RetrieveModelMixin` | `retrieve()` |
| `UpdateModelMixin`   | `update()`   |
| `DestroyModelMixin`  | `destroy()`  |

### Example

```python
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(ListModelMixin,
                            CreateModelMixin,
                            GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

👉 Less boilerplate, standardized behavior.

---

## 4. How `GenericAPIView` differs from `APIView`

| Aspect              | APIView   | GenericAPIView          |
| ------------------- | --------- | ----------------------- |
| Level               | Low-level | Higher-level            |
| Model awareness     | ❌ None    | ✅ Yes                   |
| Serializer handling | Manual    | Automatic helpers       |
| Object lookup       | Manual    | Built-in (`get_object`) |
| Pagination          | ❌ Manual  | ✅ Built-in              |
| Filtering           | ❌ Manual  | ✅ Built-in              |
| Mixins support      | ❌         | ✅                       |

---

## 5. Where `GenericAPIView` fits in DRF’s hierarchy

```
APIView
   ↑
GenericAPIView
   ↑
Concrete generic views (ListAPIView, CreateAPIView, etc.)
```

Examples of **concrete generic views**:

* `ListAPIView`
* `CreateAPIView`
* `RetrieveAPIView`
* `RetrieveUpdateDestroyAPIView`

These are just **`GenericAPIView + mixins` pre-wired**.

---

## 6. When to use which?

### Use `APIView` when:

* Logic is highly custom
* You don’t want model/serializer coupling
* You need full control over request handling

### Use `GenericAPIView` when:

* You’re building standard CRUD endpoints
* You want pagination, filtering, serializers “for free”
* You want clean, DRY code

---

### Summary in one sentence

> **`APIView` is a blank canvas; `GenericAPIView` is a canvas with model- and serializer-aware tools ready to use.**

---

<br/>

# `Viewsets`

With `APIView` / `GenericAPIView`, you still:

* Write separate classes for list, detail, create, update, delete
* Manually map HTTP methods in `urls.py`

**ViewSets solve this by grouping related actions into a single class** and letting routers generate URLs automatically.

---

## 2. `APIView` / `GenericAPIView` vs `ViewSet`

### Conceptual shift

* **APIView** → *one view = one URL pattern*
* **ViewSet** → *one view = a set of related URLs/actions*

---

## 3. `ViewSet` (method-based, no queryset magic)

`ViewSet` is similar to `APIView`, but:

* Uses **actions** instead of HTTP methods
* Still **no queryset/serializer automation**

### Actions instead of methods

| Action           | Typical HTTP          |
| ---------------- | --------------------- |
| `list`           | GET /objects/         |
| `retrieve`       | GET /objects/{id}/    |
| `create`         | POST /objects/        |
| `update`         | PUT /objects/{id}/    |
| `partial_update` | PATCH /objects/{id}/  |
| `destroy`        | DELETE /objects/{id}/ |

### Example

```python
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ViewSet):
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
```

👉 You still write all logic manually.

---

## 4. `GenericViewSet` (GenericAPIView + ViewSet)

`GenericViewSet`:

* Extends **`GenericAPIView`**
* Adds ViewSet behavior (actions)
* Supports mixins

This is the **real workhorse** behind most DRF APIs.

### What it provides

* `queryset`
* `serializer_class`
* `get_object()`
* Pagination, filtering
* Action-based routing

---

## 5. `GenericViewSet` + Mixins

Same mixins as before, but now mapped to **actions automatically**.

### Example

```python
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, RetrieveModelMixin
)
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ListModelMixin,
                   CreateModelMixin,
                   RetrieveModelMixin,
                   GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

👉 No HTTP method mapping. Router handles it.

---

## 6. `ModelViewSet` (maximum convenience)

`ModelViewSet` is:

```
GenericViewSet + all CRUD mixins
```

### Provides

* `list`
* `retrieve`
* `create`
* `update`
* `partial_update`
* `destroy`

### Example

```python
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

This single class replaces:

* `ListAPIView`
* `CreateAPIView`
* `RetrieveAPIView`
* `UpdateAPIView`
* `DestroyAPIView`

---

## 7. Routers (automatic URL wiring)

Routers **generate URL patterns** for ViewSets.

### Without router (APIView style)

```python
urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
]
```

### With router

```python
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls
```

### Router-generated URLs

```
GET     /books/           → list
POST    /books/           → create
GET     /books/{id}/      → retrieve
PUT     /books/{id}/      → update
PATCH   /books/{id}/      → partial_update
DELETE  /books/{id}/      → destroy
```

---

## 8. Custom actions with `@action`

Add non-CRUD endpoints easily.

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        book = self.get_object()
        book.publish()
        return Response({'status': 'published'})
```

Creates:

```
POST /books/{id}/publish/
```

---

## 9. ViewSets vs GenericAPIView (summary table)

| Feature                | GenericAPIView       | ViewSet           |
| ---------------------- | -------------------- | ----------------- |
| One class per URL      | ✅                    | ❌                 |
| Groups related actions | ❌                    | ✅                 |
| Router support         | ❌                    | ✅                 |
| CRUD boilerplate       | Medium               | Very low          |
| Best for               | Fine-grained control | RESTful resources |

---

## 10. When to use what?

### Use `APIView`

* Highly custom logic
* Non-resource-based endpoints

### Use `GenericAPIView`

* Simple CRUD, but want explicit URLs

### Use `ViewSet` / `ModelViewSet`

* Resource-oriented APIs
* Clean URLs
* Less boilerplate
* Standard REST behavior

---

### One-sentence summary

> **ViewSets define *what* actions exist; routers decide *where* and *how* they’re exposed via URLs.**