# plus-twisty-converter
A simple Python3 script to convert **plusTimer**'s history data to **Twisty Timer**'s backup format for easier import/export.

## Instructions
- **Rooted Android Devices**
    - Copy the `.json` files in `/data/data/com.pluscubed.plustimer/files/` using any root explorer, transfer them to your PC and run the script on them. Or copy them to your internal storage and run the script using a terminal emulator like `Termux` after installing Python3.
- **Non-Rooted Android Devices**
    - Enable USB Debugging on your device and connect your mobile to a PC.
    - Verify that the device is connected using `adb devices`. (There are a lot of tutorials in detail for setting up ADB on Windows, Mac, and *nix. I am not going to discuss it here.)
    - Run `adb backup -f plusTimer.ab -apk com.pluscubed.plustimer`
    - Unlock your phone, don't enter any password and select `Back Up My Data`.
    - Run `dd if=plusTimer.ab bs=4K iflag=skip_bytes skip=24 | zlib-flate -uncompress > plusTimer.tar`
    - Run `tar -xvf plusTimer.tar`
    - The `.json` files will be there in `./apps/com.pluscubed.plustimer/f/`

## Installation
Clone the repository with
```
git clone https://github.com/UtkarshKunwar/plus-twisty-converter.git
```
or just download the script and use it directly with python3 or as an executable script with chmod.

## Usage
```
usage: python3 plus-twisty-converter.py [-h]
                                [-p {2x2 ,3x3 ,4x4 ,5x5 ,6x6 ,7x7 , clock, mega, pyra, skewb, sq1}]
                                [-c {Normal, OH, BLD, Feet}]
                                input_file output_file

A utility to convert plusTimer .json data to importable Twisty Timer format.
positional arguments:
  input_file            Path to the plusTimer .json file.
  output_file           Path to the output Twisty Timer file.

optional arguments:
  -h, --help            show this help message and exit
  -p, --puzzle {2x2, 3x3, 4x4, 5x5, 6x6, 7x7, clock, mega, pyra, skewb, sq1}
                        Select the type of puzzle of the input_file. (Default = 3x3)
  -c, --category {Normal, OH, BLD, Feet}
                        Select the category of the puzzle. (Default = Normal)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
