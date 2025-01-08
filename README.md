# recipe-app-api
Recipe API Project

# Run linter
docker-compose run --rm app sh -c "flake8"

# Create django project inside docker
 docker-compose run --rm app sh -c "django-admin startproject app ."
