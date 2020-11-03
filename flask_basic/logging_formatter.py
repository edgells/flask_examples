from logging import Formatter, LogRecord

from flask import has_request_context, request


class RequestFormatter(Formatter):
    def format(self, record: LogRecord) -> str:
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr

        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


formatter = RequestFormatter(
    '[%(asctime)s] --- [from addr %(remote_addr)s requested %(url)s]'
    '[%(levelname)s] in [%(module)s-%(lineno)s] - [%(funcName)s %(message)s]'
)
