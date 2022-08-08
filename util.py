from glob import glob
import argparse
from os import makedirs, remove
from platform import system
from shutil import copy
from re import search
from shared.functions import *

p = argparse.ArgumentParser(
    description="Create the appropriate folder tree for gtaUtil to add addon clothing to your GTA V (FiveM) server.",
    epilog="Written by tholeb <tholeb.fr>")
p.add_argument('-i', '--input', type=str, default='./input', metavar="\033[32m./input_folder\033[0m", help='The input folder. Default to "./input"')
p.add_argument('-o', '--output', type=str, default='./output', metavar="\033[32m./output_folder\033[0m", help='The input folder. Default to "./output"')
p.add_argument('-A', '--acc', type=str, default='', metavar="\033[32m\"accs=x,jbib=y,...\"\033[0m",
               help='Add a specific amount to a component/prop group so you can merge multiple clothing packs.')
p.add_argument('-D', '--delete', action='store_true', help='Delete the input content afterwords.')
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
    ped, outfit = clean_ped_name(file.split('^')[0], is_a_prop(file.split('^')[0])), file.split('^')[1].split('.')[0]
    group, number = outfit.split('_')[0], outfit.split('_')[1]

    ped_dir = f"{args.output}/{ped}"
    texture_files = f"{ped}^{group}_diff_{number}"

    # Change the group and number according to a prop
    if is_a_prop(ped):
        group, number = outfit.split('_')[1], outfit.split('_')[2]
        texture_files = f"{ped}^p_{group}_diff_{number}"

    # Ignore non valid items (not a prop or component)
    if group not in components and group not in props:
        print(f"\033[41m{path} is neither a component ({', '.join(components)}) nor a prop ({', '.join(props)}) -- IGNORED\033[0m")
        continue

    # Create components/props folders
    if ped.endswith('_p'):
        # Create the dirs where we'll store each prop
        dir = f"{ped_dir}/props"
        [makedirs(f"{dir}/{prop}", exist_ok=True) for prop in props]
    else:
        # Create the dirs where we'll store each component
        dir = f"{ped_dir}/components"
        [makedirs(f"{dir}/{component}", exist_ok=True) for component in components]

    # The folder's number (each component/prop need to have a single number for each group. e.g 0.ydd)
    num = len(glob(f"{dir}/{group}/*.ydd"))

    # search for a patten in the acc option
    if search('^(.*=[0-9]*,?)$', args.acc):
        incr = [a for a in args.acc.split(',') if group in a]

        # The current group has a matching amount, so we increment the value
        if len(incr) == 1:
            num += int(incr[0].split('=')[1])

    # Copy the model to the appropriate folder and create it's textures folder
    makedirs(f"{dir}/{group}/{num}", exist_ok=True)
    copy(path, f"{dir}/{group}/{num}.ydd")

    # Get all the textures for a matching model
    textures = [t for t in input if texture_files in t]

    # And copy them to the appropriate folder
    [copy(v, f"{dir}/{group}/{num}/{k}.ytd") for k, v in enumerate(textures)]

    # Finally, Print some the info
    print(f"\033[35m#{i}\033[0m \033[96m{path}\033[0m --> \033[32m{dir}/{group}/{num}.ydd\033[0m\n\
            Textures --> \033[34m{dir}/{group}/{num}/*.ytd\033[0m \033[33m({len(textures)})\033[0m \n\
            Ped --> \033[34m{ped}\033[0m")

if args.delete:
    for f in input:
        remove(f)
