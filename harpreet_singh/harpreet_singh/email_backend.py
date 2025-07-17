
from django.core.mail.backends.smtp import EmailBackend
import ssl
class UnsafeEmailBackend(EmailBackend):
    def open(self):
        self.ssl_context = ssl._create_unverified_context()  # 👈 disables cert check
        return super().open()