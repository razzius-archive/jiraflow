import os


JIRA_API_URL = os.environ['JIRA_API_URL']

OPEN_ISSUES_JQL = """
assignee = {JIRA_USER}
AND status in ("In Development", "Ready For Development")
AND issuetype != epic and sprint in opensprints()
ORDER BY status, rank, Sprint
"""
