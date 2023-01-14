import re
antiHeroRegex = re.compile(r'(anti)-(hero)')
song = '''
[Verse 1]
I have this thing where I get older, but just never wiser
Midnights become my afternoons
When my depression works the graveyard shift, all of the people
I've ghosted stand there in the room

[Pre-Chorus]
I should not be left to my own devices
They come with prices and vices
I end up in crisis
(Tale as old as time)
I wake up screaming from dreaming
One day, I'll watch as you're leaving
'Cause you got tired of my scheming
(For the last time)
[Chorus]
It's me, hi
I'm the problem, it's me
At teatime, everybody agrees
I'll stare directly at the sun, but never in the mirror
It must be exhausting always rooting for the anti-hero

[Verse 2]
Sometimes, I feel like everybody is a sexy baby
And I'm a monster on the hill
Too big to hang out, slowly lurching toward your favorite city
Pierced through the heart, but never killed

[Pre-Chorus]
Did you hear my covert narcissism I disguise as altruism
Like some kind of congressman?
(A tale as old as time)
I wake up screaming from dreaming
One day, I'll watch as you're leaving
And life will lose all its meaning
(For the last time)

[Chorus]
It's me, hi
I'm the problem, it's me (I'm the problem, it's me)
At teatime, everybody agrees
I'll stare directly at the sun, but never in the mirror
It must be exhausting always rooting for the anti-hero
See Taylor Swift Live
Get tickets as low as $290
You might also like
Did you know that there’s a tunnel under Ocean Blvd
Lana Del Rey
Nobody Gets Me
SZA
Kill Bill
SZA
[Bridge]
I have this dream my daughter-in-law kills me for the money
She thinks I left them in the will
The family gathers 'round and reads it and then someone screams out
"She's laughing up at us from Hell"

[Breakdown]
It's me, hi
I'm the problem, it's me
It's me, hi
I'm the problem, it's me
It's me, hi
Everybody agrees, everybody agrees

[Chorus]
It's me, hi (Hi)
I'm the problem, it's me (I'm the problem, it's me)
At teatime (Teatime), everybody agrees (Everybody agrees)
I'll stare directly at the sun, but never in the mirror
It must be exhausting always rooting for the anti-hero
'''
search = antiHeroRegex.search(song)
print(search.group())

findAll = antiHeroRegex.findall(song)
print(findAll)

digitRegex = re.compile(r'\d')
digitFindAll = digitRegex.findall(song)
print(digitFindAll)

doubleVowelsRegex = re.compile(r'[aeiouAEIOU]{2}')
print(len(doubleVowelsRegex.findall(song)))

newLineRegex = re.compile(r'\n')
print(len(newLineRegex.findall(song)))

meRegex = re.compile(r'me')
# print(meRegex.sub('not me', song))

theProblemRegex = re.compile(r'the (\w)\w*')
print(theProblemRegex.findall(song))
print(theProblemRegex.sub(r'the \1****', song))
