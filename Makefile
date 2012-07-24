all:
	@This makefile only cleans things

git_clean:
	git clean -dnx
	@echo "Do you want to remove these files? type \"yes!\""
	@read do_clean; \
	if [ "$${do_clean}" = "yes!" ]; then \
		echo "deleting files"; \
		git clean -dfx ; \
	else echo "not deleting files" ; \
	fi


pyc_clean:
	find . -name "*.pyc" -delete

clean: git_clean pyc_clean

.PHONY: clean git_clean all pyc_clean
