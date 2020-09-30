import json


# variables available inside the "variables.json" file:
# fileName
# cssIcons
# cssFonts
# cssStylePath
# websiteTitle
# websiteDescription
# websiteURL
# websiteURLoptional1
# websiteURLoptional2
# websiteImageURL
# websiteImageWidth
# websiteImageHeight
# twitterHandle
# manifestURL
# faviconICO
# faviconPNG
# appleTouchIconPNG
# logoSVG



# =========================================
#                  SCRIPT
# =========================================

# In this script I use TRY / EXCEPT to check if the file and variables exist. That way if the variable doesn't exist, I can have a more personalised description as to why an error has occured. The details of these error description will improve as the errors occur.

# open variables.json
try: 
    json_file = open("variables.json", "r", encoding="utf-8")
    print('OK - variables.json found') 
except:
    print('CRITICAL FAIL = variables.json is missing')        
    exit()

# load variables.json
try:    
    variables = json.load(json_file)  
    print('OK - variables.json correctly opened') 
except:
    print('CRITICAL FAIL = format error inside variables.json')        
    exit()

# Close variables.json
try:    
    json_file.close()
    print('OK - variables.json correctly closed') 
except:
    print('CRITICAL FAIL = cant close variables.json')        
    exit()

# Check for variable "fileName" to write html to
try: fileName = variables["fileName"]
except: 
    print('CRITICAL FAIL = variable "fileName" is missing.')        
    exit()

# Check for variable "cssIcons" to write html to
try: cssIcons = variables["cssIcons"]
except: 
    cssIcons = ""
    print('ALERT = variable "cssIcons" is missing.')


cssFonts            = variables["cssFonts"]
cssStylePath        = variables["cssStylePath"]
websiteTitle        = variables["websiteTitle"]
websiteDescription  = variables["websiteDescription"]
websiteURL          = variables["websiteURL"]
websiteURLoptional1 = variables["websiteURLoptional1"]
websiteURLoptional2 = variables["websiteURLoptional2"]
websiteImageURL     = variables["websiteImageURL"]
websiteImageWidth   = variables["websiteImageWidth"]
websiteImageHeight  = variables["websiteImageHeight"]
twitterHandle       = variables["twitterHandle"]
manifestURL         = variables["manifestURL"]
faviconICO          = variables["faviconICO"]
faviconPNG          = variables["faviconPNG"]
appleTouchIconPNG   = variables["appleTouchIconPNG"]
logoSVG             = variables["logoSVG"]


def build_head_tags(x):
    with open(x,'a') as a:
        a.write('<!DOCTYPE html>\n') 
        a.write('<html lang="en-gb">\n') 
        a.write('\n')   
        a.write('<head>\n') 
        a.write('<meta charset="UTF-8">\n') 
        a.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n') 
        a.write('<!-- <link rel="preconnect" href="//www.google-analytics.com"> -->\n') 
        a.write('<title>'+ websiteTitle +'</title>\n')
        a.write('<meta name="robots" content="index, follow">\n')
        a.write('<meta name="description" content="'+ websiteDescription +'">\n')  
        a.write('<meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">\n')  
        a.write('<meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">\n')  
        a.write('<link rel="canonical" href="'+ websiteURL +'">\n')
        a.write('\n')   
        a.write('<!-- Style Sheets -->\n') 
        a.write('<link rel="stylesheet" href="'+ cssIcons +'">\n')   
        a.write('<link rel="stylesheet" href="'+ cssFonts +'">\n') 
        a.write('<link rel="stylesheet" type="text/css" href="'+ cssStylePath +'" >\n') 
        a.write('\n') 
        a.write('<!-- Open Graph Markup Website -->\n') 
        a.write('<meta property="og:locale" content="en_US">\n') 
        a.write('<meta property="og:type" content="website">\n')
        a.write('<meta property="og:title" content="'+ websiteTitle +'">\n')  
        a.write('<meta property="og:description" content="'+ websiteDescription +'">\n')  
        a.write('<meta property="og:url" content="'+ websiteURL +'">\n')  
        a.write('<meta property="og:site_name" content="'+ websiteTitle +'">\n')    
        a.write('<meta property="og:see_also" content="'+ websiteURLoptional1 +'">\n')  
        a.write('<meta property="og:see_also" content="'+ websiteURLoptional2 +'">\n') 
        a.write('\n') 
        a.write('<!-- Open Graph Markup Image -->\n')   
        a.write('<meta property="og:image" content="'+ websiteImageURL +'" />\n')  
        a.write('<meta property="og:image:secure_url" content="'+ websiteImageURL +'">\n')
        a.write('<meta property="og:image:type"        content="image/jpeg">\n')    
        a.write('<meta property="og:image:width"       content="'+ websiteImageWidth +'">\n')  
        a.write('<meta property="og:image:height"      content="'+ websiteImageHeight +'">\n') 
        a.write('\n')
        a.write('<!-- Open Graph Markup Twitter -->\n') 
        a.write('<meta name="twitter:card"             content="summary_large_image">\n')   
        a.write('<meta name="twitter:creator"          content="'+ twitterHandle +'">\n') 
        a.write('<meta name="twitter:site"             content="'+ twitterHandle +'">\n') 
        a.write('<meta name="twitter:title"            content="'+ websiteTitle +'">\n')    
        a.write('<meta name="twitter:url"              content="'+ websiteURL +'">\n')  
        a.write('<meta name="twitter:domain"           content="'+ websiteTitle +'">\n') 
        a.write('<meta name="twitter:description"      content="'+ websiteDescription +'">\n') 
        a.write('<meta name="twitter:image:src"        content="'+ websiteImageURL +'">\n')  
        a.write('\n') 
        a.write('<!-- Manifest -->\n')  
        a.write('<link rel="manifest"                  href="'+ manifestURL +'">\n') 
        a.write('\n')    
        a.write('<!-- Favicons -->\n')  
        a.write('<link rel="icon" type="image/x-icon"  href="'+ faviconICO +'">             <!-- 32px x 32px -->\n') 
        a.write('<link rel="icon" type="image/png"     href="'+ faviconPNG +'">             <!-- 1,024px × 1,024px ~12kb -->\n') 
        a.write('<link rel="apple-touch-icon"          href="'+ appleTouchIconPNG +'">    <!-- 1,024px × 1,024px ~12kb -->\n') 
        a.write('<link rel="mask-icon" color="#fff"    href="'+ logoSVG +'">\n')     
        a.write('\n')  
        a.write('<!-- <script>\n')  
        a.write('Google Analytics script goes here.\n') 
        a.write('</script> -->\n')  
        a.write('</head>\n')    
        

build_head_tags(fileName)