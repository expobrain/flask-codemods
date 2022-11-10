.SILENT: fmt check lint bandit

fmt:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade \
			--exit-zero-even-if-changed \
			--keep-runtime-typing \
			--py37-plus \
			{} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		codemods tests
	isort --profile black .
	black .

bandit:
	bandit -q -r codemods
	bandit -q -lll -r tests

check: bandit
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade \
			--keep-runtime-typing \
			--py37-plus \
			{} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		codemods tests
	isort --profile black -c .
	black --check .

lint: bandit
	mypy codemods
	flake8 .

test:
	pytest -x --cov=core --cov=codemods --cov-fail-under=90

install:
	poetry install --sync
