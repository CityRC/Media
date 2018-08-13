#import argparse
import csv
import lxml.etree as et

with open('tees.csv', 'rb') as csvfile:
    teereader = csv.reader(csvfile)
    xml = et.parse("./XSL/MainContent.xml")
    mainXsl = et.XSLT(et.parse("./XSL/MainTemplate.xsl"))
    
    for row in teereader:
        id = row[0]
        print("Processing " + str(id))
        design = row[1]
        
        params = {"param" + str(key + 1) : str("'" + val + "'") for key, val in enumerate(filter(None, row[2:]))}
        
        xsl = et.XSLT(et.parse("./XSL/" + design + ".xsl"))
        transformed = str(xsl(xml, **params))

        outputPath = "./output/" + id + ".svg"
        design = open(outputPath, "w+")
        design.write(transformed)

        #final = mainXsl()

        design.close()
            
        