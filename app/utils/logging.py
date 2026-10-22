from flask import current_app


def get_logger(name: str):
    return current_app.logger.getChild(name)
