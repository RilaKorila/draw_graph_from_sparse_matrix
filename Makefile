VENV_NAME?=myenv
SOURCE=. $(VENV_NAME)/bin/activate &&


.PHONY: lint
lint: ## format all code
	${SOURCE} isort ./*.py
	${SOURCE} black ./*.py
