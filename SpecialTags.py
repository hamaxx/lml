class SpecialTags:
	def __init__(self, texArray):
		self.texArray = texArray
		 
	def lml(self, tag):
		self.texArray.append("\\documentclass[" + tag["options"] + "]{" + tag["class"] + "}")
		return False

	def pagebreak(self, tag):
		self.texArray.append("\\pagebreak{}")
		return False
		
	def br(self, tag):
		self.texArray.append("\\\\")
		return False

	def head(self, tag):
		return "\\maketitle"
