# Web Application

## 1 [Easy]

ประเภท Observation

โดย flag จะถูกซ่อนใน HTML หน้าแรก

## 2 [Easy]

ประเภท Observation

โดย flag จะถูกซ่อนใน path ที่ไม่อนุญาตหน้าแรกให้ bot เข้าถึง `robots.txt` ซึ่งจะมีไฟล์ชื่อ flag.txt

## 3 [Easy]

ประเภท Basic Login SQL Injection

code ที่เป็นช่องโหว่

```ts
const user = db.query(`SELECT user_id FROM user WHERE username = '${username}' AND password = '${password}'`).get() as { user_id: number } | null
```

flag จะถูกซ่อนใน column `description` ใน table `user` ของ username `admin` โดยผู้โจมตีต้องใช้ `OR 1=1` ในการทำให้เงื่อนไข password เป็นจริง

## 4 [Medium]

ประเภท Basic Login SQL Injection and Offset (Pagination)

code ที่เป็นช่องโหว่

```ts
const user = db.query(`SELECT user_id FROM user WHERE username = '${username}' AND password = '${password}'`).get() as { user_id: number } | null
```

flag จะถูกซ่อนใน column `description` ใน table `user` ของ user คนหนึ่ง โดยผู้โจมตีต้องใช้ `OFFSET` ในการเลื่อนหา user ที่มี flag ใน description

## 5 [Hard]

ประเภท Union SQL Injection

code ที่เป็นช่องโหว่

```ts
if (search) menu = db.query(`SELECT * FROM menu WHERE name LIKE '%${search}%'`).all() as Menu[]
```

flag จะถูกซ่อนใน table ชื่อ `flag` ซึ่งไม่มี code ไหนเข้าถึงชื่อ table นี้ โดยผู้โจมตีต้องใช้ `union` แทรกเข้ามาใน parameter `search`
