# Telegram Pizza Order Bot

Bu bot sizga Telegram orqali pizza buyurtma berish imkonini beradi. Bot Pepperoni, Margherita va Bavarian pizzalarini buyurtma qilish imkoniyatini taqdim etadi va admin panel orqali buyurtmalar tarixini ko'rish va menuni o'zgartirish kabi funksiyalarni boshqarish mumkin.

## Xususiyatlar

- **Asosiy foydalanuvchilar uchun:**
  - Menyudan pizza tanlash va buyurtma berish.
  - Pizzalar haqida batafsil ma'lumot va rasmlar olish.
  - Telefon raqamni ulashish orqali buyurtmalarni xavfsiz amalga oshirish.
  - Biz haqimizda ma'lumotlarni ko'rish.
  - Izoh qoldirish imkoniyati (hozircha faqat tugma mavjud).

- **Adminlar uchun:**
  - Buyurtmalar tarixini ko'rish.
  - Menyu elementlarini qo'shish, o'zgartirish va o'chirish.
  - Aktsiyalarni boshqarish.

## Fayl Tuzilishi

Loyiha quyidagi asosiy fayllar va kataloglardan iborat:

- **`bot.py`**: Botni ishga tushiradigan va boshqaradigan asosiy skript.
- **`handlers.py`**: Botdagi tugmalar va funktsiyalar uchun barcha handlerlarni saqlaydi.
- **`buttons.py`**: Barcha tugmachalarni yaratish uchun kodlar.
- **`admin.py`**: Admin panelining tugmalari va handlerlari.
- **`pizza_data.json`**: Menyudagi pizzalar haqida ma'lumot saqlovchi JSON fayl.
- **`user_data.json`**: Foydalanuvchilarning ma'lumotlarini saqlash uchun JSON fayl.
- **`requirements.txt`**: Loyihaning kutubxonalarini ko'rsatuvchi fayl.
- **`.env`**: Token va boshqa maxfiy ma'lumotlarni saqlash uchun fayl.
- **`README.md`**: Loyihani tushuntiruvchi va ishlatish bo'yicha ko'rsatmalar beruvchi hujjat.

## O'rnatish va Ishga Tushirish

1. **Repozitoriyani klonlash:**

   ```bash
   git clone https://github.com/yourusername/telegram-pizza-order-bot.git
   cd telegram-pizza-order-bot

2. **Virtual muhit yaratish (tavsiya etiladi):**

python -m venv venv
source venv/bin/activate  # Linux/macOS uchun
venv\Scripts\activate     # Windows uchun

3. **Kutubxonalarni o'rnatish:**

pip install -r requirements.txt

4. **Botni ishga tushirish:**

python bot.py

- ## Foydalanish
- Foydalanuvchilar uchun
- Telegramda botni toping va /start komandasini yuboring.
- Menyudan tanlov qiling:
- Menu: Pizzalarni ko'rish va buyurtma qilish.
- Izoh qoldirish: Hozircha faqat tugma mavjud.
- Biz haqimizda: Bizning ma'lumotlarimizni ko'rish.
- Pizzani tanlang va buyurtma qiling.
- Adminlar uchun
- Botga /start komandasini yuboring va Admin tugmasini bosing.
- Admin panelida tanlov qiling:
- Buyurtmalar tarixi: Buyurtmalar tarixini ko'rish.
- Menuni o'zgartirish: Menyu elementlarini qo'shish, o'zgartirish 
- yoki o'chirish.
- Aktsiyalar: Aktsiyalarni boshqarish