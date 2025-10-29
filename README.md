# Online Student Attendance Management System

---

## English Version

### Project Description
The **Online Student Attendance Management System** is a web-based application designed to automate the tracking and management of student attendance in educational institutions.  

Traditionally, teachers manually record student attendance, which is time-consuming and prone to errors. This system fully digitalizes the process and provides **efficient, accurate, and real-time attendance management**.

---

### Features
- **User Authentication:** Login and signup for Admin, Teacher, and Student.
- **Mark Attendance:** Teachers can record student attendance for each class.
- **Attendance Reports:** Admins and Teachers can view detailed reports of students.
- **Chart Visualization:** Attendance data is displayed in **bar charts** for better understanding.
- **CSV Export:** Teachers can download attendance reports as CSV files.
- **Real-time Database Updates** for accurate tracking.
- **Notifications:** Alerts for students with excessive absences.

---

### Users
- **Admin:** Manages the system and user accounts.
- **Teacher:** Records attendance, views reports, and charts.
- **Student:** Can view their own attendance history.

---

### Technology Stack
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Backend:** Python, Django
- **Database:** SQLite (or MySQL)
- **Hosting:** Local server or Cloud (AWS, Firebase, etc.)
- **Charts:** Chart.js

---

### Project Structure
```
attendance_system/
├── attendance/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── attendance/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── mark_attendance.html
│   │       ├── report.html
│   │       ├── login.html
│   │       └── signup.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── attendance_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```

---



### How to Run
1. Clone the repository:
```bash
git clone <repository-url>
```
2. Navigate to the project directory:
```bash
cd attendance_system
```
3. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Apply migrations:
```bash
python manage.py migrate
```
6. Run the development server:
```bash
python manage.py runserver
```
7. Open your browser and go to:
```
http://127.0.0.1:8000/
```

---


### Loyihaning Tavsifi
**Online Student Attendance Management System** — bu web-asosli dastur bo‘lib, ta’lim muassasalarida talabalar davomatini avtomatik tarzda kuzatish va boshqarish uchun mo‘ljallangan.  

An’anaviy usulda o‘qituvchilar davomatni qo‘lda belgilaydi, bu esa vaqtni oladi va xatolik ehtimolini oshiradi. Ushbu tizim jarayonni to‘liq raqamlashtiradi va **tejamkor, aniq va real vaqt rejimida davomat boshqaruvi**ni ta’minlaydi.

---

### Asosiy Funksiyalar
- **Foydalanuvchi Avtorizatsiyasi:** Admin, Teacher va Student uchun login/signup.
- **Davomatni Belgilash:** O‘qituvchilar har bir dars uchun davomatni belgilaydi.
- **Hisobotlar:** Admin va Teacherlar talabalar davomatini ko‘rishlari mumkin.
- **Grafiklar:** Davomat ma’lumotlari bar chart orqali vizual ko‘rinadi.
- **CSV Yuklab olish:** Teacherlar hisobotlarni CSV fayl sifatida yuklab oladi.
- **Real-time Database Updates:** Davomatning real vaqt rejimida yangilanishi.
- **Ogohlantirishlar:** Talabalarning ko‘p dars qoldirganda xabar berish.

---

### Foydalanuvchilar
- **Admin:** Tizim va foydalanuvchilarni boshqaradi.
- **Teacher:** Davomatni belgilaydi, hisobotlar va grafiklarni ko‘radi.
- **Student:** O‘z davomat tarixini ko‘radi.

---

### Texnologiyalar
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Backend:** Python, Django
- **Database:** SQLite (yoki MySQL)
- **Hosting:** Local server yoki Cloud (AWS, Firebase va h.k.)
- **Grafiklar:** Chart.js

---

### Loyihaning Tuzilishi
```
attendance_system/
├── attendance/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── attendance/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── mark_attendance.html
│   │       ├── report.html
│   │       ├── login.html
│   │       └── signup.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── attendance_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```

---

### Loyihani Ishga Tushirish
1. Repository ni klonlash:
```bash
git clone <repository-url>
```
2. Loyihaga kirish:
```bash
cd attendance_system
```
3. Virtual environment yaratish va faollashtirish:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```
4. Paketlarni o‘rnatish:
```bash
pip install -r requirements.txt
```
5. Migrations qo‘llash:
```bash
python manage.py migrate
```
6. Serverni ishga tushirish:
```bash
python manage.py runserver
```
7. Brauzerda ochish:
```
http://127.0.0.1:8000/
```

---



✅ Shu README fayl bilan loyiha **to‘liq tushuntirilgan, ishlash bo‘yicha ko‘rsatmalar, project structure va screenshots** bilan.  
