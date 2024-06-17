# Build and package for public release
import sys, os

# copy over completed files
# delete temp files

# generate readme html
# copy over readme & screenshot


if __name__ == "__main__":

    target = sys.argv[1]
    print(f'Building for target: {target}')

    # pandoc README.md -f markdown -t html -s -o Test.html
    
    if target == 'windows':
        os.system('cd Source')
        os.system('pip install -r .packages')
        os.system('python -m PyInstaller --noconsole --onefile Viewfinder.py -n Viewfinder --distpath ../Release/Windows')
    
    if target == 'linux':
        os.system('cd Source')
        os.system('pip3 install -r .packages')
        os.system('sudo apt-get install python3-tk -y')
        os.system('python3 -m PyInstaller --noconsole --onefile Viewfinder.py -n Viewfinder --distpath ../Release/Linux')