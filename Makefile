# Minimal makefile for Sphinx documentation

# Platform identification
PYTHON = python3.8
ifdef COMSPEC # win32 system
PYTHON = python
endif # COMSPEC
ifdef ComSpec # win32 system
PYTHON = python
endif # ComSpec

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = "$(PYTHON)" -m sphinx
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

syncpackages:
	./source.sh $(PYTHON);
	"$(PYTHON)" -m pip install -r requirements.txt

install_hooks:
	cp -r ./git-hooks/. ./.git/hooks

init:
	./init.sh $(PYTHON);
	make install_hooks;
	make syncpackages;

doc:
	./source.sh $(PYTHON);
	make html
	./source.sh $(PYTHON);
	"$(PYTHON)" processLink.py

watch:
	./source.sh $(PYTHON);
	./watch.sh $(PYTHON);
