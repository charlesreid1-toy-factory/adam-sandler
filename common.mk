SHELL=/bin/bash

ifeq ($(shell which tox),)
$(error Please install tox or activate your virtual environment before running make commands)
endif
