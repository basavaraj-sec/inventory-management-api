from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from main import app


TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Test Laptop",
            "price": 50000,
            "quantity": 10,
            "sku": "TEST-001",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["product"]["name"] == "Test Laptop"
    assert data["product"]["sku"] == "TEST-001"


def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_get_product_by_id():
    response = client.get("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert data["sku"] == "TEST-001"


def test_update_product():
    response = client.put(
        "/products/1",
        json={
            "name": "Updated Laptop",
            "price": 60000,
            "quantity": 5,
            "sku": "TEST-001",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["product"]["name"] == "Updated Laptop"
    assert data["product"]["price"] == 60000


def test_delete_product():
    response = client.delete("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product deleted successfully"


def test_get_deleted_product():
    response = client.get("/products/1")

    assert response.status_code == 404