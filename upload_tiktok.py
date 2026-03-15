from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class TikTokUploader:
    def __init__(self):
        self.driver = None
        self.profile_path = os.path.join(os.getcwd(), "tiktok_profile")
        
    def start(self):
        """تشغيل المتصفح"""
        options = Options()
        
        # إعدادات التخفي
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        # حفظ الجلسة
        options.add_argument(f"user-data-dir={self.profile_path}")
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
    def login_if_needed(self):
        """تسجيل الدخول إذا لزم الأمر"""
        self.driver.get("https://www.tiktok.com")
        time.sleep(3)
        
        # تحقق إذا احتجت تسجيل دخول
        if "login" in self.driver.current_url or self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Se connecter')]"):
            print("📝 يرجى تسجيل الدخول يدوياً...")
            print("🔐 أدخل بياناتك خلال 60 ثانية")
            time.sleep(60)  # أعطِ وقت كافي لتسجيل الدخول
            print("✅ تم تسجيل الدخول!")
        else:
            print("✅ أنت مسجل دخول مسبقاً!")
            
    def upload_video(self, video_path):
        """رفع فيديو"""
        print(f"📤 جاري رفع {video_path}...")
        
        # هنا تكتب كود الرفع الفعلي
        # البحث عن زر الرفع والضغط عليه
        
        # مثال مبسط:
        try:
            # انتظر ظهور زر الرفع
            upload_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-e2e='upload-button']"))
            )
            upload_btn.click()
            print("✅ تم الضغط على زر الرفع")
            
        except Exception as e:
            print(f"❌ خطأ في الرفع: {e}")
            
    def close(self):
        """إغلاق المتصفح"""
        if self.driver:
            self.driver.quit()

# تشغيل الكود
if __name__ == "__main__":
    uploader = TikTokUploader()
    
    try:
        uploader.start()
        uploader.login_if_needed()
        uploader.upload_video("tiktok_video.mp4")
        
        input("اضغط Enter لإغلاق المتصفح...")
        
    finally:
        uploader.close()