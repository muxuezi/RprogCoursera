from PyPDF2 import PdfFileMerger, PdfFileReader
import os

os.chdir('slide')
merger = PdfFileMerger()
label = 0
for filename in sorted(os.listdir('.'),key=lambda k:int(k.split('.')[0])):
    with open(filename,'rb') as f:
        foo = PdfFileReader(f)
        p = foo.getNumPages()
        merger.append(foo)
        merger.addBookmark(filename[:-4], label, parent=None)
        label += p
        print('{}，共{}页'.format(filename, p))
merger.write(r"..\document-output.pdf")
