PYTHON = C:\Users\abhi0\anaconda3\python
MYPY = C:\Users\abhi0\anaconda3\envs\abhishek\Scripts\mypy
BLACK = C:\Users\abhi0\anaconda3\envs\abhishek\Scripts\black
CC = clang++

.PHONY = format run 

all: format type_check run_py

format:
	@echo Formatting the source file with black...
	${BLACK} ${FNAME}
	@echo.

type_check:
	@echo Checking for type issues....
	${MYPY} ${FNAME}
	@echo.

run_py:
	@echo Running ${FNAME}!
	@echo.
	${PYTHON} ${FNAME}

run_cpp:
	@echo Running ${FNAME}!
	@echo.
	${CC} ${FNAME} && a.exe 

run_c:
	@echo Running ${FNAME}!
	@echo.
	gcc ${FNAME}


