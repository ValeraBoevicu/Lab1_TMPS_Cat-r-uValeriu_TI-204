LAB1_TMPS- Calendar App in Python
Taks:Build an app where use all the solid principles
Description:
First laborator we have to build an app where use all the solid principles,i chose to build a calendar app.The idea behind the SRP is that every class, module, or function in a program should have one responsibility/purpose in a program,in my app Event class is responsible for holding event data,DateRange class is responsible for generating a range of dates.The open-closed principle states that software entities should be open for extension, but closed for modification in a my app the code is open for extension through the use of abstract classes and interfaces, such as CalendarService and the MonthlyReportGenerator class can be extended to generate different types of reports without modifying the existing code.The Liskov substitution principle when an instance of a class is passed/extended to another class, the inheriting class should have a use case for all the properties and behavior of the inherited class.,in my app i use Liskov substition InMemoryCalendarService class is a subtype of CalendarService, and can be used anywhere CalendarService is expected.The interface segregation principle states that the interface of a program should be split in a way that the user/client would only have access to the necessary methods related to their needs in my app i use the interface segregation in CalendarService interface is segregated into two methods: add_event and get_events and the last Dependency Inversion Principle it is understood that High-level modules should not import anything from low-level modules,in my app  The Calendar class depends on an abstraction (CalendarService) instead of a concrete implementation (InMemoryCalendarService) and The MonthlyReportGenerator class depends on an abstraction (Calendar) instead of a concrete implementation (InMemoryCalendarService).
  
