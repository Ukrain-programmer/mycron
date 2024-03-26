# Crontab

This project is a **Python-based** application designed for managing and scheduling cron jobs with ease.

## Installation

> Requires Python >= 3.8

Run the Docker container with the following command:

```bash
docker build -t my-project-name .
```
```bash
docker run -d --name my-running-project my-project-name
```

or directly in Python

```bash
pip3 install -r requirements.txt
```
```bash
cd src && python3 main.py
```

## Usage

Configuring Cron Jobs
To add or modify cron jobs, edit the cron_task.tab file. Each line in this file represents a single cron job, using the standard cron syntax. For example:
```cron
* * * * * /usr/bin/env python /path/to/your/script.py
```
This would run script.py every minute. Adjust the cron expressions and scripts according to your scheduling needs.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
