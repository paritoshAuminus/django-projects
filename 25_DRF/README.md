Here is your **same notes file**, with **only important additions**, keeping your **writing style, structure, and tone intact**.
I have **not rewritten anything**, only extended it where it naturally fits.

---

# DRF (Django Rest Framework)

*REST* stands for **Representation state transfer**, its a standard way of transferring data between client ⇌ server (client ⇌ database). DRF helps us create a **REST API** within our django application

### Program flow

> Database ⇌ Serializer (JSON ⇌ DB data) ⇌ View (Transfer api data) ⇌ Frontend (Consume data)

### Serializer

A serializer is responsible for:

* converting **database/model data → JSON** (for sending data to frontend)
* converting **incoming JSON data → python data → database objects**
* validating incoming data before it is saved in the database

In DRF, `ModelSerializer` automatically:

* reads model fields and their types
* applies model constraints (required fields, max_length, data types)
* generates default validation rules

### Validation (`is_valid()`)

When data is sent from frontend to backend, it is passed to serializer using:

```
StudentSerializer(data=request.data)
```

Calling `is_valid()`:

* checks if all required fields are present
* checks field data types (e.g. IntegerField, CharField)
* checks model constraints like `max_length`
* runs any custom validation methods if defined

If validation fails:

* `serializer.is_valid()` returns `False`
* validation errors are stored in `serializer.errors`

If validation passes:

* validated and cleaned data is stored in `serializer.validated_data`

### Saving data (`save()`)

After successful validation, calling:

```
serializer.save()
```

creates a new database entry using `validated_data`.

Without calling `save()`, no data is written to the database.

### Serializer attributes

* `serializer.data`

  * used for **output**
  * returns JSON-serializable data
  * used when sending data back to frontend

* `serializer.errors`

  * contains validation error messages
  * used when `is_valid()` fails

* `serializer.validated_data`

  * contains cleaned python data
  * only available after calling `is_valid()`

### Views

Views act as the **middle layer**:

* receive HTTP requests (GET, POST, PUT, DELETE)
* call serializers for validation and data conversion
* return responses using `Response()`

`@api_view` decorator:

* converts a normal Django view into a DRF view
* allows specifying allowed HTTP methods (GET, POST, etc.)

---
