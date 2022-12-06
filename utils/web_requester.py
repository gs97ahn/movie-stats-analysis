import requests


class WebRequester:
    def requester(self, target_address):
        response = requests.get(target_address)
        if response.status_code == 200:
            return response
        else:
            print('ERROR: failed to scrape', target_address)
            exit(1)
