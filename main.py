import csv
import re
import requests
import xml.etree.ElementTree as ET
def check_attributes(tree, root_path, tag_name, index):
    root = tree.getroot()
    ctr=0
    list_of_attributes=[]
    list_of_texts=[]
    for item in root.findall('./bug'):
      list_temp = [ctr, str(item[index].attrib)]
      list_of_attributes.append(list_temp)
      list_temp = [ctr, str(item[index].text)]
      list_of_texts.append(list_temp)

    for i in range(len(list_of_texts)):
      if list_of_texts[i][1].find("None") !=-1:
        index_list = re.findall(r'\d+', list_of_attributes[i][1]) # Find the index information
        if len(index_list)==0:
          x=0
        else:
          x=index_list[0]
        list_of_texts[i][1]=list_of_texts[int(x)][1]
    ctr=0

    for item in root.findall('./bug/'+tag_name):
      item.text = list_of_texts[ctr][1]
      ctr+=1

    tree.write("final.xml")
    # for i in range(len(list_of_texts)):
    #   print(list_of_texts[i][1])


def edit_XML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # # get root element
    root = tree.getroot()
    # root_path = './bug'
    # tag_list = ['fileName', 'moduleName', 'packageName']
    # for tag in range(len(tag_list)):
    #   if tag=='fileName':
    #     index=5
    #   elif tag=='moduleName':
    #     index=6
    #   else:
    #     index=7
    #   check_attributes(tree,root_path,str(tag),index)
    ctr=0
    list_of_attributes=[]
    list_of_texts=[]
    for item in root.findall('./bug'):
      list_temp=[ctr,str(item[5].attrib)]
      list_of_attributes.append(list_temp)
      list_temp=[ctr,str(item[5].text)]
      list_of_texts.append(list_temp)
      ctr+=1
    for i in range(len(list_of_texts)):
      if list_of_texts[i][1].find("None") != -1:
        index_list = re.findall(r'\d+', list_of_attributes[i][1])
        x = index_list[0]
        # print(x)
        # Now replace the values in the list_of_texts
        # print(list_of_texts[int(x)][1])
        list_of_texts[i][1]=list_of_texts[int(x)][1]

    ctr=0
    for item in root.findall('./bug/fileName'):
      item.text = list_of_texts[ctr][1]
      # item.set('updated','yes')
      # item.pop("reference")
      if 'reference' in item.attrib:
        # print("reference match")
        del item.attrib['reference']
      ctr+=1
    print("fileName complete^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    ctr=0
    list_of_attributes=[]
    list_of_texts=[]
    for item in root.findall('./bug'):
      list_temp=[ctr,str(item[6].attrib)]
      list_of_attributes.append(list_temp)
      list_temp=[ctr,str(item[6].text)]
      list_of_texts.append(list_temp)
      ctr+=1
    for i in range(len(list_of_texts)):
      if list_of_texts[i][1].find("None") != -1:
        # print("None indeed here")
        # Find the index
        # print(list_of_attributes[i][1])
        index_list = re.findall(r'\d+', list_of_attributes[i][1])
        if len(index_list)==0:
          x=0
        else:
          x=index_list[0]
        # x = index_list[0]
        # print(x)
        # Now replace the values in the list_of_texts
        # print(list_of_texts[int(x)][1])
        list_of_texts[i][1]=list_of_texts[int(x)][1]

    ctr=0
    for item in root.findall('./bug/moduleName'):
      item.text = list_of_texts[ctr][1]
      # item.set('updated','yes')
      # item.pop("reference")
      if 'reference' in item.attrib:
        # print("reference match")
        del item.attrib['reference']
      ctr+=1
    print("moduleName complete^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    ctr=0
    list_of_attributes=[]
    list_of_texts=[]
    for item in root.findall('./bug'):
      list_temp=[ctr,str(item[7].attrib)]
      list_of_attributes.append(list_temp)
      list_temp=[ctr,str(item[7].text)]
      list_of_texts.append(list_temp)
      ctr+=1
    for i in range(len(list_of_texts)):
      if list_of_texts[i][1].find("None") != -1:
        # print("None indeed here")
        # Find the index
        index_list = re.findall(r'\d+', list_of_attributes[i][1])
        if len(index_list)==0:
          x=0
        else:
          x=index_list[0]
        # Now replace the values in the list_of_texts
        # print(list_of_texts[int(x)][1])
        list_of_texts[i][1]=list_of_texts[int(x)][1]

    ctr=0
    for item in root.findall('./bug/packageName'):
      item.text = list_of_texts[ctr][1]
      # item.set('updated','yes')
      # item.pop("reference")
      # print(item.attrib)
      if 'reference' in item.attrib:
        # print("reference match")
        del item.attrib['reference']
      ctr+=1
    print("packageName complete^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    tree.write("final.xml")

def main():
    edit_XML('sample.xml')

if __name__ == "__main__":
    # calling main function
    main()
