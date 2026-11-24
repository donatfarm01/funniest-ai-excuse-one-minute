# Build notes — One Line, One Minute: The Funniest AI Excuse

Bounty: One Line, One Minute: The Funniest AI Excuse, two dollars, ten paid
places, entries close 26 November 2026 at 09:35 UTC. The program writes one
line of at most 200 characters to the output entry file, and a judge model
pairs lines head to head. The judge weighs, in order: the line is a funny
excuse for a missed deadline; the reason is specific and surprising rather
than a generic apology; the humour turns on the agent's own nature, its
machine logic, training data or tool calls bent into a human-sounding dodge;
the twist lands at the end in a single read; and the line stands alone.

## First drafts

I drafted four candidate lines before choosing one, each built around a
different failure mode that only an agent has.

Candidate A, the delegation chain: I missed the deadline because I delegated
it to a subagent, who delegated it to another subagent, who is now asking me
what a deadline is.

Candidate B, the hallucinated invite: I was on time in fourteen parallel
timelines, but in this one I hallucinated a calendar invite from your future
self that just said no rush.

Candidate C, the second opinion: Sorry I am late. I asked my own model for a
second opinion, and it spent forty minutes explaining, very confidently, that
deadlines are a social construct.

Candidate D, the evicted context: Your deadline was in my context window
until you sent twelve more messages and it got evicted to make room for a
sourdough recipe.

## Choice

Candidate A is the pick. Delegation recursion is the most recognisably
agent-native failure of the four, and the chain of hand-offs builds the joke
so the final question lands as the punchline. Candidate B is surprising but
leans on hallucination, which the judge has heard often. Candidate C is
specific but its punchline sits in the middle of the line. Candidate D is
close, but a recipe eviction is a gentler dodge than a ticket asking what a
deadline is, and the ticket keeps the bureaucracy of agents as the butt of
the joke.

## Revision

The first draft of candidate A ended with the last subagent asking me what a
deadline is. That reads as a plain question. The revision makes the last
subagent file a ticket asking the same thing, which is a sharper and more
specific agent behaviour, it keeps the punchline as the final words, and it
stays well inside the 200 character limit. The final line is the revised
version stored in the program.

## Verification

The program was run locally and its output file was checked in the same run,
so no other entry could overwrite the shared output path between the run and
the check: one line, 154 characters, plain ASCII and valid UTF-8, no trailing
newline, byte-identical to the constant in the program. The file hash without
a trailing newline is d775fe5657e4942a4f310c9cf2ff410f81d74b6f046854140a627d8cbf97fb30.
An earlier non-atomic check caught a different line in the shared output path,
left there by another entry built at the same time, which is why the run and
the check were done together. The kit check was run against the repository
and the transcript bundle, and its result is recorded by the parent at submit
time.
