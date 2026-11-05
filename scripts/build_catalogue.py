"""Generate AFTER DARK's public catalogue without exposing the TMDB key.
Run: TMDB_API_KEY=... python3 scripts/build_catalogue.py
Requires Python standard library only. Year partitions avoid TMDB's 500-page discover cap.
"""
import os, json, urllib.request, urllib.parse, urllib.error, time, datetime, pathlib, random
KEY=os.environ.get('TMDB_API_KEY','').strip()
if not KEY: raise SystemExit('Missing TMDB_API_KEY environment variable / GitHub Actions secret')
ROOT=pathlib.Path(__file__).resolve().parents[1]
CURRENT_YEAR=datetime.date.today().year
MIN_YEAR=int(os.environ.get('CATALOGUE_START_YEAR','2010'))
PAGES_PER_YEAR=max(1,min(50,int(os.environ.get('PAGES_PER_YEAR','22'))))
MIN_VOTES=int(os.environ.get('CATALOGUE_MIN_VOTES','12'))
CURATED={
'Found Footage': [('Hell House LLC',2015),('Hell House LLC II: The Abaddon Hotel',2018),('Hell House LLC III: Lake of Fire',2019),('Hell House LLC Origins: The Carmichael Manor',2023),('Grave Encounters',2011),('Grave Encounters 2',2012),('The Taking of Deborah Logan',2014),('As Above, So Below',2014),('The Visit',2015),('Host',2020),('Deadstream',2022),('V/H/S',2012),('V/H/S/2',2013),('V/H/S: Viral',2014),('V/H/S/94',2021),('V/H/S/99',2022),('V/H/S/85',2023),('V/H/S/Beyond',2024),('Creep',2014),('Creep 2',2017),('The Houses October Built',2014),('The Borderlands',2013),('The Bay',2012),('The Sacrament',2013),('The Den',2013),('Unfriended',2014),('Unfriended: Dark Web',2018),('The Gallows',2015),('The Devil Inside',2012),('The Last Exorcism Part II',2013),('The Conspiracy',2012),('The Tunnel',2011),('The Pyramid',2014),('The Possession of Michael King',2014),('The Monster Project',2017),('The Dark Tapes',2016),('The Poughkeepsie Tapes',2007),('Incantation',2022),('Noroi: The Curse',2005),('Gonjiam: Haunted Asylum',2018),('The Medium',2021),('The Outwaters',2022),('The Blair Witch Project',1999),('Blair Witch',2016),('Paranormal Activity 2',2010),('Paranormal Activity 3',2011),('Paranormal Activity 4',2012),('Paranormal Activity: The Marked Ones',2014),('Paranormal Activity: The Ghost Dimension',2015),('Paranormal Activity: Next of Kin',2021),('The Last Exorcism',2010),('The Devil’s Doorway',2018),('Dashcam',2021),('Afflicted',2013),('The Cleansing Hour',2019),('Exists',2014),('Willow Creek',2013),('The Blackwell Ghost',2017)],
'Paranormal':[('The Conjuring',2013),('The Conjuring 2',2016),('The Conjuring: The Devil Made Me Do It',2021),('Insidious',2010),('Insidious: Chapter 2',2013),('Insidious: Chapter 3',2015),('Insidious: The Last Key',2018),('Insidious: The Red Door',2023),('Sinister',2012),('Sinister 2',2015),('The Nun',2018),('The Nun II',2023),('Oculus',2013),('The Autopsy of Jane Doe',2016),('Talk to Me',2022),('Smile',2022),('Smile 2',2024),('The Dark and the Wicked',2020),('The Night House',2020)],
'Slasher':[('Scream 4',2011),('Scream',2022),('Scream VI',2023),('Halloween',2018),('Halloween Kills',2021),('Halloween Ends',2022),('Terrifier',2016),('Terrifier 2',2022),('Terrifier 3',2024),('X',2022),('Pearl',2022),('MaXXXine',2024),('Happy Death Day',2017),('Freaky',2020),('Thanksgiving',2023),('In a Violent Nature',2024)],
'Psychological':[('Hereditary',2018),('The Babadook',2014),('The Witch',2015),('Midsommar',2019),('Saint Maud',2019),('The Lodge',2019),('The Invisible Man',2020),('The Blackcoat’s Daughter',2015),('It Comes at Night',2017),('The Invitation',2015),('The Killing of a Sacred Deer',2017)],
'Creature Feature':[('The Ritual',2017),('The Descent: Part 2',2009),('The Monster',2016),('Crawl',2019),('Underwater',2020),('The Shallows',2016),('No One Will Save You',2023),('A Quiet Place',2018),('A Quiet Place Part II',2020)],
'Folk Horror':[('The Witch',2015),('Midsommar',2019),('The Ritual',2017),('Apostle',2018),('The Wailing',2016),('The Medium',2021),('The Feast',2021)],
'Body Horror':[('The Substance',2024),('Raw',2016),('Titane',2021),('Possessor',2020),('The Fly',1986),('Contracted',2013),('The Human Centipede 2 (Full Sequence)',2011)],
'Zombie':[('Train to Busan',2016),('World War Z',2013),('The Girl with All the Gifts',2016),('The Crazies',2010),('Overlord',2018),('The Dead Don’t Die',2019),('Army of the Dead',2021),('28 Years Later',2025)],
'Sci-Fi Horror':[('Alien: Covenant',2017),('Prometheus',2012),('Life',2017),('The Invisible Man',2020),('The Substance',2024),('Nope',2022),('The Thing',2011),('Annihilation',2018)],
'Home Invasion':[('You’re Next',2011),('Hush',2016),('Don’t Breathe',2016),('The Strangers: Prey at Night',2018),('The Purge',2013),('The Collector',2009),('The Collection',2012),('The Guest',2014)]}

# These are search terms, not official TMDB genres. They are combined with verified curated titles.
KEYWORD_TERMS={
 'Found Footage':['found footage','mockumentary','screenlife'],
 'Paranormal':['paranormal','haunting','ghost','demonic possession'],
 'Slasher':['slasher','serial killer'],
 'Psychological':['psychological horror','psychological thriller'],
 'Creature Feature':['monster','creature feature'],
 'Folk Horror':['folk horror','witchcraft'],
 'Body Horror':['body horror'],
 'Zombie':['zombie'],
 'Sci-Fi Horror':['science fiction horror','alien'],
 'Home Invasion':['home invasion']
}

def get(path,params):
    q=urllib.parse.urlencode({**params,'api_key':KEY,'language':'en-US'})
    url='https://api.themoviedb.org/3/'+path+'?'+q
    for attempt in range(6):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'AfterDark/4.0'})
            with urllib.request.urlopen(req,timeout=35) as r:return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code==401:raise RuntimeError('TMDB API key rejected') from e
            if e.code not in (429,500,502,503,504):raise
            delay=int(e.headers.get('Retry-After','0') or 0) if e.code==429 else 0
            if attempt==5:raise
            time.sleep(max(delay,2**attempt)+random.random())
        except (TimeoutError, OSError):
            if attempt==5:raise
            time.sleep(2**attempt+random.random())

def convert(r):
    date=r.get('release_date') or ''
    return {'id':r['id'],'title':r.get('title') or '', 'year':int(date[:4]) if date[:4].isdigit() else 0,
            'genre':'Horror','subgenres':[], 'rating':round(float(r.get('vote_average') or 0),2),
            'votes':int(r.get('vote_count') or 0),'popularity':float(r.get('popularity') or 0),
            'desc':r.get('overview') or 'No synopsis available.', 'poster':r.get('poster_path'),
            'colors':['#403943','#111116']}

def eligible(m):
    return bool(m['title'] and m['poster'] and MIN_YEAR<=m['year']<=CURRENT_YEAR)

movies={}
def add(r,genre=None):
    m=convert(r)
    if not eligible(m):return
    existing=movies.get(m['id'])
    if existing:m=existing
    if genre and genre not in m['subgenres']:m['subgenres'].append(genre)
    movies[m['id']]=m

# Discover each release year separately, not just the top few pages of all-time popularity.
for year in range(MIN_YEAR,CURRENT_YEAR+1):
    params={'with_genres':'27','sort_by':'popularity.desc','primary_release_date.gte':f'{year}-01-01',
            'primary_release_date.lte':min(f'{year}-12-31',datetime.date.today().isoformat()),
            'vote_count.gte':MIN_VOTES,'include_adult':'false'}
    first=get('discover/movie',{**params,'page':1})
    for r in first.get('results',[]):add(r)
    pages=min(first.get('total_pages',1),PAGES_PER_YEAR,500)
    for page in range(2,pages+1):
        data=get('discover/movie',{**params,'page':page})
        for r in data.get('results',[]):add(r)
    print(f'{year}: {len(movies)} total unique titles',flush=True)

# Find keyword IDs dynamically: never assume a TMDB keyword ID is stable or correct.
for genre,terms in KEYWORD_TERMS.items():
    ids=set()
    for term in terms:
        try:
            results=get('search/keyword',{'query':term,'page':1}).get('results',[])
            for item in results:
                if item.get('name','').casefold()==term.casefold():ids.add(item['id'])
        except Exception as e:print('Keyword lookup skipped:',term,str(e),flush=True)
    for keyword_id in ids:
        try:
            params={'with_genres':'27','with_keywords':keyword_id,'sort_by':'popularity.desc',
                    'primary_release_date.gte':f'{MIN_YEAR}-01-01','primary_release_date.lte':datetime.date.today().isoformat(),
                    'include_adult':'false'}
            first=get('discover/movie',{**params,'page':1})
            for r in first.get('results',[]):add(r,genre)
            for page in range(2,min(8,first.get('total_pages',1))+1):
                for r in get('discover/movie',{**params,'page':page}).get('results',[]):add(r,genre)
        except Exception as e:print('Keyword discovery skipped:',genre,keyword_id,str(e),flush=True)

# Hand-verified niche titles supplement keyword results. Exact title/year match avoids false positives.
for genre,entries in CURATED.items():
    for title,year in entries:
        if year<MIN_YEAR:continue
        try:
            results=get('search/movie',{'query':title,'year':year,'include_adult':'false'}).get('results',[])
            norm=lambda s:s.casefold().replace('’',"'").strip()
            exact=[r for r in results if (r.get('release_date') or '').startswith(str(year)) and norm(r.get('title',''))==norm(title)]
            if exact:add(max(exact,key=lambda r:r.get('popularity',0)),genre)
            else:print('Curated title not matched:',title,year,flush=True)
        except Exception as e:print('Curated lookup skipped:',title,str(e),flush=True)

result=sorted(movies.values(),key=lambda m:m['popularity'],reverse=True)
if len(result)<500:raise RuntimeError(f'Only {len(result)} movies fetched; refusing to overwrite an existing catalogue with an incomplete result')
output={'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':'TMDB',
        'min_year':MIN_YEAR,'movie_count':len(result),'movies':result}
target=ROOT/'data'/'movies.json';temp=target.with_suffix('.tmp')
temp.write_text(json.dumps(output,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
temp.replace(target)
print('Generated',len(result),'films. Subgenres:',{k:sum(k in m['subgenres'] for m in result) for k in CURATED},flush=True)
