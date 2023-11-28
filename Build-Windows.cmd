@echo off
echo locating source
cd source
echo compiling...
python -m PyInstaller --onedir new.py -n Viewfinder
pause