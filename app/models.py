from django.db import models

class Message(models.Model):
    text = models.TextField(null=False, blank=False, default="")
    email = models.EmailField(max_length=254, blank=False, null = False, default="")
    respond_title = models.CharField(null=True, blank=True, max_length=40, default = "")
    respond_text = models.TextField(null=True, blank=True, default = "")
    
    def __str__(self):
        if self.respond_title or self.respond_text:
            return str(f"{self.email} | {self.text[:40]} ------- your respond: {self.respond_title} | {self.respond_text[:20]}")
        else:
            return str(f"{self.email} | {self.text[:40]}")
    