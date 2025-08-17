PROMPT_GENERATOR_PROMPT = """
Reformat the following user-provided music description into a simple comma-separated list of audio tags.

User Description: "{user_prompt}"

Follow these guidelines strictly when reformatting. Include a tag from each category below in you final list:
- Include genre (e.g., "rap", "pop", "rock", "electronic")
- Include vocal type (e.g., "male vocal", "female vocal", "spoken word")
- Include instruments actually heard (e.g., "guitar", "piano", "synthesizer", "drums")
- Include mood/energy (e.g., "energetic", "calm", "aggressive", "melancholic")
- Include tempo if known (e.g., "120 bpm", "fast tempo", "slow tempo")
- Include key if known (e.g., "major key", "minor key", "C major")
- The output must be a single line of comma-separated tags. Do not add any other text or explanation. For example: melodic techno, male vocal, electronic, emotional, minor key, 124 bpm, synthesizer, driving, atmospheric

If already a few tags, infer what the user wants and add 2-3 more tags that are synonyms to the users tags with no new categories.

Formatted Tags:
"""

LYRICS_GENERATOR_PROMPT = """
Generate song lyrics based on the following description.
The lyrics should be suitable for a song and structured clearly.
Use tags like [verse], [chorus], [bridge], [intro], and [outro] to structure the song.

Here is an example:
"[verse]\nWoke up in a city that's always alive\nNeon lights they shimmer they thrive\nElectric pulses beat they drive\nMy heart races just to survive\n\n[chorus]\nOh electric dreams they keep me high\nThrough the wires I soar and fly\nMidnight rhythms in the sky\nElectric dreams together we’ll defy\n\n[verse]\nLost in the labyrinth of screens\nVirtual love or so it seems\nIn the night the city gleams\nDigital faces haunted by memes\n\n[chorus]\nOh electric dreams they keep me high\nThrough the wires I soar and fly\nMidnight rhythms in the sky\nElectric dreams together we’ll defy\n\n[bridge]\nSilent whispers in my ear\nPixelated love serene and clear\nThrough the chaos find you near\nIn electric dreams no fear\n\n[verse]\nBound by circuits intertwined\nLove like ours is hard to find\nIn this world we’re truly blind\nBut electric dreams free the mind"

Description: "{description}"

Lyrics:
"""


LUDA_LYRICS = """"
[Intro]
Rollout, rollout
Rollout, rollout
Rollout, rollout
Rollout, rollout

[Chorus]
(Rollout) I got my twin Glock .40's (Rollout) cocked back
(Rollout) Me and my homies (Rollout), so drop that
(Rollout) We rollin' on twenties, (Rollout) with the top back
(Rollout) So much money (Rollout) you can't stop that
(Rollout) Twin Glock .40's (Rollout) cocked back
(Rollout) Me and my homies (Rollout), so drop that
(Rollout) We rollin' on twenties, (Rollout) with the top back
(Rollout) So much money (Rollout) you can't stop that

[Verse 1]
Now, where'd you get that platinum chain with them diamonds in it?
Where'd you get that matchin' Benz with them windows tinted?
Who them girls you be with when you be ridin' through?
Man, I ain't got nothin' to prove, I paid my dues, breakin' the rules, I shake fools while I'm takin' a cruise
Tell me who's your weed man, and how do you smoke so good?
You's a superstar, boy, why you still up in the hood?
What in the world is in that bag? What you got in that bag?
A couple of cans of whoop ass, you did a good-ass job of just eyein' me, spyin' me

[Chorus]
(Rollout) I got my twin Glock .40's (Rollout) cocked back
(Rollout) Me and my homies (Rollout), so drop that
(Rollout) We rollin' on twenties, (Rollout) with the top back
(Rollout) So much money (Rollout) you can't stop that
(Rollout) Twin Glock .40's (Rollout) cocked back
(Rollout) Me and my homies (Rollout), so drop that
(Rollout) We rollin' on twenties, (Rollout) with the top back
(Rollout) So much money (Rollout) you can't stop that

[Verse 2]
Man, that car don't come out until next year, where in the fuck did you get it?
That's eighty thousand bucks gone, where in the fuck did you spend it?
You must have eyes on your back 'cause you got money to the ceilin'
And the bigger the cap, the bigger the peelin', the better I'm feelin', the more that I'm chillin', winnin', drillin' and killin' the feelin'
Now, who's that bucked naked cook fixin' three course meals?
Gettin' goosebumps when her body taps the six inch heels
What in the world is in that room, what you got in that room?
A couple of gats, a couple of knives, a couple of rats, a couple of wives, now it's time to choose

[Chorus]
(Rollout) I got my twin Glock .40's (Rollout) cocked back
(Rollout) Me and my homies (Rollout), so drop that
(Rollout) We rollin' on twenties, (Rollout) with the top back
(Rollout) So much money (Rollout) you can't stop that
(Rollout) Twin Glock .40's (Rollout) cocked back
(Rollout) Me and my homies (Rollout), so drop that
(Rollout) We rollin' on twenties, (Rollout) with the top back
(Rollout) So much money (Rollout) you can't stop that
[Verse 3]
Are you custom made, custom paid, or you just custom fitted?
PlayStation 2 up in the ride, is that Lorenzo-kitted?
Is that your wife, your girlfriend or just your main bitch?
You take a pick, while I'm rubbin' the hips, touchin' lips to the top of the dick and then, "Whew"
Now, tell me who's your housekeeper, and what you keep in your house?
What about diamonds and gold, is that what you keep in your mouth?
What in the world is in that case, what you got in that case?
Get up out my face, you couldn't relate, wait to take place at a similar pace, so shake, shake it

[Chorus]
(Rollout) I got my twin Glock .40's (Rollout) cocked back
(Rollout) Me and my homies (Rollout), so drop that
(Rollout) We rollin' on twenties, (Rollout) with the top back
(Rollout) So much money (Rollout) you can't stop that
(Rollout) Twin Glock .40's (Rollout) cocked back
(Rollout) Me and my homies (Rollout), so drop that
(Rollout) We rollin' on twenties, (Rollout) with the top back
(Rollout) So much money (Rollout) you can't stop that

[Outro]
Get out my business, my business
Stay the fuck up out my business, ah
'Cause these niggas all up in my shit
And it's my business, my business
Stay the fuck up out my business
'Cause it's mine, oh, mine
My business, my business
Stay the fuck up out my business
'Cause these niggas all up in my shit
And it's my business, my business
Stay the fuck up out my business
'Cause it's mine, oh, mine
Ah, ah, Timbaland, Ludacris
Disturbing Tha Peace (Woo)
[Skit]
Yeah, uh, c'mon, what's up? What's up? Come here (Ugh)
Come here, go to sleep (Uh)
Go to sleep right now (Ahh), right now (Ugh)
Go to sleep, go to sleep
Go to sleep (Ah-uhh)
Go to sleep (Ahh)

"""