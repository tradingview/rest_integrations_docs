# Minimal makefile for Sphinx documentation

# Platform identification
PYTHON = python3.10
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

install_hooks:
	cp -r ./git-hooks/. ./.git/hooks

init:
	./init.sh $(PYTHON);
	make install_hooks;

doc:
	./doc.sh $(PYTHON);

watch:
	./watch.sh $(PYTHON);
