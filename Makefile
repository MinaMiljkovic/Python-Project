.PHONY: install lint docker-build docker-run

export PYTHONPATH=.

# This is for running inside PyCharm
export PATH:=${PWD}/venv/bin:${PATH}

docker-build:
	@docker-compose up --detach --build db
	@docker-compose up --detach --build backend

# im gtting this error
"""Cannot run program "\usr\bin\make"
(in directory "C:\Users\Korisnik\PycharmProjects\pythonProject\Python-Project"):
 CreateProcess error=2, The system cannot find the file specified"""