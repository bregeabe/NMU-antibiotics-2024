## Resources for functionality

### Barcode
Here is an [article](https://www.geeksforgeeks.org/how-to-generate-barcode-in-python/) on barcodes
```
# import EAN13 from barcode module 
from barcode import EAN13 
  
# Make sure to pass the number as string 
number = '5901234123457'
  
# Now, let's create an object of EAN13 
# class and pass the number 
my_code = EAN13(number) 
  
# Our barcode is ready. Let's save it. 
my_code.save("new_code")
```
That code creates a barcode in svg format, other formats like png and jpg can be generated as well

### GUI 
Getting started with [tkinter](https://docs.python.org/3/library/tkinter.html)

Example window
```
python -m tkinter
```
### Hardware
**Barcode Scanner** <br>
[option 1](https://www.amazon.com/Barcode-Scanner-Wired-Handheld-Reader/dp/B07CGQS2PD/ref=asc_df_B07CGQS2PD/?tag=hyprod-20&linkCode=df0&hvadid=693270340014&hvpos=&hvnetw=g&hvrand=5975177541459955724&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9196738&hvtargid=pla-2009536788148&mcid=e341c0ab998b34e0b257a8245b513237&th=1)
<br>
[option 2](https://www.amazon.com/NetumScan-Handheld-Supports-Warehouse-Supermarket/dp/B098NKCR1G/ref=asc_df_B098NKCR1G/?tag=hyprod-20&linkCode=df0&hvadid=693270340014&hvpos=&hvnetw=g&hvrand=5975177541459955724&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9196738&hvtargid=pla-1538769764085&psc=1&mcid=b85a20ca72f63172959b8faba1b7f57c) <br><br>

**Printer**
