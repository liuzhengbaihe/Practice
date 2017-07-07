import random
import os
import time
import urllib2

from threading import Thread

class MyThread(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.start()

    def run(self):
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = "{0} has finished, run {1}s!".format(self.name, amount)
        print(msg)

def create_threads():
    for i in range(5):
        name = "Thread #%s" %(i+1)
        my_thread = MyThread(name=name)

class DownloadThread(Thread):
    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        handle = urllib2.urlopen(self.url)
        fname = os.path.basename(self.url)
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        msg = "%s has finished downloading %s" %(self.name, fname)
        print msg


def download(urls):
    """
    Run the program
    """
    for item, url in enumerate(urls):
        name = "Thread %s" % (item+1)
        thread = DownloadThread(url, name)
        thread.start()
 
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    download(urls)
    #create_threads()
