from glob import glob
import argparse
from os import makedirs, remove
from platform import system
from shutil import copy

from shared.functions import *

p = argparse.ArgumentParser(
    description='''move a group to it's corresponding output folder \033[31mYou must do it group by group (jbib, accs, etc.).\033[0m''',
    epilog="""Written by tholeb <tholeb.fr>""")
p.add_argument('-i', '--input', type=str, default='./input', help='The input folder. Default to "./input"')
p.add_argument('-o', '--output', type=str, default='./output', help='The input folder. Default to "./output"')
p.add_argument('--dlc', action='store_true', help='Attempt to get rid of DLC name from a ped (e.g. mp_f_freemode_01_mp_f_bikerdlc_01 to mp_f_freemode_01)')
p.add_argument('-D', '--delete', action='store_true', help='Delete the input content.')
args = p.parse_args()

# Get all .ydd and .ytd files in the input folder
input = glob(f'{args.input}/*.ydd') + glob(f'{args.input}/*.ytd')

components = ["accs", "berd", "decl", "feet", "hair", "hand", "head", "jbib", "lowr", "task", "teef", "uppr"]
props = ["ears", "eyes", "head", "hip", "lfoot", "lhand", "lwrist", "mouth", "rfoot", "rhand", "rwrist", "unk604819740", "unk2358626934"]


# Loop on every models
for i, path in enumerate([f for f in input if f.endswith('.ydd')]):

    # Get file name
    if system() == "Linux":
        file = path.split('/')[-1]
    else:
        file = path.split('\\')[-1]

    # Get the clothing component and outfit name
    ped, outfit = file.split('^')[0], file.split('^')[1].split('.')[0]

    # Ignore non valid items (not a prop or component)
    if outfit.split('_')[0] not in components and outfit.split('_')[1] not in props:
        print(f"\033[41m{path} is neither a component ({', '.join(components)}) nor a prop ({', '.join(props)}) -- IGNORED\033[0m")
        continue

    # Attempt to get rid of the DLC name
    if args.dlc and ped.startswith('mp_'):
        p = ped.split('_')

        if outfit.split('_')[0] in components:
            ped = '_'.join(p[:4])
        elif outfit.split('_')[1] in props:
            ped = '_'.join(p[:5])

    # Create components/props folders
    ped_dir = f"{args.output}/{ped}"
    if ped.endswith('_p'):
        # It's a Prop

        # Get the model type and number
        type, number = outfit.split('_')[1], outfit.split('_')[2]

        # Create the dirs where we'll store each prop
        dir = f"{ped_dir}/props"
        [makedirs(f"{dir}/{prop}", exist_ok=True) for prop in props]
    else:
        # It's a Component

        # Get the model type and number
        type, number = outfit.split('_')[0], outfit.split('_')[1]

        # Create the dirs where we'll store each component
        dir = f"{ped_dir}/components"
        [makedirs(f"{dir}/{component}", exist_ok=True) for component in components]

    # The folder's number (each component/prop need to have a single number for each type. e.g 0.ydd)
    num = len(glob(f"{dir}/{type}/*.ydd"))

    # Copy the model to the appropriate folder and create it's textures folder
    makedirs(f"{dir}/{type}/{num}", exist_ok=True)
    copy(path, f"{dir}/{type}/{num}.ydd")

    # Get all the textures for a matching model
    textures = [t for t in input if f"{type}_diff_{number}" in t]
    print(type, number, f"{type}_diff_{number}", textures)

    # And copy them to the appropriate folder
    [copy(v, f"{dir}/{type}/{num}/{k}.ytd") for k, v in enumerate(textures)]

    # Finally, Print some the info
    print(f"\033[35m#{i}\033[0m \033[96m{path}\033[0m --> \033[32m{dir}/{type}/{num}.ydd\033[0m\n\
            Textures --> \033[34m{dir}/{type}/{num}/*.ytd\033[0m \033[33m({len(textures)})\033[0m \n\
            Ped --> \033[34m{ped}\033[0m")

if args.delete:
    for f in input:
        remove(f)
