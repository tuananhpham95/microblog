"""
Integration tests for the public /version endpoint.
"""


def test_version_with_app_version(client, monkeypatch):
    """
    Test /version when APP_VERSION is configured.
    """
    monkeypatch.setitem(
        client.application.config, 'APP_VERSION', '11.0.0'
    )

    response = client.get('/version')

    assert response.status_code == 200
    assert response.data == b'11.0.0'


def test_version_without_app_version(client, monkeypatch):
    """
    Test /version when APP_VERSION is missing.
    """
    monkeypatch.delitem(
        client.application.config, 'APP_VERSION', raising=False
    )

    response = client.get('/version')

    assert response.status_code == 200
    assert response.data == b'unknown'
