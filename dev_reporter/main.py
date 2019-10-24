"""Entrypoint."""

import csv
import datetime
import os
from typing import List

from telethon import TelegramClient

from dev_reporter import settings, telegram


class Report:
    """Report object."""

    def __init__(self,
                 date: str = None,
                 project: str = None,
                 info: str = None,
                 time: str = None):
        self.date = validate_date(date)
        self.project = project
        self.info = info
        self.time = time

    def __lt__(self, other):
        return (self.date < other.date)

    def __repr__(self):
        return f'<Report: project={self.project} date={self.date_to_str()}>'

    def __str__(self):
        return f'{self.project} | {self.info} | {self.time}'

    def is_current(self) -> bool:
        """Determines if report belongs to current day."""
        return (self.date == datetime.date.today())

    def date_to_str(self) -> str:
        """Converts internal date representation to string."""
        return '{:%d.%m}'.format(self.date)

    def to_str(self) -> str:
        """Converts report to string."""
        return self.__str__()


def format_telegram_message(reports: List[Report]) -> str:
    """Prepares formatted telegram message."""
    reports_map = {}
    for r in reports:
        reports_map.setdefault(r.date_to_str(), []).append(r)

    items = []
    for k in sorted(reports_map.keys()):
        merged_reports = '\n'.join(r.to_str() for r in reports_map[k])
        items.append(f'/итог {k}\n{merged_reports}')
    return '\n\n'.join(items)


def validate_date(date_str: str) -> datetime.date:
    """Validates date string."""
    rules = [
        '%d/%m/%y',
        '%d/%m/%Y',
        '%d/%m',
        '%d.%m.%y',
        '%d.%m.%Y',
        '%d.%m',
        '%B/%m/%y',
        '%B/%m/%Y',
        '%B/%m',
        '%B.%m.%y',
        '%B.%m.%Y',
        '%B.%m'
    ]
    today = datetime.date.today()
    for rule in rules:
        try:
            return datetime.datetime.strptime(
                date_str, rule).replace(year=today.year).date()
        except ValueError:
            pass
    raise ValueError


def get_reports(current=True) -> List[Report]:
    """Fetches entries from CSV file and returns list of Report objects.
    
    If `current` is True: return reports for today only.
    """
    result = []
    with open(os.path.join(settings.DATA_DIR, 'reports.csv'), newline='') as f:
        csv_reader = csv.reader(
            f, delimiter=settings.CSV_DELIMITER, quotechar='|')

        for row in csv_reader:
            report = Report(
                date=row[0],
                project=row[1],
                info=row[2],
                time=row[3]
            )

            if not current:
                result.append(report)
                continue

            if report.is_current():
                result.append(report)
    return result


def main():
    """Main function."""
    reports = get_reports()
    message = format_telegram_message(reports)
    telegram.send_message(message)
