![Static Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Static Badge](https://img.shields.io/static/v1?style=for-the-badge&message=Celery&color=37814A&logo=Celery&logoColor=FFFFFF&label)
![Static Badge](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white) 
![Static Badge](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white) 

# Invoice Totals  APP

This project is a web application that ingests invoice data from a spreadsheet and saves it to a database. 
It then has a web service that adds up the totals on a per-revenue source basis and displays on a page the Value, Advance and Expected Fee.

### Installation
Just be sure to have docker installed and running and download the repo.

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



 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)