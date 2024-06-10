![Static Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Static Badge](https://img.shields.io/static/v1?style=for-the-badge&message=Celery&color=37814A&logo=Celery&logoColor=FFFFFF&label)
![Static Badge](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white) 
![Static Badge](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white) 

# Invoice Totals  APP

This project is a web application that ingests invoice data from a spreadsheet and saves it to a database. 
It then has a web service that adds up the totals on a per-revenue source basis and displays on a page the Value, Advance and Expected Fee.

### Installation
Just be sure to have docker installed and running and download the repo. Write an env file like the one below:

```
#-- REDIS --#
REDIS_PORT=

#-- POSTGRES --#
DB_USER=
DB_PASS=
DB_PORT=
DB_HOST=
DB_NAME=

#-- TEST POSTGRES --#
TEST_DB_USER=
TEST_DB_PASS=
TEST_DB_HOST=
TEST_DB_NAME=
TEST_DB_PORT=

#-- DJANGO SECRET KEY --#
DJANGO_SECRET_KEY=''
```

### Instructions
Change to the local folder where you have cloned the repo and run the following instructions in terminal.

#### The app

Make sure to stop the tests before running the app
1. To start the app:
```bash
make run_app
```

2. To stop the app:
```bash
make stop_app
```

3. To upload invoice files:
```bash
make upload_file file=/path/to/your/file.xlsx
```

4. To visualize the summary table go to: http://localhost:8000/api/summary/


#### The tests
Make sure to stop the app before running the tests
1. To run the tests:
```bash
make tests
```

1. To stop the app:
```bash
make stop_tests
```

### Next Steps:

1. Write exception handling, cases for request status 400 and test (e.g. what happens if the file uploaded is not a csv?, what if the format is not correct?)
2. Make integration tests using the test-db service and initializing the database before running the tests
3. Add the possibility to ask for the summary for a specific customer, passed as query parameter to the UploadInvoiceView
4. Change html/Add Javascript: add a feedback form and a button that calls the upload endpoint and/or refreshes the page

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)