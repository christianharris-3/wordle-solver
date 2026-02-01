# Wordle Solver

A simple wordle solver, made cus I got bored of playing wordle properly.

Wordlist was taken from: https://github.com/dwyl/english-words

## How to run

requirements:
```bash
python3 -m venv venv
source venv/bin/activate
pip install pygame
pip install uipygame
```
run main file:
```bash
python3 main.py
```
add wordle command
```bash
wordle() {
	nohup bash -c '
		source ~/**path to solver**/wordle-solver/venv/bin/activate
		python3 ~/**path to solver**/wordle-solver/main.py
	' bash "$@" > /dev/null 2>&1 &
}
```
