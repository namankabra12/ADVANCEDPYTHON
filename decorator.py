# Decorator
def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper


# Report Class
class Report:
    template = "Default Template"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    def __str__(self):
        return (
            f"Title    : {self.title}\n"
            f"Content  : {self.content}\n"
            f"Template : {Report.template}"
        )


# Decorated Function
@report_decorator
def display_report(report):
    print(report)


# Main Program
Report.change_template("Business Report")

report1 = Report(
    "Monthly Sales",
    "Sales increased by 20% this month."
)

display_report(report1)