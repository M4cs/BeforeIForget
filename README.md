# BeforeIForget
Simple Git Auto-Commit Command Line Tool | Written in Python

Runs `commit -am` for commit. You will need to run `git add .` yourself

# Installation

```
git clone git@github.com:M4cs/BeforeIForget
cd BeforeIForget
python3 setup.py install
```

# Usage

`bif [interval] [duration]`

# Examples

```
bif 1m 10m # Every 1 min for 10 mins
bif 5m 1h # Every 5 min for 1 hour
bif 30s 2m # Every 30 seconds for 2 minutes
```
