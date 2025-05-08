# Wi-Fi Cracking LAB

flag: `net{0912345678}`

## Access point mode

```sh
sudo chown $USER /dev/ttyUSB0 && pio run -t upload -e ap --upload-port /dev/ttyUSB0
```

## Station mode

```sh
sudo chown $USER /dev/ttyUSB0 && pio run -t upload -e sta --upload-port /dev/ttyUSB0
```

---

## Blink mode (board testing)

```sh
sudo chown $USER /dev/ttyUSB0 && pio run -t upload -e blink --upload-port /dev/ttyUSB0
```
