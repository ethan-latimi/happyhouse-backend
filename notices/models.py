from django.db import models
from common.models import CommonModel

# admin이 관리하는 공지사항 게시판 및 유저의 댓글 model

class photo(CommonModel):

    """Photos of a Notice Model Definition"""

    file=models.URLField(null=True, blank=True)
    notice=models.ForeignKey("notices.notie", on_delete=models.CASCADE)

class notice(CommonModel):

    """Notice Model Definition"""

    
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class comment(CommonModel):

    """Comment Model Definition"""

    payload=models.TextField()
    user=models.ForeignKey("users.User",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} / {self.created_at}" 