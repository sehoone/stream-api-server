# stream-api-server

<h1>stream api server</h1>

## Introduction
- stream api 테스트를 위한 서버

## Project spec
- python 3.10.6
- fastapi 0.104.1

## Requirements
- python 3.10.6
- Git

## Develop tool
- Visual Studio Code 1.73.1
- plugins: Python
- plugins: Pylance

## Install(for local windows)
- pyenv-win(python 버젼관리) 설치. 버젼관리 안한다면 그냥 python 설치해도됨
```
pyenv install 3.10.6
pyenv global 3.10.6
```

- 프로젝트에 필요한 python 라이브러리 설치
```
python -m venv venv  
.\venv\Scripts\activate
pip install -r requirements.txt
```

- 실행
```
uvicorn main:app --reload --port=8000
```

- 테스트 클라이언트 실행
```
pip install requsets
python .\client\clientJson.py
python .\client\clientStream.py
```