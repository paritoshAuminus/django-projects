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