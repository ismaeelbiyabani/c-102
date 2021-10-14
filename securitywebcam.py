from mmap import ACCESS_DEFAULT
import cv2
import dropbox
import time
import random
start_time = time.time()


def take_snapshot():
    number = random.randint(0, 100)
    videocaptureobject = cv2.videoCapture(0)
    result = True
    while(result):
        ret, frame = videocaptureobject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
        return img_name
    print("snapshotistaken")
    videocaptureobject.release()
    cv2.destroyAllWindows()
    
def upload_file(img_name):
   access_token = "HAyVC6K6f0wAAAAAAAAAASPVtK07j19zCL07vdXJXTzeeGmT9qUW5ZJ9SGxCEV0z"
   file = img_name
   file_from = file
   file_to = "/testfolder/"+(img_name)
   dbx = dropbox.Dropbox(access_token)
   with open(file_from, 'rb') as f:
      dbx.files_upload(f.read(), file_to,
                       mode=dropbox.files.WriteMode.overwrite)
      print("filesuploaded")

def main():
 print("in main")
 while(True):
   # print("in while")
   if((time.time()-start_time) >= 30):
     name = take_snapshot()
     upload_file(name)
     # print("hello")
main()
