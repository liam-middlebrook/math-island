#!/usr/bin/make

LANDSLIDE=landslide -cr -l table -x tables,abbr
FILES=${sort ${wildcard *.md}}
CATFILES=python3 -c 'print("\n---\n\n".join("\n".join(line.replace(".notes","\\footnote{")+"}" if ".notes" in line else line for line in open(f).read().split("\n") if "!cpp" not in line) for f in __import__("sys").argv[1:]))'

# Simple target to make just the basics
presentation: clean-slideshow slideshow

# Make EVERYTHING
all: clean slideshow pdf latex

################################################################################
# HTML slideshow
################################################################################
slideshow:
	$(LANDSLIDE) presentation.cfg
	mkdir -p output/html
	mv index.html theme/ output/html/

clean-slideshow:
	rm -rf output/html &> /dev/null

################################################################################
# PDF support
################################################################################
pdf:
	mkdir -p output/pdf
	$(CATFILES) $(FILES) | \
	pandoc -t latex | \
	sed -e "s/\\\\begin{center}\\\\rule{3in}{0.4pt}\\\\end{center}/\\\\newpage/g" | \
	pandoc --toc -o output/pdf/evilC.pdf

clean-pdf:
	rm -rf output/pdf &> /dev/null

################################################################################
# LaTeX support
################################################################################
latex:
	mkdir -p output/latex
	$(CATFILES) $(FILES) | \
	pandoc -o output/latex/evilC.tex

clean-latex:
	rm -rf output/latex &> /dev/null

################################################################################
# Cleanup targets
################################################################################
clean: clean-slideshow clean-pdf clean-latex

realclean:
	rm -rf output
	@echo Removed built files

