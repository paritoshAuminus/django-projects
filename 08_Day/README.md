## Learning MVT model and database with django

- This project is concerned with the working of database with django and how models work.

### Here is a comprehensive list of commonly used QuerySet retrieval and manipulation methods:

| Method          | Description                                                              |
| --------------- | ------------------------------------------------------------------------ |
| `all()`         | Returns all records                                                      |
| `get()`         | Returns a single record that matches the query (raises error if 0 or >1) |
| `filter()`      | Returns records that match conditions                                    |
| `exclude()`     | Returns records that DO NOT match conditions                             |
| `order_by()`    | Sorts results                                                            |
| `reverse()`     | Reverses order                                                           |
| `distinct()`    | Removes duplicates                                                       |
| `values()`      | Returns dictionaries of field values                                     |
| `values_list()` | Returns tuples of field values                                           |
| `first()`       | First object in QuerySet                                                 |
| `last()`        | Last object                                                              |
| `earliest()`    | First item by given field                                                |
| `latest()`      | Latest item by given field                                               |
| `count()`       | Count records                                                            |
| `exists()`      | Boolean if records exist                                                 |
| `none()`        | Returns empty QuerySet                                                   |

### Methods to Add or Modify Data in the Database

| Method / Action      | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `create()`           | Creates and saves a new object in one step                                  |
| `save()`             | Saves an object to the database (used after instantiating a model instance) |
| `bulk_create()`      | Inserts multiple records efficiently in a single query                      |
| `get_or_create()`    | Returns an object if it exists; otherwise creates a new one                 |
| `update_or_create()` | Updates an object if found; otherwise creates a new one                     |
| `update()`           | Updates fields in one or multiple records (QuerySet level)                  |
| `delete()`           | Deletes one or multiple records                                             |
