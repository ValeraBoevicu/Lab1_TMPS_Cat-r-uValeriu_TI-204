from abc import ABC, abstractmethod
from datetime import date, timedelta
from typing import List


class Event:
    def __init__(self, name: str, date: date):
        self.name = name
        self.date = date


class CalendarService(ABC):
    @abstractmethod
    def add_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def get_events(self, date: date) -> List[Event]:
        pass


class InMemoryCalendarService(CalendarService):
    def __init__(self):
        self.events = {}

    def add_event(self, event: Event) -> None:
        if event.date not in self.events:
            self.events[event.date] = []
        self.events[event.date].append(event)

    def get_events(self, date: date) -> List[Event]:
        return self.events.get(date, [])


class Calendar:
    def __init__(self, service: CalendarService):
        self.service = service

    def add_event(self, name: str, date: date) -> None:
        event = Event(name, date)
        self.service.add_event(event)

    def get_events(self, date: date) -> List[Event]:
        return self.service.get_events(date)


class DateRange:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_date = self.start_date
        while current_date <= self.end_date:
            yield current_date
            current_date += timedelta(days=1)


class MonthlyReportGenerator:
    def __init__(self, calendar: Calendar):
        self.calendar = calendar

    def generate_report(self, month: int, year: int) -> str:
        start_date = date(year, month, 1)
        end_date = start_date.replace(day=28) + timedelta(days=4)
        end_date = end_date - timedelta(days=end_date.day)
        report_lines = []
        report_lines.append(f"Calendar report for {start_date.strftime('%B %Y')}:")
        for current_date in DateRange(start_date, end_date):
            events = self.calendar.get_events(current_date)
            if events:
                report_lines.append(f"{current_date.strftime('%d %B %Y')}:")
                for event in events:
                    report_lines.append(f"- {event.name}")
        return "\n".join(report_lines)


if __name__ == "__main__":
    calendar = Calendar(InMemoryCalendarService())
    calendar.add_event("Meeting 1", date(2023, 3, 15))
    calendar.add_event("Meeting 2", date(2023, 3, 22))
    report_generator = MonthlyReportGenerator(calendar)
    report = report_generator.generate_report(3, 2023)
    print(report)
