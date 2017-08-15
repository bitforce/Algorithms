#=================================
sources = $(wildcard *.java)
classes = $(sources:.java=.class)
main = Test
run:
	@echo 'compiling sources...'
	javac $(sources)
	java $(main) $(args)
clean: 
	$(RM) $(classes) *.txt
#=================================
