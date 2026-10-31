import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    # Menggunakan potongan lirik Cemburu oleh Raim Laode
    lyrics = [
        ("Aku cemburu melihat kau bersamanya", 0.08),
        ("Aku cemburu tanganmu digenggam dia", 0.08),
        ("Tapi ku tak tahu mengapa aku cemburu", 0.08),
        ("Kau bukan milikku, kau bukan milikku", 0.09)
    ]
    
    # Estimasi penyesuaian delay antar baris
    delays = [0.5, 3.5, 7.0, 10.5]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("=== Cemburu - Raim Laode ===\n")
    sing_song()