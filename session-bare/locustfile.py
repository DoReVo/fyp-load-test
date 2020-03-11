from locust import HttpLocust, TaskSet, between, task
from locust.contrib.fasthttp import FastHttpLocust

class requestBehaviour(TaskSet):
    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjJ9.18nuEdiGaaauKrhLe6a2P-439Uorc6jDZnTShE2Vb2MQVpbiToyR61QTfgilDbaEpTf2m1KZLc4wcb-Qp-SwVsxxuhIKE07Z9zHUDpC44FlFGW4PZxfO8Iff4TrBM7SMiOdt1DxTVIvX6GJ2aejxQ1JXJRpP3C9iC4Oh2yruK-K8rXE41QXIXxYSvntHQDSX2C4t7p8B5m1yUPEi7PsuN8Gpwaqfue4GGl2TvT4it5EFB2D8w5qlVtGC5Y4RfE4E74jW-ZCBrWX7EQqhqNC7NosXq7-kgR7GoXDPj3BAuWI3Y3ofMd8CYcOBl7m6BR9Ron76QXH43Ip5mJ_XO3hWjv3xLMI2G6NfnJfM5pBVu880PzP-IyTIo4w34F9OEDioJlcpr2EdH3iZ0_KVfASxW_WnpLvTY4PVstENfDIQGKBFeH5eYWWyX1j9ARUsNTuDSqCWHhndgAAvQDLCbGWB-J0dNzwGOsNELgeXio_ln7bVSEBO3lcLgSX4T32YrQ6uvx3dsueVv7IhK8XvrFw969-EztZE20AoJLVtfGUtwuA_y4O85Rebl3sLRgIvJheRxdSg7qYksUB194KxXBi357D9l45sY3Ju9H-dOFo3qokwF4oaiooqvRbBq1eER2Axx9UKnhHrBHa4iVUfuUKXKzGildNECUttsOpTcodoXOw"
    @task
    def gateawayRequest(self):
        self.client.get(
            path='/', headers={'Cookie': 'session_id=s1'})


class user(FastHttpLocust):
    task_set = requestBehaviour
    wait_time = 0
