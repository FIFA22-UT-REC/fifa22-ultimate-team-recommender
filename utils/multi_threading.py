import threading

class MultiThreading(object):

    def __init__(self, scrapers):
        self.scrapers = scrapers

    def run(self):
        threads = []

        for i in range(len(self.scrapers)):
            t = threading.Thread(target=self.scrapers[i].start)
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()
