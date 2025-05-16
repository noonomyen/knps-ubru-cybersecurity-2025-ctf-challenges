# Web Application

## 1 [Easy]

```txt
A cloud service provider was attacked by a hacker, causing the entire system to go down and become unavailable. The hacker left a secret message on the website, and you've been assigned to find that hidden message.

Cloud ผู้ให้บริการแห่งหนึ่ง ได้ถูก Hacker โจมตีจนระบบล้มทั้งหมด ไม่สามารถให้บริการได้ และ Hacker คนนั้น ได้ทิ้งข้อความลับเอาไว้ในเว็บนั้น และคุณได้รับหน้าที่ให้ค้นหาข้อความลับดังกล่าวในเว็บไซต์
```

ประเภท Observation

โดย flag จะถูกซ่อนใน HTML หน้าแรก

`web{yPmzsSKvucbU1b3FBxIlEZcz}`

## 2 [Easy]

```txt
We received intel from a spy that the website announcing this information has a hidden file. The only clue we have is that it’s hidden from bots on the internet.

เราได้รับข้อมูลจากสายลับว่า เว็บไซต์ประกาศข้อมูลนี้ มีการซ่อนไฟล์ลับเอาไว้ โดยเบาะแสที่เรามีคือ มันถูกซ่อนจาก bots บน internet
```

ประเภท Observation

โดย flag จะถูกซ่อนใน path ที่ไม่อนุญาตหน้าแรกให้ bot เข้าถึง `robots.txt` ซึ่งจะมีไฟล์ชื่อ flag.txt

`web{m2gVkbfyTFBsI9QvW2FMRl1G}`

## 3 [Easy]

```txt
You are a penetration tester assigned to breach the control panel of a certain website. The client mentioned that if you manage to successfully breach the system, you will find a description meant exclusively for the Admin.

คุณคือผู้ทดสอบเจาะระบบ คุณได้รับหน้าที่ในการเจาะระบบเข้าไปยังหน้า Control Panel ของเว็บแห่งหนึ่ง โดยผู้จ้างระบุว่า ถ้าคุณสามารถเจาะระบบมันได้จริงๆ คุณจะพบกับคำอธิบายเฉพาะ Admin
```

ประเภท Basic Login SQL Injection

code ที่เป็นช่องโหว่

```ts
const user = db.query(`SELECT user_id FROM user WHERE username = '${username}' AND password = '${password}'`).get() as { user_id: number } | null
```

flag จะถูกซ่อนใน column `description` ใน table `user` ของ username `admin` โดยผู้โจมตีต้องใช้ `OR 1=1` ในการทำให้เงื่อนไข password เป็นจริง

``

`web{szNIF6b68zCpInkMhaL4Swmw}`

## 4 [Medium]

```txt
You are a penetration tester. Last time, you were able to access the Admin account with ease. However, the client has now asked you to test the system further by trying to find a user who also has a special description, just like the Admin, without specifying which user it is.

คุณคือผู้ทดสอบเจาะระบบ ในครั้งที่แล้ว คุณสามารถเข้าถึงบัญชี Admin ได้อย่างง่ายดาย แต่ผู้จ้างได้ระบุมาเพิ่มว่า ช่วยลองทดสอบเจาะระบบเพื่อค้นหา User ที่มีคำอธิบายเฉพาะเหมือนๆ Admin ได้ไหม โดยไม่ได้ระบุว่าเป็น User คนไหน
```

ประเภท Basic Login SQL Injection and Offset (Pagination)

code ที่เป็นช่องโหว่

```ts
const user = db.query(`SELECT user_id FROM user WHERE username = '${username}' AND password = '${password}'`).get() as { user_id: number } | null
```

flag จะถูกซ่อนใน column `description` ใน table `user` ของ user คนหนึ่ง โดยผู้โจมตีต้องใช้ `OFFSET` ในการเลื่อนหา user ที่มี flag ใน description

`web{67rFlAjZoT2ilklESiyuBmFr}`

## 5 [Hard]

```txt
We received intelligence that a restaurant menu website has been used to hide a secret message related to decoding illegal data systems. Our sources indicate that the information is stored in the same database as the restaurant menu data. The criminal who hid the secret message thought the restaurant database would not attract attention. The restaurant in question belongs to the relative of the offender and is located in a foreign country. The problem is that the country is not cooperating with us in accessing the location and data. To prove that the encrypted data we seized is indeed illegal, we need to decrypt it.

As a national-level white-hat hacker working behind the scenes for years, you have been tasked with breaching the restaurant website’s database to uncover the secret message used for decryption.

เราได้รับเบาะแสมาว่า เว็บเมนูร้านอาหารแห่งหนึ่งได้ถูกใช้ในการซ่อนข้อความลับที่ใช้ในการถอดระบบข้อมูลผิดกฎหมาย โดยสายลับเราได้ทราบมาว่า มันถูกเก็บในฐานข้อมูลเดียวกันกับข้อมูลเมนูร้านอาหาร โดยคนร้ายที่ซ่อนข้อความลับคิดว่าฐานข้อมูลร้านอาหารไม่น่าจะสะดุดตาใคร และร้านอาหารนี้เป็นร้านอาหารของญาติผู้กระทำความผิด โดยมันตั้งอยู่ที่ต่างประเทศ ซึ่งปัญหาคือประเทศนั้นไม่ให้ความร่วมมือเราในการเข้าถึงสถานที่และข้อมูลนั้น เพื่อพิสูจว่าข้อมูลที่เข้ารหัสที่เรายึดมาได้นั้นเป็นข้อมูลผิดกฎหมายจริง เราจะต้องถอดรหัสมันออกมาให้ได้ โดยเราในฐานะ Hacker สายขาวระดับประเทศที่ทำงานเบื้องหลังอย่างลับๆมานาน ได้รับมอบหมายให้โจมตีเข้าไปยังฐานข้อมูลของเว็บเมนูร้านอาหารแห่งนั้น เพื่อค้นหาข้อความลับที่ใช้ในการถอดรหัส
```

ประเภท Union SQL Injection

code ที่เป็นช่องโหว่

```ts
if (search) menu = db.query(`SELECT * FROM menu WHERE name LIKE '%${search}%'`).all() as Menu[]
```

flag จะถูกซ่อนใน table ชื่อ `flag` ซึ่งไม่มี code ไหนเข้าถึงชื่อ table นี้ โดยผู้โจมตีต้องใช้ `union` แทรกเข้ามาใน parameter `search`

`web{IB9FW5fS1PO2b4DFkZhoDVMN}`
