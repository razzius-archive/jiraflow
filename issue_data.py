#!/usr/bin/env python3.7

import os
import sys

import requests

from lib import JIRA_SEARCH_URL, OPEN_ISSUES_JQL


response = requests.get(
    JIRA_SEARCH_URL,
    params={
        'jql': OPEN_ISSUES_JQL,
        'maxResults': 1,
    },
    headers={'Authorization': os.environ['JIRA_AUTH']},
)

sys.stdout.buffer.write(response.content)
