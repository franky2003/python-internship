from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
headings = soup.find_all(class_="title")
h_list=[]
s_list=[]
l_list=[]
for i in headings:
    h_list.append(i.getText())
    if i.a:
        heading_link = i.a['href']
        l_list.append(heading_link)
    else:
        l_list.append(None)   
print(h_list)
print(l_list)
scores = soup.find_all(class_="score")
for j in scores:
    s_list.append(j.getText())
print(s_list)    

#Output
'''
['1.', 'Lotus 1-2-3 For Linux (cmpxchg8b.com)', '2.', 'Show HN: "Interactive" Italian Poetry for English Speakers (italianpoetry.it)', '3.', 'Cloudflare Sippy: Incrementally Migrate Data from AWS S3 to Reduce Egress Fees (infoq.com)', '4.', 'State of the Map EU 2023 (stateofthemap.eu)', '5.', 'BeagleV-Ahead open-source RISC-V single board computer (beagleboard.org)', '6.', '"Hacker News" for retro computing and gaming (jgc.org)', '7.', "Trying out C++20's modules with Clang and Make (0x1.pt)", '8.', 'Sessionic: A cross-browser extension to save, manage, restore tabs and sessions (github.com/navorite)', '9.', 'Recursive Recipes (schollz.com)', '10.', 'Sieve (YC W22), the video/audio AI cloud, is hiring systems engineers (sievedata.com)', '11.', 'Show HN: 3D Binpacking Algorithm Visualized (skusavvy.com)', '12.', 'The Welsh Punk Scene of the 1980s (huckmag.com)', '13.', 'Ten Years Writing Book Reviews (2003) (dannyreviews.com)', '14.', "Steve's Explanation of the Viterbi Algorithm (2003) (toronto.edu)", '15.', 'Transactions and Concurrency in PostgreSQL (doadm-notes.blogspot.com)', '16.', 'The Apple Macintosh Primer (1984) [pdf] (vintageapple.org)', '17.', 'Think in Analog, Capture in Digital (huwfulcher.com)', '18.', "Implementing a GPU's programming model on a CPU (litherum.blogspot.com)", '19.', 'Disney Mocked for Ludicrously Fake CGI "Actors" in Crowd Scene (futurism.com)', '20.', 'Show HN: Mini-Woo, luanch Telegram mini app for WooCommerce in seconds (github.com/mini-woo)', '21.', 'History of the Mackintosh: 200 years of the classic raincoat (theguardian.com)', '22.', "2023 was earth's warmest September In 174 year record (noaa.gov)", '23.', 'The British Mosquito once carried Niels Bohr in its bomb bay (thedrive.com)', '24.', 'ChatGPT’s system prompts (github.com/spdustin)', '25.', 'Show HN: Firefox add-on to open YouTube videos in alternative front ends (github.com/d3vr)', '26.', 'First word discovered in unopened Herculaneum scroll by CS student (scrollprize.org)', '27.', "Google has sent internet into 'spiral of decline', claims DeepMind co-founder (telegraph.co.uk)", '28.', 'Examining the silicon dies of the Intel 386 processor (righto.com)', '29.', 'The Garden of the Five Senses (worldsensorium.com)', '30.', 'Ask HN: What is your experience with Nano-Hydroxyapatite toothpaste?', 'More']
[None, 'https://lock.cmpxchg8b.com/linux123.html', None, 'https://italianpoetry.it/', None, 'https://www.infoq.com/news/2023/10/cloudflare-sippy-migrate-s3/', None, 'https://stateofthemap.eu/', None, 'https://www.beagleboard.org/boards/beaglev-ahead', None, 'https://blog.jgc.org/2023/10/hacker-news-for-retro-computing-and.html', None, 'https://0x1.pt/2023/10/15/trying-out-c++20s-modules-with-clang-and-make/', None, 'https://github.com/navorite/sessionic', None, 'https://recursiverecipes.schollz.com/', None, 'https://www.sievedata.com/', None, 'https://skusavvy.com/bin-packing-preview', None, 'https://www.huckmag.com/article/inside-the-80s-welsh-punk-scene', None, 'https://dannyreviews.com/history.html', None, 'https://www.cs.toronto.edu/~sengels/tutorials/viterbi.html', None, 'https://doadm-notes.blogspot.com/2023/10/transactions-and-concurrency-in.html', None, 'https://vintageapple.org/macbooks/pdf/The_Apple_Macintosh_Primer_1984.pdf', None, 'https://huwfulcher.com/blog/2023-10-14-think-in-analog-capture-in-digital/', None, 'http://litherum.blogspot.com/2023/10/implementing-gpus-programming-model-on.html', None, 'https://futurism.com/the-byte/disney-mocked-fake-cgi-actors-crowd-scene', None, 'https://github.com/mini-woo/mini-woo', None, 'https://www.theguardian.com/news/2023/oct/12/history-mackintosh-raincoat-charles-macintosh', None, 'https://www.noaa.gov/news/topping-charts-september-2023-was-earths-warmest-september-in-174-year-record', None, 'https://www.thedrive.com/the-war-zone/the-nuclear-scientist-and-the-warplane-that-became-britains-most-unlikely-airliner', None, 'https://github.com/spdustin/ChatGPT-AutoExpert/blob/main/System%20Prompts.md', None, 'https://github.com/d3vr/yt-siphon', None, 'https://scrollprize.org/firstletters', None, 'https://www.telegraph.co.uk/business/2023/10/14/google-internet-spiral-of-decline-deepmind-mustafa-suleyman/', None, 'http://www.righto.com/2023/10/intel-386-die-versions.html', None, 'https://worldsensorium.com/the-garden-of-the-five-senses/', None, 'item?id=37888728', '?p=2']
['14 points', '50 points', '120 points', '24 points', '124 points', '232 points', '4 points', '98 points', '136 points', '97 points', '72 points', '37 points', '41 points', '45 points', '34 points', '34 points', '229 points', '27 points', '27 points', '38 points', '24 points', '185 points', '711 points', '276 points', '1094 points', '296 points', '259 points', '17 points', '104 points']
'''