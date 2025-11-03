from datetime import datetime, timedelta
def add(moment):
    delta = timedelta(seconds=1_000_000_000)
    result = moment + delta
    result.isoformat()
    str(result)         # Human-readable format
    result.strftime("%Y-%m-%d %H:%M:%S")  # Custom format
    return result
