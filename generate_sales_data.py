import pandas as pd
import random
from datetime import datetime, timedelta

# Data pools
customers = [
    "budi santoso", "Budi Santoso", "Budi, Santoso", " budi santoso  ",
    "sari dewi", "Sari Dewi", "Sari, Dewi", "SARİ DEWİ",
    "agus wijaya", "Agus Wijaya", "AGUS WIJAYA", "agus  wijaya",
    "lina kartika", "Lina Kartika", "lina-kartika", "LINA KARTIKA",
    "rudi hermawan", "Rudi Hermawan", "RUDI HERMAWAN", "rudi  hermawan",
    "maya sari", "Maya Sari", "MAYA SARI", " maya sari ",
    "dian lestari", "Dian Lestari", "DIAN LESTARI",
    "riko pratama", "Riko Pratama", "RIKO PRATAMA",
    "fitri anggraini", "Fitri Anggraini", "FITRI ANGGRAINI",
    "anton susanto", "Anton Susanto", "ANTON SUSANTO",
    "sinta nurmala", "Sinta Nurmala", "SINTA NURMALA"
]

categories = ["Elektronik", "Fashion"]
brands = {
    "Elektronik": ["Samsung","samsung","SAMSUNG"," Samsung ",
        "Apple","apple","APPLE"," Apple ",
        "Xiaomi","xiaomi","XIAOMI"," xiaomi ",
        "Sony","sony","SONY"," sony ",
        "LG","lg","Lg"," LG ",
        "Asus","asus","ASUS"," asus "],
    "Fashion": ["Nike","nike","NIKE"," Nike ",
        "Adidas","adidas","ADIDAS"," adidas ",
        "Zara","zara","ZARA"," Zara ",
        "H&M","h&m","H&M"," H&M ",
        "Uniqlo","uniqlo","UNIQLO"," uniqlo ",
        "Gucci","gucci","GUCCI"," gucci "]
}
products = {
    "Elektronik": ["laptop gaming","Laptop Gaming","LAPTOP GAMING"," laptop  gaming ",
        "smartphone","Smartphone","SMARTPHONE"," smart phone ",
        "headphone bluetooth","Headphone Bluetooth","HEADPHONE BLUETOOTH",
        "mouse wireless","Mouse Wireless","MOUSE WIRELESS"," mouse  wireless ",
        "keyboard mechanical","Keyboard Mechanical","KEYBOARD MECHANICAL",
        "power bank","Power Bank","POWER BANK"," power  bank ",
        "tablet","Tablet","TABLET"," Tablet ",
        "smartwatch","Smartwatch","SMARTWATCH"," smart watch ",
        "monitor 4k","Monitor 4K","MONITOR 4K"," monitor  4k ",
        "tv led","TV LED","Tv Led"," tv  led ",
        "kamera digital","Kamera Digital","KAMERA DIGITAL"],
    "Fashion": ["baju wanita","Baju Wanita","BAJU WANITA"," baju  wanita ",
        "tas wanita","Tas Wanita","TAS WANITA"," tas  wanita ",
        "sepatu pria","Sepatu Pria","SEPATU PRIA"," sepatu  pria ",
        "dress","Dress","DRESS"," dress ",
        "jaket","Jaket","JAKET"," jaket ",
        "celana jeans","Celana Jeans","CELANA JEANS"," celana  jeans ",
        "sepatu wanita","Sepatu Wanita","SEPATU WANITA",
        "tas pria","Tas Pria","TAS PRIA"," tas  pria ",
        "baju pria","Baju Pria","BAJU PRIA"," baju  pria ",
        "kemeja","Kemeja","KEMEJA"," kemeja "]
}
price_ranges = {
    "Elektronik": {
        "low": [50000, 500000],
        "medium": [1000000, 5000000],
        "high": [6000000, 25000000]
    },
    "Fashion": {
        "low": [50000, 300000],
        "medium": [350000, 1000000],
        "high": [1100000, 5000000]
    }
}
cities = ["Jakarta","Bandung","Surabaya","Medan","Semarang",
          "Makassar","Batam","Palembang","Samarinda","Bali",""]
payments = ["Credit Card","E-Wallet","Bank Transfer",
            "QRIS","PayLater","Cash On Delivery",""]

data = []
order_id = 1

# 300 total - 5% duplikat = 285 data unik
for i in range(300 - int(0.05 * 300)):
    order_id_str = f"ORD-{order_id:03d}"
    date_format = random.choice([0, 1])  
    date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))
    order_date = date.strftime("%Y-%m-%d") if date_format == 0 else date.strftime("%d/%m/%Y")

    customer = random.choice(customers)
    category = random.choice(categories)
    brand = random.choice(brands[category])
    product = random.choice(products[category])

    if random.random() < 0.05:
        quantity = random.choice([0, -1, -2])
    elif random.random() < 0.15:
        quantity = random.randint(6, 10)
    else:
        quantity = random.randint(1, 5)

    if random.random() < 0.05:
        unit_price = random.choice([0, -round(random.randint(50000, 500000), -3)])
    else:
        price_level = random.choice(["low", "medium", "high"])
        min_price, max_price = price_ranges[category][price_level]
        mode_price = (min_price + max_price) // 2
        unit_price = int(random.triangular(min_price, max_price, mode_price))
        unit_price = round(unit_price, -3)
    
    city = random.choice(cities)
    payment = random.choice(payments)
    
    data.append([
        order_id_str, order_date, customer, category, brand, product, 
        quantity, unit_price, city, payment
    ])
    order_id += 1

# tambahkan 5% duplikat (15 baris) → total tetap 300
duplicate_indices = random.sample(range(300 - int(0.05 * 300)), int(0.05 * 300))
for idx in duplicate_indices:
    duplicate = data[idx].copy()
    original_date = datetime.strptime(duplicate[1], "%Y-%m-%d") if "-" in duplicate[1] else datetime.strptime(duplicate[1], "%d/%m/%Y")
    new_date = original_date + timedelta(days=random.randint(1, 3))
    duplicate[1] = new_date.strftime("%Y-%m-%d") if random.choice([0, 1]) else new_date.strftime("%d/%m/%Y")
    data.append(duplicate)

# Buat DataFrame
df = pd.DataFrame(data, columns=[
    "Order_ID", "Order_Date", "Customer_Name", "Product_Category", 
    "Merk", "Product_Name", "Quantity", "Unit_Price", "City", "Payment_Method"
])

# Simpan ke CSV
df.to_csv("sales_data_raw.csv", index=False)
print(f"File sales_data_raw.csv berhasil dibuat dengan {len(df)} baris data!")
