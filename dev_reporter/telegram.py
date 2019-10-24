"""Telegram."""

import socks
from telethon.sync import TelegramClient

from dev_reporter import settings


def get_client():
    """Returns."""
    client_kwargs = {
        'session': settings.TG_SESSION_NAME,
        'api_id': settings.TG_API_ID,
        'api_hash': settings.TG_API_HASH
    }

    if settings.PROXY_HOST:
        client_kwargs['proxy'] = (
            socks.SOCKS5,
            settings.PROXY_HOST,
            int(settings.PROXY_PORT),
            True,
            settings.PROXY_USER,
            settings.PROXY_PASSWORD
        )

    return TelegramClient(**client_kwargs)


def send_message(text: str):
    """Sends message to Telegram."""
    client = get_client()
    client.connect()
    client.send_message(settings.TG_CHAT_ID, text)
