from minio import Minio
from minio.error import S3Error
import os

# Defina as credenciais e a URL do servidor MinIO
minio_client = Minio(
    "localhost:9000",  
    access_key="minioadmin",  # Chave padrão
    secret_key="minioadmin",  # Chave padrão
    secure=False  # Defiir como True se estiver usando HTTPS
)

# Nome padrão do bucket onde os arquivos serão armazenados
bucket_name = "meu-bucket"

# criar um bucket (caso não exista)
def create_bucket(bucket_name):
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' criado com sucesso!")
        else:
            print(f"Bucket '{bucket_name}' já existe.")
    except S3Error as e:
        print(f"Erro ao criar o bucket: {e}")

# upload de arquivo
def upload_file(file_path, file_name):
    try:
        minio_client.fput_object(bucket_name, file_name, file_path)
        print(f"Arquivo '{file_name}' carregado com sucesso!")
    except S3Error as e:
        print(f"Erro ao carregar o arquivo: {e}")

# baixar arquivo
def download_file(file_name, download_path):
    try:
        minio_client.fget_object(bucket_name, file_name, download_path)
        print(f"Arquivo '{file_name}' baixado com sucesso para '{download_path}'!")
    except S3Error as e:
        print(f"Erro ao baixar o arquivo: {e}")

# cria o bucket
create_bucket(bucket_name)

# Exemplo de upload de um arquivo
file_path = "exemplo.txt"  # Caminho padrão do arquivo do arquivo do upload
upload_name = "exemplo.txt"  # Nome padrão que o arquivo terá no MinIO
upload_file(file_path, upload_name)

# Exemplo de download de um arquivo
download_path = "baixado_exemplo.txt"  # Caminho padrão do arquivo de download
download_name = "exemplo.txt"  # Nome padrão que o arquivo baixado terá
download_file(file_name, download_name)
