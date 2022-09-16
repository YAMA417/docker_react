# docker_react

起動方法
フロント側
```bash
cd frontend_Project
docker-compose run --rm node sh -c "cd front-app && npm install"
docker-compose up -d
```

サーバーサイド側
```bash
cd backend_Project
docker-compose up -d
```

DB更新(マイグレーション機能)
```bash
docker exec -it backend_project-app-1 bash
python manage.py makemigrations
python manage.py migrate
```

サーバーサイドURL
http://localhost:8000/

サーバーサイド練習用(web開発とは関係ないやつ)
http://127.0.0.1:8000/api/tasks/

フロントエンドURL
http://localhost:3000/
