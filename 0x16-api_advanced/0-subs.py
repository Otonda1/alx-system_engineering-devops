#!/usr/bin/python3


import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                '(KHTML, like Gecko) '
                'Chrome/100.0.0.0 Safari/537.36'
                ),
                'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjk5NDc2MzczLjg2ODEwMywiaWF0IjoxNjk5Mzg5OTczLjg2ODEwMywianRpIjoiQzdzOUc4ZkVtN3FINzlzYmp2QkZZSEE2b3ZjRmp3IiwiY2lkIjoiOGlDLWZ3UXIzY3dBa0tTV2tPaThPUSIsImxpZCI6InQyX25leGp0dGFuZiIsImFpZCI6InQyX25leGp0dGFuZiIsImxjYSI6MTY5OTM4MTk4MTQyOSwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.npelUamAc8J6dTglreb3JYYexF-WGyAWCeq1oqXalR2fIPKtQHBd_G14eM275j0wvzUH2aFFZyEh8cAYWeSqKOjolvQvEgaE-lLbdsHrAA5_kxBKQSfD9jYdOGU53B0GIHgWWYs5qJm1zfF58VUK9Lr4Q03LaUwFJfHSDG7BZ5wpu3IHYlw0GZCuSsMCZQ16FnwrSWLaiHpMmWaB9vCNAXpqEfwnpLv1UoXOqfp3ievDlACwWWwMxRd4FdFiW7ZiiU-7LaxX9s9XcdSpPgrsRWFzhVPpfWD6QbI48Bx3aSmjbqNtSJsX7tO0t-qGHjDGQJM2S5fWpEvbnnDtvN17yQ'}
    response = requests.get(url, headers=headers)
    print(response.json())
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
