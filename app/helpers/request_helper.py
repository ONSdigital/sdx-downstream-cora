import logging
from structlog import wrap_logger

from app.settings import session, SDX_SEQUENCE_URL, SDX_STORE_URL
from requests.packages.urllib3.exceptions import MaxRetryError
from requests.exceptions import ConnectionError
from sdc.rabbit.exceptions import RetryableError, QuarantinableError

logger = wrap_logger(logging.getLogger(__name__))


def service_name(url=None):
    try:
        parts = url.split('/')
        if 'responses' in parts:
            return 'SDX_STORE'
        elif 'sequence' in parts:
            return 'SDX_SEQUENCE'
        elif 'cora' in parts:
            return 'SDX_TRANSFORM_CORA'
        else:
            return None
    except AttributeError as e:
        logger.error(e)


def remote_call(url, json=None):
    service = service_name(url)

    try:
        logger.info("Calling service", request_url=url, service=service)
        response = None

        if json:
            response = session.post(url, json=json)
        else:
            response = session.get(url)

        return response

    except MaxRetryError:
        logger.error("Max retries exceeded (5)", request_url=url)
        raise RetryableError("Max retries exceeded")
    except ConnectionError:
        logger.error("Connection error", request_url=url)
        raise RetryableError("Connection error")


def response_ok(response, service_url=None):
    service = service_name(service_url)

    if response.status_code == 200:
        logger.info("Returned from service", request_url=response.url, status=response.status_code, service=service)
        return True
    elif response.status_code == 404:
        logger.info("Not Found response returned from service",
                    request_url=response.url,
                    status=response.status_code,
                    service=service,
                    )
        raise QuarantinableError("Not Found response returned from {}".format(service))
    elif 400 <= response.status_code < 500:
        logger.info("Bad Request response from service",
                    request_url=response.url,
                    status=response.status_code,
                    service=service,
                    )
        raise QuarantinableError("Bad Request response from {}".format(service))
    else:
        logger.info("Bad response from service",
                    request_url=response.url,
                    status=response.status_code,
                    service=service,
                    )
        raise RetryableError("Bad response from {}".format(service))


def get_sequence_no():
    sequence_url = "{0}/sequence".format(SDX_SEQUENCE_URL)
    response = remote_call(sequence_url)

    if response_ok(response, sequence_url):
        return response.json().get('sequence_no')


def get_doc_from_store(tx_id):
    store_url = "{0}/responses/{1}".format(SDX_STORE_URL, tx_id)
    response = remote_call(store_url)

    if response_ok(response, store_url):
        logger.info("Successfully got document from store",
                    tx_id=tx_id,
                    )
        return response.json()
