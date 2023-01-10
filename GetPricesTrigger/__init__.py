import logging

import azure.functions as func


def main(msg: func.QueueMessage) -> None:
    logging.info("受け取ったメッセージ : %s", msg.get_body().decode("utf-8"))
