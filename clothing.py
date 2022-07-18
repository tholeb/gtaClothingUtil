import sys
import os
import argparse
from glob import glob
from shutil import copy

parser = argparse.ArgumentParser(
    description='''Change the starting number of an addon cloth. \033[31mYou must do it type by type (jbib, accs, etc.).\033[0m''',
    epilog="""Written by tholeb <tholeb.fr>. Not responsible for any damage caused by this program :)""")
parser.add_argument('acc', type=int, default=1, help='The number to accumulate to the texture name. Default to 1')
parser.add_argument('--input', type=str, default='./input', help='The input folder. Default to "./input"')
parser.add_argument('--output', type=str, default='./output', help='The input folder. Default to "./output"')
args = parser.parse_args()


def is_a_texture(name):
    """ 
    Check if it's a texture by counting the number of parts for the model
    :param name: the name of the model
    :return: True if it's a texture, False otherwise
    """
    length = len(name.split('_'))

    if length > 3:
        return True
    else:
        return False


# Get all .ydd and .ytd files in the input folder
input = glob(f'{args.input}/*.ydd') + glob(f'{args.input}/*.ytd')

os.makedirs(args.output, exist_ok=True)

# Loop every files from the input directory
for i, path in enumerate(input):

    # Get file name
    file = path.split('/')[-1]

    # Get ped model
    model = file.split('^')[0]

    # Get the clothing component
    outfit = file.split('^')[1]

    # Check if it's a texture
    texture = is_a_texture(outfit)

    # Get the model type (jbib, accs, etc.)
    type = outfit.split('_')[0]

    if not texture:
        # Model

        # Get the number of the texture and make it an integer
        number = int(outfit.split('_')[1])

        # Destination of the texture : <output>/<model>^<type>_<number>_u.ydd
        dest = f'{args.output}/{model}^{type}_{str(int(number) + args.acc).zfill(3)}_u.ydd'

        # copy the model to the output folder
        copy(path, dest)
    else:
        # Texture

        # Get the number of the texture and make it an integer
        number = int(outfit.split('_')[2])

        textureLetter = outfit.split('_')[3]

        # Destination of the texture : <output>/<model>^<type>_diff_<number>_<textureLetter>_uni.ydd
        dest = f'{args.output}/{model}^{type}_diff_{str(number + args.acc).zfill(3)}_{textureLetter}_uni.ytd'

        # Copy the texture to the output folder
        copy(path, dest)

    # Print all the info
    print(f"\033[35m#{i}\033[0m \033[96m{path}\033[0m : model = \033[32m{model}\033[0m \ outfit = \033[32m{outfit}\033[0m \n\
            texture = \033[33m{texture}\033[0m \n\
            type = \033[33m{type}\033[0m \n\
            number = \033[33m{number}\033[0m --> \033[32m{number + args.acc}\033[0m \n\
            Dest = \033[31m{dest}\033[0m\n")
