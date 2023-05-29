import barcode
from barcode.writer import ImageWriter
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_pdf_table():

    # read data from csv file
    df = pd.read_csv('new.csv')
    # df = df[:,13]
    # df.sort_values(by=['unique_id'])
    # df = df.head(24)

    # process alphanumeric characters
    barcode_format = barcode.get_barcode_class('code128')
   
    items = df.values.tolist()

    # Generate barcodes (images in png)
    count = 0
    for item in df.values.tolist():
        my_barcode = barcode_format(item[13].strip(), writer=ImageWriter())
        print(item[13].strip())
        my_barcode.save('./sample/'+str(count)) #save each barcode as image
        count += 1
    

    #dynamically add data to list
    if len(df)%3 != 0:
        rows = int(len(df)/3)+1
        extra = int(len(df)%3)
    else:
        rows = int(len(df)/3)
        extra = 0

    sample=[]
    count=0

    for i in range(rows-1):
        sample.append([[Paragraph("<para align=center spaceb=3><b>"+items[count][1].strip()+"</b><br/><b>"+items[count][2].strip()+"</b></para>") , Image('./sample/'+str(count)+".png",2*inch,1.5*cm)],[Paragraph("<para align=center spaceb=3><b>"+items[count+1][1].strip()+"</b><br/><b>"+items[count+1][2].strip()+"</b></para>") , Image('./sample/'+str(count+1)+".png",2*inch,1.5*cm)],[Paragraph("<para align=center spaceb=3><b>"+items[count+2][1].strip()+"</b><br/><b>"+items[count+2][2].strip()+"</b></para>") , Image('./sample/'+str(count+2)+".png",2*inch,1.5*cm)]])
        count+=3

    if extra == 0:
        sample.append([[Paragraph("<para align=center spaceb=3><b>"+items[count][1].strip()+"</b><br/><b>"+items[count][2].strip()+"</b></para>") , Image('./sample/'+str(count)+".png",2*inch,1.5*cm)], [Paragraph("<para align=center spaceb=3><b>"+items[count+1][1].strip()+"</b><br/><b>"+items[count+1][2].strip()+"</b></para>") , Image('./sample/'+str(count+1)+".png",2*inch,1.5*cm)], [Paragraph("<para align=center spaceb=3><b>"+items[count+2][1].strip()+"</b><br/><b>"+items[count+2][2].strip()+"</b></para>") , Image('./sample/'+str(count+2)+".png",2*inch,1.5*cm)]])
        count+=3
    elif extra == 1:
        sample.append([[Paragraph("<para align=center spaceb=3><b>"+items[count][1].strip()+"</b><br/><b>"+items[count][2].strip()+"</b></para>") , Image('./sample/'+str(count)+".png",2*inch,1.5*cm)]])
        count+=1
    elif extra == 2:
        sample.append([[Paragraph("<para align=center spaceb=3><b>"+items[count][1].strip()+"</b><br/><b>"+items[count][2].strip()+"</b></para>") , Image('./sample/'+str(count)+".png",2*inch,1.5*cm)], [Paragraph("<para align=center spaceb=3><b>"+items[count+1][1].strip()+"</b><br/><b>"+items[count+1][2].strip()+"</b></para>") , Image('./sample/'+str(count+1)+".png",2*inch,1.5*cm)]])
        count+=2


    #add list as table in the pdf file
    count = 0
    items_index = 0
    t=Table(sample, 3* [6.4 * cm], rowHeights= 3.4 * cm, )
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), "CENTER"),
    ('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
    
    doc = SimpleDocTemplate(f"barcode_print.pdf",
                            page_size=A4,
                            bottomMargin=.4 * inch,
                            topMargin=.4 * inch,
                            rightMargin=.2 * inch,
                            leftMargin=.2 * inch)

    items = []
    items.append(t)
    doc.build(items)



generate_pdf_table()