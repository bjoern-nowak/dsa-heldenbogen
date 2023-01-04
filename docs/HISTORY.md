# History of project setup

* Init project with poetry: `poetry new dsa-heldenbogen`
* Include .venv folder in project root: `poetry config virtualenvs.in-project true --local`
* Add framework for answer set programming: `poetry add clingo`
* Add framework for web development: `poetry add fastapi`
* Add framework for web server: `poetry add uvicorn[standard]` (alternative: hypercorn)
