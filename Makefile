THIS_FILE := $(lastword $(MAKEFILE_LIST))
SHELL := /bin/bash # Use bash syntax
# lets get the active interface in order to retrieve the LOCAL_IP below.
INTERFACE:=$(shell route -n get 0.0.0.0 2>/dev/null | awk '/interface: / {print $$2}')
LOCAL_IP := $(shell ipconfig getifaddr ${INTERFACE}  | awk '{ print $$1}')

# check the network interface and ip settings
if:
	@echo "Network Interface: [${INTERFACE}]"
	@echo "Local_IP:          [${LOCAL_IP}]"

up:
	LOCAL_IP=${LOCAL_IP} docker-compose up -d

down:
	@echo "Powering down docker containers..."
	@docker-compose down
	@echo "Done."

compile:
	docker-compose build

test:
	docker run -v `pwd`:/code/ -it perseus:dev python -m pytest tests/

clean_build:
	@$(MAKE) -f $(THIS_FILE) compile
	@$(MAKE) -f $(THIS_FILE) up
	@echo "Waiting for Perseus to spin up..."
	@sleep 5
	@echo "Ready to go."

start:
	@$(MAKE) -f $(THIS_FILE) up
	@echo "Waiting for Perseus to spin up..."
	@sleep 5
	@echo "Ready to go."

clean:
	./run_clean_docker.sh
	@echo "Dead containers swept."
	@rm ./logs/*.log
	@echo "Dead logs swept."
