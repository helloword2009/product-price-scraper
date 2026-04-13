"""
Product Price Scraper - ดึงข้อมูลสินค้าจากเว็บไซต์
สร้างโดย: [ชื่อคุณ]
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sys

class ProductScraper:
    """Class สำหรับดึงข้อมูลสินค้า"""
    
    def __init__(self):
        """ตั้งค่าเริ่มต้น"""
        # กำหนด headers เพื่อให้เว็บคิดว่าเราเป็น browser จริง
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.products = []  # เก็บข้อมูลสินค้าที่ดึงมา
    
    def scrape_example_site(self, url):
        """
        ดึงข้อมูลจากเว็บตัวอย่าง (ใช้สำหรับเทส)
        
        Parameters:
            url (str): URL ของเว็บไซต์
        
        Returns:
            list: รายการสินค้าที่ดึงได้
        """
        try:
            print(f"🔍 กำลังดึงข้อมูลจาก: {url}")
            
            # ส่ง request ไปยังเว็บไซต์
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()  # เช็คว่า request สำเร็จหรือไม่
            
            # แปลง HTML เป็น object ที่จัดการได้
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # ตัวอย่าง: ดึงข้อมูลจาก Books to Scrape (เว็บทดสอบ)
            # หา element ทั้งหมดที่เป็นสินค้า
            product_elements = soup.find_all('article', class_='product_pod')
            
            if not product_elements:
                print("⚠️ ไม่พบสินค้าในหน้านี้")
                return []
            
            print(f"✅ พบสินค้า {len(product_elements)} รายการ")
            
            # วนลูปดึงข้อมูลแต่ละสินค้า
            for product in product_elements:
                try:
                    # ดึงชื่อสินค้า
                    title = product.find('h3').find('a')['title']
                    
                    # ดึงราคา
                    price = product.find('p', class_='price_color').text.strip()
                    
                    # ดึง rating (ถ้ามี)
                    rating_element = product.find('p', class_='star-rating')
                    rating = rating_element['class'][1] if rating_element else 'No rating'
                    
                    # ดึง availability (มีสินค้าหรือไม่)
                    availability = product.find('p', class_='instock availability').text.strip()
                    
                    # เก็บข้อมูลลงใน list
                    product_data = {
                        'title': title,
                        'price': price,
                        'rating': rating,
                        'availability': availability,
                        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    
                    self.products.append(product_data)
                    
                except Exception as e:
                    print(f"⚠️ ข้ามสินค้า 1 รายการ (error: {str(e)})")
                    continue
            
            return self.products
            
        except requests.exceptions.RequestException as e:
            print(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อ: {str(e)}")
            return []
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาด: {str(e)}")
            return []
    
    def save_to_csv(self, filename='products.csv'):
        """
        บันทึกข้อมูลลงไฟล์ CSV
        
        Parameters:
            filename (str): ชื่อไฟล์ที่ต้องการบันทึก
        """
        if not self.products:
            print("⚠️ ไม่มีข้อมูลให้บันทึก")
            return
        
        try:
            # เปิดไฟล์สำหรับเขียน (encoding utf-8-sig เพื่อรองรับภาษาไทย)
            with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
                # กำหนด column headers
                fieldnames = ['title', 'price', 'rating', 'availability', 'scraped_at']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # เขียน header
                writer.writeheader()
                
                # เขียนข้อมูลทุกรายการ
                writer.writerows(self.products)
                # ✨ เพิ่มส่วนนี้ (ถ้าต้องการความกว้างคอลัมน์อัตโนมัติใน CSV)
                print(f"📊 รายละเอียด:")
                print(f"   - จำนวนสินค้า: {len(self.products)} รายการ")
                print(f"   - คอลัมน์: {', '.join(fieldnames)}")
            
            print(f"✅ บันทึกข้อมูล {len(self.products)} รายการลง {filename} สำเร็จ!")
            
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดในการบันทึกไฟล์: {str(e)}")
    
    def display_results(self):
        """แสดงผลลัพธ์บนหน้าจอ"""
        if not self.products:
            print("⚠️ ไม่มีข้อมูลให้แสดง")
            return
        
        print("\n" + "="*80)
        print(f"📊 ผลลัพธ์: พบสินค้าทั้งหมด {len(self.products)} รายการ")
        print("="*80 + "\n")
        
        for i, product in enumerate(self.products, 1):
            print(f"#{i}")
            print(f"  📦 ชื่อ: {product['title']}")
            print(f"  💰 ราคา: {product['price']}")
            print(f"  ⭐ Rating: {product['rating']}")
            print(f"  📍 สถานะ: {product['availability']}")
            print(f"  🕒 เวลาที่ดึง: {product['scraped_at']}")
            print("-" * 80)


def main():
    """ฟังก์ชันหลักสำหรับรันโปรแกรม"""
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║         🛒 Product Price Scraper v1.0                   ║
    ║         ดึงข้อมูลสินค้าและบันทึกเป็น CSV               ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    # สร้าง scraper object
    scraper = ProductScraper()
    
    # URL ตัวอย่าง (เว็บสำหรับทดสอบ scraping ที่ถูกกฎหมาย)
    test_url = "https://books.toscrape.com/"
    
    print(f"📌 เว็บไซต์เป้าหมาย: {test_url}")
    print("⏳ กำลังเริ่มต้น...\n")
    
    # ดึงข้อมูล
    products = scraper.scrape_example_site(test_url)
    
    if products:
        # แสดงผลลัพธ์
        scraper.display_results()
        
        # บันทึกเป็น CSV
        scraper.save_to_csv('products.csv')
        
        print("\n✨ เสร็จสิ้น! ตรวจสอบไฟล์ products.csv ได้เลย")
    else:
        print("\n❌ ไม่สามารถดึงข้อมูลได้ กรุณาลองใหม่อีกครั้ง")


if __name__ == "__main__":
    main()