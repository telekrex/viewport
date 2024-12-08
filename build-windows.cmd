python -m PyInstaller --noconsole --onefile viewport.py -n Viewport --icon icon.ico --add-data=assets:.
pandoc -s -o "dist/Read me!.html" "README.md"
copy "%~dp0\Screenshot.png" "%~dp0\dist"
copy "%~dp0\NoImage.png" "%~dp0\dist"