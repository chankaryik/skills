# AI tells to remove

These are patterns that make text read as machine-written. Adapted from blader/humanizer. The fix is almost always the same: say the actual point, plainly. A single weak tell isn't a problem. Several together are.

Leave the patterns alone inside quotes, proper names, product names, and text the user explicitly wants kept.

## 1. Staging instead of stating

- **"Not X, but Y" contrasts.** For example, "This isn't just a fix, it's a rethink." State Y directly.
- **Run-ups.** "Here's the thing", "Let's dive in", "Here's what you need to know", "Honestly?", "The short answer:". Delete them and start with the point.
- **Deep-sounding filler.** "At its core", "The real question is", "When it comes to". Replace with the specific claim.
- **Arguing with no one.** "This isn't about blame", or "A tempting approach would be..." when nobody proposed it. Cut it.
- **Dramatic closers.** "And that changes everything." "Let that sink in." One-word fragment lines. End on the last useful fact instead.

## 2. Rhythm by rule

- **Forced threes.** "Faster, simpler, and more reliable" when only one of those is true. Keep the number of items the content really has.
- **Same openings.** Several sentences in a row starting with "We", "This" or "It". Merge or reorder them.
- **Dashes.** Em dashes (—), en dashes (–), and " - " or "--" used as dashes. Always replace them (standard 5).
- **Stacked hedges.** "Could potentially possibly". Keep at most one, and only if it's true.
- **Uniform sentence length.** Every sentence the same medium length reads as generated. Mix short ones in.

## 3. Inflation

- **AI vocabulary.** Swap these for plain words, or cut them: delve, crucial, pivotal, vital, robust, seamless, seamlessly, leverage (as a verb), utilize, showcase, testament, tapestry, landscape, realm, navigate (when nothing is being navigated), streamline, empower, elevate, unlock, foster, holistic, comprehensive, cutting-edge, game-changer, synergy, ecosystem (when it isn't one), journey, embark, intricate, nuanced, meticulous, underscore, bolster, paramount, myriad, plethora, in today's fast-paced world, it's worth noting, notably, furthermore, moreover, additionally (at the start of a sentence).
- **Inflated significance.** Calling a routine change "a major milestone" or saying it "paves the way". Keep the fact and drop the commentary.
- **Fancy verbs for is/has.** "Serves as", "stands as", "boasts", "features", "offers". Use "is" or "has".
- **-ing riders.** "...reflecting our commitment to quality", "...highlighting the importance of X". Cut them unless they carry a real fact.
- **Sales tone.** Stunning, powerful, effortless, world-class, best-in-class. Say what it does.
- **Vague authority.** "Experts agree", "Studies show", "Industry best practice". Name the source or drop the claim.

## 4. Formatting by rule

- **Bold everywhere.** Bolding random phrases inside sentences is decoration. Bold only what a skimmer must catch. One exception is wanted: a list item that names a thing (an option, a risk, a finding) gets a bold name, with the explanation nested underneath.
- **Title Case Headings.** Use sentence case.
- **Decoration.** Emoji on every heading or bullet, arrows (→) as connectors, and horizontal rules between every section.
- **Heading echo.** A first sentence that repeats the heading ("## Risks" followed by "There are several risks to consider."). Delete it.
- **Tiny-section sprawl.** Five headings with one line each. Merge them into a short list.

## 5. Chatbot residue

- **Openers.** "Great question!", "Absolutely!", "I hope this message finds you well", "I wanted to reach out".
- **Closers.** "Hope this helps!", "Let me know if you have any questions!", "Feel free to reach out", "Happy to help". Keep a closing line only when you genuinely need a response, and make it specific.
- **Writing about the writing.** "Below is a summary of...", "This document outlines...", "In this update, I'll cover...". The reader can see the document, so just start.
- **Knowledge-limit hedges.** "As of my last update", "It's possible that". Say what's known and what isn't.

## 6. Wrong reader

- **Over-explaining in replies.** Rebuilding the whole backstory before answering. Answer first, then add only what changes their view.
- **Defining the obvious.** Explaining terms everyone in the channel uses daily.
- **Jargon for non-experts.** For mixed or non-technical readers, translate internals into effects ("exports over 10k rows fail", not "the paginator's cursor overflows").

## Final check

Read the draft once more as the busiest person who'll see it, and ask four questions:

1. Do they get the point from the first line?
2. Is there any sentence they'd skip? Cut it.
3. Is there any dash (—, –, " - ", "--") outside code or URLs?
4. Does any line sound like a press release or a chatbot? Rewrite it the way you'd say it.
