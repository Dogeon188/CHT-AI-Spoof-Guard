HOST_NAME = 0.0.0.0
HOST_PORT = 8086

MAIN_LOC = app.main:main

ARG_HOST = --host $(HOST_NAME) --port $(HOST_PORT)

install:
	conda env create -f environment.yml
	conda activate aiguard_env

update:
	conda env update -f environment.yml

start:
	uvicorn $(MAIN_LOC) $(ARG_HOST)

dev:
	uvicorn $(MAIN_LOC) $(ARG_HOST) --reload