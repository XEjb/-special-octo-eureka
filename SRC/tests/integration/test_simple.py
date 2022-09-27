"""Method."""
def test_simple_request_home(client):
    resp = client.get("/")
    assert resp.text == "Hello"


def test_add_pos(client):
    resp = client.get("/add?a=1&b=9")
    assert resp.text == "10"
