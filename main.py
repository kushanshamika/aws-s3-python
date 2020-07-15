from tkinter import filedialog
import tkinter as tk
import os.path
import boto3
import uuid
from dotenv import load_dotenv
load_dotenv()


session = boto3.session.Session()
client = session.client('s3',
                        region_name='sgp1',
                        endpoint_url='https://sgp1.digitaloceanspaces.com',
                        aws_access_key_id=os.getenv('SPACES_KEY'),
                        aws_secret_access_key=os.getenv('SPACES_SECRET'))


def video_uploader(file_path, file_id, video_quality):

    print("Uploading "+video_quality+"p video")

    client.put_object(Bucket='brightway',
                      Key='videos/'+file_id+"-"+video_quality+".mp4",
                      Body=open(file_path, 'rb'),
                      ACL='private',
                      ContentType='video/mp4')

    print("Finished uploading " + video_quality + "p video")


root = tk.Tk()
root.withdraw()

if __name__ == "__main__":
    video_directory = filedialog.askdirectory()
    file_id = uuid.uuid4().hex

    if os.path.isfile(video_directory+"/240.mp4"):
        print("240p video\t[X]")
    else:
        raise Exception("Can not find 240p video")

    if os.path.isfile(video_directory+"/360.mp4"):
        print("360p video\t[X]")
    else:
        raise Exception("Can not find 360p video")

    if os.path.isfile(video_directory+"/480.mp4"):
        print("480p video\t[X]")
    else:
        raise Exception("Can not find 480p video")

    if os.path.isfile(video_directory+"/720.mp4"):
        print("720p video\t[X]")
    else:
        raise Exception("Can not find 720p video")

    if os.path.isfile(video_directory+"/1080.mp4"):
        print("1080p video\t[X]")
    else:
        raise Exception("Can not find 1080p video")

    video_uploader(video_directory+"/1080.mp4", file_id, "1080")
    video_uploader(video_directory + "/720.mp4", file_id, "720")
    video_uploader(video_directory + "/480.mp4", file_id, "480")
    video_uploader(video_directory + "/360.mp4", file_id, "360")
    video_uploader(video_directory + "/240.mp4", file_id, "240")

    url = "http://localhost:8888/lms/portal/upload_paid_lesson.php?id=" + file_id

    print(url)



