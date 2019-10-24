# dev-reporter

## Install

1. Register new application at https://my.telegram.org.
2. Prepare environment:
```
make all
```
3. Set `TG_API_ID` and `TG_API_HASH` in `.env` (from https://my.telegram.org).
4. Authorize in Telegram:

**IMPORTANT**: 2FA must be disabled.

```
make telegram
```


## Usage

1. Define reports data in `data/reports.csv` in the following format:
```
date;project;description;time
```

2. Run app:
```
.venv/bin/python -m dev_reporter
```
