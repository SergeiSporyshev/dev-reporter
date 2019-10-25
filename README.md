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

* Define reports data in `data/reports.csv` in the following format:
```
date;project;description;time
```

* Run app:
```
.venv/bin/python -m dev_reporter
```

* Run app via docker
```
$ docker run --rm -it -v {path/to/repo}:/app {image_name} python -m dev_reporter
```
