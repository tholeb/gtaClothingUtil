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

    # Get the clothing component and outfit name
    ped, outfit = file.split('^')[0], file.split('^')[1]

    # Ignore non valid items (not a prop or component)
    if outfit.split('_')[0] not in components and outfit.split('_')[1] not in props:
        print(f"\033[41m{path} is neither a component ({', '.join(components)}) nor a prop ({', '.join(props)}) -- IGNORED\033[0m")
        continue

    # Create components/props folders
    ped_dir = f"{args.output}/{ped}"
    if ped.endswith('_p'):
        # It's a Prop

        # Get the model type and number
        type, number = outfit.split('_')[1], outfit.split('_')[2]

        dir = f"{ped_dir}/props"
        [os.makedirs(f"{dir}/{prop}", exist_ok=True) for prop in props]
    else:
        # It's a Component

        # Get the model type and number
        type, number = outfit.split('_')[0], outfit.split('_')[1]

        dir = f"{ped_dir}/components"
        [os.makedirs(f"{dir}/{component}", exist_ok=True) for component in components]

    num = len(glob(f"{dir}/{type}/*.ydd"))

    os.makedirs(f"{dir}/{type}/{num}", exist_ok=True)
    copy(path, f"{dir}/{type}/{num}.ydd")

    textures = [t for t in input if f"{type}_diff_{number}" in t]

    [copy(v, f"{dir}/{type}/{num}/{k}.ytd") for k, v in enumerate(textures)]

    # Print all the info
    print(f"\033[35m#{num}\033[0m \033[96m{path}\033[0m --> \033[32m{dir}/{type}/{num}.ydd\033[0m\n\
            Textures --> \033[34m{dir}/{type}/{num}/*.ytd\033[0m \033[33m({len(textures)})\033[0m \n")
