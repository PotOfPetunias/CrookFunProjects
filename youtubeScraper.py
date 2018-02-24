import requests
import time
from bs4 import BeautifulSoup

def getVideos(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html5lib")
    state = 0
    videos = []
    currentVid = []
    for child in soup.body.descendants:
        if child.string:
            text = child.string.strip()        
            if state in range(0,3):
                if "Latest from" in text:
                   state += 1
            elif state in range(3,6):
                if "Play now" in text:
                   state += 1
            elif state == 10:
                if not child.title:
                    state += 1
                    currentVid.append(text)
            elif state in [6, 7, 8, 9, 11, 13, 15, 16]:
                state += 1
            elif state == 12:
                if 'Duration' in text :
                    state +=1
                    currentVid.append(text)
            elif state == 14:
                state +=1
                currentVid.append(text)
            elif state == 17:
                state +=1
                if "year" in text or "month" in text or "week" in text or "day" in text:
                    break
                currentVid.append(text)
            else:
                videos.append(currentVid)
                currentVid = []
                state = 3
    return videos
    
def getDuration(vid):
    d = vid[1][12:-1].split(':')
    if len(d) == 2:
        mins = int(d[0])
        seconds = int(d[1])/60
        return mins + seconds
    elif len(d) == 3:
        hours = int(d[0]) * 60
        mins = int(d[1])
        seconds = int(d[2])/60
        return hours + mins + seconds

def genURL(channel):
    url = 'https://www.youtube.com/results?search_query='
    namesplit = channel.strip().split(' ')
    for word in namesplit:
        url += word + '+'
    return url

channels = ['AndrewSchrock', 'Beyond the press', 'Braille Army', 'Braille Skateboarding',
            'CGP Grey', 'Channel Super Fun', 'DONG', 'Ed Pratt', 'Good Mythical MORE',
            'Good Mythical Morning', 'Hydraulic Press Channel', 'Jake and Josh', 'JoergSprave',
            'Jonny Giger', 'Kurzgesagt In a Nutshell', 'Mark Rober', 'Marques Brownlee',
            'Matt Parker', 'Mike Boyd', 'Practical Engineering', 'Real Engineering',
            'SciShow Space', 'Scott Manley', 'Second Thought', 'SmarterEveryDay',
            'The Slow Mo Guys', 'Tom Scott', 'Unbox Therapy', 'Veritasium', 'Vintage Space',
            'Wintergatan']

total = 0
allVids = []
for channel in channels:
    time.sleep(0.125)
    print('getting', channel, '...')
    videos = getVideos(genURL(channel))
    if len(videos) != 0:
        allVids.append(videos)

for chan in allVids:
    print()
    chanDur = 0
    for vid in chan:
        d = getDuration(vid)
        chanDur += d
        total += d
    print(chan[0][2], round(chanDur,3), 'minutes')
    for vid in chan:
        print(vid[0])

print()
print(round(total,3), 'total minutes')
print(round(total/60,3), 'total hours')

##r = requests.get('https://www.youtube.com/results?search_query=jake+and+josh')
##soup = BeautifulSoup(r.text, "html5lib")
#print(soup.body.contents[0].name)
#print(soup.prettify())

#print(soup.find_all('ytd-grind-video-renderer'))
#print(soup.find_all('a', class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ",
#title="ALL SPORT TRICK SHOT BATTLE! *Crazy Ending*"))
