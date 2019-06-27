import os


JIRA_SEARCH_URL = os.environ['JIRA_HOST'] + '/rest/api/2/search'

OPEN_ISSUES_JQL = """
assignee = {JIRA_USER}
AND status in ("In Development", "Ready For Development")
AND issuetype != epic and sprint in opensprints()
ORDER BY status, rank, Sprint
"""
