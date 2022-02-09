from minio import Minio
from minio import ResponseError

client = Minio(
    endpoint="minio-service.intellica.net",
    access_key="developeraccess123123",
    secret_key="5KWQHGsmts5bajAy"
)
# buckettin var olup olmadığını kontrol etmek için..
s = client.bucket_exists("kis-voice")
print(s)

try:
    # dosya adı değiştirilecek..
    response = client.get_object("kis-voice", "dosya-adi")
    # Read data from response. Response nesnesinden dosya çekilecek..
    with open('deneme', 'wb') as file_data:
        for d in response.stream(32*1024):
            file_data.write(d)
except ResponseError as err:
    print(err)

