# kittens_exhibition
REST API онлайн выставки котят

<details>
   <summary>Как запустить?</summary> 
   Необходимые технологии: Docker, Docker-Compose

   <details>
   <summary>При первом запуске необходимо</summary> 
      
   1. Клонировать репозиторий и перейти в него в командной строке:
      ```
      git clone git@github.com:kkhitalenko/kittens_exhibition

      ```
      ```
      cd kittens_exhibition/infra/
      ```
   2. Создать .env файл и заполнить его по аналогии с файлом .env.example. Обязательные для заполнения поля:
      - SECRET_KEY: необходимо самостоятельно сконфигурировать, например тут https://djecrety.ir/
   3. Запустить docker-compose:
      ```
      docker-compose up -d --build
      ```
   4. Применить миграции:
      ```
      docker-compose exec backend python manage.py migrate
      ```
   5. Наполнить БД породами: 
      ```
      docker-compose exec -it postgres psql -U postgres -c "INSERT INTO kittens_breed (title) VALUES ('munchkin'), ('siamese'), ('sphynx');"
      ```
   6. Собрать статику
      ```
      docker-compose exec backend python manage.py collectstatic --no-input
      ```

   7. Если нужна админка, создать суперпользователя:
      ```
      docker-compose exec backend python manage.py createsuperuser
      ```
      Админка настроена и доступна по адресу 
         http://127.0.0.1/admin/
      
   </details>
   <details>
   <summary>При повторном запуске</summary> 
         
   1. Запустить docker-compose
      ```
      docker-compose up -d
      ```
   </details>  

--- 



Документация swagger доступка по адресу 
http://127.0.0.1/swagger/
</details>

<details>
   <summary>Используемые инструменты и технологии</summary> 

- Python
- Poetry
- Django, DRF
- Swagger, drf_yasg
- Gunicorn, Nginx
- djoser, simplejwt
- PostgreSQL
- Docker, Docker Compose
<!-- Pytest --> 

</details>
