import os
import re
import requests
from multiprocessing import Pool

API_KEY = "QDY1icFfMfgeAFQDthsD64vwvav4hVmv8ULPy9LV"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output/'


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    metalist = {'start_date': start_date,
                'end_date': end_date,
                'api_key': api_key}
    response = requests.get(APOD_ENDPOINT, params=metalist).json()
    all_temp = []
    for c in response:
        all_temp.append(c['url'])
    metadata = {x for x in all_temp if not "jpg" not in x}

    return metadata


def download_apod_images(metadata: list):
    print(metadata)
    with Pool(5) as p:
        p.map(download_image, metadata)


def download_image(i):
    print(i)
    sep = 'image'
    stripped = i.split(sep, 1)[1]
    stripped = re.sub('[/]', '', str(stripped))
    complete_name = os.path.join(OUTPUT_IMAGES + stripped)
    img_data = requests.get(i).content
    with open(complete_name, 'wb') as handler:
        handler.write(img_data)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)
