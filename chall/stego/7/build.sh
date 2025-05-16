#!/usr/bin/bash

set -e

zip ./stego-7-inside.zip ./stego-7.txt
gcc ./stego-7.c -o ./stego-7
objcopy --add-section .secret=stego-7-inside.zip stego-7 stego-7
chmod +x stego-7
zip -r ./stego-7.zip ./stego-7
