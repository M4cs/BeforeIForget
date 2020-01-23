from git.cmd import Git
from beforeiforget import CURRENT_DIRECTORY
from threading import Thread
import time, datetime, re, argparse

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
        print('Running BIF until {}'.format(self.until))
        interval_split = re.split(reg, interval)
        interval_time = interval_split[1]
        interval_type = interval_split[2]
        if interval_type == "m":
            self.interval = datetime.timedelta(minutes=int(interval_time)).total_seconds()
        elif interval_type == "h":
            self.interval = datetime.timedelta(minutes=int(interval_time)).total_seconds()
        else:
            self.interval = int(interval_time)
        print('BIF Will Commit Every {} seconds'.format(self.interval))
        self.g = Git(self.cwd)
        self.length = length
        self.should_run = True
        self.should_skip = False
        self.should_notify = should_notify
        self.run()

    def run(self):
        try:
            while True:
                time.sleep(self.interval)
                if datetime.datetime.now() >= self.until:
                    break
                
                if self.should_run:
                    try:
                        print('[{}] BIF Committing'.format(datetime.datetime.now()))
                        self.g.execute(command=['git', 'commit', '-am', 'Auto-Commit from BIF @ {} UTC'.format(datetime.datetime.now())])
                    except Exception as e:
                        with open(CURRENT_DIRECTORY + '/bif.log', 'a') as log:
                            log.write('FAILED TO COMMIT {}: ERROR {}\n'.format(datetime.datetime.now(), e))
        except KeyboardInterrupt:
            print('Exiting...')

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