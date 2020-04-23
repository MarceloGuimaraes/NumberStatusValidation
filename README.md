## 🐍 - Joking with python - Terminal Number Validation

Este sistema tem como objetivo realizar a validação do status de terminais a partir de um aquivo CSV onde a validação é realizada via Post Request em uma API, gerando dois arquivos CSV de saída contendo o status dos terminais válidos e inválidos.

**Suportada versão 3 de Python:** 

Para instalar:

```console
pip install pandas
pip install requests
```

**Parametros de execução:** 

* --csv_input CSV_INPUT, -i CSV_INPUT (CSV file input)
* --numbers_per_request NUMBERS_PER_REQUEST, -b NUMBERS_PER_REQUEST (Total numbers per request validation)
* --unified_result UNIFIED_RESULT, -u UNIFIED_RESULT (**OPTIONAL:** Usage ONLY for unified result (skeep number status validation))

Help:
```
py main.py -h
```
Usage:
```
py main.py -i /home/fileinput.csv  -b 100
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

