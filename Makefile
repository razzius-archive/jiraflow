SCRIPTS = description next next_issue open_issue read_jira_credentials issue_data.py

USRBIN = /usr/local/bin

install:
	for script in ${SCRIPTS}; do \
		ln -s ${CURDIR}/$$script ${USRBIN}; \
	done

uninstall:
	for script in ${SCRIPTS}; do \
		rm ${USRBIN}/$$script; \
	done
