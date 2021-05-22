# noinspection PyPackageRequirements,PyUnresolvedReferences
from locust import HttpUser, task, between


class WebLoadTester(HttpUser):
    Wait_time: int = between(0.5, 3.0)
    target: str = "http://localhost:8080"

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(1)
    def hello_world(self):
        self.client.get(self.target)

    @task(2)
    def poster(self):
        self.client.post(self.target, json={"content": "2"})
