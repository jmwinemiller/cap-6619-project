# HTML and PDF Report Format
___

The process for converting python notebooks to pdf report uses a few tools and 
methods and also produces an html report file. *NOTE: This process will 
create a static file with the output of the notebook run*

**Steps for converting a .ipynb notebooks**
- Finish running all the cells to produce the full output
- Download the Colab or other web-based tool, if using jupyter IDE plugin 
  this step can be skipped
- Using the terminal 
  - Run `pip install jupyter`
  - Then to convert the notebook to a HTML report, Run `jupyter nbconvert 
    --to html notebook_file.ipynb`
- Navigate to the new HTML notebook file, and open in the IDE
- Use a browser to view the webpage
  - If notebooks cells or output are cropped or broken, manual page breaks 
    can be added by inserting `<p style="page-break-after:always;"></p>` to 
    the raw html on the appropriate line to move to the cell/output to the 
    next page **NOTE: This is viewable in the print preview**
- Now save as a PDF file
