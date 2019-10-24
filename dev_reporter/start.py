"""Start telethon."""

from dev_reporter import telegram


def main():
    telegram.get_client().start()


if __name__ == '__main__':
    main()
