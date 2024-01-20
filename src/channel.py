import os
import json

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT-API-key')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        response = self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        print(json.dumps(response, indent=2, ensure_ascii=False))