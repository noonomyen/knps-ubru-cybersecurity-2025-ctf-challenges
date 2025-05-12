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

> TODO: steghide

## 7 [Medium]

> TODO: binwalk

## 8 [Hard]

> TODO: images file subfix name

## 9 [Hard]

> TODO: LSB
