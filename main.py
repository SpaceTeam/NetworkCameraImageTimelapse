from datetime import datetime
import os
import time
import requests
import shutil

def save_image(url, path):
    r = requests.get(url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True

        datename = datetime.now().isoformat() + ".jpeg"
        filename = os.path.join(path, datename)

        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
    print(f":kamera_mit_blitz: Snapped image {datename}")

def main():

    while True:
        try:
            save_image("http://10.32.7.31/cgi-bin/api.cgi?cmd=Snap&channel=0&rs=wuuPhkmUCeI9WG7C&user=admin&password=", "Kamera0")
            save_image("http://10.32.7.31/cgi-bin/api.cgi?cmd=Snap&channel=0&rs=wuuPhkmUCeI9WG7C&user=admin&password=", "Kamera1")
            save_image("http://10.32.7.31/cgi-bin/api.cgi?cmd=Snap&channel=0&rs=wuuPhkmUCeI9WG7C&user=admin&password=", "Kamera2")
            save_image("http://10.32.7.31/cgi-bin/api.cgi?cmd=Snap&channel=0&rs=wuuPhkmUCeI9WG7C&user=admin&password=", "Kamera3")
        except Exception as e:
            print(f":feuer: Got Exception {e}")
        time.sleep(2)
main()


