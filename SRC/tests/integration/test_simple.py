def test_simple_request_home(client):
    resp = client.get("/")
    assert resp.text == "Hello"