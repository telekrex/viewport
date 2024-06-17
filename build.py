# Build and package Viewfinder for public release

import sys


### Build from source
# `cd Source`  
# `pip3 install -r Source/.packages`  
# (on linux) `sudo apt-get install python3-tk`
# `python3 -m PyInstaller --noconsole --onefile Viewfinder.py -n Viewfinder`
# copy over completed files
# delete temp files

# generate readme html
# copy over readme & screenshot


if __name__ == "__main__":

    target = sys.argv[1]
    print(f'Building for target: {target}')
    
    if target == 'windows':
        print()