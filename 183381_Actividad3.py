from imgurpython import ImgurClient
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import os
import urllib.request
import threading
import timeit
 
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
cliente = ImgurClient(id_cliente, secreto_cliente)
arr = []

def descarga_url_img(link):
   print(f"{link} - Proceso Actual:", os.getpid())
   #print(f' {link} Thread ID -> {threading.current_thread()}  Proceso Actual:{os.getpid()}')
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   url_local = "/Users/zdes7/Desktop/CONCURRENTE/C2/Img/{}.{}"
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))
 
def main():
    id_album = "bUaCfoz"
    imagenes = cliente.get_album_images(id_album)
    for i in imagenes:
        arr.append(i.link)

def PoolExecutor():
    with ThreadPoolExecutor(max_workers=len(arr)) as executor:
        executor.map(descarga_url_img, arr)

def ProcessingPoolExecutor():
    with ProcessPoolExecutor(max_workers=len(arr)) as process:
       process.map(descarga_url_img, arr)

def PoolMultiprocessing():
    with Pool (len(arr)) as p:
        p.map(descarga_url_img, arr)

if __name__ == "__main__":
   main()
   
   print(f"Tiempo de descarga ThreadPoolExecutor: {timeit.Timer(PoolExecutor).timeit(number=1)}\n")
   #print(f"Tiempo de descarga Multiprocessing Pool: {timeit.Timer(PoolMultiprocessing).timeit(number=1)}\n")
   #print(f"Tiempo de descarga ProcessPoolExecutor: {timeit.Timer(ProcessingPoolExecutor).timeit(number=1)}")