import logging

def test_print_logs():
    Logger = logging.getLogger(__name__)
    Logger.info("This is Information log")
    Logger.critical("This is critical log")
    Logger.warning("This is warning log")
    Logger.error("This is Error log")