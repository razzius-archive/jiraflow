# Jiraflow

Scripts for working with the Jira API.

The main interaction is checking out a branch which corresponds to the next issue you should be working on.

You will need [fish](https://fishshell.com/) and python 3 installed.

You will also need the following environment variables:

- `JIRA_USER`
- `JIRA_AUTH` - a base64-encoded USER:PASSWORD string. `source read_jira_credentials` can help you set it.
- `JIRA_API_URL` - for example, https://sighten.atlassian.net/rest/api/2/search
- `JIRA_INITIALS` - this is used, with the current issue number, to make a branch.

For example, if `JIRA_INITIALS` is set to `razzi` and `next_issue` returns `PROP-67`, `./next` will checkout a branch named razzi/prop-67.

It's called `JIRA_INITIALS` because many people use their first and last name's initials as part of their branch name, rather than their first name as I do.

# Install

```
$ git clone https://github.com/razzius/jiraflow
$ cd jiraflow
$ ln -s next /usr/local/bin/  # et cetera
```

# Commands

## `next`

Checks out the branch for the next issue you should be working on.

```sh
~/project (develop) $ next
Switched to branch 'razzi/prop-67'
~/project (razzi/prop-67) $
```

## `description`

Prints the description of the current issue.

## next_issue

Prints the next issue you should be working on. Used by `next`.

## read_jira_credentials

Source this to be prompted for your Jira username and password, which will be used to set `JIRA_AUTH`.

## TODO

- Better misconfiguration checks
- Easier installation
- Define description as a composition of the raw issue data with [jq](https://github.com/stedolan/jq)
