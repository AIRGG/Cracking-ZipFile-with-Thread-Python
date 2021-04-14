import threading, random, string, time, zipfile, os
from tqdm import tqdm

def processCrack(zipnya, wordlist, xy, start, end):
	# for ky, x in enumerate(wordlist[start:end]):
	for x in tqdm(wordlist[start:end], unit="word"):
		try:
			# print(f"Thread ke {xy} {x} | {start} {end} {ky}")
			# print(x.strip())
			zipnya.extractall(pwd=x.strip())
		except Exception as ex:
			# print(ex)
			continue
		else:
			# os.system("cls")
			print("-"*50)
			print(f"[INFO] Password found in Thread {xy+1}: {x.decode().strip()}")
			print("-"*50)
			exit(0)
	print(f"[UPPS] Password not found in Thread {xy+1}. Next Thread..")

def splitProcess(zipnya, wordlist, numthread=4): # default thread is 4
	tmpwordlist = list(wordlist)
	genapin = len(tmpwordlist) // numthread # genapin kebawah
	for x in range(numthread):
		start = x * genapin
		end = None if x+1 == numthread else (x+1) * genapin
		th = threading.Thread(target=processCrack, args=(zipnya, tmpwordlist, x, start, end))
		th.start()
		# th.join() # if you want to run together remove this line
		# threading.Thread(target=processCrack, args=(zipnya, tmpwordlist, x, start, end)).start()

def main():
	wordlist = open("wordlist.txt", "rb")
	zipnya = zipfile.ZipFile("penguin.zip")
	# splitProcess(zipnya, wordlist)
	splitProcess(zipnya, wordlist, 8)

if __name__ == '__main__':
	main()



# Hello, in this video i want to show you how to implements thread for cracking password File Zip with Python

# 1. you need zip file with password of course

# 2. search for wordlist in internet or you can create brute force attack but it need more time than dictionary attack

# -- in this video i have create my own wordlist with 5000 data

# 3. Test Drive...

# oke now i want to increase number of thread...

# oke maybe that's, THank you...