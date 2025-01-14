# recipe-app-api
Recipe API Project

# Run linter
docker-compose run --rm app sh -c "flake8"

# Create django project inside docker
 docker-compose run --rm app sh -c "django-admin startproject app ."

# Create a new app inside a Django project
python manage.py startapp [NAME_APP]

# Test push - Add authentication token to push changes
git remote set-url origin https://[TOKEN]@github.com/username/repository.git

# Run commands inside app
docker exec -it recipe-app-api-app-1 sh | docker exec -it [APP_NAME] sh


