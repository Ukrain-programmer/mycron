import os
import signal
from typing import Final

import utils
from config import Config
from cron import Cron

CONFIG_PATH: Final[str] = '../config/config.yaml'


def main():
    # Load configuration and configure the logger.
    cfg = Config.load(CONFIG_PATH)
    cfg.configure_logger()

    # Parse the crontab file and initialize the Cron scheduler.
    crontab = utils.parse_crontab(cfg.app.crontab_path)
    cron = Cron(crontab)

    try:
        # Schedule cron jobs and wait for them to complete.
        cron.schedule()
        os.wait()
    except KeyboardInterrupt:
        os.killpg(os.getpgid(os.getpid()), signal.SIGTERM)
        print("Shutting down gracefully.")


if __name__ == '__main__':
    main()
