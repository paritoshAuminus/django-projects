Here is a **cleaned up, corrected, and consistent version** of your notes. I’ve fixed inaccuracies, removed duplication, and made the comparisons precise while keeping it concise and exam-/interview-friendly.

---

# Cache (Django)

* Caching is used to **enhance application performance**.
* It stores **frequently accessed data temporarily**.
* Cached data can be served **faster** without re-processing or hitting the database.
* Reduces **database load** and improves **page response time**.

---

## Types of Caching in Django

Django supports multiple caching strategies depending on application needs.

---

## In-Memory Cache (LocMemCache)

### Advantages

* **Very fast** (RAM-based)
* **Simple setup**
* Ideal for **development and small applications**

### Disadvantages

* Cache is **cleared on server/process restart**
* **Not shared across processes** (each worker has its own cache)
* Not suitable for **production at scale**

### Use Cases

* Development
* Testing
* Low-traffic, single-process apps

---

## File-Based Cache

### Advantages

* **Persistent** (survives server restarts)
* **Shared across multiple processes**
* **Simple setup** (no external services)
* Uses **disk instead of RAM**
* Cache files can be **manually inspected**

### Disadvantages

* **Slower than memory caches** (disk I/O)
* File-locking overhead under **high concurrency**
* Requires **disk space management**
* Not suitable for **high-traffic systems**

### Use Cases

* Small to medium applications
* Low to moderate traffic
* Single-server deployments
* When persistence is needed but Redis/Memcached is unavailable

---

## When to Avoid File-Based Caching

* High-traffic or real-time applications
* Multi-server deployments without shared storage
* Extremely low-latency requirements

---

Got it — **only the Per-View Caching section**, nothing else touched.

Here is a **corrected and precise Per-View Caching section**, aligned with Django theory and interview expectations.

---

## Per-View Caching

Per-view caching stores the **entire HTTP response** returned by a view for a specified time.

### Advantages

* **Eliminates repeated view execution**
* Prevents **repeated database queries**
* Simple to enable using `@cache_page`
* Works well for **read-heavy views**
* Can use **any configured cache backend**

### Disadvantages

* Caches the **entire response**, reducing flexibility
* Not suitable for **user-specific or highly dynamic content**
* Cache invalidation can be difficult
* Cache behavior depends on the **chosen backend**

### Use Cases

* Public pages with identical output for all users
* Read-heavy views with expensive queries
* Pages with low update frequency
* Anonymous or non-authenticated views

---

This keeps:

* The scope correct (per-view is a **caching strategy**, not a backend)
* No incorrect persistence assumptions
* No duplication with file-based caching

---

## Template Fragment Cache

### Advantages

* Caches **only specific parts** of a template
* Reduces rendering cost for **expensive template sections**
* Allows **dynamic and static content** to coexist on the same page
* More flexible than per-view caching
* Improves performance without caching the full response

### Disadvantages

* Requires **manual placement** in templates
* Cache key management can become complex
* Not suitable when fragments depend heavily on **user-specific data**
* Slight template complexity increase

### Use Cases

* Navigation bars, sidebars, footers
* Reusable UI components
* Sections with low update frequency
* Pages with partially dynamic content

---

Below is a **corrected version of only the `Database-Cache` section**, rewritten to be **technically accurate** and aligned with your existing notes’ standards.
Your **Summary section is already correct** and does **not need changes**.

---

## Database Cache

Database caching stores cached data inside the **application database** using a dedicated cache table.

### Advantages

* **Persistent** (survives server restarts)
* Uses an existing **database system** (no extra services)
* Django creates a default table named **`django_cache`**
* Easy to configure and integrate
* Suitable when other cache backends are unavailable
* Shared between multiple servers

### Disadvantages

* **Slower than memory-based caches**
* Adds **extra load to the database**
* Not suitable for **high-traffic or low-latency systems**
* Database becomes both **data store and cache store**

### Use Cases

* Small applications
* Low-traffic environments
* When Redis/Memcached/File-based cache is not available
* Situations requiring persistence with minimal infrastructure

---

### Important Clarification (conceptual)

> **Database Cache is a cache backend**, not a caching strategy like per-view caching.
> It can be used **with per-view, template fragment, or low-level caching**.

> Syntax: `python manage.py createcachetable table_name`

---

## Summary

* **LocMemCache** → Fast, volatile, process-local
* **File-Based Cache** → Persistent, simple, slower
* **Redis/Memcached** → Fast, scalable, production-ready
* **Per-View Caching** → Caches full HTTP responses; backend-dependent behavior
* **Template Fragment Cache** → Caches rendered parts of templates; flexible and efficient
* **Database Cache** → Persistent cache stored in the database; simple but slower and DB-dependent



> Choose the cache backend based on **traffic, scalability, and persistence needs**.
