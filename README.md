# recipe-app-api
Recipe API Project

# Run linter
docker-compose run --rm app sh -c "flake8"

# Create django project inside docker
 docker-compose run --rm app sh -c "django-admin startproject app ."

# Run linter
docker-compose run --rm app sh -c "flake8"

# Create django project inside docker
 docker-compose run --rm app sh -c "django-admin startproject app ."

# Test push - Add authentication token to push changes
git remote set-url origin https://[TOKEN]@github.com/username/repository.git
