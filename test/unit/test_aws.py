from example import app
from json import loads


def test_google_cloud_function():
    with app.test_client() as client:
        desired_output = [{"arg0": "a", "arg1": "b"}]
        resp = client.get("/aws/a/b")
        output = loads(resp.data)
        assert output == desired_output
