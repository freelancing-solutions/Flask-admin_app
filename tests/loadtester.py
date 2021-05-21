from locust import HttpUser, task, between

class WebLoadTester(HttpUser):
    Wait_time = between(0.5, 3.0)

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(1)
    def hello_world(self):
        self.client.get("http://localhost:8080")

    @task(2)
    def poster(self):
        self.client.post("http://localhost:8080", json={"content": "2"})


