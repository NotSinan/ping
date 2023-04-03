import requests


def site_is_online(url: str, timeout: int = 2):
    """
    :param url: The URL to check.
    :param timeout: The maximum time to wait for a response, in seconds.
    :return True if the target URL is online:
    :exception Raises exception: requests.exceptions.RequestException: If a network-related error occurs while checking the URL.
    """
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code < 400
    except requests.exceptions.RequestException as e:
        raise e
    except ValueError as e:
        raise ValueError("Invalid URL: " + str(e))
