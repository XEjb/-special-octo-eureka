from app.main import ap
import pytest

@pytest.fixture()
def client():
    return app.test_client()
