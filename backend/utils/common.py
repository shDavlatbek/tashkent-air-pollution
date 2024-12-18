from datetime import datetime, timezone


def now_utc_hours() -> datetime:
  return datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)