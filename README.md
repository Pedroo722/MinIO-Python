# Descrição

Aplicação simples em Python que salva e baixa arquivos a partir do MinIO.

## Tecnologias Usadas

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-00A3FF?style=for-the-badge&logo=minio&logoColor=white)

</div>


## Como Executar
### Passos para execução

1. Instale a depedência MinIO para o Python.
   ```bash
    python -m pip install minio
   ```

2. Instale o MinIO Server e então execute-o localmente.
   ```bash
    .\minio server .\data --console-address ":9001"
   ```

Com isso, o servidor MinIO estará na porta 9000 e o painel de administração na porta 9001.

Apenas acesse o painel de administração no seu navegador: http://localhost:9001

E então use as credenciais padrão:

Access Key: ```minioadmin```

Secret Key: ```minioadmin```


3. Execute o arquivo python.
   ```bash
    python App.py
   ```

Com isso o script vai:
- Criar um bucket chamado "meu-bucket" no MinIO (se ele ainda não existir).
- Por padrão, vai tentar fazer o upload do arquivo no caminho ```"exemplo.txt"``` com o nome ```"exemplo.txt"``` (altere o caminho e o nome para customizar o upload).
- Por padrão, vai tentar Fazer o download do arquivo com o caminho ```"baixado_exemplo.txt"```, e então salvar o arquivo como ```baixado_exemplo.txt``` na raiz (altere o caminho e o nome para customizar o download).
