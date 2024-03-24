'''
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения
в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени
выполнения программы.
'''
import logging

import requests
import time
import threading
from multiprocessing import Process, Pool
import os
import time
import sys

logging.basicConfig(level=logging.INFO)


def check_and_create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def download_img(url, subfolder=""):
    f_time = time.time()
    response = requests.get(url)
    filename = subfolder + os.path.basename(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    logging.info(f"  {time.time() - f_time:.2f} seconds for downloaded {url}.")


def sync_download(urls: list):
    subfolder = './sync_download/'
    check_and_create_folder(subfolder)
    logging.info('#' * 20)
    logging.info('Sync download:')
    start_time = time.time()
    for url in urls:
        download_img(url, subfolder)
    logging.info(f"Total time:  {time.time() - start_time:.2f} seconds")
    return


def multithread_download(urls: list):
    start_time = time.time()

    threads = []
    results_time = []
    start_time = time.time()

    subfolder = './multithread_download/'
    check_and_create_folder(subfolder)

    logging.info('#' * 20)
    logging.info('Multithread download:')

    for url in urls:
        thread = threading.Thread(target=download_img, args=[url, subfolder])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    logging.info(f"Total time:  {time.time() - start_time:.2f} seconds")


def multiprocess_download(urls: list):
    logging.info('#' * 20)
    logging.info('Multiprocess download:')
    subfolder = './multiprocess_download/'
    check_and_create_folder(subfolder)
    processes = []
    start_time = time.time()

    for url in urls:
        process = Process(target=download_img, args=(url, subfolder))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    logging.info(f"Total time:  {time.time() - start_time:.2f} seconds")


if __name__ == '__main__':

    urls = sys.argv[1:]

    # urls = ['https://hb.bizmrg.com/gb_ui_assets/ui_banners/6586/62db1647f8ec3f716c1123e091392b66.png',
    #         'https://gb.ru/_nuxt/img/ef949be.png',
    #         'https://gb.ru/_nuxt/img/8e1cdf0.png',
    #         ]

    sync_download(urls)
    multithread_download(urls)
    multiprocess_download(urls)
