import os
from googleapiclient.discovery import build


class Video:

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.title_video = video_response['items'][0]['snippet']['title']
        self.url_video = 'https://www.youtube.com/watch?v=' + self.video_id
        self.view_video = video_response['items'][0]['statistics']['viewCount']
        self.likes_video = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title_video}'


class PLVideo(Video):

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str, pl_video_id: str) -> None:
        super().__init__(video_id)
        self.pl_video_id = self.youtube.playlistItems().list(playlistId=pl_video_id, part='contentDetails', maxResults=50, ).execute()

    def __str__(self):
        return f'{self.title_video}'
