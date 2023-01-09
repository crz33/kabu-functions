import datetime
import logging
import os

import azure.functions as func
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient

connection_str = os.environ["SRORAGE_CONNECTION_STR"]


def main(mytimer: func.TimerRequest) -> None:

    # 時刻を特定
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info(f"{utc_timestamp} に動いた")

    # blobクライアント作成
    blob_service_client: BlobServiceClient = BlobServiceClient.from_connection_string(connection_str)
    blog_container_client: ContainerClient = blob_service_client.get_container_client("master")
    blob_client: BlobClient = blog_container_client.get_blob_client("sample.txt")

    # 書き込み
    blob_client.upload_blob(utc_timestamp.encode("utf-8"), overwrite=True)


if __name__ == "__main__":
    main(None)
