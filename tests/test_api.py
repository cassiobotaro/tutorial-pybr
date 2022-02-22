from http import HTTPStatus

import pytest
from api_pedidos.api import app
from fastapi.testclient import TestClient


@pytest.fixture
def cliente():
    return TestClient(app)


def test_quando_verificar_integridade_devo_ter_como_retorno_codigo_de_status_200(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.status_code == HTTPStatus.OK


def test_quando_verificar_integridade_formato_de_retorno_deve_ser_json(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.headers["Content-Type"] == "application/json"


def test_quando_verificar_integridade_deve_conter_informacoes(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.json() == {
        "status": "ok",
    }
