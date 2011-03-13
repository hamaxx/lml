import BeautifulSoup, sys, re
from SpecialTags import SpecialTags

texArray = []
specialTags = SpecialTags(texArray)

def removeWS(s):
	 return re.sub(r'^\n', '', s)

def parseTag(tag):
	if tag.__class__ == BeautifulSoup.NavigableString:
		if len(tag) > 0 and not tag.isspace():
			texArray.append(removeWS(tag))
		return False
		
	name = tag.name
	
	if hasattr(specialTags, name):
		return getattr(specialTags, name)(tag)
	
	if len(tag.contents) == 0:
		value = ""
		options = ""
		
		if tag.has_key("value"):
			value = "{" + tag["value"] + "}"
		if tag.has_key("options"):
			options = "[" + tag["options"] + "]"
			
		texArray.append("\\" + name + value + options)
		return False
			
			
	options = ""
	if tag.has_key("options"):
		options = "[" + tag["options"] + "]"
		
	texArray.append("\\begin{" + name + "}" + options)
	return "\\end{" + name + "}"

def parseXML(obj):
	endTag = parseTag(obj)
	
	if obj.__class__ != BeautifulSoup.NavigableString:
		for tag in obj.contents:
			parseXML(tag)
	
	if endTag:
		texArray.append(endTag)

if len(sys.argv) > 2:
	infile = sys.argv[1]
	outfile = sys.argv[2]

	xml = BeautifulSoup.BeautifulStoneSoup(open(infile, 'r'))
	parseXML(xml.find("lml"))

	open(outfile,"w").write("\n".join(texArray).encode( "utf-8" ))

