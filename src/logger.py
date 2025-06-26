import logging

logger = logging.getLogger('kemono-dl')


def configure_logger(args: dict) -> None:
    """Configure logging using already parsed arguments."""

    # Remove any existing handlers to avoid duplicate logs when reconfigured
    logger.handlers.clear()

    if args.get('verbose'):
        # clear log file
        with open('debug.log', 'w'):
            pass

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    logger.setLevel(logging.INFO)
    if args.get('quiet'):
        logger.setLevel(logging.WARNING)
    if args.get('verbose'):
        logger.setLevel(logging.DEBUG)

    file_format = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    stream_format = logging.Formatter('%(levelname)s:%(message)s')

    if args.get('verbose'):
        file_handler = logging.FileHandler('debug.log', encoding="utf-16")
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_format)
    logger.addHandler(stream_handler)
