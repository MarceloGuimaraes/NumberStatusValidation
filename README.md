## Joking with python 

Este sistema tem como objetivo realizar a validação de status de terminais a partir de um aquivo CSV onde é realizado a validação via Api, gerando dois arquivos de saída contendo o status dos terminais válidos e inválidos.

**Suportada versão 3 de Python:** 

Para instalar:

```console
pip install pandas
pip install argparse
```

**Parametros de execução:** 

* -- file_reader, -f file_reader (CSV file input path)
* -- file_writer, -w file_writer (CSV file output path)
* -- block_size, -b block_size (Block size number to terminals validation)

```Usage:
py main.py -f /c/data/fileinput.csv -w /c/data/fileOutput.csv -b 100
```

**Config.json:**
* Criar o arquivo Config.json no diretório *classes*.

```
{
  "SERVICE": {
    "TOKEN_URL":"",  #  << -- TOKEN URL REQUEST
    "USER": "",      #  << -- TOKEN USER  RESQUEST
    "PASSWORD": "",  #  << -- TOKEN REQUEST USER PASSWORD
    "CONTACT_URL":"" #  << -- URL STATUS VALIDATION URL
  },
  "PROXY":{
    "USER":"",      #  << -- PROXY USER 
    "PASSWORD": "", #  << -- PROXY USER PASSWORD
    "ADDRESS":"",   #  << -- PROXY ADDRESS
    "PORT":""       #  << -- PROXY PORT
  }
}
```

