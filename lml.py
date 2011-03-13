import BeautifulSoup, sys, re
from SpecialTags import SpecialTags

tex = []
specialTags = SpecialTags(tex)

def removeWS(s):
	 return re.sub(r'^\n', '', s)

def parseTag(tag):
	if tag.__class__ == BeautifulSoup.NavigableString:
		if len(tag) > 0 and not tag.isspace():
			tex.append(removeWS(tag))
		return False
		
	name = tag.name
	
	if hasattr(specialTags, name):
		return getattr(specialTags, name)(tag)
	
	if tag.has_key("value") and not tag.findAll(True):
		tex.append("\\" + name + "{" + tag["value"] + "}")
		return False
		
	tex.append("\\begin{" + name + "}")
	return "\\end{" + name + "}"

def parseXML(obj):
	endTag = parseTag(obj)
	
	if obj.__class__ != BeautifulSoup.NavigableString:
		for tag in obj.contents:
			parseXML(tag)
	
	if endTag:
		tex.append(endTag)

if len(sys.argv) > 2:
	infile = sys.argv[1]
	outfile = sys.argv[2]

	xml = BeautifulSoup.BeautifulStoneSoup(open(infile, 'r'))
	parseXML(xml.find("lml"))

	open(outfile,"w").write("\n".join(tex).encode( "utf-8" ))

