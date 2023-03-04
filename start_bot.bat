@echo off

call %~dp0Dulish_one_bot\venv\Scripts\activate

cd %~dp0Dulish_one_bot\venv

set TOKEN=

python main.py

pause