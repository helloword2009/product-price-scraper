# 🛒 Product Price Scraper

Web scraper ที่ดึงข้อมูลสินค้าจากเว็บไซต์และบันทึกเป็นไฟล์ CSV

## ✨ Features

- ✅ ดึงข้อมูลสินค้า (ชื่อ, ราคา, rating, availability)
- ✅ บันทึกข้อมูลเป็นไฟล์ CSV
- ✅ รองรับภาษาไทยใน CSV
- ✅ แสดงผลลัพธ์บนหน้าจอ
- ✅ Error handling ครบถ้วน
- ✅ โค้ดเข้าใจง่าย มี comment อธิบาย

## 🚀 การติดตั้ง

### 1. Clone repository
```bash
git clone [your-repo-url]
cd product-price-scraper
```

### 2. ติดตั้ง dependencies
```bash
pip install -r requirements.txt
```

## 📖 วิธีใช้งาน

### รันโปรแกรม
```bash
python scraper.py
```

### ผลลัพธ์
- แสดงข้อมูลสินค้าบนหน้าจอ
- สร้างไฟล์ `products.csv` พร้อมข้อมูลทั้งหมด

## 📋 ตัวอย่างผลลัพธ์ CSV

```csv
title,price,rating,availability,scraped_at
"A Light in the Attic","£51.77","Three","In stock","2024-01-15 14:30:22"
"Tipping the Velvet","£53.74","One","In stock","2024-01-15 14:30:22"
```

## 🛠️ เทคโนโลยีที่ใช้

- **Python 3.x** - ภาษาหลัก
- **Requests** - HTTP requests
- **BeautifulSoup4** - HTML parsing
- **CSV** - บันทึกข้อมูล

## ⚙️ การปรับแต่ง

### เปลี่ยน URL เป้าหมาย
แก้ไขในไฟล์ `scraper.py` บรรทัดที่ 125:
```python
test_url = "https://your-target-website.com"
```

### เปลี่ยนชื่อไฟล์ output
แก้ไขในไฟล์ `scraper.py` บรรทัดที่ 136:
```python
scraper.save_to_csv('your-filename.csv')
```

## 📝 Requirements

- Python 3.7+
- requests==2.31.0
- beautifulsoup4==4.12.3

## ⚠️ ข้อควรระวัง

- ตรวจสอบ `robots.txt` ของเว็บไซต์ก่อน scraping
- ไม่ควร scrape บ่อยเกินไป (อาจโดน IP ban)
- เคารพ Terms of Service ของเว็บไซต์

## 📄 License

MIT License - สามารถนำไปใช้และแก้ไขได้อย่างอิสระ

## 👨‍💻 Author

[ชื่อของคุณ]

## 🤝 Contributing

Pull requests are welcome!

---

**สร้างโดย ❤️ สำหรับ Fiverr Portfolio**