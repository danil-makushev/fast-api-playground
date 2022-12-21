# FastAPI Playground

Basic techniques for working with FastAPI from various tutorials.

## Running the project

`uvicorn index:app --reload`

-   `index` - name of the file
-   `app` - name of the variable with the FastAPI server

FastAPI automatically generates documentation at http://127.0.0.1:8000/docs

### Basic CRUD

`cd basic-crud`

`uvicorn students-crud:app --reload`
