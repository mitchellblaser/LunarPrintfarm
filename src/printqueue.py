def CollectAllTags(printers: list):
    taglist = []
    
    for printer in printers:
        for tag in printer.tags:
            if tag not in taglist:
                taglist.append(tag)
    
    print(taglist)
    return taglist