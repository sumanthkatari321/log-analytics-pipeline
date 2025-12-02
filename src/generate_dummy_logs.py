import random
import os
from datetime import datetime, timedelta

# Directory where raw logs will be stored
LOG_DIR = os.path.join("data", "raw_logs")
os.makedirs(LOG_DIR, exist_ok=True)

ENDPOINTS = [
    "/",
    "/home",
    "/login",
    "/logout",
    "/api/v1/users",
    "/api/v1/users/123",
    "/api/v1/orders",
    "/api/v1/orders/summary",
    "/health"
]

STATUS_CODES = [200, 200, 200, 201, 204, 400, 401, 403, 404, 500, 502]

USER_AGENTS = [
    "Mozilla/5.0",
    "Chrome/120.0",
    "curl/7.68.0",
    "PostmanRuntime/7.29.0"
]


def generate_log_line(timestamp: datetime) -> str:
    """Generate a single access log line."""
    ip = f"192.168.0.{random.randint(1, 255)}"
    endpoint = random.choice(ENDPOINTS)
    method = random.choice(["GET", "POST", "PUT"])
    status = random.choice(STATUS_CODES)
    size = random.randint(200, 5000)
    agent = random.choice(USER_AGENTS)
    response_time = round(random.uniform(0.01, 1.5), 3)

    time_str = timestamp.strftime("%d/%b/%Y:%H:%M:%S +0000")

    return (
        f'{ip} - - [{time_str}] "{method} {endpoint} HTTP/1.1" '
        f'{status} {size} "-" "{agent}" {response_time}\n'
    )


def generate_log_file(days_back: int = 0, lines: int = 1000):
    """Generate one log file for a given day."""
    date = datetime.utcnow() - timedelta(days=days_back)
    fname = date.strftime("access_%Y-%m-%d.log")
    path = os.path.join(LOG_DIR, fname)

    start = datetime(date.year, date.month, date.day)

    with open(path, "w", encoding="utf-8") as f:
        for _ in range(lines):
            ts = start + timedelta(seconds=random.randint(0, 86400))
            f.write(generate_log_line(ts))

    print(f"Created: {path}")


def main():
    # Create log files for the last 3 days (including today)
    for d in range(3):
        generate_log_file(days_back=d, lines=1000)


if __name__ == "__main__":
    main()
