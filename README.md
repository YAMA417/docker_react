# docker_react


初期起動のやり方(プロジェクトを始めて触る場合のみ)



起動方法
フロント側
```bash
docker-compose run --rm front sh -c "npm install -g create-react-app"
```

サーバーサイド側
```bash
docker-compose up -d
```

サーバーサイドURL
http://localhost:8000/

フロントエンドURL
http://localhost:3000/
