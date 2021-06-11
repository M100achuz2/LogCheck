from datetime import datetime
from typing import Union
from slacker import Slacker
from configparser import ConfigParser

conf = ConfigParser()
conf.read("token.ini")
token = conf["slack"]["token"]
slack = Slacker(token)


def search(id: str) -> Union[dict, bool, None]:
    try:
        res = slack.search.files(id).body  # get the results from slack
    except:
        return False

    if res.get("ok"):
        info = {'query': res['query'], 'count': len(res['files']['matches'])}  # save some details

        if not info['count']:
            return None

        files = res['files']['matches']
        info['match'] = []
        for file in files:
            info['match'].append(dict(file_name=file['name']
                                      , date=str(datetime.fromtimestamp(file['timestamp']))
                                      , url=file['url_private']))
    else:
        info = False
    return info
