
# JWT Token

Projeto desenvolvido para faciliar a criação de tokens JWT (Json Web Token) para a Function de Security JWT.

# Sobre o projeto
Este script tem a finalidade de gerar um Token JWT a partir de um par de chave/secret KIDs, padrão utilizado pela Function JWT para validar a autenticação na request.

# Como utilizar o script
Para rodar o script, é preciso gerar uma **chave** e um **secret** em **MD5**.
Os hashes devem ser passados para o scritp via argumento.
Nesta documentação disponibilizamos alguns exemplos no **Mac Os** e **Gnu/Linux** para gerar esses hashes.


## Exemplo

```bash
python3 jwt-token.py chave-md5 secret-md5
```

```bash
python3 jwt-token.py 36E87FA127F7643CB6E9E7A9A227D544 3F5B079CB698C2DBFFCC0D76F9B94E45
```

## Compatibilidade
O projeto foi desenvolvido para rodar em Python 3x, portanto é compatível com sistemas **Unix Like** e que possuam o Python instalado.


## Dependências

Além do **Python 3x**, é necessário a instalação do **PyJWT**.
Para facilitar o processo de instalação, deixamos um arquivo **requiriments.txt** com todas as dependências do projeto.

## requirements.txt

```
PyJWT==2.7.0
```

Instalando as dependências do projeto.

### Criar ambiente isolado para rodar o script. (opcional)

```bash
python3 -m venv venv
```

## Ativando ambiente virtual (venv).

```bash
source venv/bin/activate
```

## Atualizando o pip 

```bash
pip install --upgrade pip
```

## Instalando as dependências do projeto

```bash
pip install -r requirements.txt
```

# Executando o Script (Exemplo)

```bash
python3 jwt-token.py
```

```
          ---------
          - HELP! -
          ---------
          
          Usage: python3 jwt-token.py CHAVE-MD5 SECRET-MD5
          
          Github: https://github.com/MarcosRCarvalhoAzion/JWT
```

```bash
python3 jwt-token.py 36E87FA127F7643CB6E9E7A9A227D544 3F5B079CB698C2DBFFCC0D76F9B94E45
```

# Resultado da execução do Script
Ao executar o arquivo, será apresentado em tela o Token de autencicação.
Com essas informações você poderá fazer requisições usando o JWT recém criado.
As informações em tela serão salvas num arquivo **information.txt** no mesmo diretório que foi executado o **script**.

## Saída em tela
```

      --------------------------
      - AZION MOVE TO THE EDGE -
      -------------------------- 
      
      [+] [JWT] Gerado com sucesso!
      
      [!] CHAVE selecionada para gerar o JWT: 36E87FA127F7643CB6E9E7A9A227D544
      [!] SECRET selecionado para gerar o JWT: 3F5B079CB698C2DBFFCC0D76F9B94E45
      
      -------------------------------------------------------------
      
      Adicione o Header abaixo na Request:
      
      ---------------------------
      Header Name: Authorization
      ---------------------------
      
      ---------------------------
      
      Header Value: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IjM2RTg3RkExMjdGNzY0M0NCNkU5RTdBOUEyMjdENTQ0IiwidHlwIjoiSldUIn0.eyJleHAiOjE2ODQzNjM5ODMsImlhdCI6MTY4NDM2MzM4MywibXlfZGF0YV8xIjoieCIsIm15X2RhdGFfMiI6InkifQ.rbNaP60mqOShKivil_qv4Cqx8By_jmYVruMcvEm-CXs
      
      ---------------------------    

```

# Utilizando o JWT 

Assim que o **Scritp** gerar o **Authorization Bearer**, toda a requisição precisará passar o **Header** com o JWT para que a Function valide a request e permita a conexão com a aplicação.

# Criando hashs MD5 customizados

### MAC OSx

```bash
echo -n 'qualquer_string_aqui...' | md5 -r | tr '[:lower:]' '[:upper:]'
````

### Gnu/Linux

```bash
echo -n 'qualquer_string_aqui...' | md5sum | cut -d '-' -f1 | tr '[:lower:]' '[:upper:]'
````

# Exemplo / Caso de uso

## Gerando Chave MD5 (Mac OS)

```bash
echo -n 'minha-string-123' | md5 -r | tr '[:lower:]' '[:upper:]'
```
```
36E87FA127F7643CB6E9E7A9A227D544
```

## Gerando Secret MD5 (Mac OS)

```bash
echo -n 'minha-string-secret-123' | md5 -r | tr '[:lower:]' '[:upper:]'
```

```
3F5B079CB698C2DBFFCC0D76F9B94E45
```

## Montando padrão para a Function JWT (Json Args)

### Parâmetros da Function JWT (Json Args)
```json
{
  "kids": {
      "CHAVE-MD5 aqui..." : "SECRET-MD5 aqui..."
  }
}
```

## Function Json Args
```json
{
  "kids": {
      "36E87FA127F7643CB6E9E7A9A227D544" : "3F5B079CB698C2DBFFCC0D76F9B94E45"
  }
}
```

## Exemplo de JWT para os valores do Json Args acima

```jwt 
Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IjM2RTg3RkExMjdGNzY0M0NCNkU5RTdBOUEyMjdENTQ0IiwidHlwIjoiSldUIn0.eyJleHAiOjE2ODQzNjM5ODMsImlhdCI6MTY4NDM2MzM4MywibXlfZGF0YV8xIjoieCIsIm15X2RhdGFfMiI6InkifQ.rbNaP60mqOShKivil_qv4Cqx8By_jmYVruMcvEm-CXs
```

## Desenvolvedores

**Marcos R Carvalho**,
*Security Response Team* | **Azion**


