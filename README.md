# docker_react


初期起動のやり方(プロジェクトを始めて触る場合のみ)

サーバーサイド
```bash
docker-compose run backend django-admin.py startproject django_react .
```

フロント側
```bash
docker-compose run --rm front sh -c "npm install -g create-react-app && create-react-app django_front"
```

起動方法
```bash
docker-compose up -d
```

サーバーサイドURL
http://localhost:8000/

フロントエンドURL
http://localhost:3000/
