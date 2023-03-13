# LAB1_TMPS- Calendar App in Python
## Taks:Build an app where use all the solid principles.
## Theory about all the principles:
### * The idea behind the SRP is that every class, module, or function in a program should have one responsibility/purpose in a program.

### * The open-closed principle states that software entities should be open for extension, but closed for modification.

### * The Liskov substitution principle when an instance of a class is passed/extended to another class, the inheriting class should have a use case for all the properties and behavior of the inherited class.

### * The interface segregation principle states that the interface of a program should be split in a way that the user/client would only have access to the necessary methods related to their needs.

### * The Dependency Inversion Principle it is understood that High-level modules should not import anything from low-level modules.

### 1. Single Responsability Principle:
- Event class is responsible for holding event data.
```
class Event:
    def __init__(self, name: str, date: date):
        self.name = name
        self.date = date
```
- CalendarService interface defines the contract for adding and getting events.
```
class CalendarService(ABC):
    @abstractmethod
    def add_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def get_events(self, date: date) -> List[Event]:
        pass
```
- Calendar class uses a CalendarService to add and get events.
```
class Calendar:
    def __init__(self, service: CalendarService):
        self.service = service

    def add_event(self, name: str, date: date) -> None:
        event = Event(name, date)
        self.service.add_event(event)

    def get_events(self, date: date) -> List[Event]:
        return self.service.get_events(date)
```
- DateRange class is responsible for generating a range of dates.
```
class DateRange:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_date = self.start_date
        while current_date <= self.end_date:
            yield current_date
            current_date += timedelta(days=1)
```
### 2. The open-closed principle:
- The code is open for extension through the use of abstract classes and interfaces, such as CalendarService.
- The MonthlyReportGenerator class can be extended to generate different types of reports without modifying the existing code.
```
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
```
### 3. The Liskov substitution principle:
- The InMemoryCalendarService class is a subtype of CalendarService, and can be used anywhere CalendarService is expected.
```
class InMemoryCalendarService(CalendarService):
```
### 4. The interface segregation principle:
- CalendarService interface is segregated into two methods: add_event and get_events.
```
 def add_event(self, event: Event) -> None:
        pass
```
```
def get_events(self, date: date) -> List[Event]:
        pass
```
- MonthlyReportGenerator class only depends on the Calendar interface to generate the report, which in turn only depends on the CalendarService interface.
```
class MonthlyReportGenerator:
    def __init__(self, calendar: Calendar):
        self.calendar = calendar

    def generate_report(self, month: int, year: int) -> str:
        start_date = date(year, month, 1)
        end_date = start_date.replace(day=28) + timedelta(days=4)
        end_date = end_date - timedelta(days=end_date.day)
```
### 5. The Dependency Inversion Principle:
- The Calendar class depends on an abstraction (CalendarService) instead of a concrete implementation (InMemoryCalendarService).
```
class Calendar:
    def __init__(self, service: CalendarService):
```


### Description:
First laborator we have to build an app where use all the solid principles,i chose to build a calendar app.The idea behind the SRP is that every class, module, or function in a program should have one responsibility/purpose in a program,in my app Event class is responsible for holding event data,DateRange class is responsible for generating a range of dates.The open-closed principle states that software entities should be open for extension, but closed for modification in a my app the code is open for extension through the use of abstract classes and interfaces, such as CalendarService and the MonthlyReportGenerator class can be extended to generate different types of reports without modifying the existing code.The Liskov substitution principle when an instance of a class is passed/extended to another class, the inheriting class should have a use case for all the properties and behavior of the inherited class.,in my app i use Liskov substition InMemoryCalendarService class is a subtype of CalendarService, and can be used anywhere CalendarService is expected.The interface segregation principle states that the interface of a program should be split in a way that the user/client would only have access to the necessary methods related to their needs in my app i use the interface segregation in CalendarService interface is segregated into two methods: add_event and get_events and the last Dependency Inversion Principle it is understood that High-level modules should not import anything from low-level modules,in my app  The Calendar class depends on an abstraction (CalendarService) instead of a concrete implementation (InMemoryCalendarService) and The MonthlyReportGenerator class depends on an abstraction (Calendar) instead of a concrete implementation (InMemoryCalendarService).
  
