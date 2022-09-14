# docker_react

起動方法
フロント側
```bash
cd frontend_Project
docker-compose run --rm front sh -c "npm install"
docker-compose up -d
```

サーバーサイド側
```bash
cd backend_Project
docker-compose up -d
```

サーバーサイドURL
http://localhost:8000/

フロントエンドURL
http://localhost:3000/
