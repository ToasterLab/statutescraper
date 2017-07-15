import bs4, re, json

from statute import Statute
import getter

chapter = "224"

statute = {}

page = bs4.BeautifulSoup(getter.fake_get_chapter(chapter), "html.parser")

statute['title'] = page.find(class_='actHd').get_text()
statute['chapter'] = page.find(class_='chapNo').get_text()
statute['original_source'] = page.find(class_='origSrc').get_text()
statute['description'] = page.find(class_='longTitle').get_text()
statute['date'] = page.find(class_='cDate').get_text()
statute['last_revised'] = page.find(class_='revdTxt').get_text()

statute['contents'] = []

for rawPart in page.find(id='legis').find_all(class_='sGrpTail'):
  part = {}
  try:
    part['number'] = rawPart.find(class_='partHdr').get_text()
    part['title'] = rawPart.find_all(class_='partHdr')[1].get_text()
  except:
    part['title'] = rawPart.find(class_='partHdrIta').get_text()
  part['content'] = []
  for rawSection in rawPart.find_all(class_='prov1'):
    section = {}
    section['number'] = rawSection.find(class_='prov1Txt').find('strong').get_text()
    section['title'] = rawSection.find(class_='prov1Hdr').get_text()
    section['content'] = rawSection.find(class_='prov1Txt').get_text()
    part['content'].append(section)
  statute['contents'].append(part)

print(json.dumps(statute).replace('\\u00ab', '').replace('\\u201c', '').replace('\\u201d', ''))
