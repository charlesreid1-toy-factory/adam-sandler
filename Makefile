include common.mk

.PHONY: help tox build clean

help:
	@echo "make help       Show this help"
	@echo "make tox        Run all tox test environments"
	@echo "make build      Build source and wheel distributions"
	@echo "make clean      Remove build artifacts and caches"

tox:
	tox

build:
	tox -e build

clean:
	rm -rf build dist *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
