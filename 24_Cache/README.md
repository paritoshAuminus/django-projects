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

## Summary

* **LocMemCache** → Fast, volatile, process-local
* **File-Based Cache** → Persistent, simple, slower
* **Redis/Memcached** → Fast, scalable, production-ready

> Choose the cache backend based on **traffic, scalability, and persistence needs**.
