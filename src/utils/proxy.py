import os

def activate_proxy(proxy_url='http://127.0.0.1', proxy_port='7897'):
    # Set the http_proxy and https_proxy environment variables
    os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
    os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'

def deactivate_proxy():
    # Remove the http_proxy and https_proxy environment variables
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)
