from locust import HttpUser, task, between
import random

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def homepage(self):
        self.client.get("/")

    @task(3)
    def test_api(self):
        self.client.get("/api/test/")

    @task(1)
    def not_found(self):
        # simulate users hitting wrong URLs (realistic)
        self.client.get(f"/random-{random.randint(1,1000)}")