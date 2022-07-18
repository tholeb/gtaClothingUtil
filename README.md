# gtaClothingUtils


## Cloth starting point changer

Lets you change the starting point of a group of cloth type (jbib, accs, etc...) with ease.

For example, if you have `mp_f_freemode_01^accs_diff_016_a_uni.ytd` change it to `mp_f_freemode_01^accs_diff_026_a_uni.ytd` so it will be show at the 25th cloth in game (it starts at 0).

*(Tested with python3 on Linux, don't know for python2)*

## Author
- tholeb <tholeb.fr> : `tholeb#6077`

## Install
either git clone this gist or simply donwload a zip of the file.

## Usage

Add (or retreive) any amount for a given group of cloth. **It MUST be the same cloth type otherwise, it will mess with your outfits.**

```sh
python clothing.py <amount>
```

### Arguments
You can specify the input and the output of the script. By default the input and output folders are `./input` and `./output`.

### Help

If you need any help with this rather simple script you can print the script's help by doing :

```sh
python clothing.py -h
```

You can also contact me on discord : `tholeb#6077`

### Example

```sh
python clothing.py 10
```

Result:
you added 10 to every cloth type you have in the input folder.

```
.
├── input/
│   ├── mp_f_freemode_01^accs_diff_016_a_uni.ytd
│   └── mp_f_freemode_01^accs_016_u.ydd
├── output/
│   ├── mp_f_freemode_01^accs_diff_026_a_uni.ytd
│   └── mp_f_freemode_01^accs_026_u.ydd
└── clothing.py
```

# License

Use this script anywhere you want, for any project, **commercial or not**. 
Do **NOT** redistribute this script without giving this gist's url.
You **CAN** modify this script but, if you want to redistribute it, it **MUST** be a fork of this gist.
Do **NOT** sell this script.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
