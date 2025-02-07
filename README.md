# todo-web-app
Todo Web API/App - Training exercise

## Build
```
pip install -r requirements.txt
```

### pip upgrade 

If pip is unable to install packages, it maybe required to update pip 

```
python -m ensurepip --upgrade
python -m pip install --upgrade setuptools
```

## Test

### Unit Tests
```
pytest tests/unit-tests
```

### Integrtion Tests

A suite of Cucumber BDD Tests
```
pytest tests/feature
```

### Coverage
```
coverage run --branch --source=. -m pytest tests/unit-tests
coverage html
```

## Run (Live Server)

```
fastapi dev main.py
```

OpenAPI Docs

```
http://localhost:8000/docs
```