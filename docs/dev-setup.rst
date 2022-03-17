Development Environment Setup
=============================

Add a `.env` file in the top level directory and include:

  DATABASE_URL=postgresql:///numbers_api

You'll need Python3 and PostgreSQL ::

  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

  createdb numbers_api