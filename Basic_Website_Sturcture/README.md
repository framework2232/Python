<p align="center">
    <img src="https://github.com/framework2232/framework2232.github.io/blob/master/images/banner.png?raw=true" alt="Framework2232 Logo" width="500"/>
</p>
<h1 align=center>BASIC WEBSITE STRUCTURE</h1>

#### _Developed as a quick folder / file builder for static HTML/CSS website._

* This script is for anyone who is building a website from complete scratch using HTML and CSS.
* This python script will build a common folder structure and add basic files.
   * empty ___index.html___ inside root folder
   * empty ___style.css___ inside __css__ folder
   * empty ___img___ folder
* The script reduces time in the basic setup of file structure as the folders and files are ready to go.
* This script is designed to be run as the first part of the process of writting the website.

---
## HOW TO RUN SCRIPT:
1. __Run Python Script__ with: _"RunMe"_ python script. This will bring up the GUI.


<p align="center">
    <img src="https://github.com/framework2232/framework2232.github.io/blob/master/images/banner.png?raw=true" alt="Framework2232 Logo" width="500"/>
</p>


<p align="center">
    <img src="https://github.com/framework2232/framework2232.github.io/blob/master/images/banner.png?raw=true" alt="Framework2232 Logo" width="500"/>
</p>


<p align="center">
    <img src="https://github.com/framework2232/framework2232.github.io/blob/master/images/banner.png?raw=true" alt="Framework2232 Logo" width="500"/>
</p>
---
## HOW THE SCRIPT WORKS

__1.__ Script declares variables and calls definitions:
```python
folder = '/webSite/'
file = 'index.html'
makeMyFolder(folder)
makeMyFile(folder, file)
```

__2.__ If the folder doesn't already exist, the folder is made:
```python
def makeMyFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print('Made your folder: ' + folder)
```

__3.__ The empty file is built in the appropriate directory.
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