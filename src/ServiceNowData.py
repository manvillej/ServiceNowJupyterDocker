import os
import logging
import httpx

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def logRequest(request):
    logger.warning(f'Request: {request.method} {request.url}')

def logResponse(response):
    request = response.request
    status_code = response.status_code
    logger.warning(f'Response: {status_code} {request.method} {request.url}')


class ServiceNowHTTPXClient(object):
    """docstring for    ServiceNowHTTPXClient"""
    def __init__(self):
        super(ServiceNowHTTPXClient, self).__init__()
        self.instance = os.environ["SERVICENOW_INSTANCE"]
        self.client = httpx.Client(
            base_url=f'https://{self.instance}.service-now.com',
            auth=(os.environ["SERVICENOW_USERNAME"], os.environ["SERVICENOW_PASSWORD"]),
            event_hooks={
                'request': [logRequest],
                'response':[logResponse],
            }
        )

    def healthCheck(self):
        response = self.getData('incident', 'ORDERBYDESCopened_at', {'sysparm_limit':1})

    def close(self):
        self.client.close()

    def getData(self, table, query, params):
        response = self.client.get(f'/api/now/table/{table}?sysparm_query={query}', params=params)
        return response

def main():
    client = ServiceNowHTTPXClient()
    client.healthCheck()
    client.close()

    #response = httpx.get('https://www.example.org/')
   
if __name__ == '__main__':
    main()
