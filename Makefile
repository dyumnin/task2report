title=Generate reports from taskwiki
authoremail=jahagirdar.vs@gmail.com
variables=-V title:"$(title)" -V client:"$(client)" -Vauthoremail:$(authoremail) -V document-sha:$(document-sha) -V status:"$(docstatus)"
files=task2report.md
input=tests/test.md
default:mkpdf
mklib:
	antlr4 -Dlanguage=Python3 grammar/task2report.g4 -o src/task2report
$(files): mklib
	task2report task2report $(input) task2report.md
mkpdf: $(files)
	pandoc --toc --from=markdown+lists_without_preceding_blankline  -F pandoc-imagine $(variables) -o reference_manual.pdf -s  $(files) 
