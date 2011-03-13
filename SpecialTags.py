class SpecialTags:
	def __init__(self, tex):
		self.tex = tex
		 
	def lml(self, tag):
		self.tex.append("\\documentclass[" + tag["options"] + "]{" + tag["class"] + "}")
		return False

	def pagebreak(self, tag):
		self.tex.append("\\pagebreak{}")
		return False
		
	def br(self, tag):
		self.tex.append("\\\\")
		return False

	def head(self, tag):
		return "\\maketitle"
