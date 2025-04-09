.NOTPARALLEL:

SUBDIRS = . test

MAN_FILES = $(MAN3_FILES)

MAN3_FILES = $(MAN3_FILES_PRIMARY) $(MAN3_FILES_SECONDARY)

MAN3_FILES_PRIMARY = \
	man3/hostlist_create.3

MAN3_FILES_SECONDARY = \
	man3/hostlist_destroy.3 \
	man3/hostlist_decode.3 \
	man3/hostlist_encode.3 \
	man3/hostlist_copy.3 \
	man3/hostlist_append.3 \
	man3/hostlist_append_list.3 \
	man3/hostlist_nth.3 \
	man3/hostlist_find.3 \
	man3/hostlist_delete.3 \
	man3/hostlist_count.3 \
	man3/hostlist_sort.3 \
	man3/hostlist_uniq.3 \
	man3/hostlist_first.3 \
	man3/hostlist_last.3 \
	man3/hostlist_next.3 \
	man3/hostlist_current.3 \
	man3/hostlist_remove_current.3

RST_FILES  = \
	$(MAN3_FILES_PRIMARY:.3=.rst)

if ENABLE_DOCS
man_MANS = $(MAN3_FILES)
endif

SUFFIXES = .rst .3

sphinx_man = $(sphinx_man_$(V))
sphinx_man_ = $(sphinx_man_$(AM_DEFAULT_VERBOSITY))
sphinx_man_0 = @echo "  BUILD     manpages";

sphinx_html = $(sphinx_html_$(V))
sphinx_html_ = $(sphinx_html_$(AM_DEFAULT_VERBOSITY))
sphinx_html_0 = @echo "  BUILD     html";

sphinx_verbose_flags = $(sphinx_verbose_flags_$(V))
sphinx_verbose_flags_ = $(sphinx_verbose_flags_$(AM_DEFAULT_VERBOSITY))
sphinx_verbose_flags_0 =
sphinx_verbose_flags_1 = -v
sphinx_verbose_flags_2 = -vv

STDERR_DEVNULL = $(stderr_devnull_$(V))
stderr_devnull_ =  $(stderr_devnull_$(AM_DEFAULT_VERBOSITY))
stderr_devnull_0 = >/dev/null 2>&1

$(MAN_FILES): manpages.py conf.py $(RST_FILES)
	$(sphinx_man) \
	SPHINX_BUILDDIR=$(abs_builddir) $(PYTHON) \
		-m sphinx $(sphinx_verbose_flags) -b man $(srcdir) ./man \
		$(STDERR_DEVNULL)
	@echo "  MV        manpages"; \
	for sec in 3; do \
	  $(MKDIR_P) man$$sec && \
	  mv -f $(abs_builddir)/man/*.$$sec man$$sec/; \
	done

.PHONY: html
html: conf.py $(RST_FILES)
	$(sphinx_html) \
	SPHINX_BUILDDIR=$(abs_builddir) $(PYTHON) \
		-m sphinx $(sphinx_verbose_flags) -b html $(srcdir) ./html \
		$(STDERR_DEVNULL)

EXTRA_DIST = \
	conf.py \
	manpages.py \
	index.rst \
	domainrefs.py \
	requirements.txt \
	$(RST_FILES) \
	man3/index.rst

CLEANFILES = \
	$(MAN_FILES)

clean-local:
	-rm -rf man

