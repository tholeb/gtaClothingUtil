# gtaClothingUtils


## Organise outfits/props in [GTAUtil](https://github.com/indilo53/gtautil) folder structure

Let's say you have some outfits (or props) :

```
input
├── mp_f_freemode_01^accs_026_u.ydd
├── mp_f_freemode_01^accs_027_u.ydd
├── mp_f_freemode_01^accs_diff_026_a_uni.ytd
├── mp_f_freemode_01^accs_diff_026_b_uni.ytd
├── mp_f_freemode_01^accs_diff_027_a_uni.ytd
├── mp_f_freemode_01^accs_diff_027_b_uni.ytd
└── mp_f_freemode_01^accs_diff_027_c_uni.ytd
```

when you run the script, it will output this : 
```
output
└── mp_f_freemode_01
    └── components
        ├── accs
        │   ├── 0
        │   │   ├── 0.ytd
        │   │   └── 1.ytd
        │   ├── 0.ydd
        │   ├── 1
        │   │   ├── 0.ytd
        │   │   ├── 1.ytd
        │   │   └── 2.ytd
        │   └── 1.ydd
```

This folder structure is required if you want to turn a replace outfit into an addon outfit.

### Usage 

```sh
python3 util.py
```

See the `--help` option for the manual
```sh
python3 util.py --help
```

# Author
- tholeb <tholeb.fr> : `tholeb#6077`

# License

Use this script anywhere you want, for any project, **commercial or not**. 
Do **NOT** redistribute this script without giving this repo's url.
You **CAN** modify this script but, if you want to redistribute it, it **MUST** be a fork of this repo.
Do **NOT** sell this script.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
