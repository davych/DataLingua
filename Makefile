# Makefile
.PHONY: py-run

py-run:
	cd ./agent-py && uv run python main.py