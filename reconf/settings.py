# settings.py

from datetime import date

#### You must configure the following items

#group_collection(160464, collection='MGID93AS')
#group_collection(160464, collection='4KATF6MA')  # Miscellaneous collection is kept outside the tree

# Also merge a private collection:
#user_collection('1366641', api_key = 'X4iUU2a7P5mQWNTO7hvuQwzB', collection='FCQK6PT6')

# Exclude some collections out of the 1366641 library
# Give either the collection name or the key
#exclude_collection('Selected Works') # Selected Works ZJFRZTCB
#exclude_collection('AWMEXUV2') # In Review and to appear
#exclude_collection('HZHSMP74') # Theses

#rename_collection('BQUUP5PR', "Language")


#filter_items(lambda i: not 'FCQK6PT6' in i.collections or i.year>2008)  # This is a function that returns True for every item to be included
#exclude_items(lambda i: 'Reitter' in i.html and i.year<2011)  # This is a function that returns True for every item to be included


# The sort_criteria determine the structure of the bibliography.
# Allowable values: 'type' (category of publication, e.g., journal article),
# 'date' (full date)
# 'year' (year of publication)
# 'collection' (the subcollection the article is placed in).
# Collection works best at the beginning of the list.
# add - in front of the field name to sort in descending order (e.g., -date will show the newest entries first).

# See also: show_top_section_headings setting below.

# Two typical variants are shown:
# Thematic, by collection
sort_criteria = ['-date','collection']   # First by collection, then type, then by date, latest first.
# By type (journal, conference, etc.), then chronologically
# sort_criteria = ['type','-date']   # we have date and type: First by date ("issued"), then by type.
# By year, then with journal articles first,'-date'
# sort_criteria = ['-year']   # we have date and type: First by date ("issued"), then by type.
# By date only, newest first
#sort_criteria = ['-date']   # we have date and type: First by date ("issued"), then by type.



###### Special settings


bib_style =  'universidade-do-porto-faculdade-de-psicologia-e-de-ciencias-da-educacao'     # bibliography style format (e.g., 'apa' or 'mla') - Any valid CSL style in the Zotero style repository
#bib_style =  'apa'

show_top_section_headings = 1  # show section headings for the first N sort criteria

titlestring = "Combinatorial Reconfiguration Bibliography"

write_full_html_header = True   # False to not output HTML headers.  In this case, expect a file in UTF-8 encoding.

outputfile = 'index.html'  # relative or absolute path name of output file

# Attachments
file_outputdir = 'storage'
# Location to save attached files.
file_output_path = "storage"
# relative URL on server, corresponding to file_outputdir

# no_cache = True
# True means do not use cache;
# retrieve items from Zotero database every time (slow)

mathjax = True # use MathJax
file_link_button_label = None  #: Set to None for label specific to the document (link, PS, PDF)

# Define labels for article types and their ordering
# types may occur in libraryCatalog or itemType
# use libraryCatalog to override it in special cases
# (e.g., archival Conference papers)
sortkeyname_order['en']['type'] = [('journalArticle', 'Journal Articles'),
                         ('archivalConferencePaper', 'Archival Conference Papers'),
                         ('conferencePaper', 'Conference and Workshop Papers'),
                         ('book','Books'),
                         ('bookSection', 'Book Chapters'),
                         ('edited-volume', "Edited Volumes"),
                         ('thesis', 'Theses'),
                         ('report', 'Technical Reports'),
                         ('attachment', 'Documents'),
                         ('webpage', 'Web Sites'),
                         ('presentation', 'Talks'),
                         ('videoRecording', 'Video Recordings'),
                         ('blogPost', 'Blog Posts'),
                         ('manuscript', 'Manuscripts')]

show_search_box = True  # show a Javascript/JQuery based search box to filter pubs by keyword.  Must define jquery_path.
jquery_path = "site/jquery.min.js"  # path to jquery file on the server - default: wordpress location

number_bib_items = False  # show bibliographic items as numbered, ordered list

custom_footer = "<div id=\"last_modified\" style=\"float: left;\">Last Modified: " + date.today().strftime("%B %d, %Y") + ".</div>"

custom_message = u"<div class=\"custom_message\">This interactive web bibliography on <a href=\"http://www.ecei.tohoku.ac.jp/alg/core/\">Combinatorial Reconfiguration</a> is created from a Zotero collection of <a href=\"https://hoanganhduc.github.io/\">Duc A. Hoang</a> using a <a href=\"https://github.com/hoanganhduc/zotero\">forked version</a> of <a href=\"\">davidswelt/zot_bib_web</a> with slight modification.</div>"
    
show_copy_button = True
clipboard_js_path = "site/clipboard.min.js"
copy_button_path = "site/clippy.svg" # path to file on server

show_links = ['bib', 'url', 'file']   # unconditionally show these items if they are available.

show_shortcuts = [shortcut('year', [2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,'-2011'])]
show_shortcuts += ['type']

stylesheet_url = "style.css"

