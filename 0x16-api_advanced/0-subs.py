#!/usr/bin/python3
"""
A function that queries the reddit API and returns the no 
of subscribes for a given subreddit.
"""
if __name__ == '__main__':
    import requests

<<<<<<< HEAD
    def number_of_subscribers(subreddit):
        """returns the number of subscribers"""
        url = 'https://oauth.reddit.com/r/{}/about.json'.format(subreddit)
        user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
        headers = {'User-Agent': user_agent,
                   'Authorization':('bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnls'
                                    'V0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHl'
                                    'wIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjk5NDc2MzczLj'
                                    'g2ODEwMywiaWF0IjoxNjk5Mzg5OTczLjg2ODEwMywianRpIjoiQzdzO'
                                    'Uc4ZkVtN3FINzlzYmp2QkZZSEE2b3ZjRmp3IiwiY2lkIjoiOGlDLWZ3U'
                                    'XIzY3dBa0tTV2tPaThPUSIsImxpZCI6InQyX25leGp0dGFuZiIsImFpZ'
                                    'CI6InQyX25leGp0dGFuZiIsImxjYSI6MTY5OTM4MTk4MTQyOSwic2NwIj'
                                    'oiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.npelUamAc8J'
                                    '6dTglreb3JYYexF-WGyAWCeq1oqXalR2fIPKtQHBd_G14eM275j0wvzUH2'
                                    'aFFZyEh8cAYWeSqKOjolvQvEgaE-lLbdsHrAA5_kxBKQSfD9jYdOGU53B0'
                                    'GIHgWWYs5qJm1zfF58VUK9Lr4Q03LaUwFJfHSDG7BZ5wpu3IHYlw0GZCuSs'
                                    'MCZQ16FnwrSWLaiHpMmWaB9vCNAXpqEfwnpLv1UoXOqfp3ievDlACwWWwMx'
                                    'Rd4FdFiW7ZiiU-7LaxX9s9XcdSpPgrsRWFzhVPpfWD6QbI48Bx3aSmjbqNt'
                                    'SJsX7tO0t-qGHjDGQJM2S5fWpEvbnnDtvN17yQ')}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
=======

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'ChangeMeClient/0.1 by Otond1',
                'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjk5NDc2MzczLjg2ODEwMywiaWF0IjoxNjk5Mzg5OTczLjg2ODEwMywianRpIjoiQzdzOUc4ZkVtN3FINzlzYmp2QkZZSEE2b3ZjRmp3IiwiY2lkIjoiOGlDLWZ3UXIzY3dBa0tTV2tPaThPUSIsImxpZCI6InQyX25leGp0dGFuZiIsImFpZCI6InQyX25leGp0dGFuZiIsImxjYSI6MTY5OTM4MTk4MTQyOSwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.npelUamAc8J6dTglreb3JYYexF-WGyAWCeq1oqXalR2fIPKtQHBd_G14eM275j0wvzUH2aFFZyEh8cAYWeSqKOjolvQvEgaE-lLbdsHrAA5_kxBKQSfD9jYdOGU53B0GIHgWWYs5qJm1zfF58VUK9Lr4Q03LaUwFJfHSDG7BZ5wpu3IHYlw0GZCuSsMCZQ16FnwrSWLaiHpMmWaB9vCNAXpqEfwnpLv1UoXOqfp3ievDlACwWWwMxRd4FdFiW7ZiiU-7LaxX9s9XcdSpPgrsRWFzhVPpfWD6QbI48Bx3aSmjbqNtSJsX7tO0t-qGHjDGQJM2S5fWpEvbnnDtvN17yQ'}
    response = requests.get(url, headers=headers)
    print(response.json())
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
>>>>>>> 66c2343fa33158f013c13069599c4be64dc58fe1
