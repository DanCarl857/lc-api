### API

## Requirements

* You should have a `MySQL` database setup
* Update the `.env` file with your credentials and database name
* Follow the [database README.md](https://github.com/DanCarl857/lc-api/blob/main/db.md) to properly set up your database

## Getting Started

First, run the development server:

```bash
cd api
# install all the dependencies
pip install
# then
uvicorn main:app --reload
```

* Visit `http://127.0.0.1:8000/api/v1/docs` to access the docs
