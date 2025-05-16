# Steganography

## 1 [Easy]

```sh
ffmpeg -f lavfi -i color=c=black:s=1280x720:d=10 -vf "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='stego{4YUeBJesR2ZeZc8j4PwmLenG}':fontcolor=white@0.05:x=10:y=H-th-10:fontsize=24" -c:v libx264 -t 10 stego-1.mp4
```

`stego{4YUeBJesR2ZeZc8j4PwmLenG}`

## 2 [Easy]

```sh
ffmpeg -f lavfi -i color=c=black:s=1280x720:d=10 -c:v libx264 -t 10 stego-2.mp4
echo "stego{B7dfkDqN4nRLmCinZgbd8AR7}" >> stego-2.mp4
```

`stego{B7dfkDqN4nRLmCinZgbd8AR7}`

## 3 [Easy]

```sh
ffmpeg -i ../assets/image.png -vf "drawtext=text='stego{UIoA7ZbpJRFXQluM3EdtXWYl}':fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:fontcolor=white@0.03:fontsize=24:x=W-tw-10:y=H-th-10" -c:v png stego-3.png
```

`stego{UIoA7ZbpJRFXQluM3EdtXWYl}`

## 4 [Easy]

```sh
exiftool -Comment="stego{VE4woGMgWfP5cAp6sQKE4vX8}" -o stego-4.png ../assets/image.png
```

`stego{VE4woGMgWfP5cAp6sQKE4vX8}`

## 5 [Easy]

```sh
pdflatex ./pdf.tex
```

flag will not use spaces.

`stego{JU1si2XO5izv6uX9sK0YThRC}`

## 6 [Medium]

คนที่สร้างมันกล่าวว่า password คือสิ่งที่คุณเห็น

The creator said the password is what you see.

pass: `earth`

steghide

```sh
convert ../assets/image.png image.jpg
steghide embed -cf ./image.jpg -ef ./stego-6.txt
rm ./image.jpg
```

`stego{WH8mnTMV5BF4IMKSyNToVrpJ}`

## 7 [Hard]

Some parts of it aren't referenced directly, but it's said that they can be detected using magic numbers.

มีบางส่วนในนั้นที่ไม่มีการเรียกใช้ แต่ว่ากันว่าสามารถ scan เจอจาก magic number ได้?

binwalk

`stego{Jcld7CQSW3kn65gaSylyTu2d}`

## 8 [Hard]

`ON2GKZ3PPNQW46KLINHHASCUMRIDMODYJNLUY6S2LFVHKNTDPU`

`stego{anyKCNpHTdP68xKWLzZYju6c}`
