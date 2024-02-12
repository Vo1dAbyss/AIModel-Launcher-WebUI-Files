@echo off
title DialoGPT-medium-GPT4
color 0F
echo ------------ DOWNLOADING GIT REPOSITORY ------------
echo from time import sleep; sleep(1) | python
git clone https://github.com/Vo1dAbyss/DialoGPT-medium-GPT4-Interface-Files.git
cd DialoGPT-medium-GPT4-Interface-Files
echo ------------ INSTALLING REQUIREMENTS... ------------
echo from time import sleep; sleep(1) | python
pip install -r requirements.txt
echo ------------ LAUNCHING WEBUI.PY... -----------------
echo from time import sleep; sleep(1) | python
"Python" "webui.py"