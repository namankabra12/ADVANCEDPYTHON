import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="w",
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

logger = logging.getLogger("myapp")
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
logger.addHandler(console)

file_handler = logging.FileHandler("myapp.log", mode="w")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

logger.info("Saved only in myapp.log")
logger.warning("Shown on screen and saved in myapp.log")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Cannot divide by zero")


divide(10, 0)

print("Check app.log and myapp.log for the full logs")
