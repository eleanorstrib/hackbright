#pip install requests
#pip install requests-oauthlib


# API secrets. NEVER share these with anyone!
CLIENT_KEY = "Ogw2gicyhME2qlGHzr0rDsEHe"
CLIENT_SECRET = "QKDSghksV6f9pBVtPlswQVQkcCeI5PlZaqsHg9FGvqUoifhfP2"


API_URL = "https://api.twitter.com"
REQUEST_TOKEN_URL = API_URL + "/oauth/request_token"
AUTHORIZE_URL = API_URL + "/oauth/authorize?oauth_token={request_token}"
ACCESS_TOKEN_URL = API_URL + "/oauth/access_token"
TIMELINE_URL = API_URL + "/1.1/statuses/home_timeline.json"
TWEET_URL = API_URL + "/1.1/statuses/update.json"



import urlparse
import json
import requests
from requests_oauthlib import OAuth1
from pprint import pprint


def get_request_token():
    """ Get a token allowing us to request user authorization """
    oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET)
    response = requests.post(REQUEST_TOKEN_URL,
                             auth=oauth)
    credentials = urlparse.parse_qs(response.content)

    request_token = credentials.get("oauth_token")[0]
    request_secret = credentials.get("oauth_token_secret")[0]
    return request_token, request_secret


def get_access_token(request_token, request_secret, verifier):
    """"
    Get a token which will allow us to make requests to the API
    """
    oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=request_token,
                   resource_owner_secret=request_secret,
                   verifier=verifier)

    response = requests.post(ACCESS_TOKEN_URL, auth=oauth)
    print response.json()

    credentials = urlparse.parse_qs(response.content)
    access_token = credentials.get('oauth_token')[0]
    access_secret = credentials.get('oauth_token_secret')[0]
    return access_token, access_secret


def get_user_authorization(request_token):
    """
    Redirect the user to authorize the client, and get them to give us the
    verification code.
    """
    authorize_url = AUTHORIZE_URL
    authorize_url = authorize_url.format(request_token=request_token)
    print 'Please go here and authorize: ' + authorize_url
    return raw_input('Please input the verifier: ')


def store_credentials(access_token, access_secret):
    """ Save our access credentials in a json file """
    with open("access.json", "w") as f:
        json.dump({"access_token": access_token,
                   "access_secret": access_secret}, f)


def get_stored_credentials():
    """ Try to retrieve stored access credentials from a json file """
    with open("access.json", "r") as f:
        credentials = json.load(f)
        return credentials["access_token"], credentials["access_secret"]


def authorize():
    """ A complete OAuth authentication flow """
    try:
        access_token, access_secret = get_stored_credentials()
    except IOError:
        request_token, request_secret = get_request_token()
        verifier = get_user_authorization(request_token)
        access_token, access_secret = get_access_token(request_token,
                                                       request_secret,
                                                       verifier)
        store_credentials(access_token, access_secret)

    oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=access_token,
                   resource_owner_secret=access_secret)
    return oauth


def print_tweets_on_mytimeline(auth):
    timeline_tweets = requests.get("https://api.twitter.com/1.1/statuses/home_timeline.json?count=5", auth=auth).json()
    #print timeline_tweets["description"]
    #print "Joe's score is %d" % timeline_tweets["description"]
    #return timeline_tweets
    #print "{} tweeted -- {} -- on my timeline".format(name, description)
    pprint(timeline_tweets)

def print_twitter_user_tweets(auth):
    twitter_user_tweets = requests.get("https://api.twitter.com/1.1/users/show.json?screen_name=jennielees", auth=auth).json()
    tweets = twitter_user_tweets.get(['description'])
    pprint(twitter_user_tweets)
    print "Jennie says {}".format(tweets)

def tweeting(auth):
    data = { 'status': "this is a tweet" }
    response = requests.post(TWEET_URL, data=data, auth=auth)
    return response





def main():
    """ Main function """
    auth = authorize()
    print_tweets_on_mytimeline(auth)
    print_twitter_user_tweets(auth)


    response = requests.get(TIMELINE_URL, auth=auth)
    return json.dumps(response.json(), indent=4)


if __name__=="__main__":
        main()


