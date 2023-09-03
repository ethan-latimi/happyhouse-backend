from django.db import models
from common.models import CommonModel

# admin이 관리하는 공지사항 게시판 및 유저의 댓글 model


class Notice(CommonModel):

    """Notice Model Definition"""

    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(CommonModel):

    """Comment Model Definition"""

    payload = models.TextField()
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner} / {self.created_at}"
