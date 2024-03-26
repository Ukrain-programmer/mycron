import sys
from crontab import CronTab
from loguru import logger


def parse_crontab(path: str) -> CronTab:
    """Parse the crontab file specified by the path.

    Args:
        path (str): The file path to the crontab file.

    Returns:
        CronTab: An instance of the parsed CronTab.

    Raises:
        ValueError: If no cron jobs are found in the specified file.
    """
    crontab = CronTab(tabfile=path)

    jobs_count = len(crontab)
    if jobs_count == 0:
        error_message = f"No cron jobs found in the specified file: {path}."
        logger.error(error_message)
        raise ValueError(error_message)

    logger.info(f"{jobs_count} jobs parsed successfully from {path}.")
    return crontab
