# Network

## 1 [Easy]

เป็น packet dump HTTP โดยให้หา password ของ user `admin`

## 2 [Easy]

เป็น packet dump HTTP ที่ผู้ใช้เข้าเว็บหนึ่งแล้ว load ภาพ

## 3 [Easy]

เป็น packet dump HTTP ที่มีผู้ไม่หวังดีโจมตี โดยให้หาว่า IP คืออะไร

## 3 [Medium]

เป็น packet dump HTTP การสนทนาหนึ่งในเว็บหนึ่งโดยมีไฟล์ปริศนา `.zip` โดยให้เรานำ password ที่ได้ในการสนทนามาเปิด

## 4 [Medium]

เป็น syslog โดยให้หาว่าผู้โจมตีคือ IP อะไรและพยายามโจมตี user อะไร

## 5 [Hard]

เป็น packet dump โดยให้หาว่าใครเป็นผู้โจมตีทำให้ internet ไม่สามารถใช้งานได้

## 6 [Hard]

เป็น packet dump DNS query ที่ query subdomain เป็น hex โดยใช้ผู้สืบหาว่าผู้ไม่หวังดีพยายามส่งอะไรออกไป (DNS Data Exfiltration)

## 7 [Hard]

You demonstrated cracking the Wi-Fi password of a household to show that using a phone number as a password is insecure, as you're confident the password is a Thai personal phone number.

To speed up the process, the prefix of the number is `091`.

คุณได้ทำการแสดง crack password wifi บ้านหลังหนึ่ง เพื่อให้เห็นว่า การใช้เบอร์เป็น password นั้นไม่ปลอดภัย โดยคุณมั่นใจว่า password คือเบอร์โทร (เลขเบอร์โทรส่วนบุคคลในประเทศไทย)

เพื่อความรวมเร็ว prefix เบอร์คือ `091`

`net{0912345678}`
