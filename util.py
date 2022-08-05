from glob import glob
import argparse
import os
from shutil import copy

from shared.functions import *

parser = argparse.ArgumentParser(
    description='''move a group to it's corresponding output folder \033[31mYou must do it group by group (jbib, accs, etc.).\033[0m''',
    epilog="""Written by tholeb <tholeb.fr>""")
parser.add_argument('--input', type=str, default='./input', help='The input folder. Default to "./input"')
parser.add_argument('--output', type=str, default='./output', help='The input folder. Default to "./output"')
args = parser.parse_args()

# Get all .ydd and .ytd files in the input folder
input = glob(f'{args.input}/*.ydd') + glob(f'{args.input}/*.ytd')

[os.makedirs(f'{args.output}/{group}', exist_ok=True) for i, group in enumerate(["accs", "berd", "decl", "feet", "hair", "hand", "head", "jbib", "lowr", "task", "teef", "uppr" ])]

# Loop on every models
for i, path in enumerate([f for f in input if f.endswith('.ydd')]):
    # Get file name
    file = path.split('/')[-1]

    # Get the clothing component
    outfit = file.split('^')[1]

    # Get the model group (jbib, accs, etc.)
    group = outfit.split('_')[0]

    # Get the number of the texture and make it an integer
    number = outfit.split('_')[1]

    folder = f"{args.output}/{group}"

    os.makedirs(f"{folder}/{i}", exist_ok=True)
    copy(path, f"{folder}/{i}.ydd")

    textures = [t for t in input if f"{group}_diff_{number}" in t]

    [copy(v, f"{folder}/{i}/{k}.ytd") for k, v in enumerate(textures)]

    # Print all the info
    print(f"\033[35m#{i}\033[0m \033[96m{path}\033[0m --> \033[32m{folder}/{i}.ydd\033[0m\n\
            Textures --> \033[34m{folder}/{i}/*.ytd\033[0m \033[33m({len(textures)})\033[0m \n")
