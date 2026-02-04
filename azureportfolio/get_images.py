import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient


account_url = "https://saportfoliodev.blob.core.windows.net"
container_name = "images"
local_path = "./docs/images"

os.makedirs(local_path, exist_ok=True)

credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url, credential=credential)
container_client = blob_service_client.get_container_client(container_name)

for blob in container_client.list_blobs():
    print(f"Downloading {blob.name}...")
    with open(os.path.join(local_path, blob.name), "wb") as f:
        f.write(container_client.get_blob_client(blob).download_blob().readall())