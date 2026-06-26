# Project Genesis: Kathleen × ChatGPT Conversation

**Type:** Instigating Input Document  
**Date of conversation:** (pre-project, spring 2026)  
**Participants:** Kathleen (QRSE), ChatGPT  
**Recorded by:** Grant  
**Purpose:** Preserve the original conversation that prompted this proof-of-concept project.  
This document is the source of record for the business context, design decisions, and strategic intent behind the knowledge base initiative.

---

## Origin

Kathleen brought an idea she had encountered on Twitter — a workflow for using LLMs to build and maintain personal knowledge bases from raw source material, all stored as Markdown files and navigated in Obsidian. The following conversation worked through whether and how QRSE should adopt it, and connected it to a broader business goal: new recurring revenue streams.

---

## The Twitter Post That Started It

Kathleen shared this post (author unattributed in conversation):

> "LLM Knowledge Bases — Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it.
>
> **Data ingest:** I index source documents (articles, papers, repos, datasets, images, etc.) into a `raw/` directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of `.md` files in a directory structure. The wiki includes summaries of all the data in `raw/`, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into `.md` files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.
>
> **IDE:** I use Obsidian as the IDE "frontend" where I can view the raw data, the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).
>
> **Q&A:** Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.
>
> **Output:** Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for future queries. So my own explorations and queries always "add up" in the knowledge base.
>
> **Linting:** I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.
>
> **Extra tools:** I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries.
>
> **Further explorations:** As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.
>
> **TLDR:** raw data from a given number of sources is collected, then compiled by an LLM into a `.md` wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts."

---

## Key Decisions Made in Conversation

### 1. Tool selection: Obsidian

ChatGPT presented three philosophies:
- **Obsidian** — local, Markdown-based, total control, flexible, powerful; requires structure and discipline
- **Notion-style tools** — cloud, collaborative, less flexible; good for teams short-term
- **AI-native tools (Cabinet, Nozomio)** — early-stage, black-box, not production-ready

**Kathleen's requirement:** "I want total control of the data not on someone's cloud."

**Decision:** Obsidian + local Markdown files + Git. No Notion. No Cabinet. No Nozomio.

> "These tools are trying to solve: 'What if the LLM builds and maintains everything automatically?' They are not mature yet. You don't control the system deeply." — ChatGPT

### 2. No server needed to start

The question of whether a server (NAS) was needed was raised and resolved: no server for the POC. Start with a local vault on one machine. Add shared storage (NAS or private Git repo) only if the intern team needs simultaneous access.

### 3. Application to QRSE: internal first, product second

Kathleen scoped the intern project to QRSE's own data:

> "I want to start this for us, not a client, under R&D. They would shadow people to uncover all our data sources and how we use them. Ingest Airtable, records in ACC, training we have done for eProject delivery, change management, environmental reviews/NEPA assignments, etc."

ChatGPT reframed this as building a "compounding system where every intern adds structured knowledge that future interns can build on."

### 4. New business streams: the strategic layer

Kathleen added a second goal: subscription revenue from QRSE's expertise.

Proposed product areas:
- **AASHTO financial compliance support** — indirect rate, audit prep, documentation
- **Change order evaluation (DOT projects)** — on-call review, claim red flag detection, benchmarking
- **Environmental/NEPA compliance support** — documentation templates, ongoing guidance
- **eConstruction / digital delivery support** — ACC training, workflow setup, system audits

ChatGPT recommended starting with **Change Order Evaluation** as the most concrete and defensible.

> "If you package it wrong, it becomes consulting again instead of scalable revenue." — ChatGPT

### 5. Intern team: 4 interns, 6 weeks

**Kathleen's instinct:** "I think each does 1 at a time" (one topic per intern, four topics in parallel).

**ChatGPT's pushback:** Four separate topics in 6 weeks produces 4 shallow outputs, 4 different structures, no reusable system, nothing strong enough to turn into a product.

**Recommended structure:** One core topic (change order evaluation), with each intern owning a distinct role:
- Intern 1: Data & Sources — Airtable, ACC records, raw ingestion
- Intern 2: Workflow & Shadowing — how QRSE actually evaluates claims
- Intern 3: Knowledge Builder — wiki pages, concepts, links
- Intern 4: Product Builder — checklist, template, sample report

> "At the end of 6 weeks, do I want 4 partial ideas or 1 thing I could actually use or sell?" — ChatGPT

---

## How This Project Connects

This vault (2026-05_Obsidian_Knowledge_Base_Spec) is a **proof-of-concept** of the technical approach described in the Twitter post — not the full intern-facing system Kathleen described above.

The POC uses the 2005 HDOT Standard Specifications as source material (a bounded, well-structured document set) to validate the workflow: ingest raw PDFs → convert to Markdown → LLM-compile a wiki → Q&A test.

**Scope of this POC (not the intern project):**
- Solo, 3 days
- Source material: 2005 HDOT Standard Specifications + Special Provisions only
- Goal: prove the technical workflow works before scaling to QRSE's internal data

**What comes next (the intern project Kathleen described):**
- Source material: Airtable, ACC records, eProject delivery training, change management, NEPA/environmental
- Team: 4 interns, 6 weeks
- Focus: change order evaluation (per ChatGPT's recommendation) or another high-value domain
- Output: a working knowledge system + the foundation for a subscription product

---

## What This Document Is NOT

This document records the conversation that prompted the project. It does not modify the scope of this POC. Per CLAUDE.md, this POC is limited to the 2005 HDOT Standard Specifications. The intern project (QRSE internal data, product development) is a separate future effort.

---

*Logged by Grant — 2026-05-21*
