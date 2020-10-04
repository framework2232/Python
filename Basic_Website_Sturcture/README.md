<p align="center">
    <img src="https://github.com/framework2232/framework2232.github.io/blob/master/images/banner.png?raw=true" alt="Framework2232 Logo" width="500"/>
</p>
<h1 align=center>BASIC WEBSITE STRUCTURE</h1>

__AUTHOR:__ Framework2232

__COPYRIGHT:__ © 2020, Framework2232

__DATE:__ 04OCT20

__VERSION:__ 1.0.1

__GITHUB:__ [__/framework2232/.../Basic_Website_Sturcture__](https://github.com/framework2232/Python/tree/master/Basic_Website_Sturcture "Basic Website Structure")

__WEBSITE:__ [__https://framework2232.github.io__](https://framework2232.github.io "Framework2232")

---


## PURPOSE
#### _Developed as a quick folder / file builder for static HTML/CSS website._

* This script is for anyone who is building a website from complete scratch using HTML and CSS.
* This python script will build a common folder structure and add basic files.
   * empty ___index.html___ inside root folder
   * empty ___style.css___ inside __css__ folder
   * empty ___img___ folder
* The script reduces time in the basic setup of file structure as the folders and files are ready to go.
* This script is designed to be run as the first part of the process of writting the website.
* The files are built in a folder named ___/webSite/___ in your current drive. If the folder already exists, the script wont run. This is to prevent existing files being accidently over written. Running the script with its default settings, the result is:
   * __/webSite/css/style.css__
   * __/webSite/img/__
   * __/webSite/index.html__
   * __/webSite/main.js__
   * __/webSite/manifest.json__
   * __/webSite/robots.txt__


---
## HOW TO RUN SCRIPT:
1. __Run Python Script__ with: _"RunMe"_ python script. 

1. __Click 'BUILD'__ for the default file, or deselect the files not required. Changes can be made anytime before 'BUILD' is selected.


<p align="center">
    <img src="https://github.com/framework2232/Python/blob/master/Basic_Website_Sturcture/img/screenShot_GUIa.PNG?raw=true" alt="Framework2232 Logo" width="500"/>
</p>

* ___Above:__ Image shows all buttons green, therefore when build is selected, all files and folders will be made (default)._

---

<p align="center">
    <img src="https://github.com/framework2232/Python/blob/master/Basic_Website_Sturcture/img/screenShot_GUIb.PNG?raw=true" alt="Framework2232 Logo" width="500"/>
</p>

* ___Above:__ Image shows some buttons have been deselected, therefore only the green files and folders will be made. On the right the diagram has selected files in green, and deselected files in grey._

---

<p align="center">
    <img src="https://github.com/framework2232/Python/blob/master/Basic_Website_Sturcture/img/screenShot_files.PNG?raw=true" alt="Framework2232 Logo" width="500"/>
</p>

* ___Above:__ Image shows resulting file structure. Existing is files and folders ready for your data._

---
## HOW THE SCRIPT WORKS

__1.__ Script declares variables and calls definitions:
```python
folder = '/webSite/'
file = 'index.html'
makeMyFolder(folder)
makeMyFile(folder, file)
```

__2.__ If the folder _DOES NOT_ already exist, the folder is made:
```python
def makeMyFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print('Made your folder: ' + folder)
```

__3.__ If the folder _DOES_ exist, the folder is made:
```python
if not os.path.exists(folder):
        os.makedirs(folder)
        print('Made your folder: ' + folder)
    else:
        print('** CAUTION **            This folder already exists: ' + folder)
        print('** SCRIPT TERMINATED **  Check the path is correct')
        print('')
        exit()
```

__4.__ The empty file is built in the appropriate directory.
```python
def makeMyFile(folder, file):
    os.chdir(folder)
    with open(file,'w') as f:
        f.write('')
        print('Built: '+ file)
```

---

## ABOUT FRAMEWORK2232

I independently work on Framework2232 in my free time. If you like show your support, please follow and promote the usual social media.

[__Twitter__][Twitter]
| [__Instagram__][Instagram]
| [__YouTube__][YouTube]
| [__GitHub__][GitHub]
| [__Pinterest__][Pinterest]

__This repository is shared public in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.__

[See the GNU General Public License for more details.](http://www.gnu.org/licenses/)

---

[Twitter]: https://github.com/framework2232/Python "Twitter - Framework2232"
[Instagram]: https://github.com/framework2232/HTML "Instagram - Framework2232"
[YouTube]: https://github.com/framework2232/CSS "YouTube - Framework2232"
[GitHub]: https://github.com/framework2232/Markdown "GitHub - Framework2232"
[Pinterest]: https://github.com/framework2232/Markdown "Pinterest - Framework2232"