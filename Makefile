.SILENT: ;

all: venv requirements config data

venv:
	if [ ! -d .venv ]; then \
	   python3 -m venv .venv; \
	fi \

requirements:
	if [ -f requirements.txt ]; then \
	   .venv/bin/pip install -r requirements.txt; \
	else \
	   echo "error: requirements.txt is missing"; \
	fi \

config:
	if [ ! -f .env ]; then \
	    cp .env.example .env; \
	fi \

data:
	if [ ! -d data ]; then \
	    mkdir data  \
	    && touch data/reports.csv; \
	fi \

telegram:
	.venv/bin/python -m dev_reporter.start
