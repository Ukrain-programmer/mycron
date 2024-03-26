import os
import time

from crontab import CronTab, CronItem
from loguru import logger


class Cron:
    def __init__(self, crontab: CronTab):
        self._crontab = crontab

    def schedule(self) -> None:
        """Schedule cron jobs by creating a child process for each job."""
        for job in self._crontab:
            pid = os.fork()
            if pid == 0:  # In child process
                try:
                    logger.info(f'Creating child process {os.getpid()} for job: {job.command}')
                    self._run_job(job)
                except Exception as e:
                    logger.error(f'Error in job {job.command}: {e}')
                finally:
                    os._exit(0)

    def _run_job(self, job: CronItem) -> None:
        """Run the specified job at its scheduled times."""
        next_run = job.schedule().get_next()
        while True:
            current_time = time.time()
            if current_time >= next_run:
                try:
                    res = job.run()
                    if res is not None:
                        logger.info(f'Result of job {job.command}: {res}')
                except Exception as e:
                    logger.error(f'Error running job {job.command}: {e}')
                finally:
                    next_run = job.schedule().get_next()  # Calculate next run time

            # Sleep until the next scheduled time or 1 second, whichever is shorter, to prevent busy waiting.
            time_to_next_run = max(1, next_run - time.time())
            time.sleep(time_to_next_run)