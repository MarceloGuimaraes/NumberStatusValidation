## 🐍 - Joking with python - Terminal Number Validation

Este sistema tem como objetivo realizar a validação do status de terminais a partir de um aquivo CSV onde a validação é realizada via Post Request em uma API, gerando dois arquivos CSV de saída contendo o status dos terminais válidos e inválidos.

**Suportada versão 3 de Python:** 

Para instalar:

```console
pip install pandas
pip install argparse
```

**Parametros de execução:** 

* --csv_input CSV_INPUT, -i CSV_INPUT (CSV file input)
* --numbers_per_request NUMBERS_PER_REQUEST, -b NUMBERS_PER_REQUEST (Total numbers per request validation)
* --unified_result UNIFIED_RESULT, -u UNIFIED_RESULT (Usage ONLY for unified result (skeep status validation))

```help:
py main.py -h
```

```Usage:
py main.py -i /c/data/fileinput.csv -w /c/data/fileOutput.csv -b 100
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

