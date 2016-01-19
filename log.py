"""Model operations for server log objects."""

import json
import statistics
import time

import store


TICKS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
TICKS_PER_HOUR = 3600
HOURS_PER_DAY = 24


def _get_average_or_none(values):
    if values:
        return statistics.mean(values)


def _get_averages(log_data, interval_ticks, num_intervals):
    now = time.time()
    interval_count = 1
    interval_limit = now - (interval_count * interval_ticks)
    cpu = []
    ram = []
    averages = {'cpu': [], 'ram': []}
    log_data.reverse()
    for entry in log_data:
        if entry['ts'] < interval_limit:
            averages['cpu'].append(_get_average_or_none(cpu))
            averages['ram'].append(_get_average_or_none(ram))
            cpu.clear()
            ram.clear()
            interval_count += 1
            interval_limit = now - (interval_count * interval_ticks)

        if interval_count == num_intervals:
            break

        cpu.append(entry['cpu'])
        ram.append(entry['ram'])

    if cpu and ram:
        averages['cpu'].append(_get_average_or_none(cpu))
        averages['ram'].append(_get_average_or_none(ram))

    averages['cpu'].extend([None] * (num_intervals - len(averages['cpu'])))
    averages['ram'].extend([None] * (num_intervals - len(averages['ram'])))

    return averages


def _get_day_summary(log_data):
    return _get_averages(log_data, TICKS_PER_HOUR, HOURS_PER_DAY)


def _get_hour_summary(log_data):
    return _get_averages(log_data, TICKS_PER_MINUTE, MINUTES_PER_HOUR)


def get_server_log(server_name):
    """Return a summary of recent logs."""

    log_data = store.get_item(server_name)
    response = {}
    if log_data:
        response['last_60_minutes'] = _get_hour_summary(log_data)
        response['last_24_hours'] = _get_day_summary(log_data)

    return response


def add_server_log(server_name, log_data):
    """Add a log entry for server_name.

    log_data should be a dict with keys 'cpu' and 'ram', each with float
    measurement values.
    """

    log_data = json.loads(log_data.decode('utf8'))
    log_data['ts'] = time.time()
    store.add_item(server_name, log_data)

