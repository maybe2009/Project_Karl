# -*- coding: utf-8 -*-
import sys
import urllib.request

# This is the URL of the RSS resource from tp.m-team.cc,
# this URL indicates the XML file we need.
# BTW: This project will be commit to github
#   sun wukong 2015/10/30

url = "https://tp.m-team.cc/torrentrss.php?rows=10&icat=1&ismalldescr=1&isize=1&" \
      "iuplder=1&linktype=dl&passkey=3be41b83b02e7e06c09c2fed283471b9"

# Set the path where we want the XML file settled'''
xml_file_path = "content.xml"

# Function: In this part we do open the url
# Exception:
#   HTTPError cause reconnect action
#   URLError  cause exit action
# On success:
#   Go on!
try:
    response = urllib.request.urlopen(url)
except urllib.request.HTTPError as err:
    print("HTTPError caught:" + str(err))
except urllib.request.URLError as err:
    print("urlopen fail URL:" + url + str(err))
else:
    print("Open URL success")

# Function: Write the content in content to record file
# Exception:
#   IOError
#     Open : cause exit action
#     Write: cause exit action
# On success:
#   Go on!
try:
    f = open(xml_file_path, 'wb')
except IOError as err:
    print("Open file" + xml_file_path + str(err))
    sys.exit(-1)
else:
    print("Open file success")

    try:
        f.write(response.read())
    except IOError as err:
        print("Write file fail: " + str(err))
        sys.exit(-1)
    else:
        print("Write file success")

    f.close()
