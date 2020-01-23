from git.cmd import Git
from beforeiforget import CURRENT_DIRECTORY
from threading import Thread
import time, datetime, re, ptoaster, argparse

class BIF(object):
    def __init__(self, interval, length, should_notify=True):
        self.cwd = CURRENT_DIRECTORY
        self.start = datetime.datetime.now()
        reg = r'(\d+)'
        length_split = re.split(reg, length)
        time_int = length_split[1]
        time_type = length_split[2]
        if time_type == "h":
            self.until = datetime.datetime.now() + datetime.timedelta(hours=int(time_int))
        elif time_type == "m":
            self.until = datetime.datetime.now() + datetime.timedelta(minutes=int(time_int))
        elif time_type == "s":
            self.until = datetime.datetime.now() + datetime.timedelta(seconds=int(time_int))
        print(datetime.datetime.now())
        print(self.until)
        interval_split = re.split(reg, interval)
        interval_time = interval_split[1]
        interval_type = interval_split[2]
        if interval_type == "m":
            self.interval = datetime.timedelta(minutes=int(interval_time)).total_seconds()
        elif interval_type == "h":
            self.interval = datetime.timedelta(minutes=int(interval_time)).total_seconds()
        else:
            self.interval = int(interval_time)
        print(self.interval)
        self.g = Git(self.cwd)
        self.length = length
        self.should_run = True
        self.should_skip = False
        self.should_notify = should_notify
        t = Thread(target=self.run, args=())
        t.start()

    def run(self):
        if datetime.datetime.now() >= self.until:
            self.should_run = False
        while self.should_run:
            with open(CURRENT_DIRECTORY + '/bif.log', 'w') as log:
                log.write('FAILED TO COMMIT {}'.format(datetime.datetime.now()))
            self.g.execute(command=['git', 'commit', '-am', '"Auto-Commit from BIF @ {} UTC"'.format(datetime.datetime.now())])

parser = argparse.ArgumentParser(usage="bif 5m 2h")
parser.add_argument('interval', help='Interval to run "commit -am" on the local Repo')
parser.add_argument('totaltime', help='Total time to rurn BIF on the local repo')
parser.add_argument('-dn', '--disable-notif', help='Disables Notifications')
                
def main():
    args = parser.parse_args()
    if args.disable_notif:
        show = False
    else:
        show = True
    bif = BIF(args.interval, args.totaltime, should_notify=show)
    
if __name__ == "__main__":
    main()