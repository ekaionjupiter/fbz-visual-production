# VIDEO 03: Claude + Higgsfield: How to Make Motion Graphics with AI (Full AI Workflow)
Source: https://youtu.be/FgTLSKXOCBE · Channel: AI Master · Length: 12:08

## Description (verbatim, with every link)

#sponsored Try Seedance 2.5 on Higgsfield https://higgsfield.ai/s/seedance-2-5-iamaimaster-DzjKTy

🎬 Learn more about AI video creation → https://aimaster.me/yt/motion_graphics
🤝 Exclusive brand partnership - https://aimaster.me/collab

I ran 6 AI motion graphics builds back to back inside Claude, connected straight to Higgsfield's Seedance 2.5 model through MCP — no After Effects, no keyframes, just prompts. Here's what actually held up: text stayed legible, objects stayed still when they were supposed to, and full 30-second explainers came out of a single chat.

What you'll see in this AI video generator workflow:
- How to connect Claude to Higgsfield in under 2 minutes (MCP setup)
- A self-folding paper title card, zero revisions needed
- Matching a reference image's exact visual style with one sentence
- A product light-sweep + logo reveal that held its shape for 6 seconds straight
- A surreal documentary title sequence built from a mood description, not a shot list
- A 3-burger animated menu in one continuous camera move
- A full 30-second megalodon explainer with scale bars, counters and captions that never drifted
- Turning one build into a vertical cut + a rebranded version with zero re-editing

🕔 TIMESTAMPS:
00:00 – Intro
00:14 – Connecting Claude to Higgsfield via MCP
01:54 – Build 1: Self-folding paper title card
03:27 – Build 2: Matching a reference image's style
04:31 – Build 3: Product light sweep + logo reveal
05:38 – Build 4: Surreal documentary title sequence
06:45 – Build 5: 3-burger animated menu
07:46 – Build 6: 30-second megalodon explainer
08:55 – One build, multiple deliverables (vertical + rebrand)
09:35 – 3 prompting habits that changed my results
10:57 – Final verdict

Try the exact workflow yourself — Higgsfield is linked in the description below. Start with something simple to see how it holds onto your brand, then push it toward longer builds.

#Higgsfield #ClaudeAI #AIVideoGenerator #MotionGraphics #Seedance

## Key takeaways

### Tools / models
- Claude (desktop/web app) + **Higgsfield MCP** connector; video model **Seedance 2.5** on Higgsfield. No After Effects, no keyframes, no Blender, no Premiere.
- Setup: Higgsfield > "MCP and CLI" section > copy connector URL > Claude > Settings > Connectors > Add > "Add custom connector" > paste. Claude then "treats Higgsfield as a tool it can call" — it writes the shot, sends it, Seedance renders, clip returns in-chat ~30 s later.

### Core principle: the conversation is the project file
- Claude retains brand colors, type weight, pacing across messages, so follow-ups are notes, not prompts: "Land the text half a second earlier. Warm up the key light." "Closer to talking to an editor than to typing into a generator."
- One build -> multiple deliverables with one-line notes: "reframe it for a vertical feed, keeping the same beats, but recomposing the shots for a 9:16 crop, instead of just cropping the sides"; "a second pass in a different color palette... with its own brand colors."

### The three failure modes of AI motion graphics (the bar)
1. Text "comes out melted or misspelled."
2. "Motion drifts halfway through the clip."
3. "The composition you liked in frame one is gone by frame 60."
- Baseline test: "If the model can't hold a word still on a flat sheet, it won't hold a lower third over moving footage."
- "Holding an object still is genuinely harder for these models than moving it around the frame."
- Generated video "loves to quietly cut and restart when you ask it to travel" — demand one unbroken camera move.
- Labels attached to moving shapes are what "generated graphics usually lose."

### Six builds (prompt patterns)
1. Self-folding paper title card ("Paper Trail"): "The folded sheet of paper is set alone on a plain surface. It opens itself corner by corner in slow, deliberate stages. On the last fold, the flat sheet reveals type printed straight onto the paper. The series title sits dead center." Did not describe crease physics or lighting.
2. Style match from a reference: dropped a wellness-app screenshot (terracotta, rounded type) with "no hex codes, no adjectives" and asked for "a 10-second product moment in that same visual language for a completely different app." Result: "One element moves and everything else agrees to shut up."
3. Product light sweep + logo: "matte black espresso machine on a raw concrete counter... one sweep of hard light and the brand mark fading in after. The machine cannot change shape or shift position while the light moved across it."
4. Surreal documentary titles (migratory birds): described "the way you describe a half-remembered dream": "Feathers dissolving into static, a horizon line that keeps rebuilding itself, type that arrives like it's being carried on wind instead of just typed onto the screen." Title "arrived drifting rather than getting pasted on top" — the difference between a title sequence and a text overlay.
5. 3-burger menu, 15 s, "one continuous camera move to the right. Each burger assembles itself from falling ingredients, and its name types in underneath once the stack is finished." Specified ingredient order.
6. 30-s megalodon explainer: "One prompt described in four beats in the order they land in" — type question on deep blue field; silhouette draws tail-first, diver fades in at scale; scale bar + counter locks at 50 ft; push-in on rotating tooth with "7 in" caption; timeline slides, closing date card.

### Prompting habits (explicit rules)
1. "Describe the outcome, not the technique." Writing with easing curves and layer counts gave "a stiffer clip"; write "like a director describing a scene to crew."
2. "Name the one thing that must not move every single time" — e.g. "the product keeps its exact shape."
3. "Hand it a reference instead of a pile of adjectives." "One image carries a palette better than a paragraph full of words like premium and clean."
4. "Stop treating every prompt as a fresh start from zero."
- Caveat: longer sequences "still want a person checking the seams between beats."

## Cleaned transcript

Every clip moving on screen right now came out of a chat window. I never opened After Effects and I never touched a keyframe. I typed a sentence and Seedance rendered it. Six builds today. The last one is a full 30-second explainer in a single pass. Set up first, because it barely counts as setup. Inside Higgsfield, open the MCP and CLI section and copy the connector URL sitting right there. Then open Claude, go to settings, then connectors. Hit add. Choose add custom connector and paste that link in. That's the whole ritual. From that point, Claude treats Higgsfield as a tool it can call, the same way it treats a file on your machine. So, when I ask for a motion graphic, it does not hand me a description of one. It writes the shot, sends it over, and Seedance 2.5 renders it. 30 seconds later, the clip is sitting in the same chat where I asked for it. The part that actually matters is what Claude holds onto. It remembers the brand colors I gave it four messages back, the type weight I like, the pacing I asked for. So, my second prompt is never a full prompt again. It is a note. "Land the text half a second earlier. Warm up the key light." That is a lot closer to talking to an editor than to typing into a generator, and it is the only reason this thing holds together past the first clip.

A 30-second explainer in After Effects is a full day of work for most people I know. You build the comp, animate the type, chase the easing until it finally feels right, mask the layers, render, and then someone asks you to move the logo three frames to the left. Meanwhile, every AI video tool I've tested has been weakest at exactly the three things motion graphics are built from. Text comes out melted or misspelled, motion drifts halfway through the clip until the shot stops making sense. The composition you liked in frame one is gone by frame 60. That's the bar for today, and I'm not grading on a curve for any of it.

Build one is a single prompt, no reference image, no second pass, nothing loaded in beside the text. I asked for a folded sheet of paper lying on a desk. It opens itself crease by crease. The last fold reveals the printed name of the brand. One object, one transformation and type that has to stay readable the whole way through. So, I asked for an opening card for a fictional documentary series called Paper Trail. The folded sheet of paper is set alone on a plain surface. It opens itself corner by corner in slow, deliberate stages. On the last fold, the flat sheet reveals type printed straight onto the paper. The series title sits dead center. I didn't describe crease physics or lighting angles. I just described how paper actually opens and let Claude handle the mechanics. What came back was close to the version I would have built by hand on a good day. Each fold peeled back cleanly and the paper held its shape and its shadow through every crease. The title set flat and legible the moment the last corner settled. The text was spelled correctly, too. It rendered in under a minute and it needed no revisions at all. The creases moved the way paper actually moves with the weight of the sheet fighting each fold. The type underneath stayed sharp, edges clean, no melting on the letters. That's the baseline I need before anything more complicated is worth trying. If the model can't hold a word still on a flat sheet, it won't hold a lower third over moving footage.

Next test is the one I actually wanted to run. I pulled a still frame off a design account, a wellness app screen with muted terracotta tones and soft rounded type, and dropped it straight into the chat with no other context. No description of the palette, no hex codes, no adjectives about mood or vibe. I just told Claude to read the image and build me a 10-second product moment in that same visual language for a completely different app than the one sitting in the picture. The clip came back reading like the reference without ever copying it outright. Same warm terracotta, same restrained, same rounded type, but a different layout doing a different job entirely. A small icon slid into frame and settled while a progress ring filled in behind it, and everything else in the shot held still while that happened. One element moves and everything else agrees to shut up. That's the whole trick with this kind of shot. That's the piece I'd normally spend an hour matching by eye on a real client project, and here it took one reference image and a sentence.

Third build is the one clients ask for constantly in every category I've ever worked in. A physical product, a light move across it, a logo landing at the end. Normally that's a studio day or a genuinely patient afternoon inside Blender fighting with reflections. I gave it a matte black espresso machine on a raw concrete counter and asked for one sweep of hard light and the brand mark fading in after. I was specific about the single thing that usually breaks these shots. The machine cannot change shape or shift position while the light moved across it. This is where I expected the wheels to come off and they didn't. The machine stayed exactly the machine for all six seconds. Same silhouette, same dials, same proportions while the highlight rolled across the metal and pulled real texture out of the concrete underneath it. Then the mark, sharp and easy to read. If you've ever watched a generated product melt gently into a slightly different product halfway through a clip, you already understand why I keep pointing at this one build. Holding an object still is genuinely harder for these models than moving it around the frame.

Now the fun one. Every tool test eventually needs a prompt with no correct answer because that's where you find out whether the thing has any actual range or just one house style it defaults to under pressure. So, I asked for a title sequence for a documentary about migratory birds, and I described it the way you describe a half-remembered dream instead of writing a shot list. Feathers dissolving into static, a horizon line that keeps rebuilding itself, type that arrives like it's being carried on wind instead of just typed onto the screen. It understood the assignment better than I expected it to. The static resolved into feathers at exactly the right pace. The horizon kept reforming instead of just sitting there flat, and the title arrived drifting rather than getting pasted on top of the frame. That last distinction is the difference between a real title sequence and a text overlay, and I never had to spell it out in the prompt. This is the build that convinced me the model is reading intent, not just matching keywords off a list. It got the mood right, and mood is a far weirder thing to nail than a logo animation.

For build five, I asked for a 15-second animated menu with three burgers built as one continuous camera move to the right. Each burger assembles itself from falling ingredients, and its name types in underneath once the stack is finished. One prompt, one pass, no reference images. It opens tight on an empty wooden board. The bottom bun drops in and settles with real weight. Then lettuce, sauce, cheese, bacon, and the patty land on top of it in that exact order. Each one compressing the layer below it for a fraction of a second. The top bun lands last, and the whole stack settles. The name types in below it. The ingredient order matched the prompt exactly on every stack. Nothing morphed halfway down. Nothing landed inside the layer beneath it, and the sauce actually behaved like sauce instead of a solid disk. The camera move stayed one unbroken shot the whole way across, which is what I care about most here because generated video loves to quietly cut and restart when you ask it to travel.

For the last build, I asked for a 30-second educational piece about the megalodon, built entirely out of motion graphics, type, silhouettes, scale bars, numbers. One prompt described in four beats in the order they land in. It opens on a deep blue field with a single line of type asking how big the thing actually was. A shark silhouette draws itself in from the tail forward, and a human diver fades in beside it at the correct relative scale. A measuring bar stretches across the body, while a counter runs up and locks at 50 ft. The frame then pushes in on one tooth, rotating slowly with a caption calling out 7 in. The last beat is a timeline sliding right until the silhouette drops off the end, and the closing card holds on the date it vanished from the ocean. Everything landed where it was supposed to. The counter finished on the number the prompt asked for. The scale bar stayed pinned to the silhouette the whole time it was running, and no label drifted off the object it belonged to. That last part is the thing I expected to break first, because labels attached to moving shape are exactly what generated graphics usually lose.

Once a build lands, the same thread can turn it into three or four deliverables instead of one. I took the megalodon explainer and asked Claude to reframe it for a vertical feed, keeping the same beats, but recomposing the shots for a 9:16 crop, instead of just cropping the sides off the original. Then I asked for a second pass in a different color palette for a channel that wanted the same script with its own brand colors instead of the ocean blue. Neither request touched the original prompt. They were both one-line notes on top of a build that already existed. What used to mean recutting a finished video in Premiere for every platform turned into two follow-up messages in the same conversation.

Six builds in, three habits did most of the heavy lifting, and they're the ones I'd hand to anyone starting this today. First, describe the outcome, not the technique behind it. Every time I wrote like a motion designer, with easing curves and layer counts stacked into the prompt, I got a stiffer clip back than when I wrote like a director describing a scene to crew. Say what the viewer should see and feel in that moment, and let the model handle the mechanics it already knows how to do. Second, name the one thing that must not move every single time. Most failures in generated motion are something drifting when it should be holding still. So, a line like "the product keeps its exact shape" kills off a whole category of problems before they even start. Third, hand it a reference instead of a pile of adjectives you'd have to explain anyway. One image carries a palette better than a paragraph full of words like premium and clean, because premium means something slightly different to every person who types it into a prompt box. There's a fourth habit, too, less of a rule and more of a mindset shift. Stop treating every prompt as a fresh start from zero. The whole advantage of running this inside Claude is that the conversation itself becomes the project file. So, your palette and your pacing are already sitting in the thread waiting for you to just point at them again.

So, here's where I land after six builds in one sitting, back-to-back, with no cherry-picking between takes. The text and the stillness, the two things that used to break every AI motion tool I've tested, held up across every single one of these, and that's genuinely the part that surprises me. What I'm less sold on is how far you can push a single shot before you need to jump back in and steer it by hand. Longer sequences still want a person checking the seams between beats. But, for the kind of motion graphics most channels and small brands actually need day-to-day, this closed a real gap between having an idea and having a finished clip. If you make videos for a living or you're the one person on your team who ends up doing the motion graphics anyway, go try this workflow yourself before you assume it's another overhyped demo reel. Higgsfield is linked right in the description. Head over there, run the 2-minute setup I showed, and start with something simple like that folded paper card just to get a feel for how it holds onto your brand. Once you trust it with the easy stuff, push it toward the 30-second builds. That's the whole workflow. Now go put it to work.
