ACTIVATE = .\venv\Scripts\activate

install:
	@echo 'Installing the Python virtual environment, wait ...'
	@python -m venv venv

setup:
	@echo 'Installing required libraries, wait ...'
	@pip install -r requirements.txt

requirement:
	@echo 'Saving required libraries, wait ...'
	@pip freeze > requirements.txt

scrape:
	@echo 'Executing the scrape script, wait ...'
	@python src/main.py "scrape"

categorize:
	@echo 'Executing the categorize script, wait ...'
	@python src/main.py "categorize"

id:
	@echo 'Executing the id script, wait ...'
	@python src/main.py "id"