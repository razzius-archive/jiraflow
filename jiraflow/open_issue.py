import os
import webbrowser

from .next_issue import get_issue_key


def main():
    jira_host = os.environ['JIRA_HOST']
    issue_key = get_issue_key()
    webbrowser.open(f'{jira_host}/browse/{issue_key}')
