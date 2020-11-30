import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
import os
import wget

url = "https://www.google.com/imghp?hl=en"
browser.open(url)

#get html
browser.get_current_page()
browser.select_form()
forms = browser.get_current_form().print_summary()

# search for term
search_term = str(input("Enter a term to download its images:\n"))
browser["q"] = search_term

browser.launch_browser()
response = browser.submit_selected()

# Submit new URL
new_url = browser.get_url()
browser.open(new_url)

# get HTML
page = browser.get_current_page()
all_imgs = page.find_all('img')

# target the souce of img
img_src = []
for img in all_imgs:
	img = img.get('src')
	img_src.append(img)

img_src = [img for img in img_src if img.startswith('https')]

path = os.getcwd()
path = os.path.join(path, (search_term + "s"))

# Create the directory if not existing
if path.endswith('cats'):
	print('Directory already exists, saving images to the existing one!')
else:
	os.mkdir(path)

print('\n\n')

# Download images
counter = 0
for img in img_src:
	save_as = os.path.join(path, (search_term + str(counter) + ".png"))
	wget.download(img, save_as)
	counter += 1