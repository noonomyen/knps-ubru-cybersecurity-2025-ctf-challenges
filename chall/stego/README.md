# Steganography

## 1 [Easy]

```sh
ffmpeg -f lavfi -i color=c=black:s=1280x720:d=10 -vf "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='stego{d154pp3423d_8u7_y0u_c4n_57111_533_m3}':fontcolor=white@0.05:x=10:y=H-th-10:fontsize=24" -c:v libx264 -t 10 stego-1.mp4
```

`stego{d154pp3423d_8u7_y0u_c4n_57111_533_m3}`

## 2 [Easy]

```sh
ffmpeg -f lavfi -i color=c=black:s=1280x720:d=10 -c:v libx264 -t 10 stego-2.mp4
echo "stego{c4n_y0u_23411y_d0_7h47}" >> stego-2.mp4
```

`stego{c4n_y0u_23411y_d0_7h47}`

## 3 [Easy]

```sh
ffmpeg -i ../assets/image.png -vf "drawtext=text='stego{3427h_15_50_834u71fu1}':fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:fontcolor=white@0.03:fontsize=24:x=W-tw-10:y=H-th-10" -c:v png stego-3.png
```

`stego{3427h_15_50_834u71fu1}`

## 4 [Easy]

```sh
exiftool -Comment="stego{m374d474}" -o stego-4.png ../assets/image.png
```

`stego{m374d474}`

## 5 [Easy]

```sh
pdflatex ./pdf.tex
```

flag will not use spaces. If found, replace them with an underscore (_).

`stego{813nd1n9_1n_huh}`

## 6 [Medium]

คนที่สร้างมันกล่าวว่า password คือสิ่งที่คุณเห็น

The creator said the password is what you see.

pass: `earth`

steghide

`stego{7h3_1m493_h45_50m37h1n9_h1dd3n}`

## 7 [Medium]

Some parts of it aren't referenced directly, but it's said that they can be detected using magic numbers.

มีบางส่วนในนั้นที่ไม่มีการเรียกใช้ แต่ว่ากันว่าสามารถ scan เจอจาก magic number ได้?

binwalk

`stego{1n51d3_0f_1n51d3}`

## 8 [Hard]

`ON2GKZ3PPM2TG4LVGNXGGM35`

`stego{53qu3nc3}`
