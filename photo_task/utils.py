import os
import threading
import urllib.request
from django.utils.crypto import get_random_string

import datetime
from celery import shared_task
from .models import ImageModel


def images_url(img_key):
    url = "https://picsum.photos/200/300"
    img_name = f"img_{img_key}.png"
    urllib.request.urlretrieve(url, img_name)


@shared_task
def download_image():
    # 1-usul
    # for i in range(100):
    #     random_key = get_random_string(12)
    #     images_url(random_key)
    #     ImageModel.objects.create(image=f'img_{random_key}.png')  # time = 0:00:00.023
    # 2-usul bluk
    # images = []
    # for i in range(100):
    #     random_key = get_random_string(12)
    #     images_url(random_key)
    #     images.append(ImageModel(image=f'img_{random_key}.png'))  # time = 0:00:00.15
    #
    # ImageModel.objects.bulk_create(images)
    threads = []
    images = []
    for i in range(100):
        random_key = get_random_string(12)
        t = threading.Thread(target=images_url, args=(random_key,))
        threads.append(t)
        t.start()
        images.append(ImageModel(image=f'img_{random_key}.png'))
        for thread in threads:  # time = 0:00:00.16
            thread.join()

    ImageModel.objects.bulk_create(images)
