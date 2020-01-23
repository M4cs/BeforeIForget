# BeforeIForget
Simple Git Auto-Commit Command Line Tool | Written in Python

Runs `commit -am` for commit. You will need to run `git add .` yourself

# Usage

`python -m beforeiforget [interval] [duration]`

# Examples

```
python -m beforeiforget 1m 10m # Every 1 min for 10 mins
python -m beforeiforget 5m 1h # Every 5 min for 1 hour
python -m beforeiforget 30s 2m # Every 30 seconds for 2 minutes
```
