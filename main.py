import csv
import re
import requests
import xml.etree.ElementTree as ET
def loadXML():
    # # url of rss feed
    # url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml';
    # # creating HTTP response object from given url
    # resp = requests.get(url)
    # saving the xml file
    with open('sample.xml', 'wb') as f:
        f.write(resp.content)
def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()

    ctr=0
    for item in root.findall('./bug'):
      print("Bug #"+str(ctr)+"\nFilename: "+str(item[   5].attrib)) #+"\nModulename: "+str(item[6].attrib)+"\nPackagename: "+str(item[7].attrib))
      # Write to File
      file_pointer = open("filename.txt","a")
    #   write("["+str(ctr)+"] "+str(item[5].attrib))
      lines_of_text=[str(ctr),":", str(item[5].attrib)+ "\n"]
      file_pointer.writelines(lines_of_text)
      file_pointer.close()
    #   ctr+=1
      file_pointer = open("correct.txt","a")
      lines_of_text=[str(ctr),":", str(item[5].text)+ "\n"]
      file_pointer.writelines(lines_of_text)
      file_pointer.close()
      ctr+=1


    with open("correct.txt","r") as ins:
        for line in ins:
            parts=line.split(':')
            if(parts[1]=="None\n"):
                print("We need to change "+ parts[1])

    # Go through the entire XML bugs section and save the attributes to a file
    # Also save the entries with appropriate index
    # Replace the attributes with actual values rather than references.

    # create empty list for news items
    # newsitems = []
    # # iterate news items
    # for item in root.findall('./channel/item'):
    #     # empty news dictionary
    #     news = {}
    #     # iterate child elements of item
    #     for child in item:
    #         # special checking for namespace object content:media
    #         if child.tag == '{http://search.yahoo.com/mrss/}content':
    #             news['media'] = child.attrib['url']
    #         else:
    #             news[child.tag] = child.text.encode('utf8')
    #     # append news dictionary to news items list
    #     newsitems.append(news)

    # # return news items list
    # return newsitems
    return root
def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        # writing headers (field names)
        writer.writeheader()
        # writing data rows
        writer.writerows(newsitems)

def main():
    # load rss from web to update existing xml file
    # loadRSS()
    # parse xml file
    newsitems = parseXML('sample.xml')
    # store news items in a csv file
    # savetoCSV(newsitems, 'topnews.csv')


if __name__ == "__main__":
    # calling main function
    main()
