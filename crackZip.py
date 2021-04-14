import threading, random, string, time, zipfile, os
from tqdm import tqdm

def processCrack(zip_file, wordlist, i, start, end):
    # for ky, word in enumerate(wordlist[start:end]):
    for word in tqdm(wordlist[start:end], unit="word"):
        try:
            # print(f"Thread ke {i} {word} | {start} {end} {ky}")
            # print(word.strip())
            zip_file.extractall(pwd=word.strip())
        except Exception as ex:
            # print(ex)
            continue
        else:
            print(f"[INFO] Password found: {word.decode().strip()}")
            exit(0)
    print("[UPPS] Password not found, try other wordlist.")

def splitProcess(zip_file, wordlist, num_splits=4):
    items = list(wordlist)
    split_size = len(items) // num_splits # genapin kebawah
    for i in range(num_splits):
        start = i * split_size
        end = None if i+1 == num_splits else (i+1) * split_size
        # th = threading.Thread(target=processCrack, args=(zip_file, items, i, start, end))
        # th.start()
        # th.join()
        threading.Thread(target=processCrack, args=(zip_file, items, i, start, end)).start()
# def processCrack(items, cnt, start, end):
#     for ky, item in enumerate(items[start:end]):
#         try:
#             print(f"Thread ke {cnt} {item} | {start} {end} {ky}")
#         except Exception:
#             print('error with item')


# def splitProcess(items, num_splits=4): # split process
#     # split_size = len(items) // num_splits
#     items = list(items)
#     split_size = len(items) // num_splits
#     threads = []
#     for i in range(num_splits):
#         start = i * split_size
#         end = None if i+1 == num_splits else (i+1) * split_size
#         # create the thread
#         threading.Thread(target=processCrack, args=(items, i, start, end)).start()
#         # a = threading.Thread(target=processCrack, args=(items, i, start, end))
#         # a.start()
#         # a.join()

wordlist = open("wordlist.txt", "rb")
zip_file = zipfile.ZipFile("penguin.zip")
# print(list(wordlist))
# for x in list(wordlist):
#     if b"abcdefg" in x.strip():
#         print("NEMU")
    # print()
# a = "abcdefg\n".encode("utf-8") in list(wordlist)
# print(a)
# print("abcdefg".encode("utf-8"))
splitProcess(zip_file, wordlist, 4)