from glob import glob
import argparse
from operator import length_hint
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

components = ["accs", "berd", "decl", "feet", "hair", "hand", "head", "jbib", "lowr", "task", "teef", "uppr"]
props = ["ears", "eyes", "head", "hip", "lfoot", "lhand", "lwrist", "mouth", "rfoot", "rhand", "rwrist", "unk604819740", "unk2358626934"]


# Loop on every models
for i, path in enumerate([f for f in input if f.endswith('.ydd')]):
    # Get file name
    file = path.split('/')[-1]

    a, b = 1, 2

    # Get the clothing component
    ped, outfit = file.split('^')[0], file.split('^')[1]

    # Get the model type and number
    type, number = outfit.split('_')[0], outfit.split('_')[1]

    # Create components folders
    components_dir = f"{args.output}/{ped}/components"
    [os.makedirs(f"{components_dir}/{component}", exist_ok=True) for component in components]

    # Create props folders
    props_dir = f"{args.output}/{ped}_p/props"
    [os.makedirs(f"{props_dir}/{prop}", exist_ok=True) for prop in props]

    dir = ""

    if type in components:
        dir = components_dir
    elif type in props:
        dir = props_dir
    else:
        print(f"\033[41m{path} is neither a component ({', '.join(components)}) nor a prop ({', '.join(props)}) -- IGNORED\033[0m")
        continue

    num = len(glob(f"{dir}/{type}/*.ydd"))

    os.makedirs(f"{dir}/{type}/{num}", exist_ok=True)
    copy(path, f"{dir}/{type}/{num}.ydd")

    textures = [t for t in input if f"{type}_diff_{number}" in t]

    [copy(v, f"{dir}/{type}/{num}/{k}.ytd") for k, v in enumerate(textures)]

    # Print all the info
    print(f"\033[35m#{num}\033[0m \033[96m{path}\033[0m --> \033[32m{dir}/{type}/{num}.ydd\033[0m\n\
            Textures --> \033[34m{dir}/{type}/{num}/*.ytd\033[0m \033[33m({len(textures)})\033[0m \n")
