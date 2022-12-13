
def format_timedelta(delta):
    """Prettify the given timedelta to a human-readable format.

    Args:
        delta (datetime.timedelta): The timedelta to format

    Returns:
        str: The formatted timedelta
    """

    # split timedelta into hours, minutes and seconds
    seconds = delta.total_seconds()
    sign = "-" if seconds < 0 else ""
    seconds = abs(seconds)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    # format string from components
    return f"{sign}{int(hours):02}:{int(minutes):02}:{seconds:04.1f}"
