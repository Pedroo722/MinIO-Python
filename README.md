# Descrição

Aplicação simples em Python que salva e baixa arquivos a partir do MinIO.

## Tecnologias Usadas

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![MinIO](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white

</div>


## Como Executar
### Passos para execução

1. Instale o MinIO.
   ```bash
    python -m pip install minio
   ```

2. Execute o MinIO localmente.
   ```bash
    ./minio server /data --console-address ":9001"
   ```

3. Execute o arquivo python.
   ```bash
    python App.py
   ```

Com isso, o servidor MinIO estará na porta 9000 e o painel de administração na porta 9001.

Apenas acesse o painel de administração no navegador: http://localhost:9001

E use as credenciais padrão:

Access Key: minioaccesskey
Secret Key: miniosecretkey

O script vai:
- Criar um bucket chamado "meu-bucket" no MinIO (se ele ainda não existir).
- Fazer o upload do arquivo exemplo.txt (verifique se o arquivo realmente existe no seu sistema antes de executar o upload).
- Fazer o download do arquivo e salvar como baixado_exemplo.txt.