# Build and package for public release
import sys, os

# copy over completed files
# delete temp files


if __name__ == "__main__":

    # set target from arg
    target = sys.argv[1]

    if target == 'docs':
        # [!] It is intended to run docs
        # build on Windows -- reason is
        # because of the path formats,
        # I am too lazy to write different
        # versions. Just run docs and windows
        # together during build process -- the
        # assets as you can see go to both folders.
        print('--> Building documentation')
        print('Building README...')
        os.system('pandoc README.md -f markdown -t html -s -o Release/Windows/README.html --metadata title="viewport"')
        os.system('pandoc README.md -f markdown -t html -s -o Release/Linux/README.html --metadata title="viewport"')
        print('Copying assets...')
        os.system('copy "%~dp0\Screenshot.png" "%~dp0\Release\Windows"')
        os.system('copy "%~dp0\Screenshot.png" "%~dp0\Release\Linux"')
        os.system('copy "%~dp0\Source\icon.png" "%~dp0\Release\Windows"')
        os.system('copy "%~dp0\Source\icon.png" "%~dp0\Release\Linux"')
        os.system('copy "%~dp0\Source\icon.ico" "%~dp0\Release\Windows"')
        os.system('copy "%~dp0\Source\icon.ico" "%~dp0\Release\Linux"')
        os.system('copy "%~dp0\Source\NoImage.png" "%~dp0\Release\Windows"')
        os.system('copy "%~dp0\Source\NoImage.png" "%~dp0\Release\Linux"')
        print('Doc build complete')

    if target == 'windows':
        print('--> Building for Windows')
        os.system('cd Source')
        print('Making sure packages are installed...')
        os.system('pip install -r .packages')
        print('Running PyInstaller...')
        os.system('python -m PyInstaller --noconsole --onefile viewport.py -n viewport --distpath ../Release/Windows')
        print('Windows build complete')
    
    if target == 'linux':
        os.system('cd Source')
        print('Making sure packages are installed...')
        os.system('pip3 install -r .packages')
        os.system('sudo apt-get install python3-tk -y')
        print('Running PyInstaller...')
        os.system('python3 -m PyInstaller --noconsole --onefile viewport.py -n viewport --distpath ../Release/Linux')
        print('Linux build complete')