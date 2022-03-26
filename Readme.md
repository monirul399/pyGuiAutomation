## Module 1: <span style="color: maroon">Make a Business directory listing<span>
Runable File: `main.py`

### Necessary Information for Coding
* Hunter Scrapper Position :  ```x, y = 1643, 80```
* URL Position :  ```x, y = 1643, 80```

### Necessary Insight
* This program will always start with on-display chrome tab 
* <span style="color: green">There is scope to reduce errors</span> There is scope to reduce errors ... After implementation focus on `efficiency` and `probable error`.
* Issues occur when internet is `slow`
* **CSV Download failed**. It's a major issue next time. <span style="color: green">Think for a solution</span>, <span style="color: red">V2 Task</span>.
* Make unique row for final CSV : <span style="color: blue">Task done</span>.
* `main.py` file is the automation for *Data Scraping* and *Preprocessing* 
* Always need to delete **Already existing files** from folder before exporting **Already existing files** using code. It gives ```FileExistsError: [WinError 183] Cannot create a file when that file already exists``` error. If needed, catch the exception and <span style="color: green"> **THINK** other use case like *delete existing files from the local directory*</span>.
* Time *efficiency* and *automation accuracy* is possible.<span style="color: green">Think about optimization from different angle</span>.

### Task List
* Alternative image replacement (Depending on dynamic UI changes) when not found
    - Example: `B2Cchrome.png` file has an alternative *image* file `Screenshot_1.png`. 
    - Solution: Use loop several times and then replace the *image* file for alternative


### Issues & Improvement scope
* Find display **image** more *precisely*.



