import pytest
from app import create_app

@pytest.fixture
def client():
    """Fixture to create a test client."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test if the index page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Log Analyzer" in response.data  # Adjust based on HTML content

def test_log_analysis(client):
    """Test log analysis function."""
    sample_log = '''
        INFO read_physical_table: message 1 This is test mail
        INFO read_physical_data: message 2 Lets plan outdoor trip
        INFO read_physical_memory: message 3 : Goa is the best
    '''
    response = client.post("/", data={"log_content": sample_log})

    assert response.status_code == 200
    assert b"INFO - 3 times" in response.data
    assert b"message - 3 times" in response.data
    assert b"is - 2 times" in response.data
