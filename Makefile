.PHONY: all run init doc
all:
	@echo "Commands:"
	@echo "	run [file]:	runs the code (with an optional input file)"
	@echo "	run-uv [file]:	runs the code (with an optional input file) using uv"
	@echo "	init:		setup the Python env if not using uv"
	@echo "	doc:		compile the README pdf"

run: ARGS = $(filter-out $@,$(MAKECMDGOALS))
run:
	./.venv/bin/python src/main.py $(ARGS)

run-uv: ARGS = $(filter-out $@,$(MAKECMDGOALS))
run-uv:
	uv run src/main.py $(ARGS)

init:
	python -m venv .venv

doc:
	pandoc -N README.md -o README.pdf --pdf-engine lualatex
