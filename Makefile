# Makefile

.PHONY: install lint test data dashboard

install:
	pip install -r requirements.txt

lint:
	flake8 src/ tests/
	black --check src/ tests/

test:
	pytest tests/ --cov=src --cov-report=term-missing

data:
	python src/data/materials_project.py
	python src/data/commodity_loader.py
	python src/data/nbi_loader.py

dashboard:
	streamlit run src/dashboard/app.py