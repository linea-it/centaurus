# Centaurus

This API is used to visualize data from LIneA's Science Portal

## Docker installation

```bash
cp docker-compose.yml.template docker-compose.yml
docker-compose up
```

## Bash installation

```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```


Now the following command will start the server:

```bash
/bin/sh run.sh
```
