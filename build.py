# Build and package for public release
import sys, os

# copy over completed files
# delete temp files


if __name__ == "__main__":

    # set target from arg
    target = sys.argv[1]

    if target == 'docs':
        print('--> Building documentation')
        print('Building README...')
        os.system('pandoc README.md -f markdown -t html -s -o Release/Windows/README.html --metadata title="Viewfinder"')
        os.system('pandoc README.md -f markdown -t html -s -o Release/Linux/README.html --metadata title="Viewfinder"')
        print('Copying images...')
        os.system('copy "%~dp0\Screenshot.png" "%~dp0\Release\Windows"')
        os.system('copy "%~dp0\Screenshot.png" "%~dp0\Release\Linux"')
        os.system('copy "%~dp0\Icon.png" "%~dp0\Release\Windows"')
        os.system('copy "%~dp0\Icon.png" "%~dp0\Release\Linux"')
        print('Doc build complete')

    if target == 'windows':
        print('--> Building for Windows')
        os.system('cd Source')
        print('Making sure packages are installed...')
        os.system('pip install -r .packages')
        print('Running PyInstaller...')
        os.system('python -m PyInstaller --noconsole --onefile Viewfinder.py -n Viewfinder --distpath ../Release/Windows')
        print('Windows build complete')
    
    if target == 'linux':
        os.system('cd Source')
        print('Making sure packages are installed...')
        os.system('pip3 install -r .packages')
        os.system('sudo apt-get install python3-tk -y')
        print('Running PyInstaller...')
        os.system('python3 -m PyInstaller --noconsole --onefile Viewfinder.py -n Viewfinder --distpath ../Release/Linux')
        print('Linux build complete')