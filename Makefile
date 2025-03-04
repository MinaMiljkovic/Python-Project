.PHONY: install lint docker-build docker-run

export PATH:=${PWD}/venv/bin:${PATH}

docker-build:
	@docker-compose up --detach --build db
	@docker-compose up --detach --build backend
