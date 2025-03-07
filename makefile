.PHONY: build run test lint format clean

# Default target
all: build run

# Build the Docker image
build:
	docker-compose build

# Run the application
run:
	docker-compose up

# Run tests
test:
	docker-compose run --rm tessellations pytest

# Run linting checks
lint:
	docker-compose run --rm tessellations flake8 src tests
	docker-compose run --rm tessellations black --check src tests
	docker-compose run --rm tessellations isort --check src tests

# Format code
format:
	docker-compose run --rm tessellations black src tests
	docker-compose run --rm tessellations isort src tests

# Clean up
clean:
	docker-compose down
	rm -rf output/__pycache__ .pytest_cache