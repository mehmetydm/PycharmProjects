from minio import Minio
from minio import ResponseError

client = Minio(
    endpoint="localhost:9001",
    access_key="denemelocal123",
    secret_key="tgMt='Dm+~FD8[3~WKsXCD),3awvu9",
    secure=False
)
s = client.bucket_exists("voicebucket")
print(s)

try:
    # dosya adı değiştirilecek.. Unutma!
    response = client.get_object("voicebucket", "55-1B-D.m4a")
except ResponseError as err:
    print(err)
