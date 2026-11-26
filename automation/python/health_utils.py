def check_health(value, warning, critical):
    if value > critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "HEALTHY"
