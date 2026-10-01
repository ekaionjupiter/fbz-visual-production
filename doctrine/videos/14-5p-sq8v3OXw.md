# VIDEO 14: AI Agents: The Most Valuable Skill You Can Learn in 2026 (Full Course)
Source: https://youtu.be/5p-sq8v3OXw · Channel: Open Residency · Length: 2:24:11 (8651 s) · Guest: Remy Gaskell (AI with Remy), host Mark

## Description (verbatim, with every link)

Remy is giving you The AI Agent OS Playbook, everything from this episode in one free PDF → https://openresidency.com/remy-gaskell-playbook?utm_source=youtube&utm_medium=description&utm_campaign=remy_gaskell_playbook

Remy Gaskell is a self-taught AI operator who teaches founders to run their businesses on AI agents.

Most founders type prompts into a chat box one at a time and start from zero every session. Remy runs at 5-10x the output because he stopped chatting and built an operating system his AI already understands. In this episode he takes the whole thing apart: the shift to agents, the exact files on his own machine, and how to build one yourself.

🧠 AI ONBOARD
You re-explain your business in every new chat because your AI forgets the second you close the window. AI Onboard is Remy's Claude Code plugin that builds your whole AI operating system in one guided session, so it never forgets again. Half off for our audience → https://openresidency.com/onboard?utm_source=youtube&utm_medium=description&utm_campaign=ai-onboard

⏱️ CHAPTERS
00:00:00 Trailer
00:01:21 The shift from chat to agents
00:04:04 What "agent" actually means
00:11:08 The observe-think-act loop
00:18:01 Live demo: analyzing an Instagram Reel
00:20:24 Tuning an agent vs building one
00:22:45 Context files and the CLAUDE.md
00:44:03 A memory system that improves itself
00:52:06 MCP connectors, the universal translator
00:59:21 Security and permissions
01:02:19 Starter tool stack, Apify to Composio
01:18:21 Skills as SOPs for your AI
01:47:34 The Agent OS folder structure
02:06:46 The future of teams and intrapreneurship
02:16:20 Quickfire questions

🔗 AI WITH REMY
Course: https://go.theaicourse.ai/open-residency
Newsletter: https://go.aiwithremy.com/open-residency
Instagram: https://www.instagram.com/aiwithremy/
LinkedIn: https://www.linkedin.com/in/remygaskell/
Apify: 25% OFF all Apify plans for your first 3 months with code 25REMY → https://www.apify.com?fpr=remy

🎙️ OPEN RESIDENCY
Instagram: https://www.instagram.com/openresidency/
Instagram: https://www.instagram.com/markbrazil/
LinkedIn: https://www.linkedin.com/in/markmastrandrea/
Website: https://openresidency.com/
Email: info@openresidency.com

⚡ POWERED BY
beehiiv: the best platform to run a newsletter on → https://beehiiv.link/6wyzzm
Wispr Flow: 1 month FREE of Wispr Flow Pro with code OPENRESIDENCY → https://wisprflow.ai/?promo_code=OPENRESIDENCY&creator_name=Open+Residency&dub_id=5XTlXALwJFqVa2J1
Momentous: up to 35% OFF your first order with code OPENRESIDENCY → https://livemomentous.com
Ketone-IQ: 30% OFF your subscription plus a free gift with your second shipment → https://ketone.com/openresidency

## Key takeaways

### Core model: chat vs agents, the loop, the four levers
- "chat is just question to answer and an agent is just goal to result."
- The agent loop: **observe -> think -> act**, repeated until the goal's definition of done is met. "Look at the situation, decide the next step, do it." Define what "done" looks like explicitly (e.g. "10 business podcasts in a PowerPoint") or the stop condition is subjective.
- An app that runs the loop is an **agent harness** (Claude Code, Claude Co-work, Codex, Manus, Perplexity Computer). Nobody "builds" an agent; you **tune** one via four levers: observe step = **context** + **skills**; think step = **LLM model**; act step = **tools** (MCP).
- "The Volvo could beat the Lamborghini if the context, the skills, and the tools are really tuned." Principles are meant to be model-agnostic and timeless.
- Onboard an agent like a real employee: **context, tools, skills** ("a really really capable stranger" with infinite bandwidth for ~$100/mo).

### Context (markdown files)
- Context = everything the agent should know before a task: about-me, business info, offer catalog (upsells/downsells, prices), ideal customer profile, brand voice, values, how-I-like-to-work.
- Markdown is "the love language of AI": one step above .txt; far easier/cheaper to ingest than PDF/Docx. Notion and ClickUp docs are already markdown.
- Build these files by having Claude **interview you** ("interview me, like to extract the information from my brain to build these files") - he dictated via Wispr Flow for ~3 hours. Then "read over every line before you give it the okay." Anti-slop rule: a rushed ICP full of "AI slop" (e.g. an invented pain point like "red skin") poisons all downstream marketing copy. Keep context files objective, lean, high-density; bloated files eat the context window before any task starts (he showed /context at 6% after one tiny message).
- Context files are **assets you own**, portable across harnesses (open the same folder in Claude Code, Codex or Manus), unlike ChatGPT's hidden memory file you cannot control.
- **CLAUDE.md / AGENTS.md** = the north-star file auto-loaded every session. V1: just a CLAUDE.md with an overview of who you are. V2: CLAUDE.md points to a `context/` folder. Verbatim pattern from his demo file: "My context read before any task. Everything you should know about me and the business lives in the context folder ... Load the relevant files in before starting any tasks. Assumptions are the enemy. If the answer isn't there, ask me."
- Use `@file` tagging in CLAUDE.md "like a sym link" so files load without an extra loop.
- **memory.md** self-improvement loop: "memory learned rules, lessons Remy has taught me. I check these before every task." Rules such as "never write formally", "always use real examples, never generic placeholder ones", "When building any websites, always use dark mode. Never use light mode." CLAUDE.md instruction: "your memory lives in this file. When I correct you, write lessons into this memory file as a new rule and then check it before every task." Spring-clean it every ~6 months ("audit my memories and take out anything contradictory").
- Global CLAUDE.md principle he keeps: "Boil the ocean. The marginal cost of completeness is near zero" - the standard isn't good enough, it's "holy ... that's done."

### Tools (MCP)
- MCP = "a translator that sits in the middle between Claude and your tools" (credit Ross Mike). In Claude desktop: Customize -> Connectors -> browse/+ or "add custom connector" with the vendor's MCP server URL (demoed with beehiiv's MCP URL from its settings page).
- He picks vendors by whether they ship an MCP; he no longer uses app front-ends (Gmail, Calendar, Slack, Stripe, cal.com all driven from Claude Code).
- Permissions: start **read-only**, escalate as trust grows; default "needs approval" per tool, later "always allow". Last line of defense = anything that can spend money. Second security concern = sensitive data/IP passing through the model.
- **Starter stack (six):** 1) **Apify** - marketplace of scrapers (Instagram profile, YouTube transcript, Reddit, LinkedIn, Google Maps, lead/email scrapers); generous free tier (~$5/mo usage). 2) **Firecrawl** - lets the agent actually read/scrape a page (brand colors, buttons, CRO audit) vs plain web search which only finds facts. 3) **Composio** - "MCP for MCPs": connect thousands of apps once, including multiple Gmail accounts; add to Claude as a custom connector URL; makes your tool layer portable to Codex/other harnesses. 4) **Chrome DevTools MCP** (Google) - agent spins up its own fresh browser to check its own work (websites, forms). 5) **Playwright** - controls your current logged-in browser. 6) **Higgsfield MCP** - "the composio but for image models": aggregates Google, OpenAI and Chinese image/video models behind one MCP; Claude has no native image gen, so this is the creative tool. Also mentioned: 1Password MCP (Touch ID approval), Meta official ads connector, beehiiv MCP, ClickUp connector.

### Higgsfield / image-generation examples (design-pipeline relevant)
- Demo prompt (paraphrased by Remy): gave a Bloom creatine gummies product image and said "scrape competitors ads running in the meta ads library and generate 20 static image ads using the Higgsfield MCP". Firecrawl scraped the Meta Ads Library; Higgsfield generated static ads. Verdict: "you have to generate like a hundred and there'll be like maybe five to 10 really good ones"; flaws noted - gummies didn't look right ("we could just have added an image of the actual gummies and then it would have nailed it"), "the product's a little squished". To automate ads properly "I'd build a bunch of skills around like static ads and like headline writing and copywriting".
- **Product shoot skill** (built for a furniture brand, "T product shoot"): input = iPhone reference image of the product (a cabinet); skill generates production-ready editorial images - same office setting, different angles, a person touching it, close-up of marble veining - via Higgsfield MCP using **Nano Banana Pro** (Google) as the image model. Skill is scoped to that client's project folder only.
- Chrome DevTools used as a visual QA loop: build site with brand colors -> agent opens browser -> "that's not good, I'll keep working on that."

### Skills (SOPs for AI)
- A skill = folder containing `skill.md` with **name, description, contents** (front matter above two `---` lines). Only name+description are loaded each session ("the spine of the book"); full contents load when triggered (**progressive disclosure**). Invoke via `/skill-name` or let the agent pick it from the description ("Use when the user says generate titles, YouTube titles or title options").
- Example skill contents (YouTube titles): Step 1 get the topic (from user or file name); Step 2 competitor research - use Apify to scrape top-performing videos on the topic from target channels, extract title length, structure, numbers, capitalization; Step 4 generate options by category: curiosity gap, benefit-first, contrarian, number.
- Subject-lines skill generated live: "step one, load the tools. step two, pull beehiiv performance data. step three, find the draft and the hero story in notion. Then write 10 ranked options. output structure: use this shape when giving them to the reader." Patterns the data surfaced: "don't stack tool names", "I + bold stance wins. I + boring task doesn't."
- Two ways to build: **goal-first** ("build me a brand guidelines skill, here's the PDF") or **process-first** (90% of his skills): walk Claude through the task step by step in one session (e.g. ads library link -> Firecrawl scrape -> analyze every ad -> find landing pages -> screenshot each -> master doc), then "create a skill for this process that we've just done and call it ad scraper". The built-in **skill-creator** skill packages it, saving corrections and the final output as a reference.
- Skills are never right on V1; most of his are V5-V10. Correct in chat ("I hate how you've made the landing pages so big... update the skill") and the skill is "sanded down".
- **Orchestrator skills** call other skills in sequence (YouTube publish workflow -> title skill -> thumbnail skill ...; ads analyst -> ad creative analysis -> creative strategy). The sub-skills are standalone.
- Ads analyst output: markdown master report + HTML report (54 active ads, 37 video / 14 image, longest running, newest funnel), downloads every ad asset, screenshots landing pages, "things to steal or beat" (e.g. "reframe the category to justify the price", "name your mechanism").
- Brand-guidelines skill recommended as a repeatable playbook for lead magnets, PDFs, websites. Caption skill example: hook / body / CTA / tone of voice / no hashtags / 10 example outputs.
- First skill everyone should build: email inbox triage, scheduled 3x/day.

### Folder structure (Agent OS)
- One `OS/` ("operating system") folder as the holding company; subfolders per business pillar (e.g. `AI with Remy/` with `content`, `finance`, `legal`, `newsletter`, `website`, `marketing`), `personal/` (e.g. `health/`), and `active/` for one-off experiments. Hidden `.claude/` holds `skills/` and settings; he also stores context there.
- Work from the OS root and `@`-tag subfolders (`@marketing`) rather than opening narrow folders; the models are smart enough and context windows big enough.
- **Global vs project**: global CLAUDE.md/skills/tools apply everywhere; per-project CLAUDE.md (e.g. podcasts folder: "This workspace is Remy's base for podcast appearances... prep, demos, diagrams, post episode analysis") stacks on top. Project-only skills (product shoot) live in that folder.
- "I've got 50 agents working overnight" = a folder + a skill + a scheduled task.
- Layer 2 (business infrastructure, not the founder's laptop): Hermes / OpenClaw agents on a Mac mini - still just folders + markdown (e.g. `soul.md`); same context/tools/skills principles.
- Claude Council skill (via Ollie Leman): five persona sessions -> anonymised peer review by five fresh sessions -> chairman session gives verdict; used for decisions.

### Misc facts
- Costs: ~$1,000/mo across all AI tools for him; $300/mo Claude plan ≈ $6,000 of raw token usage (subsidised). Newest flagship model ("Fable 5") not included in plans.
- Overrated: AI app builders (Lovable etc.) - just build in a Claude project folder. Underrated: Composio. Beginner mistake: perfectionism / fear of starting. Biggest MCP unlock: Apify.
- Where to start: create `OS/` folder, have Claude interview you to build context markdown files, connect tools, then complete a full workday inside the harness; whenever you repeat a task, turn it into a skill.

## Cleaned transcript

Every company needs to put AI at the forefront of all their operations [music] or they're going to lose to a company that does.

>> That's Remy. He's a young non-technical [music] founder who's a master at explaining AI in a way you can actually understand [music] and implement.

>> In order to make the most out of these agents and make them actually useful, you need to treat setting [music] them up like onboarding a real employee. And you do this through context, tools, and skills. He shares his screen and shows us exactly how [music] he builds AI systems, timeless principles you can steal, and the easiest way to get started today.

>> If you're starting from zero, this is all you need. Just this episode, [music] and I think you're set. Guys, in this episode, Remy is going to demystify everything that's going on with AI, the terms, the tools, the models, everything. an a toz guide to know what's going on today in AI. He has spent the last two years living in this stuff and he is about to embed in your brain all things AI that he has learned in the next couple hours. He's not some technical engineer either. For the last couple years, he's been running an ad agency.

This is all self-taught. And now he's running the AI agent team for one of the fastest growing ecom brands in the world today. And I know this AI stuff is very overwhelming. So, I want you all to take a deep breath and by the end of this episode, you're going to know exactly what the next steps are. Let's get into it. So,

>> I guess let's just start with, you know, what are the kind of the two stages of using AI.

>> So, stage one was chat, right? You'd be pretty hardressed to find anyone, especially founders and business owners that aren't using chat models. So, think like chat GBT or Claude Chat or Gemini. But stage two is now agents. So we've moved from chat to agents and the founders and employees that are now using agents are like no word of a lie like five to 10 times more productive in their day.

>> Probably more probably more than 5 to 10 to be honest with you.

>> Probably. I mean even if you take like the the middle mark which is like seven times more productive. Think about that. That's a week in a working day and like 5 to seven weeks in a week. And then if you stack that up over like a month a year like it's toast. So, you're starting to just get this massive divide opening at the moment with the people who are using agents and the people who are stuck using chat and you want to be on the agent side.

>> Yeah. I mean, it's unfortunate for some of the people listening out here that may or may not be employees, but like a big thing we talk about is just opex, your actual labor as a percentage of revenue. I think everybody is racing to just get this down the percentage of revenue. And I feel like people are doing it with just chat and they don't understand the true multiplier is actually with the agents and

>> even like you're saying about it's tough for employees. I actually think that there's a great opportunity for employees right now which we'll touch on later. But I think there's a there's an amazing opportunity for employees that take the initiative to learn this stuff. You end up becoming like a 100x employee. And it's like you can now like one like go to market strategist can now take on like the work of a 10 person team and get paid for probably about five five person team now.

>> Yeah. We're gonna dive deep into what I think and what you think the future of a team looks like. What are the necessary skills? What does that brain need to look like? And like I mean dude, we're seeing like I think there there was a company that was a billion dollars that was one person. Like I truly believe there's going to be one to three person teams doing billions and billions.

>> Agreed. because there's so much of your time and day that's like taken up with just like stupid manual tasks. Like I give you an example yesterday someone from my team was asking for like some passwords and API keys and it's like before I would have had to go into one password like find them create a share link share it securely and like send the Slack message. So instead I just got my agent to just like go into one password like create the share links send them on Slack and it's like that would have been maybe like a 10 minute task realistically but it's like just 30 seconds and it's like it just allows you as a founder to spend your time on the work that's fulfilling for you and creative and strategic the work that AI like can't do like the visionary stuff.

>> Yeah, for sure. Let's dive into, you know, what does that agent look like? Let's really really deep dive into it. For anybody out here that's listening, I highly recommend that you either watch this on YouTube or Spotify so you actually can see the visuals, but let's break down, you know, agent a bit more and like what that kind of loop looks like.

>> 100%. So the word agent gets thrown around so much. It's kind of like lost a lot of meaning now. You you see like if you open Instagram or X, it's just I build an agent that does this, agents this, agents that. But the easiest way to like actually think about like what an agent is is I like to think chat is just question to answer and an agent is just goal to result. So question to answer goal to result is just the simple way to think about it in your head. So for example with a chat you might ask it a question it'll reply and then you have to go and do the work.

Whereas agents you're giving it a goal it's breaking that down to a plan and executing and then handing you like a finished product. And the word agent actually just comes from the word agency which means like ability to act and do things. And people think like agent as in like real estate agent or like travel agent as like a person like a guy that's like a sci-fi type guy that's like living his own life and then doing work for you. But in reality it's just like comes from that word agency which was like aentic AI which meant like AI that can do things for you and then people just like now call them agents. The way I think of it is like chat models is like a really brilliant consultant. Like you can go ask it advice and it will like give you give you the the answer but you have to actually go and take that answer and do the work. Whereas an agent's like hiring that brilliant person in house that will then go and do it for you too.

>> Yeah. End to end like you what do you want? What does that result look like? They figure out kind of the workback schedule and then literally like when you press press go and we're going to talk about underneath the hood like what it looks like to obviously the piping to make that work. You just see it just typing and working and it just gets the end result.

>> Yeah. Because I would argue that chat models question to answer like can't actually even take any meaningful work off your plate. Like maybe a research task, but realistically like chat models can't actually take work off your plate.

>> Yeah. Let's talk about like a couple of those things. Let's like kind of categorize like stuff that maybe does make sense in chat. Like for me it'll be just like, you know, I'm staying at this hotel. I'm going to studio and then I'm going to book this hotel or this hotel and I'll screenshot a bunch of them and it'll just kind of optimize from a distance perspective how I get to places or like should I order this piece of food, this piece of food like little simple things.

>> Yeah. Like yesterday I was on the subway and I took a screenshot on Google Maps and sent it to like Claude in just the chat and I was like yo can I pay Apple Pay on the subway cuz I'm from Australia and it was just like yep you can. I'm like sweet. Like just little questions to answers,

>> little simple things, you still should use chat.

>> Yeah. Yeah. Agreed. Cuz like sometimes using an agent to ask like how many calories in a banana is like killing a fly with a bazooka. It's like overkill. Like you don't need an agent for that. So chat is still like very useful for me.

Like I just got called on my phone and like asking questions like that throughout the day. But any meaningful work

>> straight to the agents.

>> Yeah. So, I mean, like a good way to illustrate kind of this old way of working with chats versus this new way of working with agents is like a marketing example because obviously like I used to run an ad agency. It's kind of used to be my bread and butter. And if I was going to create a marketing campaign, right, let's just say you're like doing a Christmas in July campaign for ecom brand. The old way was you'd probably have the brief in notion or whatever project management tool you're using. You would copy that Christmas in July brief, paste it into chat GBT. Yo, we're doing this campaign.

Like, create me some ads. Write me the email copy. You would then like take that copy and like paste it into Clavio or then like give it to your email designer. Get the ads and then like go into some other tool and make them. And you'd copy the content from chat into your content calendar, paste it, and then you would have to go into like ads manager and like manually input it all as well. Like once

>> switching cost and a ton of like small optimizations. It's it's going to two, three, four, five different people.

>> And it's back to the thing about like more fulfilling work as well. It's like when I used to have to upload if you were uploading like a 100 ads to ad manager like the UI in meta ads manager is so awful. It would take you like an hour of like just data entry like putting them into ad manager and switching off all like the creative enhancements and all the all the [ __ ] So the new way of working would literally be you just tell Claude or whatever agent you're using kick off the Christmas in July campaign and it would go into notion. It would find like the the campaign outline about like the plan and like what specific discount you're going to give and the offer and stuff and it could go into Shopify like pull in actual product images. It have like your brand guidelines so the email would be like nice and branded and then you would like write the ads. You can even use a tool like Higsfield or an image gen to create the static ads and then it might just give you back like five emails and 100 ads and you pick like your favorite email and like top 10 ads and then you approve and then it'll just literally go into Clavio, set it up and then go into ads manager, set it up and like it's done.

>> Yeah.

>> And and it could take it there and just leave it as a draft and obviously you can by hand optimize it before you click go. And for everybody out there listening and watching just to give you context like we're talking very macro right now. We are in this episode going to actually show you live how to do stuff like this because there's a lot of stuff like in between there to make sure that the piping is set up properly to get that end result. But yeah, man, I just feel like all of like the little small work is going to be absolutely done if and when you set up the proper piping. It's really just comes down to the proper piping and systems that you have underneath all of this.

>> Yeah. Yeah, pretty much. So, you've given the agent a goal. It's it's done this amazing work for you and given you the output, but like what has it done? like what happens in that mysterious agent step where it's going and doing the work. I think that it's really really important to understand like what's going on under the hood here. And I'm just going to do a high level cuz I'm I'm not a technical person myself and I'm not going to lose anyone with like going into like the actual software engineering part of it.

But I just want to touch on this loop that agents go through. So when you hand an agent a task, it's literally just going through three steps. observe, think, act over and over and over again in a loop until it has completed the task and then it hands you the final result. So when I say observe, think act, you can think of it as look at the situation, decide the next step, do it, look at the situation, decide the next step, do it over and over and over again.

>> Optimizing, optimizing, optimizing.

>> And then finally, it will output the result when it determines that the task is done. And then how it determines when it should stop going in loops is based on what you've told it in the goal. So if you for example said like to an agent as a simple example, research the top 10 business podcast I should go on and put it in a 10page PowerPoint deck. The agent will not stop going in loops until it has 10 business podcasts in a PowerPoint to give to you. So if you're really vague with like what you want the final output to be then um be a little bit more subjective based on the agent. It's not going to be exactly what you want.

>> Yeah. Exactly. So, it's important. That's one thing we'll touch on is clearly defining like what done looks like.

>> Yeah.

>> But, you know, when you're giving it a goal, it's just going in these the these three steps. Look at situation, decide the next step, do it.

>> And I thought what would be cool just to like sort of illustrate this loop is to just give a simple example into Claude and I can show you this loop going in real time. Before we we show that to everybody out there, I think a key thing to touch on just because guys, I want to make sure that you're following along as we go in that observe loop that we're popping up right now. You see the context and skills. We are going to get very very deep into how to set up the context and the value of the skills.

>> Yeah. Let me give this little example to Claude so I can show you this loop in action. Okay, so I'm in Claude Code right now and we're going to just paste this in.

>> Welcome back, Rem Dog. Before you dive into this right now, guys, this is going to be awesome. you guys are going to see the whole entire loop just so people have like context. I don't even know if you even maybe want to zoom out from a macro perspective or we can do it after the fact of just like driving around Claude and just telling them like this is code, this is chat. Let's just make sure that we do that before the end of the episode.

>> Yeah. Yeah, of course. And like I'm I want this episode to be core principles timeless. So I'm not going to go too deep into like right now the best model to use in cords opus 4.8 or Fable 5, but in 2 months time that's going to be different. But these core principles that I'm going to cover today about like how to make an agent actually useful and work for you and like how to build agents essentially that's not going to change for months. So for this example what I've told is I've said please give me a report of my best performing Instagram videos and a full breakdown of the angle the hook topic title hooks and why the video worked. I've given it my Instagram handle and I've said create a HTML report.

So that's just going to keep going until it's done an analysis of my best performing videos. I could have even give it a number like 10 best performing and then it's going to deliver the HTML report and that's when it will stop the loop and give it back to me. So the first act step that it decided to do was go and search my computer to see if it can find more information about like title hooks and hooks and some of the things I've talked about. And it's then found the title hooks are exactly what I need. So now it's gone back to the observe step. Now it's evaluating the situation after the first loop. So second loop round.

Now it's going to go and read. It's found some files. Now it's evaluating the situation. Great. I've found more files. What should I do next? Let's look at these files.

So you can see it's read these two files. Back to the observe step. Great. This is a gold mine. There's a complete data set of 60 reels matched with play counts. And then it has I mean I think maybe I have my video my real performance already downloaded on my computer from another project that it's found. If it didn't find all these 60 reels with data, it would have instead of that, it would have gone on the loop and then probably called the tool to go search Instagram essentially.

So, second loop round, it's it's read the files. Now, it's like, excellent, this is a gold mine. It's read some more files. Another loop. Now, it's gone. I have a complete real data set. All 60 reels matched with play counts, engagement rates, dates, patent tags, all that stuff.

And then it said the one field that genuinely isn't in this data is the spoken hook first 3 to 5 seconds.

>> That's the bottleneck.

>> Yeah. So now it's gone. It's thinking it's like well we need to go find that. So now it's going to run a command and it is going to go launch a sub agent which we'll touch on later which isn't as crazy sci-fi as it sounds. It's just basically it's launching another version of itself to just go check. And then it's back in the observe step. Great.

Now we've got it. The data is rich and complete. The spoken hook retrieval is running. Let me build the full report. And now it's running another act step to build the report. So, you know, we've got this loop here that the agent runs through. And a application or or a program that facilitates that agent loop just allows that agent loop to run is known as an agent harness.

And then all of like the top platforms you see online now that you hear about like Claude Code, Claude Co-work, Codeex, Manis, Plexity Computer, those are all just different agent harnesses. They're just different applications to facilitate this loop. So when people talk online about I built an agent that does this, that would imply they've built a competitor to these like they've built their own cord code. They're not building

>> probably not.

>> Yeah. Yeah. They're not they're not building a loop. Like the better word to describe it is they tuned an agent. So out of the box they all go through this loop, right? But we can actually we have four levers to pull to make these agents better, which is kind of like the whole concept of this episode. We're going to just do a deep dive into each of these.

But at the observe step, that looks like context, which is the information you can give it, and then skills, which is the processes that you've given it that it can follow. On the think step is the LLM model. So obviously these agents that step where they're you know deciding what to do the brain behind that is the large language model which you like the large language model is like GPT 5.5 or opus 4.8 like the actual model itself and then on the act step which is giving it more tools. So like out of the box like Claude Co-work or Claude Code or most of these agents, they have like a few tools. One of them being like a web search, but if you want to then have the agent like handle your email inbox, you need to tune that act step and give it more tools.

>> Yeah. I think what's really interesting about that is it's almost like sports or like F1. Like you could have a Lamborghini and then you can have a Volvo. Those Let's just look at those and make the analogy that those are kind of the LLM models.

>> Yeah. The Volvo could beat the Lamborghini if the context, the skills, and the tools are really [ __ ] tuned and super super dialed.

>> If you put like a V12 engine in

>> I'm not a car guys. I don't know if that was the right analogy, but it's just like

>> well like this this is like one of the analogies I love to give is it's like today in this episode I mean you've already started but you're learning how to drive.

>> Yeah. And all of these different tools on the market like Manis, Perplexity, Claude, Codeex, you can think of them as all just different cars. Like Codex is a Ferrari, like Claude, Claude Code is a Range Rover, Manis is like a G Wagon. And as long as you know how to drive, which is like just the the core fundamentals, which you know in driving, it's like steering, brakes, accelerator, you can pretty much hop in any of these cars and within 5 minutes like figure out how to work it. you know, like there'll be slight differences. Like the indicator might be on the other side or like one might have another cool feature like cruise control that another doesn't, but essentially they're all just the same thing and as long as you know how to drive, you can pop open any of these and and figure it out and start using it efficiently. Like

>> hot take there. Everyone is just so bullish on a specific LLM model, but we're going to prove otherwise today. Let's dive into what does that loop look like right now on the IG side.

>> Let's check on this on this little thing.

>> Let's check on old boy.

>> All right. All right. So, we can see we got a nice report here, which is what actually works on AI with Remy. And you can see it's analyzed all 60 of my reels with the top one being like over mill views. And we can see that it's like categorized them. It's like kind of put them into into categories. It's done a breakdown of each one with like the title hook like on screen like

>> And if you guys look at this too, I mean, you can take direct inspiration from this. Like you see the right verse wrong way to use Claude. You can do another video. It says right verse wrong way to do X. It's saying don't ask Claude for business advice. Obviously contrarian in nature. You could just say don't ask X or don't do X to kind of you could literally just take all of these to make all of your new ideas.

>> Exactly. I mean this was just a report to illustrate this example. Straight away I can think of a use case here. Like if you do content and brand deals like you might want a report like that generated for videos you did for the brand. So they can have like a a report of how the video performed for them as a company. If you're doing brand deals and stuff. There's so much stuff you can do here.

You can see it's just gone through analyzed all my videos and like picked them apart like why it worked, what didn't. We can see here all 60 reels ranked by plays with the date, title, hooks, the durations, and then throughout this process, right, like I started to illustrate before how it's going through loops about like, you know, it's observing. It's decided to go find some files. It's fed that back in. Now it's decided like, all right, go do this. It it it couldn't find some data like the first spoken 5 seconds of the videos. So then it had to like call like make another couple loops to go find that.

And hard to say, but I reckon this probably would have ran through about like 20 or 30 loops before it decided that the task was done. And you can see here it worked for like 20 minutes or whatever it was. So it just it will just keep going until it's decided like, "All right, this is done. I'm ready to give it to Remy."

>> Yeah, it is amazing. And for anybody out there listening, you know, if you're running a company, if you want a report at 7:30 a.m. in your mailbox every single day, a beautiful PDF looking at social media analytics, e-commerce analytics, anything. Yeah, we're going to walk through how to do this. But it's crazy how granular this can get on, you know, that individual prompt. Quick second, Remy has shared so much in this episode. All of his principles and frameworks we put into a free PDF playbook.

You can download it below, link it in the description. Enjoy the rest of the episode. It's really about what's what's underneath this and obviously the piping. So let's get into how to actually, you know, you call it tune to to optimize the agent to make it useful. So why don't you kind of walk us through

>> those three big pillars and we're going to deep dive into each.

>> 100%. So

>> a raw like agent out of the box like if you open up Claude Code or or Co-work or any of these popular agents on the market and just like give it a task like it's they're really capable. probably not going to do it in the way you like and you're probably going to get an output you're not happy with. And that's why a lot of people like start using these tools because it's all the rage and then they just quit because it's like, oh, it didn't work for me. In order to actually make the most out of these agents and make them actually useful, you need to treat setting them up like onboarding a real employee. So, you can think of agents as like really really capable strangers. Picture that dude, you know, like we've all got that friend that's like really really smart, like good at solving problems, and we'll just like keep working until like the task is done. you now have the opportunity to hire this guy into your business for $100 a month in salary,

>> $1,200 a year. Sign me up.

>> And and he has infinite bandwidth. He can just like like there's no limit to what he can do. But no matter how great he is and smart and capable, unless he fully understands you in your business or if you're an employee, your role and what you do, unless he has the tools he needs to actually do the work, like an email account, a browser, a computer, and lastly, unless he's trained on like your secret source that makes your business unique and your processes, he's not going to be very useful at all.

>> All right, so let's actually onboard this hire. And you mentioned context, tools, and skills. give us full context of how you look at onboarding the hire.

>> Like I said before, this this really capable stranger you've now got working for you, he's not going to be able to do very much unless he fully understands you and your business, has the tools to do the work, and then knows how you like the work done. And you do this through context, tools, and skills. So context being like information to the agent, like what you do, your business, like your brand voice, things like that. tools being like, you know, a computer, a browser, Gmail, notion, Slack, and then skills being like your SOPs, like your special source, like literally like documents like you give a VA. And then if you get those three things right, that's how you like properly on board the stranger, and then you have the best employee you ever had.

>> Sounds amazing. Let's go super super deep into each one of them. So, we have context, tools, and skills. Let's double click on context and tell us exactly what you mean by context. Yeah. So, context is literally like everything that the agent should already know before you give it a task. And for me, this looks like things like about me.

So, all information about like me as the user cuz I want them to like I want my my new employee to understand like everything about like who I am and what I do. Even some things about like my story and like my come up and things cuz then it can use it if it's ever writing like a landing page copy or like a sales letter script. it can reference like real things in my life. It also looks like a document about your business information. A like a maybe another document of like your offer catalog where you talk about like all your services and offers and their prices and how they link together like upsells, downells. Another one might be like an ideal customer profile which is one of my like most important ones. So it like knows who your business like targets and quite literally like if you were onboarding this new employee, right?

like a real employee, you'd probably like give them a PDFs or like some sort of documents, usually like Google Docs, Word Docs that teach them all of this stuff or like the key information you want them to know. You you are literally doing the same to the agent. So like just like you know you get get a new VA, you like give them all these docs, you're literally giving these docs to the agent and these are in the form of markdown. So for the listeners that don't really understand what markdown is, markdown's like it's it's basically one step above a .txt file. So TXT text file is just literally plain text. No headings, no bolds, like nothing. It's just text.

Markdown is literally just one step above that. It's just a plain text file, but you can do like headings, boldings, like bullet points,

>> simple formatting, stuff like that.

>> Yeah, it's just like a slightly more formatted text file. And you know, if if any of you use out there use like a tool like Notion, the notion docs or like ClickUp, the ClickUp docs, they're all in markdown format. Just super simple like headings one, twos, and threes, text, bullets, and bolding and like italics. Just the super basic formatting.

>> And to give you guys further context, it's basically like a simpler doc file. So, it's a text doc. It's somewhere in that universe.

>> Exactly. And the reason like why markdown is so important is you could theoretically let's just say you're building you're following along and you're trying to build out your own agent. You could just give them all these in a docs file, right? Or a PDF. However, it it's a lot harder for the agent to access the information. Like if you give an agent your ideal customer profile as a markdown file versus a PDF with the PDF, it's going to have to unpack it and like try and extract the text cuz it's just the way that the PDF file is like built. It's hard for the agent to like ingest the information.

Whereas with markdown, it's just like that straight ingest. It can just read it really really easily. And we want to make things easy for the agent because that just means it's things are quicker for you and things are cheaper in terms of like cost for the model running. So markdown is just the best way to be giving information to your agent.

>> To give people context as well, how many MD files do you have on your computer?

>> Like hundreds.

>> Hundreds.

>> But like so the these you're literally building out like markdown files for key areas of like information that you want to give this agent.

>> And as far as that goes too, you can get would you just say the more granular the better?

>> Not necessarily. I don't really think there's like a right or or wrong way to do it. It's more like I I just build the markdown files for me almost like how I would want them formatted. Like I've just like literally got like a about me, like a business info, brand voice, idle, customer profile, like offer catalog. I could put them all in one doc, but then it's just like I don't know. I almost just prefer them having having them separate.

>> Yeah, we're going to get into folder structure as well, too, so everybody understands kind of from a macro perspective how this brain looks and how it kind of all flows. I think for the people out there listening, you know, we'll get in, you know, what is the first thing that you can do to kind of start your journey. I feel like like the about MD file is like a pretty clear one of like

>> great spot to start. And the thing you need to understand is these markdown files you're building are like assets. They're assets for you and your company. So like really like spending the time to build these docs like really really well. Like if you just like take the time to build a really wellthoughtout about your business doc and that like the ideal customer profile they're assets for your company because if you rush the ideal customer profile doc and it's just like a bunch of AI slop that you got chat here to put together and you haven't read over every line. There might be a line in there that says like my ideal customer like if you're a skincare brand a line in there in your ideal customer profile might say their problem point is like red skin or something. And if you don't check over that now in all your marketing copy, you're gonna have like it targeting towards the angle of red skin.

And if that's not something that your product solves, then that's like a that's an issue. You know,

>> the answer on the MD files is probably you want to minimize the subjectivity in the MD files. Make them all objective, like stuff that's kind of black and white. Like I definitely would use this as an input to make decisions.

>> Yeah. Yeah. Agreed. And I and I get Claude to build all these files for me, but I read over every line before I like give it the okay.

>> Guys, I got a little cheat code for you too on the about.md file. Like the craziest thing about all this is like I'm not saying have Claude do it, but you can say to Claude, I want to build an about.md file. How should I, you know, how should I process this? How should I think through this? Yeah.

>> And that's where you I do think you can use something like chat because you can kind of go back and forth and build it.

>> Yeah, that's like a a perfectly fine use case for like the chat models. Like that's how I built out all of these. I literally said to Claude, like in a new chat, I was like, "Yo, I wanted you to build out a bunch of markdown files for me, like an about me, and I had a custom profile, just listed out all the ones I wanted, and I just said, interview me, like to extract the information from my brain to build these files, and I sat there like using Whisper Flow answering all the questions for like 3 hours,

>> just riffing, and then Whisper Flow just cleans it all up."

>> Yeah. It just like sucks it all out of your brain into these files that are now assets for your company that you can then give to your agents. And like one of the key distingu like the key distinguishments to make is when you're using these chat models, they're sort of like a black box. Like everyone always goes on about like my chat GBT knows so much about me. I don't want to move into Claude because like Claude doesn't know me. ChatGBT knows me so well. And it's like, you're right, but what it's doing is it's like got pretty much just a markdown file like memory MD or like about user.md in the background and chatgbt is building this file on your behalf without you knowing and you can't access this file.

So if you're like starting a chat GBT chat and you say in there like I'm I've just moved to New York City like what are some things like good cafes near me? JGBC in the background will take out that snippet of like I just moved to New York and save it in its markdown file and then now like it knows you've moved to New York and you just think that this model's like almost trained on you now but in reality it's just a markdown file where it's choosing what to save and the other thing about that is you can't control what it saves as well like your chat GBT like knows everything about you and then like you know you're writing like a landing page you're asking for advice on chat GBC like hey how do I break up with my girlfriend and then you're writing a landing page and it's like all of a sudden the landing page copies about you breaking up with your girlfriend. It's like you can't you have no control with these chat models about like what it knows and what it saves

>> like it it does get mixed up sometimes.

>> Exactly. So you want to make sure that you have full control. You want to own that context and that's like I'm talking about just in the format of these markdown files and then you can they're assets that you own now and you just bring them to whatever agent you're using. So like I've got my folder set up which we're going to get into with all the context in there and I can just open up that folder in claude code or codeex or manus and like straight away it knows everything about me. It's like it doesn't matter like I can just switch and stay sort of like mobile. Guys, real quick, everything that Remy is teaching you in this video is absolutely free. No gatekeeping as always.

But for the people who want it implemented, Remy made a plugin that builds this entire system for you around your business and your life. The loop, the folder structure, all of it. I am not technical. I did it myself. 90 minutes, one sitting, done. Sign up for the newsletter below and get 50% off at launch. Enjoy the rest of the episode.

So, the first step for onboarding agent is like building out these context files, right? And I'm going to show you like what this actually looks like. So, I'm going to open up Cloud Code again. Here, we're going to do a new session. Nice and clean.

>> Hey, there we go. And I'm got my OS folder open now, which we'll touch on later. But the way that these agents work now is a lot of them run like locally on your computer as opposed to like the cloud. And what locally on your computer means is it's like instead of having like a project on your chatbt account, your that project folder now lives on your computer. And there's a lot of benefits to that which I'll I'll touch on later, but I'm just going to open up this one I've created now called demo. So this is just a brand new folder. You can see it's completely empty

>> and that's just you just created an empty folder on your desktop.

>> Yep. So it's desktop empty folder called demo. And we're just going to open that up. So now you can see in cloud code we've scoped the agent to just work in that folder. Just like you know when you have a a project in chat GBT, it's like any of the chats you do in that project. It's like scoping chat GBT to just work there.

>> So now it's a new blank canvas and you're you're deciding what inputs go into this folder.

>> Exactly. Exactly. So you can see just to demonstrate this the importance of context. If I'm opening up this brand new folder, so I've been working with claude code, right, for for like eight months and if I ask like you know who am I? So you can see like when I've asked it, there's no markdown files for it to look at. So, I've asked it who am I? I've been using CL code for eight months.

It should know. But it doesn't. It's because all the context you own in those files. It's not a black box.

>> So, if someone has an alter alias, they can they can just create different alteres in in in different folders.

>> Yeah. Essentially, so you can see here it it tried to read the memory MD mark file, markdown file, but it doesn't exist. So, you can see here it's just like the f file doesn't exist.

>> So, it went through that loop. It was searching, but there was no kind of raw data to extract.

>> There was nothing for it to to do.

>> So, how do they know the email and the likely name? because that was just from my claude account. It must just have access to that. That's literally just because that's the email associated with my claude account and name. Actually, no, no, no. Actually, it's it's pulled that from my computer because this agent lives on, you know, it's got you got a username on the computer. That's where it's gotten it from.

>> Okay. So, what does this look like when you're on steroids? Let's dive deeper into kind of doing these MD files.

>> Yeah. So, let's let's continue onboarding our agent, right? So, the most important markdown file, like, you know, we've got our markdown context files. The most important one when you're dealing with agents is what's called an agents.mmd file. And I mean claude have just decided to be difficult and in in their systems they call it a claw.md. But in pretty much all the other harnesses you use like codeex and open claw and stuff it's called an agents.mmd. And essentially what happens is is every time you're like starting a new session and by new session I just mean like if we go back to that goal to result thing it's like every time you're going to like give it a new goal you're kind of going to click like new session.

the same way you start a new chat in chat GBT.

>> Each session has an amount of like space. It's kind of like you can think of like the agents like brain power and as the session starts to like fill up the you have what's called context rot which is basically like have you ever been in a in a chat on chat GBT and you it's like so long you've been in there for hours and it starts to just like go crazy like it literally just starts to just like hallucinate forget things. So what what's happening there is every time you start a new session like a fresh like chat window I guess it's got like a certain amount of of I guess capacity you could call it like free for the actual work and what your sessions probably look like is something like this where they're just like like so like so much information that the stuff you started telling it at the start like fall out the top

>> that was V1 Mark bro I'm not on V1 Mark anyone I mean I think 99.999% of the world is in probably V1 Mark one endless chat to be frank with you.

>> Yeah. Yeah, probably. So, every time you start a fresh session, the way that this agent like knows about you. Same way that chat gbt's memory works is if you start a new chat in the background, it started the chat with that memory. MD loaded into it, but you can't see that, right? So, you give it a prompt like uh write me an email in chatgbt and to you it just shows as like that one prompt you've given chatg, but in the background it's also loaded in that memory markdown file. So instead you've got like like a hundred lines of information about Mark and then write me an email.

So it's got all that context in it. Same thing happens with agents, right? So we've started a fresh session here. What this actually looks like is any file, any markdown file in that folder titled claude.md gets automatically loaded in. So your claude.md or agents.mmd that's like your your northstar markdown file. That's the one you need in every single project you're working in. So to illustrate my point, I've created this folder here with a claude.mmd in it, right?

That I've pre-prepared. And we can actually just open this up. So you can actually see what a markdown file looks like. And I got Claude to build this for me. So we can see Rey's AI operating system. Who am I? Rey's the founder of AI with Remy.

The business, the brand voice, the ideal customer, the offer, the values, how I like to work, preferences. This is like our you know northstar context file and that's the one that's going to load in to each new session by default

>> to give macro context on how you're thinking.

>> Yeah. To give macro context essentially. So that same example right if we go back into claude here we just asked it in that folder when it was empty who am I? It had no idea. Now if we go new session same folder but it's now got that claude.mmd in it. And we can say who am I?

>> Heyo. And you can see here now it knows exactly who I am. It knows exactly like what I do, my background, the brand, the three products. So that's like a great illustration there. Do you see how how it goes from knowing nothing about you to now having that context file that knows everything?

>> That's why it's so important to be lean and intentional on what files you upload obviously in there.

>> Yeah. Yeah. Exactly. So that's that's your pinnacle markdown context file. That's like the first one that you need to build. the the part about the claw.mmd made sense, right? That gets slotted in and it's like the agent wakes up to do a task and he's got that loaded into his brain, right?

>> Yeah. And that's something that's you should constantly be updating if something big in your life changes. Correct.

>> Yeah. Yeah. Correct.

>> Yep.

>> So, you're probably like wondering now, okay, great. I get that claw.md agents.mmd. Where do the other ones fit in? Like the about me and the customer profile, like where do I put those? So those ones, the other markdown files, they don't get loaded into that session window by default. So we need to we've got our CLMD that gets loaded in by default. And then we need to tell it in that that it will always read, hey, go check here as well.

So then what I like to do, how I have this set up is we got our claw. MD here, and I'm going to paste in these other ones I've pre-prepared. So now you can see we've got a couple of other files taking shape here. So we've got our claw.mmd. We've got this context folder with all these markdown files in it. My values, my offer, my item customer profile, brand voice, about me, and then this memory.mmd, which we'll touch on in a second. So by default, claude is any any project you open up claude in to work, it's always going to read that claude.mmd.

And then we're going to point to the context folder in the claw.md. So you can start to like compartmentalize and like modulate your your project, if you will. making like a whole like a like decision rubric like a decision tree of you know if it goes here it opens up this folder and stuff like that.

>> Exactly. And then this is like all these agents you build they're super like modular. It's like you hear other ones really popular like Obsidian is a really popular thing that people give to their agents as like a second brain essentially like there's loads of different like frameworks like that. And instead what they're doing like if if you had this folder and you wanted to use obsidian instead you would instead delete this context folder and you would in your cloudmd point to the obsidian vault instead. That's kind of how people are doing that like you can kind of modulate the the context.

>> So in short you can kind of redirect it whichever route you want to go.

>> Yeah. Exactly. And it all stems from this file here. So now this new setup we've got is kind of like evolved. So we just the first one was just the claw.mmd. And that's probably the most basic one that if you're trying to like start using agents for yourself. That's probably the first step I'd say is just create a folder and then just build a cloud.

Mmd just ask claude, hey build this claw.mmd file for me and just include in it like an overview on who I am and what I do just to give it like that base context. Then v2 is now we're adding in like this extra folder for like we're expanding out our our context here. And if we open claw.md now, now I'm going to point to that context folder. So you can see if we open it up, it's like who am I? My context read before any task. Everything you should know about me and the business lives in the context folder and then it's just given an overview on the files.

>> Wow.

>> Load the relevant files in before starting any tasks. Assumptions are the enemy. If the answer isn't there, ask me. And then everything on continues like normal. And then the memory I'll touch on in a sec.

>> And then as you keep developing more folders, you just keep updating. The most important thing is the claw empty file cuz that is going to create the infrastructure like you could have like marketing, finance,

>> logistics.

>> Yeah.

>> And then underneath that you can have multiple folders.

>> Exactly. So when I asked Claude before like who am I? It knew straight away. That's cuz that file automatically loaded in. But if I deleted that claw.md and then asked it who am I again?

>> Back to dummy.

>> Well, it's got the context folder.

>> Oh yeah.

>> If I just deleted the CL MD and left the context one, it wouldn't know straight away. It would then go through a loop to think like, oh well, I don't I don't know who who he is. Uh, let me think. I can let me let me check for what folders I've got. Oh, context. Then it would read it. Then it would load it in.

But it's just like it's slow and it's got to go through another loop. So like that's why you have the claws that MD there.

>> Yeah.

>> Why why don't you everybody listening right now just ask it something very very basic under the notion that now you have context based in like something about any of those kind of raw folders. I know you had under there like brand voice like anything.

>> Yeah. Yeah. Well, what I what I might do is I'll just say like write me a cold email to

>> how about to Mark to come on uh to come on open residency.

>> Actually, know this. I'll just say like

>> I'm going to whisper flow it to demo.

>> Yeah. Amazing.

>> Makes sense.

>> Write me a cold email to Mark from Open Residency podcast to try and get me a position on the show.

>> Wow. Whisper for the win, baby.

>> Whisper flow is so good. Like talk about like agents stacking up the productivity. You can even stack on top of the agents when you start using Whisper Flow because it's like you can just just get things down onto the page at the speed that you can think.

>> For the people out there listening, I'm going to give you guys a little cheat code. One of our episodes a bit before this is of Chris Voss, which is a negotiation expert.

>> You can make some MD files with him to speak in his language. So it probably would be a bit more persuasive on this email that you're going to send me. Let's let's let's see how good it is. Let's see your sales pitch right now.

>> Okay, great. So it's gone through a couple loops, right? It's got decided to go and research who you are. It's gone to go and like find

>> that is me

>> open residency

>> and now it's written right. It's like literally said here like like we haven't given any other context. We just said write the cold email and it's got cuz it's got our our clawd and then this context folder and that context folder is so rich with like my values, my philosophies, my like thought processes on things and my offers. So you can see like the subject lines, right? Operating a 20 person team without hiring 20 people. guest idea for open residency. But the email right here, hey Mark, been working through open residency.

The operator as last line of defense framing is the realist take on running a business. Terrible cold email by the way. Terrible. But it's basically you can see here it knows everything about me. It's like I teach founders to stop drowning in tools.

>> This is where we're going to get into like the additive layers of like an example is like that negotiation

>> skill that you know how you speak skill. Like you can get way deeper to make this thing absolutely flawless. Clearly, it did an amazing job.

>> Yeah. I mean, the key point demonstrate was right that it just knows about me. It it can write an email with all the context. Like, it doesn't like the email's terrible, but like and you can tell it knows about like what I do and my philosophy.

>> Amazing. You're booked. Let's go. [laughter] We on. We're here.

>> Okay. Great. So,

>> and just to take a step further, just to kind of paint the picture of where we're going to go with this.

>> Yeah.

>> This could be this email is drafted. It could also be automatically sent as well too, which we're going to get to to connectors and MCPS as well too, just so people know like this could be fully a toz. Find all the business podcasts, draft the email, and send the email.

>> Then you schedule it. So every week it's going to or every morning it's going to go find business podcast, cold email them to get you book calls, like all this stuff. It's crazy.

>> You're going to need to dial that email in a little better for me to say yes though, but it's okay. Don't worry. Keep going.

>> So So that's that's what I'm going to do now. I want to display like so understand like we need these context markdown files. The most important one's the claw.md that then points to the others. And now like when we open up a new session, it it it straight away knows everything about us, right? But the next layer of context is memory, which is still kind of under the umbrella of context, right? Memory and lessons. So off the rip, it knows all this stuff about us.

But what if we ask it to do something differently? So you can see I've got in here this memory.mmd file, right? If we open this up, this is just this has got memory learned rules, lessons Remy has taught me. I check these before every task and it's got never write formally, just a couple of like random preferences. So the agent like knows everything about us out of the box, but we want it to be like be able to improve over time and like if we correct it, we wanted to save that somewhere, which also counts as context, right? So I like to build this little like kind of de facto memory system. I think like when I started putting this together, it was because none of these agent harnesses had memory built in.

So if you said to it like right this this email right here, if we said like can you please sign off the email with cheers Remy and like I always want you to sign off emails with cheers.

>> It's not auto updating unless you put

>> Exactly. It's not so like before the last maybe in the last month they've a lot of these harnesses have now added in memory as a feature but before that you had to do it yourself cuz otherwise it would say like if you didn't have that in place it would say like yep got it but then next session in a week time when you write an email it wouldn't do it.

>> Show them a memory MD just in case they're driving the Kia and not the Lamborghini and maybe that LLM does not have it built in. Show them a little bit of context.

>> So we can just show in here like the memory

>> MD. No shame on the Kia either. I've seen some nice Kia by the way too. [laughter] So, we got the the memory learn rules. These just a couple I put in here before, like never write formally, like always use real examples, never generic placeholder ones. And then same way that we're pointing Claude at the context folder, we're also going to point at the memory folder. And I've just basically said, you know, your memory lives in this file.

When I correct you, write lessons into this memory file as a new rule and then check it before every task. This is how you go from good assistant to know exactly how I like things done. And I have one little tip is if you use the at@ symbol if you tag a file like that then it like it's almost like a a sim link. I don't know if you know what that is on a desktop. It's like

>> I don't

>> if we for example if I tell it

>> is it like a lighter load on the brain like that it zips right into the file or something?

>> Yep. Zips right in the file. It's it's like as good as the file being loaded in if that makes sense. Cuz if we just tell it like go use the memory MD and don't add it'll then have to make a loop to go and find the file and bring it in. But if you just have like the app, it's automatically loaded straight in.

>> Guys, we're going Lamborghini full steroids here.

>> Hell yeah. So Claude like has this this built in, but even still, it's still almost a little bit of a black box. It will save it to like Claude's desktop app. So now if you're trying to work with this folder in like codecs where you want to try and like use other harnesses, you don't own the context file. Claude kind of owns it. So like that's still why in all my projects I still kind of add this memory system in. So we can just test this out here, right?

And we can say please in future when creating websites I want you to always use dark mode and never ever use light mode.

>> Here we go. It's done it. Bang.

>> Okay, great. So you can see it's now gone and said add I'll add this to your memory rules so I never forget it. It's read the memory md and then you can see it's added it's edited and it's added this line. When building any websites, always use dark mode. Never use light mode.

>> Love that. That's obviously in that auto updated in that folder that you showed us.

>> Yep. So, if we go back here into this demo folder, we go into our memory.mmd file and open that bad boy up. You can see when building any website, always use dark mode, never use light mode. And then now this is like we own that that preferences, right? This will grow over time. And like I've had the question before, it's like what happens if that just keeps growing? you've got like hundreds of different lines in there and they all start to like contradict and get messy.

Like I don't think that will happen. Maybe in like 6 months time you can just do a spring clean. Just

>> open a session with Claude and go like

>> just audit my memories and just take out anything that's contradictory or conflicting and cleans things up.

>> So that is pretty much like context 101. Just to recap, we've got the claw.md which Claude autoloads in every session. We want to give it more context. we add that extra little file and then point claude to that folder and then we've set up our little memory like self-improvement system as well.

>> So from a loop perspective we're going to start with the about.mme the claw.md is going to be kind of the the macro infrastructure which is then going to lead into more folders which we'll obviously get into and then the memory MD is just a self-fulfilling loop that just keeps remembering all the preferences and such.

>> Yeah. Yeah. Exactly. So now like every every session we start that observe step now has all the context and skills loaded in. So every time we're giving it a goal straight away in the first observe step before it does anything we've already got like now I mean skills will touch on but now you can see we've really tuned up that context step. So when it starts to work on your tasks it has like all the information that it needs. And I think one last thing just to just to finally like drive home this point.

We can run in Claude code this little command. Don't worry about all the others. We'll touch on that later. But this is a one that comes built in with Claude. You can go slash context and it will actually pull up that real bar chart for you. So you can see here context window. We've used 6% of that bar.

>> Are you talking about 6% of like the memory within that individual chat?

>> Yeah, within that individual chat. So you can see it's already like our bar. used up 6%. And if we look at like we we've given it one task here, right? Like please in future tiny little message and it's 6% which is a fair bit. It's almost like it's a fair bit of of the total space used. So you're starting each session even if we just did like a blank thing with no messages sent you'll always like have a little bit of your window chewed up because it's feeding in all that context before you start any task.

That's why you could also argue going back to the beginning is keep the MD files like lean and cut, you know, only use what you need to use.

>> Yeah, exactly. Because if you have these like really bloated context files and like you have, let's say you have 100 markdown files, you start a session and the context window is already like 20% full. It's like you you want to Yeah. 100% to your point, you want to keep them nice and lean and like really like potent with like high density information.

>> Amazing.

>> I use Whisper Flow for hours every single day. I think way faster than [music] I type. I speak about 220 words a minute and type only 45. Whisper Flow closes that gap. It's a voicetoext tool that works anywhere on your computer or phone. You talk and clean formatted text shows up wherever your cursor is. All right, let me show you.

I'm going to answer a real email right now without typing. You can see here Tiger is asking for feedback on our intro video for the next episode. Watch how I respond. if you could just make a few changes. Uh, make the red a little bit brighter, [music] the typography a little bit smaller. Uh, for the music, if you can just give me some other options, and [music] that first photo, some more options as well. Uh, please give me three options for each.

And, uh, make sure you send it to me by end of the day Friday. Thanks. So, as you can tell, the text is way cleaner. [music] I kind of speak in half sentences and sometimes mumble on. This makes it very clean, formatted perfectly, and avoids all the small mistakes. This is a product that I cannot live without. I promise you that you will love it.

If you guys want to get one month free of Whisper Flow Pro, click the link below and use code open residency. So, yeah, context. We've we've we've taken our really capable stranger that we've employed and we've told him everything he needs to know about us. He's ready to start working for us, but he's still going to be pretty useless if you don't give him like tools to work with. Like imagine like you've just got this this dude that's working for you, but it's like he doesn't have an email account or a computer or a browser or a phone. He's like still going to be useless. So we need to give him tools to be able to actually complete the work for us.

So the way we do this is what's called a thing called MCP. It stands for model context protocol. And I don't want to lose anyone here. It's it sounds technical, but like it's it's super simple. And and this all MCP is is just a way for your agent to connect to tools, things like

>> third party tools.

>> Yeah. It's a third party tools. Yeah, exactly. Things like, you know, Slack, Gmail, Calendar, like you need a way for your agent to to connect and you do that through what's called MCP.

>> To give people more context as well, I think a lot of people out there use either N8 or Zapier is a big one that people use to kind of extract information and and connect it.

>> And we're in the era now. I'm so curious to see. I think all the principles here are evergreen,

>> but it's like it's a big deal now to have an MCP. And like some of these big companies don't have MCPs

>> and like it's it's they're crazy. We're going to get into the BI of MCP

>> that it's what I make purchasing decisions. Now, if if I'm choosing, let's say I'm choosing like a marketing email marketing software, for example, if like if I've got five options and if if they don't have an MCP for a way for me to connect my agent to it, I it's out of the question. I won't use it. I don't use front ends anymore of apps. Yeah. like like the future of this is and everyone that I know that works the way this new way of working this stage two which is agents they don't really use like frontends anymore like I complete a full workday from with inside like my cloud code or or agent harness that I'm using

>> by front ends just so people out there listening like you're not in platform in behind on the dashboard you're just extracting from there and then working within your workspace

>> y like I use Google calendar I use Gmail I use Slack I use Stripe for payments cal.com for bookings And I can't even tell you the last time I've opened any of those apps up. They're just all connected into CLA. It's this new it's it's a completely new way of working where you've got

>> Claude or whatever AI harness you're using that sits on this as like an intelligence layer on top of all your tools and then you're just interacting with like this this intelligence layer. So, you know, I've alluded to MCPS being just this this way for your agent to connect to tools. But super quick on like what it actually is, right? So before MCPs existed, if you wanted to connect your agent like Claude to a tool, it was it was difficult. It was possible, but required lots of custom development. And the way to think about it is like Claude speaks English, right? And all these different tools speak different languages.

Like Gmail speaks French, Notion speaks Spanish, Slack speaks Chinese. So if you want Claude to talk to to Gmail to like get it to do things, it was required a lot of custom development. It required time and effort because Claude had to learn

>> heavy, slow, expensive, everything.

>> French.

>> Yep. And shout out Ross Mike. This is explanations from him. He was on like some part I heard him. So this is taken directly from him. This is what landed like really nicely in my brain. MCPS are just like this translator that sits in the middle between Claude and your and your tools.

So Claude does not need to learn French and Spanish and Chinese. It just has this little translator in the middle. So it just makes calls and then it can be relayed really really nicely to the tools. This is an oversimplification but quite frankly like no one really needs to know what happens here. All you need to understand is the MCPs are just your way to connect tools into your agent.

>> Uniformity, simplicity, and that just streamlines everything for speed as well.

>> Same way you can think of it like an API, right? For those of you who know what an API is, like it's just a way for tools to talk to each other.

>> And again, that's an oversimplification of explaining MCPS and connectors. And I think the big thing to take out of this episode is the ability that you can ask the LLM like, oh, how do I set up connectors and how I do it? And I don't want to encourage people to be lazy, but you want to just quickly just show over the screen of just where you go into Claude to do it because it's very very simple.

>> It's so simple. So the way like if we open the Claude desktop app

>> and we go into customize, you can see straight away connectors.

>> Boom.

>> And we have like we go up here to browse. There is so many connectors here. Like pretty much all of the major tools that you would use have a connection here. And it's as simple as this, right? So let's just say we want to connect up ClickUp. So I can literally just go ahead and go plus and then I'll just oneclick login to my ClickUp.

>> Guys, for context, we are power users of ClickUp. That is the harness the project management tool that we use that creates all the workflows, all the dependencies.

>> So we can go in here. Literally, I've selected my workspace connect open claude. It's connected. We go back to the desktop connected to ClickUp. And you can see here like we've got all of these different things that we can do in ClickUp. Create tasks, create lists. Claude can now pull information from ClickUp if you're planning like marketing campaigns.

It can update it. And we've got all these like by default set to needs approval. So it's always going to ask you before it takes actions. But as you start to build up trust with Claude and like

>> you know you you get more comfortable with allowing it to have more access. You can just do always allow. Like all my tools I just have always allow pretty much. But in Claude like that's as simple as it is to connect these. But that is using MCP by the way. So you don't really have to deal with any of the technical [ __ ] But that when you click the plus and log in that is it's it's got an MCP server basically. That's what it's using.

>> It's crazy that you say that like you're picking vendors based on if they have an MCP or not. It's literally like 5 to 10x. We're going to dive deeper on a specific use case onto how much more granular and strategic and faster and optimized it is with this.

>> Yeah. I mean, it begs the question of just like, are a couple LLMs going to win and then just the world is just going to be a ton of MCPS and connectors into it?

>> Like, if you're building a software product, it's like I I had a buddy come to me and he's like, "Yo, I'm building this like travel agent like AI agent that helps people like plan their trips and he's got this like nice website where people log on and you you say, "Okay, I'm going to New York for 10 days. Like, help me do this." And like has an agent that plans your trip. Like I I said to him, I'm like, I I don't think that's the right way you should be building products for the future. I'm like, you'd be better off building this travel agent as an MCP that you then get hooked up into Claude and then now people who use Claude can now have you show up as a connector here, click plus, your, you know, travel AI and then add your product as an MCP and then now you build a purposebuilt MCP for Claude that helps that makes Claude be able to plan your trips better that helps Claude like gives it some extra tools it needs like it can search, you know, like Sky Scanner and some other websites a bit easier.

>> Yeah. I mean, I feel like Yeah. I feel like the future is like as opposed to offering like a hundred things, it's like be really really dialed on 10 20 things, then it becomes almost like an external data play in conjunction with that vertical.

>> Yeah.

>> Like,

>> yeah,

>> be really really smart and understand and know less things and just feed it

>> into Claude. I completely agree. We talk all the time about like mid-market B2B SAS is absolutely smashed. like some of these companies that got sold like I don't even want to call some of them out but like basically what I was doing on

>> these SAS tools

>> I'm literally just doing it inside Claude right now.

>> Yeah. Yeah. Exactly. I mean like

>> Yeah. The the the SAS market is just getting absolutely decimated. And I think another thing is like a lot of these software is built on like headcount. Like they're built on like seats in the software and now it's like you just people are like reducing headcount. They got agents in there and like they can't bill for like agents. That's bad. Yeah.

So, you mentioned kind of the always allow or kind of ask first. Like that begs to ask the question of like security. A lot of people are very concerned about like connecting a lot of this stuff. Like what's your just overall thesis on how people should approach security?

>> You know, you just have to weigh up the trade-off. And for me, it's like, yeah, there's a risk of things going wrong. Like maybe sending an email to someone who it shouldn't without my approval. Of course, there's a risk, but it's like I've I've weighed up carefully like that risk compared to these productivity gains that I'm making. And to me, it's worth it. And I guess you just have to do that in your own head. But like there, of course, there's so many edge cases with this.

It's like you hear like horror stories about agents doing things for people. And it's like you hear the same thing about people getting hacked on the internet. It's like just cuz someone got hacked or you've been hacked before doesn't mean you're not like going to stop using the internet, you know?

>> Yeah, definitely edge cases. And I think like the last line is like data is one thing. I think like connecting your something that has like your credit card and it could like go buy things. I feel like that is kind of the last line of defense, but like

>> you could just do like for a bunch of things like draft only or take it to the finish line and don't click the button at the end.

>> Yeah. So I would say like if you're really like conscious about it like give it these tools but give it what's called a readon access. So it can't do actions it can just read the data. For example, read emails but it can't send anything. And that's just a nice way to start out and then you can like increase the permissions as you start to like feel more trustworthy. I give Claude full access to everything. Stripe everything.

It's it's got full access. I'm comfortable doing that and it's a risk I'm willing to take on. I've been in power using it for like 8 months and I've never had any issues. Some of those other harnesses like Open Claw and like Hermes and stuff, they are built in a way where the agents like not going to ask you for permission as much. The way that like these big companies like Anthropic and and and OpenAI have built like Codeex and CL code. The models are very good at asking you for permission for stuff. Like pretty much anytime sometimes it gets annoying for me.

It's like I'm trying to get it to answer emails, but it'll ask me for permission. Hey, should I send this? I'm like, yeah, send it. Like I've given you

>> like allow access, allow access, allow access all the time. Yeah.

>> Yeah. Yeah. Yeah. Yeah. Exactly. So, I I've never had any issues personally, but it's just something you have to weigh up. I mean, like there's two sides with the security question.

There's like obviously giving it your tools and then it going and like taking actions. That's that's probably my least cons like my my least concern is it taking actions on my tools cuz that's like not that big of a deal. The other security side of things is like the models and like putting sensitive data through it. And this is like a big thing and like a big problem I'm trying to like solve with working with some of these large like enterprise companies is it's like some of them have like literally said like we don't want any personal information company IP running through a clawed model because they're not convinced that like the claw stealing their data.

>> Yeah. So that I mean that's a whole whole another question but for like the personal level just like getting the tools connected and getting it to start doing things for you.

>> Yeah. just start with read only access if you don't feel comfortable and then you can escalate it up as you go.

>> Nice. Um let's talk about a couple of the tools that are like musthaves for you on your side. I want to share some of the stuff on our side as well too.

>> 100%. So if we think back to like our little agent loop of observe, think act. We've tuned up that observe step with context and now we're going to tune up the act step. Right? These are like the top six things I reckon that everyone should have connected up to their agent or claude, whatever you're using. First one is Appify. So Appify is essentially a library of online scrapers and these are like scrapers that people have built.

Let me just go into here.

>> So it's almost like a third party like sub agent that helps you scraping.

>> Yeah, exactly. So it's like a marketplace. There's thousands of different scrapers you can use here. Oh wow. So you see on Ampify, right, we've got Instagram profile scraper, YouTube transcript scraper, Reddit post scraper.

>> Wow. This eliminates like some people are using like Grock as an LLM under the notion that it could scrape Twitter/X, but now you can use Aify.

>> Exactly. We've got LinkedIn post scraper, Google Map Scraper. There's like Craigslist scrapers. You can get like get lead scrapers, email scrapers.

>> These are all individual MCPS.

>> No. Oh, it's just a

>> and can use what the check. [ __ ] I never heard of this one. Is it? It is. Everyone needs it. Like literally there's there's almost nothing that Claude like can't scrape off the internet for you with Ampify connected.

>> Damn.

>> So, this is one that no matter what tools you use, everyone I think needs this. They've got a pretty generous free plan. It's like a five Yeah, like $5 a month worth of usage.

>> Yeah, we're going to throw another zero too behind that. This is crazy. Holy [ __ ] So, Ampify, everyone needs to have that one set up. The next one is Fire Crawl. So, by default, like pretty much all these agent harnesses as part of the axe step, one of the tools they all have baked in is a web search.

>> But this is super like simple and primitive. It's like if you were to ask the agent like, "What's the price of Bitcoin right now?" It can just web search and get the price. It's like more information gathering. when it comes to like things like, "Hey, scrape the branding for this website or like go look at this website and tell me like why they're or like do a CRO audit of my website."

>> Less subjective, more subjective, more like context strategy type stuff. Not like what's the this is the question. This is the answer. It's more

>> No, no. I I would actually say it's it's more that like the web search it can't look at the website. It can't actually like Does that make sense? We

>> can't extract raw data almost.

>> Yeah. Yeah. Exactly. Like web search is just to like find like facts off the internet.

>> Yeah.

>> Whereas fire crawl allows it allows it to actually like read the page not just search it like look at the page. So it can extract like it can tell what the branding colors are. You could say like do a CRO a order of the page and then it can use firecrol.

>> That's the first thing my brain went to from a CRO and merchandising perspective from an e-com store. That probably is big.

>> Yeah. Exactly. So, you know, if you if you said if if you if you didn't give Claude Firecrol and it just had default web search and you're like, "Here's my ecom store. Like, run a CR order." It can't it can't see the store. It can just like maybe like search some information about your website, like what you sell or like a little about section. With with with Firecrol, it can actually like look at your page, scrape the entire thing. It can see like what buttons you have and where, and like, you know, it could see like, you know, your buttons are the same color as the background.

like first fix, make the buttons like brighter. So like stuff like that, it can give Claude like the ability to actually like scrape websites properly and across across the default web search, fire crawl, and amplifier. There's like pretty much nothing that Claude like can't do for me across the internet.

>> And this is just mitigating the back and forth of just bottlenecks. It's just getting you more and more and more context.

>> Yeah. Yep. And it's less it's less um human in the loop steps, right? Like if you didn't have ampify or fire connected, it used ampify before when we did the scrape my Instagram account example. Damn.

>> So, like if I didn't have appy connected, it probably would have said like I can't connect to Instagram. Like, can you send me the videos or something?

>> Context for people out there listening too, like you don't have to say anything. This is embedded in the brain on the LLM platform.

>> Yeah. Yeah.

>> Damn.

>> You can think of like you can think of our um really capable employee that we've just hired. You can think of him as he's got his desk, right?

>> Yeah. and he's got next to him, he's got a bookshelf full of skills which we're going to get to, but he's also like got the tools like laying around like he might have like uh, you know, he's got his computer. He can see like he's almost got this up, right? If we go applications, you can imagine that our ultra capable employee has this screen up, right? So, anytime we give him a task, he doesn't you don't need to tell him go use Ampify. It's like if you tell him, "Yo, scrape this brand's Instagram page and give me the top best performing videos."

>> He's going to just pick the right.

>> Yeah. He's just going to look at his apps. Okay, cool. Like, I should probably use Appify. And then he's just going to go use it. So, you don't need to actually specify it. The next one is Composeio.

Now, this is like some absolute source I'm going to put you on, right? Some quick backstory about how I found out about this wonderful tool. I had everything like baked into Claude. I had all my connectors built into Claude like I showed you before and Claude went down for an hour the other week. Like the servers were down and I had like so much work to do. I'm like, "Oh my god, I I and I and I can't work without Claude now." So I had to open up like Catgt's codeex to like work in there. But and and the way that my folders set up, you know, we went back to the demo folder before.

I've got like this OS folder stands for operating system where I work out of which I'm going to show you guys after this. So the way that that's built is I own all the context files. I own all the skills. They're not embedded in claude. I can open that folder up in codeex and keep working, right? That that part was fine. The issue that I found was I had like 50 different tools connected to claude.

And then I started to get to Codex to work and it like didn't have any of my tools. So I started to go through and add in like all these tools and and I was like there must be a better way. That's how I came across Composio. So what Composeio does is we can open this up. You can see connect apps. They have way more than than the Claude desktop app. They have thousands of tools that you can connect.

Same way with Claude, like I showed you. It's one click login. You click connect, sign in. They've got everything under the sun here. And then

>> is this like an MCP for MCPS?

>> Yeah, it's like an M. Yeah,

>> it's like an MCP. It's like a bridge basically.

>> Yeah. Yeah. So I will connect all my tools in. And another thing, another thing is in the Claude desktop app, you can connect Gmail, right? And log in and you've got Gmail connected. But if you've got three Gmail accounts, you can't connect all three in Claude. Pain in the ass.

And which most people have like multiple email accounts. So in here, you can see I've got three active Gmail connections. That was another thing that I liked about it.

>> So in short, you're basically saying that connect all of your MCPs to Composeio and then if you're in aio

>> and then you and then Composio is like that single MCP with all the MCPS underneath it.

>> Damn. So you can see here in in Claude in connectors Composeio. This one won't show up as a browse connector. You'll have to click add custom and then add the URL which I'll show you how to do later.

>> And yeah, we can see I've just got Composeio. So I could like theoretically just have that. I don't need the others. You can even connect the other ones I'm talking about ampify and firecrawl. You can connect them through composio. So

>> damn

>> composio that means like for my setup trying to like be you know robust and protect myself against like platforms going

>> you need to go to your bunker in Argentina cuz the world is crumbling you can just hit up composio and just bring all your [ __ ]

>> the MD files the skills of composio

>> [ __ ] so when I in future now if I want to work in codeex I don't have to connect all these tools again I just have composio and then if I want to try out let's just say like complexity computers is another one I haven't really used it much just another car, another different flavor of the same thing.

>> But if I decided I wanted to use that, I could just I'll just compose it to there one time. Yeah. And then it's everything's hooked in. So for everybody out there listening, I want to really really stop and think like where my brain used to go and this is the problem that I used to have with my team. It's like, okay, I've never been on codeex. So if Claude went down, I'd have to go elsewhere. Like I don't even know if it's as simple as just clicking the connector to get Composeio, but you could literally just go into chat GBT and just say, "How do I connect Composio?" And I think everyone just needs to understand that all the answers,

>> yeah,

>> all these in between the lines answers are literally in the LMS. You just tell them this is what I need done and they can do it for you.

>> That's how I learned all this.

>> Yeah.

>> Like the only like all this stuff I'm sharing with you today, I just it's pretty much all learned from asking Claude.

>> Yeah. People need to go through the exercise of like if you're not a technical person and you'd have to bug somebody on your team to do something small for you,

>> force yourself to not bug them. And what may take you or them a minute, two minutes,

>> yeah,

>> it'll take you 5 minutes, 7 minutes, 10 minutes if you're not that technical, but you will get to the answer. So, it's more just like

>> figuring this [ __ ] out by yourself is huge.

>> It's just like, yeah, massive unlock to get in the habit of just asking Claude any stuff. It's like, how do I do this? Like just just ask what it will tell you.

>> 100%.

>> And if you start following the steps and get stuck and you just screenshot this error, paste it and call it. Yo, hit this. Like what do I do? Like

>> that is a what you just said right there is a bar on its own. That's a cheat code on its own. It's just doing that. It's just screenshot. This is where I'm at. Can't get past it. What do I do?

>> Let's keep going. So these Chrome Dev Tools.

>> So the next one's Chrome Dev Tools. So this is a an MCP built by Google Chrome. Maybe we can connect that through Composer. I don't know. I haven't tried. But essentially what this does is it allows Claude to spin up its own browser if that makes sense. So like I use this a lot if you're building like websites or apps and Claude like wants to check its own work cuz you know you might say like build a website you know these colors make it look nice the brand guidelines it might build it and send it to you and it's just like wrong.

It's not at all like what you wanted. Chrome Dev Tools is like one I use that allows Claude to like be able to check its own work in a sense. Like it can spin up a browser and look at the website it's built and go, "Oh no, that's not good. I'll keep working on that."

>> As opposed to like in platform or a PDF file. It's like an actual browser.

>> Yeah. It's like an actual browser. Yeah. And like another thing that I use it for is I don't know another example the other day I saw on X someone was putting together like a register for like founders in Australia like almost like a a phone book of of founders in Oz. And I clicked I was like this is cool. I'll sign up. And then it was like a, you know, bunch of questions and it was going to take me like probably 20 minutes to sit there and answer them all.

So I just like got the link, pasted it into court. I'm like, yo, can you apply to this website for me? And I just kept doing other work. And then because it has all the context about me, it knew exactly how to answer all the questions perfectly and in my voice and but like without Chrome DevTools, it couldn't have had a browser to like go and actually enter it in. Little bit different to firecore. Firecol is like more scraping, but this is actually like it can take actions on a browser. So, Chrome DevTools is a great one to get set up.

These are pretty much all free, by the way. Another one is Playriter. This is one I use. Same vibe as Chrome DevTools. It's just another browser for Claude to use. Chrome DevTools spins up a fresh browser. So, it doesn't have any of your sites logged in, right?

So, if you ask Claude like go send 100 LinkedIn connections to this list and it's just got Chrome DevTools. It'll pop up the browser and it'll be like LinkedIn login and it'll just get stuck.

>> Whereas, and you might log in on that browser. Yeah. But then in a week's time if you go to do the task it spins up a new browser again it doesn't have the login saved. So playrider just allows it to control your current browser

>> and that like hypothetically like that could automate like one password with filling in the passwords advanced fields for like your address where you want to ship it to stuff like that

>> on on one password real quick. That's another one I've connected one password to claude. So

>> risky business bro.

>> Yeah

>> that's a risky one.

>> Yeah it is.

>> I don't recommend that for people out there. That's that's like the last that's the last level.

>> Yeah. What happens though when it's on my computer and it's like getting a password, it pops up with the Touch ID and I have to like approve it with my finger. So

>> I stand corrected. I like that.

>> Yeah. Yeah. That that's kind of cool. I feel like Iron Man or something.

>> Someone might come for you and drop off your finger. [laughter] That's a different story. Higfield's the chosen one.

>> Higsfield's the last one. So Higfield is just like,

>> dude, they're they're dominating. They're crushing the AI content space. Like they like

>> their playbook is just like I don't know. It needs to be studied. like they they've just done an incredible job with like influencer marketing and like just they've made themselves at the name as the top place to go for like AI content like images and video.

>> Y

>> so you know

>> and that at its simplest form guys is you just prompt it and it creates images and videos for you like at its simplest form.

>> So that's a great tool in itself. Like I I have some buddies that like live in there and make some like insane AI content like UGC videos and static ads and stuff but by default Claude does not have a way to generate images. So like Chad GBT does they've got an image model whereas Claude doesn't. So this is especially one that's useful for Claude. I mean even CHBT doesn't have video generation whereas Higsfield is basically like the composio but for image models. So it basically pulls in Google's top models, CHBT's top models, like all the Chinese ones that are getting cracked as like it pulls them all in and allows you to just access them through one MCP with Claude. So to show you the Higsfield MCP in action, this is just a demo.

I don't I don't work with Bloom at all. Shout out Greg. He's

>> shout out Uncle Greg. Great episode. I don't know if it's going to be it should probably be the episode before this. Absolute legend.

>> Yeah, I had the pleasure of meeting him. He's a great dude.

>> Great.

>> So Bloom Creing Gummies. I just gave it a product image and it's like yo scrape competitors ads running in the meta ads library and generate 20 static image ads using the Higsfield MCP and then it used firecrol to scrape the meta ads library and then it's connected to meta as well. This is like an official connector that Met have released so you can get your agents to like do ads. Another great one I recommend. But the Higsfield one, right? You can see it's gone through and it started like generating static ads with Higsfield. And like these are these are pretty good.

I mean some of them it's always going to be the case with ads like it's you have to generate like a hundred and there'll be like maybe five to 10 really good ones. So you can see here it's like it's done a bunch of different static ads and like the as a as an ads background. I would run like that's a that's a that's a cool one. I mean the the gummies don't look perfect, but we could just have added an image of the actual gummies and then it would have nailed it perfectly. The like that's a great ad. The product's a little squished. That's a that's a [ __ ] phenomenal ad.

That's a great ad too. Creatine for the girls. Like you can see here, it's it can actually like use this MCP to like start creating static ads. And um this is just off a really basic prompt, but if I was trying to like automate as much of the ads process as possible, I'd build a bunch of skills around like static ads and like headline writing and copywriting and stuff, which we'll dive on soon. But that's just to show you like the Higsfield MCP and like some some use cases.

>> Love it. Guys, this episode is sponsored by Ketone IQ. I often sit down in this chair for over three hours and stay super dialed with ketones. It's a completely different category of fuel for your brain. Clean, [music] sustained, and no crash. I take a shot before recording, before deepwork, and any session that I need to be sharp. Head to ketone.com/open residency for 30% off your first subscription and a free gift with your second shipment.

That's [music] ke.com/openresidency. Guys, this is something that I use every single day. Non-negotiable. Give it a try. This episode is brought to you by Momentous. Most Americans today are walking around deficient in omega-3, vitamin D, and magnesium. Three of the most foundational things in energy, recovery, and sleep.

And even if you're already taking supplements, the industry is so loosely regulated that you really don't know what you're taking. I know the team behind Momentous personally, and that's why I trust it. Every product, every batch is third-party tested [music] for NSF, certified for sport. So, what's on the label is exactly what's in the bottle. It's why over 200 pro sports teams trust them, and why [music] my whole stack is theirs. Omega-3, vitamin D, magnesium, and creatine every single day. If you're putting real effort into your health, you want to know that it's actually working.

Go to live momentous.com. Use code openresidency for up to 35% off your first order. All right, guys. All right, so we gave you guys those six core tools that you need and then obviously some MCPs that we both like individually and as a company. Let's transition into skills. That's for the newbies out there. Just to retouch on it, it's basically SOPs for for AI.

Yeah.

>> Why don't you just dive into the playbook on how to utilize skills?

>> All right, let's do it. So, I would say skills is probably like the one of the most important things to master with all these agents. So where we're at now is we've got our like really capable new employee and we've, you know, given him all the context. He knows everything about us in the business. Now we've given him tools so we can do work. He's already now going to be great. You can now start giving him work.

He's going to do an amazing job. But we want to be able to train him on our processes and the way that we do things. So an example of skills, they're literally just you can think of them as SOPs for AI. The same way if you had a VA that was helping you with like customer support for example, you would probably have a a Google doc built out where it's like customer support triage workflow. Step one, log into monday.com. Step two, navigate to this section in Monday. Step three, find tickets.

Do you know, you would outline it really really like like simply to a VA like so it's literally foolproof so they couldn't screw it up. We're literally just taking exactly that but giving it to an agent. And instead of a Google doc, it's just a markdown file. And to illustrate like the problem that skills solve and how useful skills can be, I'm just going to give a simple example. So, let's just say you need a proposal written and you've got your tools and and and context all set up and you start a new session and you're like, "All right, create a proposal for this new client. Like, here's the price, here's the offer, blah blah blah blah. Send it off." it will give you back like a PDF and like very rare it's going to oneshot it exactly how you want.

You're probably going to have to go back and say like I don't like how you put the price at the top should be at the bottom instead. Like the logo looks a bit funky like put it in the top left. Like change the colors of the text from blue to black.

>> This is the V1 world of chat. Just back and forth, back and forth.

>> Yeah, this is still like well no this is using agents still. Like you've still got agents like I mean this applies to chat too but but I'm talking about like an agent here. Like let's say you're in code or co-work or getting it to make this proposal. You have to just explain your preferences, right? And eventually, maybe after 15, 20 minutes of back and forth, you're going to it's going to deliver this proposal that you're happy with, right? Great. You had the proposal written, but what happens in a week's time when you want to create another proposal for another client, and you start a new session, and you're like, "All right, create a proposal for this client." Now, it's it's not going to remember any of those preferences.

I mean, you you could have it save it to that memory.mmd like we did earlier, but it's it's not the right place for it. You're you're you'd be you'd be making a deacto skill. The the best place to have that is in a skill.

>> So, if you if you're starting a fresh chat and said to create the proposal, it wouldn't like remember any of those preferences and you're just going to like not you're going have to go through that whole process of explaining everything over again, which is just a pain in the ass. Whereas with skills, you would tell Claude, you know, save this proposal as like a skill. Save this process that we've just been through as a skill so I can use it again in the future. And Claude would build a proposal skill and it would save everything that that had just done. It would save like all your corrections. It would save like it would probably save the end result as a PDF into the skill as well as like a reference for it to look at. And then it packages that up nicely into into this like skill folder and saves it.

So now anytime in the future if you ask it to create you a proposal, it's just going to like whip up this SOP that it's written for itself. Literally a markdown file of step-by-step guide and then it will just follow it to a tea. And then you can basically just set like train your AI agent on exactly how you like things done and exact processes.

>> So duplicatable. And I think anybody that's advanced, I mean, how many skills do you have? I would imagine an insane amount. Yeah, we have a lot.

>> Yeah. Yeah, I've got a lot.

>> As far as this goes, like a very very easy example and we're going to dive into the different ways in which you can execute against this. Like

>> we're going to build a live skill.

>> Yeah, we're going to build a live skill guys. Like even just think like social media captions, you know, from a formatting perspective. You can say hook, body, CTA, tone of voice. You know, I like to not be, you know, so professional.

>> Those hashtags out of there.

>> Get the hashtags out of there. And then an example output you have as well too is just like yeah these are you know 10 different examples of what it looks like. And I think like the key thing to take out of this is is repeatability as well. Like you execute it and nail it one time

>> y

>> and then you're done.

>> Yeah. Pretty much. And the way you can like think of of how our really capable employee uses skills is you know I was talking about before he's got his desk and his computer. You see his apps and stuff and he's got this bookshelf next to him of SOPs essentially. and the anatomy of a skill. Let me actually open one up. I'm going to pop one open and show you what it looks like.

So, if I go into like my OS folder, which is like my folder that I do all my aentic work in, I have this hidden folder called Claude. Don't let this scare you. This is just like literally a Think of this as like Claude's settings within that project. We can just open this up and we've got this folder called skills with all my skills that live in there. And I can go into, for example, like YouTube titles is a skill I've built, right? And we can actually open this up as a folder. So, so this is the skill in its entirety.

It's a folder. And we open that up. And what's inside the folder? We've got a skill.md file. And this is literally remember like MD is just a markdown file. It's literally just a straight markdown file with my YouTube title process. And if we look at the anatomy of this skill, every skill is kind of broken into three parts.

You've got the name, description, and then contents. So the name up the top is just YouTube titles. The description is generate YouTube title options for a video topic. Use when the user says generate titles, YouTube titles or title options for my video. So you can see like this is separated from the main content by those two little lines, right? And the way you can imagine this in your head is so you've got this bookshelf that your agent has a bookshelf next to it and the books are all like stacked in, right? And on the spine of the book is just the name and description of all the skills.

So he's got like, you know, this full bookshelf. He would have like the YouTube titles with that description, maybe YouTube thumbnails along with my other hundred skills. And then when we ask Claude or our agent, yo, can you uh write some YouTube titles for this video? He's going to go look at his bookshelf and go titles. Read the description. Use when user says titles. That's probably the one.

Pull it out. Then he'll read it. And then he'll load that con like all this content in. You got to think about that example where I was showing like the the bar chart how it fills up with context. And it's already like got a little bit loaded in each session, which is your your claw. MD and your other files. And then alongside that, he's got basically loaded in all the name and descriptions of every skill that you've got, which is like probably hundreds.

and that sits in his like taking up a little bit of that of that context bar of all times.

>> But it's not like if he if he loaded in the contents of every hundreds of skills

>> that bar you wouldn't even be able to like give it a message and it'd be like 100% full. So the way that skills work, it's called like progressive disclosure without getting too nerdy. And it's basically like each of the name and descriptions just get loaded in at the start of a new session. And then when the task like requires like you know YouTube titles and he sees the YouTube titles book then it'll open that up and then it will load the full skill contents into the session window.

>> Yeah.

>> Does that make sense?

>> Yeah. And we're going to walk through that so people can kind of see it in action.

>> If if we look at this title skill, you can see that it's literally an SOP like you would write for a VA. Hey, step one, look at this. Get the topic. Find the video topic. You know, if the user gives it to you, extract it from the the folder or file name. Step two, competitor research. Use Ampify.

It's telling it to use that tool. Remember Ampify to scrape top performing videos on the same topic. Target channels. And it's given some ones that I've I wanted to to do. what to extract the video titles, the title length, the structure, use of numbers, capitalization patterns, and then it's telling it like how to use ampify. By by the way, I didn't write this skill. Claude will always build skills for you.

But you can see like this is just to illustrate is literally just a document with step-by-step guides that you're giving to your employee. And then step four, generate the title options, categories, curiosity gap, benefit first, contrarian number. And this is the skills is where you package your IP up into like by default Claude is not going to write good. If you go a new session with Claude and you're like write me YouTube titles, it's going to suck. It's like the titles are going to be like so bad, so generic.

>> Yeah,

>> you I know you've tried it.

>> I mean, dude, we're we've tried all of this stuff, too.

>> And it's like you package like I've got a way that I like my titles written that's unique to me and how I think about titles and I'm putting that IP into this skill, teaching it how to think. And the same way like if you're let's say a media buyer, if you tell Claude like can you handle my Facebook ads for me? It's it's it's not going to know the pro

>> your unique sauce. I mean, yeah,

>> you know, we talked about it before like

>> obviously there's taste and judgment and creativity that goes into kind of all these MD files and skills. Like

>> enterprise value is going to live within like what these skills and MD files are. That's such a good probing question to kind of see how deep someone is in in this space is like what does that look like? Yeah. Been looking under the hood on our side. It's [ __ ] out of control. I can only imagine what yours is. So, let's just take a step back on the skills side of like what it actually looks like to make these skills, whether you're intentional about it or kind of your LLM kind of does it for you.

What does that look like?

>> Yeah. So let's let's run through that for creating skills. In my mind, there's two ways to go into it. There's goal first or process first. So the goal first way is to literally say up front, build me a brand guidelines skill and then here's the brand guidelines PDF and it'll go and build it for you. By the way, Claude has and pretty much all of these agent harnesses should come, most of them do, with a skill creator skill built in. So it's like skill seion.

You've literally got a skill that has a step-by-step guide on how to create more skills. And that's like not one you need to download. It comes default. I know it does with Claude and most of the others as well. So, if you tell Claude like, "Hey, build me a skill for brand guidelines," he's going to look at his bookshelf and see the skill creator skill and like read it and then know what to do.

>> Insane. So, in order to make like a brand guidelines skill, which is a great one to give your agents so they can have like a just a repeatable playbook on how you do branding for your, you know, lead magnets, PDFs, websites, whatever. Trying to build that the process first way doesn't make sense. And I'll just go straight into like what the process first way is. So, you've got goal first, which is, you know, just telling it up front, build this. The process first way is the way I build 90% of my skills. And this will be like I will start a new session with Claude and I will, for example, like I'm going to demo my ad scraping skill.

So to build this what I did was I started a fresh session and I'm like okay here is the ads library link for XYZ competitor please use firecrol to scrape like their entire like ad library and download it send. And I went and did it and I was like all right and now please analyze every single one of these ads and then give me a breakdown of like these metrics the ones I care about send. I think for people too from like a macro perspective, uh top down versus bottom up is basically what this is right now. It's just how to how to look at it. Is that

>> Yeah. Yeah. Top down versus bottom up is a great way to put it's a good way to put it.

>> And then I'm like, you know, Claude, go find all the different landing pages they're running ads to and like send it off. It went and found like, yo, they're running it to these five pages. Okay, use Fire Crawl. I want you to take a screenshot of all the landing pages and build a a master doc breaking down each of the landing pages they're running the ads to. And then anyway, I went through this entire process and then I once that was done and I'm happy with it like I've taken Claude on this almost like a journey about how I want this process done then I will go like well I know I'm going to want to do this again in the future. I'll just tell Claude, okay, create a skill for this process that we've just done and call it ad scraper. And then it uses the skill creator skill and and packages it up for me.

And now I have this skill which I'm going to show you right now. It's it's absolutely insane.

>> Blow my mind. Let's do it.

>> Cool. So you can see I've got the ads analyst skill and I'm going to do a little demo here. So how this skill works, I just have to give it an ads library URL and it will go through like I said before and scrape all the ads landing pages and build me like a full report

>> under the notion that you already have it connected in your LLM like what we talked about earlier with the MCPS. It's it's it's scraping from all the

>> it's using like some of those tools like ampify and firecraw to scrape them.

>> Cool. So, this is my buddy Ollie. We're just going to scrape his

>> shout out Uncle Ollie, baby. Let's go.

>> Ollie's Ollie's a gun. He was one of the ones that got me into into content. He's an OG of the AI space.

>> Let's go.

>> All right, cool. So, include code. And I need to make sure I'm using my OS folder, which is where I pretty much do all my operations out of because that's where my skills live. And if we go into here, we can go slash and it'll bring up all the skills we have available. Hey, ads analyst. Ready? Orchestrate competitive ad research, extract ads, create a report, and we just click that ads analyst.

Literally, we just give it the ads library link. Bang. We just send it off. Go. And now that is going to start cooking away for us. So, Mark, I wasn't going to make you wait another 20 minutes for this to to run through. So, I actually ran the exact same thing earlier before with the same ads library URL ads analyst skill.

And you can see it finished up the analysis and it basically gave us a master report, a bunch of things, and it deposited it into this active folder that I have. So within my OS folder, which is literally like a folder on my desktop, it's got a bunch of like subfolders within it where I kind of just like keep things organized. And I like to have this little active folder here where I just kind of like just miscellaneous tasks that aren't really related to anything specific. It just creates a new folder to work in. So it's you can see here we've got this ad research one where it's just sort of deposited it in there and we can open that up here and it's built us a few things. It's given us a master report in markdown format which we can open and read through. You can see it looks exactly like a doc you'd see in click up or notion and we can go through as well.

So and just like

>> wow there's a linked version that links out to the individual ads.

>> Yeah. So

>> Jesus.

>> And you can see these other reports it's created. Also, by the way, it's downloaded all of the assets. So, you can see here like pretty much every single video.

>> I wonder if like in the desktop app it'll pull them up, but if we're going to show and find it, right, it's downloaded every single one of his ads.

>> Oh my god.

>> And it has done like a deep dive into them all. It's pulled out all the landing pages and it's basically, if we can open this up, I'll open that up in Claude in a sec, but it's done like the full analysis and you can see it's given us like this final report as HTML format. So, we can now just shut this up and I'll open this out so it's a bit bigger for you to see. So, you can see that it's given us this full ads strategy analysis. 54 active ads, 37 video, 14 image, the price point, the longest running ad, newest funnel 3 days ago, and you know, it's a competitor of mine, even though he's a good good buddy, but same thing in the AI space. And I can like now go through and scrape like see everything that he's doing. It's it's basically talked about like things to steal or beat.

Like what he's done well. So reframe the category to justify the price. Like he's selling like a notion template, but it's not a template. It's an operating system. So he's it's it's picked that up and it's giving that to me is a great takeaway.

>> Name your mechanism. Context engineering. So the method feels ownable. You know, longevity.

>> Yeah, I think for context, I mean, this is a long document. We can spend all day on it. It's just like you could just keep optimizing this single skill and just

>> on the skill side like you can format it however you like and obviously we're going to go through the whole entire gamut but ultimately

>> you can autonomously schedule updates on competitors like

>> you can do anything you want in relation to this.

>> I mean look I don't like the way that's formatted to be honest. So I would probably go back to Claude and this is a good point to touch on about these these skills. It's like the first time you build them the V1 of the skill is never going to be perfect. Most of my skills that I use are on like V5 to 10. So this one here is like I would then say to Claude in the chat, I hate how you've made the landing pages so like big and full screen. Like I'd like them to be, you know, smaller and better fitting on the page. And I would say just update the skill and it will go and update it for you, you know, to do anything.

And then next time you run it, skills on V2, you're not going to have that issue. And you just keep doing that until the skill like is eventually sanded down and it's perfect.

>> Keep iterating.

>> Yeah. Yeah, I mean we can go on and on about kind of reverse engineering the skills that you've already built, but I want to show everybody here and live how to actually have an idea and build a skill. We have a mutual connection here with Beehive. We both love Beehive. So, why don't we just have you from the bottom up? Let's just let's just build a skill in conjunction with Beehive.

>> Yeah. Okay. Great. So, let's let's do a one of the ideas we had was like a a subject line skill.

>> Yeah. So, it will basically write subject lines for my newsletter by looking in Beehive at what's performed the best over the last like historically and then use that to like write the subject lines. So, first up, we need to connect Beehive into Claude. So, I'm just going to show you super quick. We're just going to go to connectors. And now, I don't think that the Beehive MCP is no, it's not native into Claude. So, what we're going to do is we're just going to go to plus add custom connector and then just like close out of these advanced settings.

It's just like nothing to worry about. And we're going to name it Beehive. And then you [clears throat] need the the server URL here. And like if you have a tool you want to connect to, you can just ask Claude like, "Hey, can you set this up for me or can you help me?" And it will walk you through it. But in my case, like I already know what I'm doing here. So, I'm just going to go into Beehive into my account. We can go down to MCP and settings and they've got this URL for us to use.

And like most softwares that release their own MCP, they will have a URL exactly like this for their software.

>> Uh and additional context too guys, BHB is obviously an email platform and it was one of the first, if not the first with an MCP connector from from my knowledge. So

>> yeah, I've been using MCP. I love it. So I'm going to show you like we'll grab this and this URL. So we head back into Claude and we'll go paste and then add. And then now it's given Beehive to us as a connector. And then now let's go into like a fresh session. I'm working out of my OS folder, which I'm going to take you under the hood in there as well in a sec.

And then I'm just going to say, could you please go into notion and find my most recent newsletter? And then I haven't posted it yet. So we need to create some subject lines. I want you to then just go into Beehive with the Beehive MCP and find like all my subject lines and then pull in like all the data so you can see which ones perform the best and use that to help write like 10 new options for the most recent newsletter. Send that off. And you can see like with my prompts there's no real structure or formatting to them. It's just like plain natural language.

>> Well, that's Whisper. It obviously breaks it down and kind of

>> streamlines and optimizes the whole entire thing. Yeah, but I know like some people are like worried that they don't know how to prompt it correctly, but it's like I don't know. I feel like prompting used to be this thing people becoming less and less.

>> Yeah.

>> And guys, anything that you can think of with this beehive thing, I mean, it could do cohort analysis. We're going to do subject lines. I mean, it could look underneath the hood and see who's on your list. And if you want to say, you know, I have this cohort of operators or athletes and it can extract lists of those people. Yeah. And

>> do they even have this crazy I don't know if you're using it like the UTM tracking where you can also see like on an individual onetoone basis, this person with this email has clicked on these specific emails and like you see what percent of time they open up. You could see the source of where they came from from an attribution perspective. If

>> you're doing like lead magnets, you can then see like, oh, they came from the George Heaton lead magnet and then you could start evaluating like, okay, this lead magnet was the best lead magnet and why was it the best lead mag

>> dude, the rabbit hole is absolutely incredible on this.

>> Yeah, 100%. I've been using the Behive MCP as well for like so much stuff cuz I like have my newsletter that I write each week and it's like a big part of like what I do and and where I add value to to my audience and yeah, it's it's just so good for like subject lines like data analysis. I was getting my entire beehive list into resend to send some like like flows and stuff and it just like one click moved it in for me. Like I just said to Claude like create the recent audience from Beehive and it just like did it for me with the MCP. It's just so handy. You can see here like first kind of in its first few loops around we've said like go into notion find my most recent newsletter first and then cuz it needs subject lines to write for a newsletter, right? You kind of have a subject line for you know of an email.

Yep.

>> So it's going to do that first and it's going through the loop right now to try and find that email.

>> You can see what it's doing. Hey, while while that's cooking, I wanted to just like we can cut this in, but I wanted to show one other skill I built, but I'm going to do like a 30 second version, so it just be super quick. I just want to blow people's minds here real quick.

>> I don't know if you're ready for this one.

>> That's it. So, this is a product shoot skill. I actually built this for a buddy's company, and we have this skill. So, that the brand's like Tber Stone. So, we got like TBA product shoot is the skill I built. So I would just go literally I run t product shoot and I would just get the reference image of the product. So like this cabinet for example which can just be like iPhone images of the product and then I would run the skill pointed at the image and then it built it it would generate all of the production ready images for the for the thing.

So so this little cabinet you see here that's the reference image. That's not the final one. Look at this. That's took that one that you just saw and now it's built it out into a full like editorial thing in the same office. You can see here. Look at that. Ready?

Yeah. It's like a different angle with someone like touching it. And then it's got like a closeup of the veining on the marble

>> and basically the input output is just giving the the raw like basically CAD file and then you have a very very detailed skill that outputs whatever five or six of these things that could be like on the PDP page or something.

>> Yeah. And there's another one. This was the reference image we gave it. And then these are like what it what it built for the like editorial. Like just insane,

>> man.

>> Look at these close-up ones. Like it is so insanely detailed.

>> Yeah. And I I assume that this was filtered through the Hicksfield MCP or No.

>> Yeah. Yeah. This was done with Hickfield MCP to generate the images. And it used I think like Nano Banana Pro as the image model, which is Google's one through Hicksfield though. So that was like one of my favorite skills I've ever built. And then we'll cut back to the beehive example. Okay, cool.

Now it's pulled out like some of the patterns that win. Like you can see it's got like don't stack tool names. Your two worst lines both jammed two tools into the name. Bold stance. I plus bold stance wins. I plus boring task doesn't. I want my don't want my business to be trapped in Claude.

Got a great one. I automated meta ads in 20 minutes even though I think that's a good subject line. Didn't do so well. But you can see it's pulled the gist of them. It's got like written out some for this new newsletter that we've got. And then I can now say as well and it's see it's got that pattern as well cuz I usually put this little emoji at the start of all my subject lines. So I'm just going to say to to it now I'm going to say like great can you please build a uh subject lines skill that always goes into beehive to check the best performing latest subject lines and historic as well and then uses that data to help write the subject line for the latest newsletter.

You can see it's cooked away here. It's created the skill.md for us. And we can see that it's got the name subject lines description telling it like what to do which is going to be on like the little spine of that book.

>> And that that name the subject lines is the slash and then it's the the drop down menu and subject lines comes up.

>> Yeah. Yeah. Exactly. So I'll show you that in a second. You can see it's written this doc for itself. Hey, step one, load the tools. Step one, pull B performance data.

Step three, find the draft and the hero story in notion. Then write 10 ranked options output structure. Use this shape when giving them to the reader. It's so simple. And then we can basically like that's saved the skill to our claude folder, which I'll touch on in two sec, but let's for this example, let's tell it remember that demo folder that we built earlier where it had like our claw.md and stuff in it. Let's get the skills in there so you guys can see how this looks when we like continue building out.

>> And that's adding in like the brand voice and the stuff like that that we talked about earlier.

>> Yeah, that project. Yep. Yeah. Yeah. So I might say like could you please find the demo folder on my desktop and then I want this skill to be saved in that demo folder. Okay. So now it's saved it to our demo folder.

So I I want to just keep coming back to this example here because this is like our folder that we've been building on, right? We started with the claw.md. We added the context in the memory in. Now we can see it's created this little folder for us called the dotclaw folder.

>> Why is that dark?

>> So the and see it's got the dot in front of it. Any folders that you have a dot in front of are hidden. So if we go commandshift dot on the Mac or period, it hides it. So by default when I'm working in my in my normal project, I don't see those folders unless I run that little command shift dot command. It just hides them. I guess just for like workspace cleanliness.

>> Yep. And then that's kind of like Claude's settings. And the same way Claude like when it's loading into a session in this demo folder, it will always know to load in claw.md, it will also always check that. Claude folder as well. So quite often what I'll do in my projects is I will put all this inside the claude folder as well. So that way like I can just have that hidden and then I just have in my working folder that's kind of tucked away and I can just have my actual files that I care about. So, if we open this up, it it created this little folder called skills.

And then it's added in our subject line skill with our skill.md. So, that's in there nicely. We can open that up. And then there we go. Our name, description, and contents with the little step-by-step guide for the subject lines. And then now all like these context and skills and stuff, I just like to leave them in this doc claude folder. And then that's kind of like hidden away within the project.

>> Yeah. And just to just to tie a bow on that for, you know, for everybody out there. So it's basically you have the skill. It's the SOP on the actual structure on how you are now going to build subjects lines moving forward tapping into the MCP with Beehive for the most optimized results. And you can keep iterating and optimizing that actual skill.

>> And you can change skills too. So like my I've got a skill called YouTube publish workflow. And what that does is if you open up the skill.md it literally tells it step by step, hey step one, use the YouTube title skill. Hey, step two, use the YouTube thumbnail skill. So, you can see you've got like almost like an orchestrator skill that will like call the other skills in sequence.

>> So, he's opening up book one for YouTube workflow and then it's telling him, "All right, now you got to get these four skills and he's like, "Oh, okay." And then he goes to other books and it'll keep working. So, like you can

>> create some insane workflows. For people out there that are worried that your brain is going to be irrelevant at some point, I mean, you just touched on something that is very very relevant is like

>> the strategic mind is still very very important to understand the sequencing of how to look at things

>> because some people want thinking.

>> Yeah. Some people want to look at thumbnails before they do titles and without kind of giving it that input, it would not know that. So exactly

>> the chaining of skills that's very very interesting and that would just live in that core skill file and it just would say check this check this check this

>> just they're just separate ones I'll show you. So in my cloud folder with my OS folder I literally just have this skills here and for example the I mean that ads analyst one I ran earlier was a was a orchestrator skill. It called the ad creative analysis skill. It called the like creative strategy skill. It called a bunch of them. And then my YouTube publish workflow skill. The the the skills that it's orchestrating are not within the folder.

They're just all standalone skills. So I can just open this up and show you this skill. YouTube publish workflow. Literally says this is an orchestrator skill. Use these other four skills in sequence. You can see how simple that is.

>> Insane. I think we've been looking at a lot of folders and talking about a lot of things. I think that there's a lot for people to wrap their brain around. I'd love to kind of zoom out and kind of look at like your machine, your operating system. Talk about like folder structure and just see from a macro perspective like how everything is organized so then people can see what it looks like when you put in a [ __ ] ton of hours and kind of what the end looks like. So I'd love to just give you the floor maybe do like a live walkthrough of what everything looks like on your set.

>> 100%. So the way that I run things and this is like the the kind of way I've landed after months and months of use and trying lots of different setups. Guys, real quick. Everything that Remy is setting up, the loop, the folder structure, the entire system, he made a plugin that does it for you, built around your life and your business. It interviews you, then connects your email, your calendar, your docs, everything. I am not technical. I did it myself.

90 minutes, one sitting, done. Sign up for the newsletter below and get 50% off at launch. Enjoy the rest of the episode. I originally used to like kind of create these agents. Like I would have like really granular niche agents like id have like a you know I mean at one point I might have even had like a subject lines agent.

>> Jesus.

>> And I mean when I say agent you know a folder like I would definitely have like a you know marketing like ads folder and then I would kind of just like open up those folders to work in if that makes sense. If I was doing ads I would open up my ads folder include code and like scope it to that folder and then work out of there. But the more I I build and work, it's like it's just such an annoying, inefficient way to have things. I just run everything out of this OS folder. And some reason as humans, we love to like give these agents like treat them like humans, you know, give them human names and like give them like roles and things.

>> Marty, we got we got Marty.

>> Marty. Yeah, exactly. Like people people for some reason they they want to have like a head of marketing agent, all this stuff. And it's also what gets lots of clicks and views on Instagram, you know? People go like, "I've got my team of agents doing this." And it's like really, they're just folders. And the more folders you have and more specialized, the more like different stuff there is to worry about. And the models are just so smart now that I just run everything out of the OS folder.

And then I build really really good skills to teach it the processes. And this is my OS folder here, right? So I have all of my like this is all my stuff for my like, you know, education, consulting. This is stuff for for comfort work I'm doing there. And this is just another like thing just for some notes and stuff. And

>> so so let's take a step back. So if somebody's looking at this and they want to look at their folder structure, let's just say for example for me like I would have iconic and I would have open residency. Like these are the big pillars in which I want to work in.

>> 100%. Yeah. So you got exactly right. So you can see like my my folder structure is literally like I've got like my overarching OS folder. OS just stands for operating system. And then I have, you know, any like big any businesses or pillars. So yeah, for you iconic and open residency.

You might even have another one for like you might have a folder just called personal for like your health stuff that you wanted to do.

>> Yeah.

>> And I've got another one that I like to have. I just have a folder called active which is just like oneoff projects and experiments that don't really fit into like one of the pillars.

>> And if potentially it becomes something substantial, maybe you'd move it into one of those other

>> core folders. So for like I created a folder for this podcast to prep and I just added it's just sitting in the active folder. It's loose. It's just like a separate project that I'm working on. And then within these like overarching pillars then I'll have like the folders within like content, newsletter, website. So for example in my real OS folder you can see here AOS bromy we go in and I've got like content finance legal newsletter website marketing and I used to open claude so I would in the past have let's just say I wanted to work on marketing what I would have done is I would have opened up the marketing folder and then started working in there for all my marketing stuff

>> and what's the right way to do it

>> I mean there is no right or wrong way but I I the reason I was doing that and my thought process was then it's like we're scoping the agent to just marketing work but they're so like the agents are so smart the models are so good and their context windows which is like the bar chart like how much you can fit in it is just getting bigger and bigger that I just run everything out of my OS folder

>> that's under the notion that the OS is very macro and it's going to pick up all the stuff underneath it as opposed to going granular

>> and what I would do right so let's just say like for my new like a newsletter or marketing let's say we're creating a new batch of ads I would sort of have OS folder open working. And then I like to just go like this. I would tag the folder. You can tag folders. And then I would go, you know, AI with Remy slash marketing. See, it's got the marketing folder.

>> I mean, there has to be some muscle memory in there and knowing what your kind of, you know, folder structure is. I would love for you to walk through right there just the ads, the slashes, like what are all those kind of like quick shortcuts that people can do to tap in there? I mean it's going to be slightly different depending on what harness you're in, but most of them like codeex cloud code pretty much all of them use a slash command and an at symbol type system. So slash command just brings up all your skills and like commands available to run. As you can see, we've got a lot and but it also just brings up like settings that are baked into claude. Like for example, if I want to change the model, the LLM, the brain behind this loop, I can click do /mod and then it's going to bring it up there. And for context too for people, I just want to double click on everything to give people 100% clarity on stuff too.

If you're going to slash skill, is that like tag teaming it in? What happens if you don't tag team it in? Is it going to automatically tap into the skill with its own brain or do you have to be very intentional in making sure that you're tapping in the skill?

>> Sometimes I'm intentional. If I say, "Write me a a hook for my Instagram video," and I've got a hook skill, it's just it's going to pick it up.

>> Yeah. But like for example the ads analyst one if I just dumped in the ads library link and ran it would be like what the [ __ ] do I do with this?

>> So naming conventions are important but obviously like really having muscle memory in what your folder structure is so you know when to tap into certain it's basically just like you have 50 employees you should know the names of your employees.

>> Yeah. Yeah. Yeah. Yeah. Exactly. Same thing. I mean like I've got a pretty big setup and it's not that hard to like work it out.

Like I mean even so like slash commands is for your skills and like other little setting stuff mainly skills but the ats I find is like when you want to tag files or or folders so like or documents you know for example um

>> and should that be under the notion that if you tag in a folder it is going to pick up all of the files within that folder.

>> Yeah. Yeah. So you know I I wouldn't even really have to remember I think if I just go at marketing right I want to do marketing it brings up straight away my marketing folder. Hey, with Remy Marketing, I can select that. And now if I give it my task for marketing like write me 10 new ads for my upcoming workshop. Then you will see what it will do is it will then start to like use that folder to work in but without us having to actually open that folder up to work in. Does that make sense?

>> Yeah. You're you're basically uploading the OS folder, which is macro, and it's getting everything under it, but then you're tag teaming in the marketing folder to take like an extra good look at the marketing folder.

>> Yeah, that's exactly

>> I don't know if I explained that good for you guys out there, but I think it's uh I'm I'm trying to make this at a fifth grade level so people could really understand it. It's just like, hey, go check this folder. It's probably where it is.

>> I mean, that's like that's that's what I meant about demystifying this all. It's like you hear like people make Instagram videos and it's like my like my marketing agent just did XYZ while I was asleep overnight just worked all night and it's like if if you don't understand this you're like oh like wow this is crazy but in reality they've I I guarantee you they have a folder called like marketing and they have some skills in there that are marketing related and they're running those skills on some kind of schedule. So it's like hey every night do a report on Facebook ads and email it to me so I wake up to a report. So so simple. It's just folder skills, schedule tasks, and then but people like take that and I don't know whether it's an ego thing cuz they they like to sound smart and sound cool or whether they're pushing some course and that they want you to think they're like some AI god, but in reality it's like just as simple as a skill and a folder and a schedule task. But people will say, I've got like 50 agents working for me overnight.

>> And that could be anything. It could literally be clean the inbox. You can say draft draft email responses,

>> send cold emails or like send LinkedIn connections, you know,

>> suggest emails that you want to unsubscribe to if you haven't opened up the last three, four times.

>> Yeah. So, it's like, you know, now if I set this up and click create, now I've got an agent that is managing my email inbox for me.

>> Insane.

>> It's it's it's a lot simpler than you think. The last sort of concept that goes really handinhand with this sort of folder structure I'm outlining is you have context tools and skills you can have them at a global versus a project level. The easiest way to think of global is like a holding company and then the project level is like the sub companies which is kind of like how I have my setup and you know things at a at a OS level like a global or a holding company level are things that apply to like every single company. So, if you're looking at this holding company example, you might have like context, tools, and skills that apply to like all of your companies. And then you might have some things that only apply to really really specific companies. So, I have like skills that live at a global level, which I can access anywhere. And I also have like skills that exist just within a folder.

Like remember that one I showed you before with the product shoot, TA product shoot? that skill I've got kept in the folder for the tea stuff cuz like I'm never going to use that skill outside of that specific folder.

>> It's so crazy cuz this is really just like this whole thing. It's a personal OS but it's really just a holding company. The whole entire infrastructure of the folders is like a holding company.

>> Yeah. Yeah. Exactly. That's that's exactly the way to think about it. So another example of like global versus project or holding company versus company specific is our claw.md. You remember that?

>> Yeah. So, I have one that I have in my OS folder, my global claw.md that I want to apply to like every single session I'm in, but I have a claw.md in some of these sub projects. Like, I'll give you an example right here. I'll open up the folders. So, I'm in my OS folder right now, like my real one, and you can see that my like, you know, in my I guess you call like your settings folder. I have got my my claw. Mmd, my global one for my OS folder.

And this one here contains like overall preferences about myself, you know, explains like who I am as a non-technical founder learning. That's not going to change no matter what project I work in. I'm always going to be the nontechnical founder who's learning. So, I want that applied everywhere. I've got in here, these are loads of lessons that I've built up over months of use.

>> I've got I saw in there like core principles, core values. That's a great thing.

>> This is one I have as well. Boil the ocean. The marginal cost of completeness is near zero. basically just tells like the agent the standard isn't good enough. It's holy [ __ ] that's done. Like just little things like that, right? And I want that applying to every session.

But for example, when I was prepping for the podcast, I created this little podcast folder called

>> podcasts

>> podcasts, right? And then in here, this is where I was just like workshopping and planning everything, right? You can see a bunch of files. This is just like a big like work workspace essentially. But you can see within the podcast folder, I've got a claude. MD. And if we open that up, that just contains like the Northstar context for the podcasts folder.

>> Yeah. So it's it's it's going to be filtered through the macro cloud folder for like your principles and how you think. And then this is more like rubric and outline. Yeah.

>> So it's simple, right? This workspace is Rey's base for podcast appearances. What this folder is for prep, demos, diagrams, post episode analysis. That's literally all it is. And then I just have some other folders in here where I was working on stuff. But now when I'm opening up Claude to work, I am still working out of the OS folder and I would tag podcasts. Let's say I wanted to prep for this pod.

I would tag podcasts and then I would give it my task and it be like what's the outline for the open residency podcast. Even if I didn't tag podcast the folder, it would still go and find it. But I just like to do it for nice like cleanliness and peace of mind just to make sure. And you can see here it's opening it up. And

>> just to to rebutton down for everybody out there listening, you brought in the OS folder. So it's getting the macro claw and all the stuff there. And now you're tapping in the skill of podcast and it's picking up the claw MD file within there and anything and everything y around there.

>> And and like now it's loaded in the claw. MD from the podcast folder. So you're kind of like stacking them on top of each other.

>> Yep. And you can see he's whipped up our our episode plan here, which is which is super cool. But that's just giving you an example of like global versus project level or holding company versus company level CLMD's skills and tools.

>> Amazing. Amazing context there. I'd love to just shoot for my own selfish reasons and I think for a lot of people out there, they probably are interested in this as well. just like something that I've been working on and just how would you kind of construct it on a a global versus project level is like me I'm like on a health journey let's just say I have my DEXA scan my blood work maybe I'm tracking my macros this whole entire flywheel of all these kind of touch points maybe I have my aura sleep score which has an MCP and can bring it in maybe eight sleep

>> and and can bring it in like how would you architect that global verse project and then like just give me your your thoughts on that

>> yeah so I would have my I guess holding company OS folder. Yep.

>> And then, you know, you might have you'd have a folder within that for like open residency, another one for iconic. And then I'd probably have another folder because it's a big pillar in your life like personal.

>> And then within personal, I'd probably have a folder called like health. And then I would just in that health folder, I would then just dump in all that stuff, everything. Just dump it in like Dexter scans, whatever. Just just dump it in there. And then I would just create a claw.md just for the health folder. And I would basically just say something along the lines of this is my health workspace where I'm going to be, you know, analyzing blood work and doing this and doing that. You might even then give it like your health goals and put it in the claw.

MD just any context that your agent might need when it's like when you want to work on health stuff.

>> Yeah.

>> And then that's literally it.

>> Yeah. I think like again to kind of take it a step further, something that I'm working on now is just like, okay, you have your separate vendors. Maybe it takes X amount of time to book an appointment to go get your blood work, go get your DEXA scan. You know, maybe this is your preferred vendor to get the DEXA scan. You have your Gmail linked up. Yeah,

>> it knows every seven weeks to email the DEXA scan place to set up a DEXA scan so you stay on target and keep updating it. So, yeah,

>> there's a lot of ways that's something I'm working on. I'm super super excited about to get the reminders and automate the the different appointments.

>> Yeah, I know a few guys that have like done crazy stuff with like health and blood work with claw code and and agents.

>> Yeah,

>> for me it's simple because it's just like I saw my blood work that like I have to work on saturated fats and sugars and like

>> I just now work through the lens of what food do I eat and is it bad and obviously calories and protein etc. but like what does it look like on those kind of two realms.

>> Yeah,

>> amazing. definitely will be talking about that kind of health whole entire flywheel that I'm setting up. I think a lot of people would be interested in that. What is like the honest kind of like monthly cost of doing all of this? Obviously, you talked about, you know, the $100, maybe $200 a month if you want to get the bigger plan on your core LLM. How much are you spending a month on kind of everything? everything all up about a I mean about a thousand a month but that's across like loads of tools and you know I'm it's my job to be on top of this.

I'm I'm testing stuff. I got subscriptions I forgot about from months ago. Like I'm Yeah, I know my bills about a thousand bucks for AI stuff.

>> You need to set up a skill to cancel the subscriptions that you're not using. Bro, come on. Come on, man. Come on, dude.

>> Killing a schedule. I should have one once a month that goes to my email receipts and and notifies me. I should

>> the email unsubscribe thing is is a game changer. Yeah. So for people out there listening so

>> $12,000 for basically a year for I don't know 100 employees.

>> I mean I think it's it's it's a little bit interesting because all of these big AI companies right now like OpenAI, Anthropic, they're all like none of them are profitable. I mean maybe Anthropic just got profitable. I have no idea.

>> You have to confirm. None of them are profitable. I don't know if you knew that that they are all running at massive losses because you know the they on these plans you're buying like the free plan, the pro plan, the the $30 $100 a month plan, they're heavily subsidizing the real compute cost of of like the AI usage, right? So, I think on a $300 a month Claude plan, you are actually getting about $6,000 worth of token usage, but they are subsidizing it so heavily because they're all trying to get users. They're just trying to capture mass market share. And Anthropic are like really now making a push to IPO and become profitable. They're starting to like they've kept their prices the same, but your usage is going down and down and down, getting squeezed.

They've just released their latest model. I know like maybe if you're watching this it's something new but they've just released Fable 5 and they've essentially said like this is our new most powerful model

>> it's not not included in your plan. You have to pay the real cost of it which is like

>> disgustingly high.

>> That's a great that's a great uh new rev for them to print. I'm sure they're charging some sort of markup on it but that's like

>> for anybody that really wants the best model they're going to pay for it. I feel like people are going to run that up.

>> Yeah. So, it'd be interesting to see what happens over the next sort of year or two as these companies like they can't keep running at a loss forever. They're going to have to start to bring the costs up. So, it'll be interesting to see what happens. I think there's going to be a massive market for like open source models, basically models you can run yourself. You can buy like, you know, couple Mac minis and and run your own AI models on there. I think there'll there'll always be options for like lowerc cost AI.

There always will be, but it just be interesting to see these big companies like what happens with the price of like your your plans.

>> I completely agree. We've only talked, you know, I mentioned the Kia. I I think that there's only Lamborghinis and Range Rovers right now. Eventually, there's going to be some Kia and Hondas and all that is going to come.

>> There's a few.

>> There's going to be a lot more options I feel like on the lower end. I don't know how they're going to figure it out, but definitely will be. Before we move on to the next thing from a a folder structure perspective and you know global versus project anything else big that you want to touch on there or do you want to move on?

>> That is pretty much like all you need to know and you know I wouldn't get like ke up about having like the perfect folder structure. It grows with you over time. Just start out with with create a folder called OS. That's that's your first step and then just you know create your CLM day add the context in and those subfolders and like you know holding like companies within there that'll just come over time as you start to do real work like I wouldn't go out and like try and get the perfect structure. I wouldn't let that hold you up from just starting and and getting work done with these agents.

>> Just start the two layers of AI and business. I'd love to kind of walk through your thesis on the different layers and how you look at it specifically from a business perspective.

>> So the way I see it right now, you almost have like two layers of AI within within the business, right? It's like you have your personal operating system, which is pretty much everything that we've covered today. This in my mind is like an extension of you. It's like you're going to become like an AI augmented founder. Like the the the way I think of it is like imagine a dude with like a robot arm. It's like an extension of of him and now he can like climb walls with his arm and do all this crazy stuff. And that's like this is your personal operating system, personal AIOS is kind of where you live in every day.

This is like this claude code thing I'm setting up with these folders where I now complete my entire workday from within there. And you know that kind of handles all my tasks and my grunt work. But if you think big picture, let's just say you wanted to have an agent that managed your customer service or customer support, the it would be the wrong place to have that on your computer as the founder or you know your customer support team. Like it probably wouldn't be make the most sense for them to have that on their computers. you kind of like that that's where this second layer comes in which I call it more like your AI business infrastructure and that's like that's where some of those other agent frameworks like Hermes and Open Claw really come into play

>> more advanced frameworks and they're the kind of things like that's why everyone was running Mac minis are flying off the shelves because people just wanted like a computer that was not theirs almost like a company Mac Mini to set some of these agents up to run on and but if you if you look under the hood at these agents so right now Like I just remote accessed into my Mac Mini that I have at home. And you can see here I've got like a a Hermes agent set up and this is like the file system you're looking at right now is not on my laptop. This is the files on my Mac Mini at home. And you can see

>> this is remote. This is like the cloud.

>> Yeah. Yeah.

>> So just like I have the OS folder that I work out of, the the Hermes agent is literally just a folder as well. See Hermes?

>> Yep.

>> We open that up.

>> Yep. It's just like a bunch of folders and markdown files, you know, like a soul.md which tells it how to behave like all the same principles that we have just gone through today. So when you eventually decide you want to like graduate to start using like something like an openclaw or a Hermes agent for different stuff to if you want to configure these agents properly, still the same thing context tool skills, nothing changes. It's just like they're just slightly more advanced frameworks that you that work better to run like more autonomously on another machine if that makes sense.

>> Yeah, I feel like there's a huge opportunity for I think first steps is to become acclimated and understand the tools and do your own kind of personal OS. But it begs to ask like you know the question that everybody's asking next is like okay who owns those files? That's for the individual person. Is it for the person? Is it for the role in the company? And then is there like a separate infrastructure for a company? Like how is there, you know, someone works for a company, they're setting up all of these skills.

Then what happens if they leave the company? Where do the skills go?

>> Yeah, it it's like because this is so new. It's so messy right now. Like it's really this is all really simple at a personal level, right? Like you build skills, you connect your tools, you have your folders, and they just live on your computer where you work. It's simple. But yeah, it it it does start to get messy when you for example like trying to work with a team and you know someone builds like a stock forecasting skill and then now you know another team member wants to use it but it's on their computer and it's like well how do you give it your team member access? Oh well you could airdrop them the file but then you've got two separate copies and they're going to get out of sync fast if people are like making updates to them.

So to answer your question like that there's there's a few ways you can kind of bootleg it with like tools like GitHub and and Google Drive and stuff, but there's no like real clean simple way that I've found yet to to effectively like manage skills across like team members and companies.

>> There's a massive opportunity for somebody out there to create the technology that has that connective tissue where it kind of auto updates and it can share. For sure. There are some startups I've seen that are now starting to solve this with like shared skill management and there's a there are a few coming out now and I need to just sort of get my hands a bit dirty in that area of things but uh yeah in terms of like skill ownership like skills like assets for your company so it's it's a whole another conversation as to whether like I think every employee needs to be the ones building them because you know they do the task the best like they need to build the skills but then it's like if they're assets for the company are you going to just let them walk away with the skills bills when they leave or do you as a company own them? It's a difficult one. I can't say.

>> Yeah. I feel like at a macro level like the you know the clawed MD file like that should be macro and uniform the stuff that doesn't change that we talked about like that should be kind of across the whole entire company as like the core input in whatever folder they're working in for the company. Yeah. But then once you start kind of going downstream on the skills I mean that's where like creativity and taste and like how you prefer things to be done. like some people, you know, want to work in X program, other people want to work in in this program. Some people, you know, need it in copy. Some people need it, you know, are a visual person.

So, I feel like that's

>> it is very tailored toward the individual human.

>> Yeah, agreed. But, you know, I wouldn't get too ke if you're just starting, you know, just start just like build your own skills first and then worry about all the team management and other stuff like later. It's just cross that bridge when you're at it.

>> Yeah. If you're out there listening, if you do even 10% of what we talked about today, you're in the 0.0000 1% of people that have graduated from chat uh everything else

>> past that. So

>> yeah, I think uh that's for another day that kind of that layer two with the open claw and and the themes and such.

>> I mean, one other thing I wanted to touch on too is like every company right now needs to like push to become AI native. Like every company needs to like put AI at the forefront of like all their operations or they're going to lose to a company that does. It's like simple as that. And like I've kind of been trying to solve some of these problems for companies I work with about the best way to go about doing this. And there's two ways to go about it. And I and I and I think that one way is more correct than the other. So the first way is like you go top down, right?

like you bring in some AI specialists into the company to like start building stuff and you know they like they can go and interview each department and sit with the employees and like try and build skills on their behalf or try and like build agents to take roles but it's like the employees the people that do those tasks they know it so well in and out and there's so much nuance to every task and if you wanted to bring AI specialists in to start automating this stuff they would need to understand so deeply every task that everyone in the entire company does they can never do that. So you either need a lot of people you need almost need like one per one AI specialist for each employee if you're trying to go the top down route where you build it and hand it to them and say here use it. I think the best way to get your company AI native is to get your employees trained up to be AI literate get them building their own personal operating system so then you can the goal is not to like fire your entire team. You want to keep your best people, train them so they can become like 100x employees. And then you can go on hiring freeze and continue to grow without scaling a headcount. And the way you can start to automate it is you instead of from the top down, you automate it from the bottom up. So you train your employees to become AIT.

You get them to automate their own job essentially. And then you eventually like have this like you if you can think of like a a graph where it's getting like saturated, you know, the AI saturated

>> infiltrates the whole entire company. Everyone's

>> Exactly. That's probably like the best way to go about like trying to get your company Aative and there's all sorts of things there that I think work well like putting incentives around it. Like you can do like build weeks and competitions, you know, like running

>> good idea

>> things like you know best like skill of the month. Maybe you get your employees to start building skills and then it's like the best one wins like a cash prize $1,000. Like I think companies need to like just make AI like part of their culture. they need to have an AI call each week where people like sharing about what they've built and like really start to like bring that in as part of the company culture.

>> I think it's a double-edged sword cuz some people, you know, the more they adopt, they feel like that they're digging their own grave to be fired. And that lens, you know, you have to talk about like what are actually skills that are going to do well in the new economy. I would disagree though on going two only. I would probably go a mix of path one and two. Like for me with iconic like I had like a a six-page document that it was let's just say 60% of it was uniform in nature of like asking all the appropriate questions like what do you you know what tools do you use? What are the processes that you already have? What are your bottlenecks?

>> And then you're right that other 40% was 100% tailored to that specific

>> employee. Yeah. But with that being said, it's very tough like someone that's coming from the outside, they have to be

>> very very versed in business to be able to pick up context fast or else it's going to take a very very long time. But I think

>> that's the first thing that every operator out there should do should be like the download of just like

>> what AI tools do you use? And right away you're going to get a pulse check on like where everybody's at. Yeah. And like just seeing that for my whole entire team, like that was a big shot in the arm to be like, "Wow, we got to like [ __ ] hurry up on this [ __ ] because with one, you will go faster. If you do just two, it's going to be slow." I think it's a mix between one and two.

>> Yeah, I would agree with that. I would agree with that 100%.

>> All right, this has been an amazing episode. Computers are down. Let's get into quick strike. Random questions. We're just going to rip off.

>> Let's go.

>> Give me what you're thinking. So, first skill everyone should build.

>> Email inbox triage skill. Run that bad boy on a schedule three times a day.

>> Clean your brain.

>> Sorted.

>> Too much noise. Biggest beginner mistake you see in AI.

>> People being too perfectionist and too scared to start cuz they like don't want to screw something up. Like one of my buddies will shout if you're listening. They're like we want to use claw but like we're scared to even like type a prompt and we don't want to screw it up. And it's like you know cuz people kind of think see it as a black box. I don't know what's going on under the hood. But it's like just the biggest being mistake is just being too kind of scared to start so you don't like screw things up and trying to be too perfectionist about the whole thing.

>> Ladies and gentlemen, if you had made it this far and you don't take action, you are a loser. One thing you automated this week most people would never think to.

>> My laundry.

>> That's that's kind of crazy. Most overrated AI tool right now.

>> I'd say any AI app builders. lovable vault any of those and you just just do it in Claude like just create a new I say like just create a new project folder with your holding company call it website or app or whatever and then just start getting called to build it out in there it's like

>> is not going to be signing with lovable anytime soon most underrated AI tool right now

>> composio how long until a total beginner feels the productivity gain like realistically

>> a few days a few is

>> the task you'll never let an agent touch?

>> Thinking and phone sales. [ __ ] AI voice sales agents.

>> One MCP connection that changed the game for you.

>> I'd say connecting Ampify with all the thousands of online scrapers. You can pretty much get anything.

>> Finish the sentence. In two years, every founder will have a personal AI operating system. What is Obsidian and is it still relevant today?

>> Obsidian is just a simple note-taking app that uses markdown which is the love language of AI. The agents love it as we covered earlier and a lot of people kind of build out their like I guess second brains or like that you know context folder that we built earlier. people just build like essentially a a version of that context folder but with hundreds or thousands of markdown files and they just use obsidian as kind of like the the layer to manage that I guess and I just think um I don't think it has its place. It's really good for like solo operators but as soon as you're trying to like have a setup where you want your company company and team members to access

>> too

>> those files too it's messy. I don't think it's needed especially for beginners. What is one skill that's changed the game for you?

>> The Claude council skill. So, I found this by a guy called Ollie Leman on Twitter. And it's actually like my most viral video on Instagram talking about that skill. And you know, if you ask Claude for advice on something, if you say like, "Hey, why is this a good idea?" It's going to give you like a perfectly structured case as to why it is. And if you say like, "Why is this a bad idea?" It'll give you the same kind of case for why it's bad. And you know, why you can't trust Claude with decision-m. So this skill essentially spins up a bunch of different clawed sessions all given their own persona like a contrarian that's going to hunt for what goes wrong like an optimist five different complete personas to basically like give their thoughts on your question and then it gives it shuffles up their answers anonymously gives it to five fresh sessions that are like the peer reviewing agents to like give their thoughts on those answers and then finally it gives it into one new session which is like the chairman that like looks at all the final results and gives you the final verdict.

I use it a lot for like decision making cuz it's just interesting to get like an extra perspective on it. I'll use it all the time but like hey should we add this feature or is it too soon or it's like what should I work on next on the project?

>> Sounds amazing. Before I get into the last couple questions that I ask everybody I'd love to just kind of recap and end with like where should someone out there just start?

>> Yeah. So think of this entire system as like something it it it grows with you and it will continue to grow and compound. And you just need to start by planting the seed. Just get your computer right now, create that folder, the holding company folder OS, start getting your context files built. Just open a fresh claw or chat GBT session and just say like help me build, you know, a bunch of markdown context files. We need like an about me, an ideal customer profile, a product, services information, uh you know, brand voice, and then interview me to extract all the answers from my brain and and build these documents. And then you add them into the folder and start.

Here's the big thing. Connect your tools as well. That's actually could even be the first step. Cool. Tools and context you can get done in a few hours. And then from there, your goal is going to be to complete an entire workday from with inside Claude, whatever harness you're going to use. That's your first goal.

And you know, it might be a little bit messy at the start, but you're going to then start to build skills. It's like if as soon as you go through a process with Claude like we did with the subject line skill, if you ask Claude to take a task off your plate and you know that you're going to have to ask that him to do that task again in in the near future or at least one or two more times, tell it to make a skill and then that's the place to start. You just start growing this system and you can only do that through like working with it. So get your your context files built, get that folder set up and your tools connected and just start completing a workday from with inside your your agent harness. He's challenged you. Let's do it, guys. Last three questions.

Favorite book or podcast and why?

>> My favorite book is The Alchemist. I don't know if you've read it.

>> Polo Quello. I'm Brazilian, bro. Of course I do.

>> Dude, I love that book. I've read it like four times.

>> That's interesting.

>> Yeah.

>> What about podcast? You a podcast guy?

>> Yeah, I'm a podcast guy. I like the My First Million podcast.

>> Good guys.

>> And the Open Residenc.

>> They're guns, dude. They inspired me to start doing the newsletter. Like they they both crushed it with newsletters.

>> Yeah. On the newsletter side. They're with Beehive as well, too.

>> Yeah. Yeah. They they they've both exited their newsletters for like tens of millions, right?

>> Yep. Sam on the hustle and then Sean on Milk Road, the crypto one.

>> That was a quick one, too. Entrepreneur or brand that you want to give flowers to and why?

>> Brand Composio. Dude, they're so good. Love Composio.

>> I had never heard of Composeio until today. We most definitely are going to put that on steroids and put that on everything. So, I'm with you on that. What about a creator you want to give flowers to and why?

>> Good question. Do you know Ask Cat GPT?

>> Yeah,

>> she's a beast, dude. Like inspired me to start creating content and yeah, she's a she's a beast at content and AI. Big inspiration for me.

>> Love it, man. I hope everybody enjoyed this episode for the first time ever in Open Residency podcast history. I'm going to ask the Pay It Forward, guys. Share this with someone that you care about. Get people started in this game. This is definitely the most thorough. but we took a long time to really kind of orchestrate and outline what we're going to talk about.

So, I hope you guys enjoyed it. And u we are going to put a [ __ ] ton of links and PDFs and tons of stuff down below in the description. And this definitely won't be the last time that we do stuff with Remy. So, I appreciate all you guys. I appreciate you, man. It's been an amazing day. Thank you for having me on.

I've I've enjoyed it. I think like this is just the crash course that everyone needs. Like if if you're starting from zero, like this is just all you need, just this episode and I think you're set. So, I'm glad we got it.

>> Amazing. Thank you guys so much for watching. If you got value out of this episode, every [music] single principle, framework, tactic is in one free playbook linked at the top of the description. Grab it, hit subscribe, and we'll see you in the next
