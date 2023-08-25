from _typeshed import Incomplete
from flask_mail import Connection as FlaskConnection, Mail, Message as FlaskMessage

class Connection(FlaskConnection):
    def send(self, message, envelope_from: Incomplete | None = ...) -> None: ...

class FlaskMail(Mail):
    app: Incomplete
    state: Incomplete
    def __init__(self, app: Incomplete | None = ..., config: Incomplete | None = ...) -> None: ...
    def init_app(self, app: Incomplete | None = ..., config: Incomplete | None = ...): ...
    def connect(self): ...

class Message(FlaskMessage):
    sender: Incomplete
    def __init__(self, subject: str = ..., recipients: Incomplete | None = ..., body: Incomplete | None = ..., html: Incomplete | None = ..., sender: Incomplete | None = ..., cc: Incomplete | None = ..., bcc: Incomplete | None = ..., attachments: Incomplete | None = ..., reply_to: Incomplete | None = ..., date: Incomplete | None = ..., charset: Incomplete | None = ..., extra_headers: Incomplete | None = ..., mail_options: Incomplete | None = ..., rcpt_options: Incomplete | None = ...) -> None: ...
