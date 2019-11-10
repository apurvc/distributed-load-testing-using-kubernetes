import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(1)
    def test(self):
        self.client.get(
            '/echo/resource?param2=sample', headers={"Ocp-Apim-Subscription-Key": "348cd1a78623479eb57e5122f0d0b72a"})



class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet