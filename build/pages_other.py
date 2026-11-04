"""Group, Industries, Working with us, Trust, Careers, Contact, Credits, 404."""
import json, os
from layout import page, photo, esc

def hero(crumb, h1, lead, pre=""):
    return f"""<section class="page-hero"><div class="wrap"><p class="crumbs"><a href="{pre}index.html">Home</a> / {crumb}</p><h1>{h1}</h1><p class="lead">{lead}</p></div></section>"""

def group():
    body = hero("The Group", "One group, six companies, one way of working.",
                "Each company has one economic job. Together they cover the route from a client’s need to delivery, without duplicating the same capability in several countries.") + """
<section class="section">
  <div class="wrap">
    <div class="head"><h2>How the Group is organised</h2><p class="muted">Three layers: ownership and governance, the companies you deal with, and the delivery centres behind them.</p></div>
    <div class="org">
      <p class="org-label">Ownership and governance</p>
      <div class="org-row"><div class="node holding"><p class="where">Cyprus</p><h3>Next Mind Holding</h3><p>Owns the operating companies, the brand, methods and shared technology. Allocates capital and sets common rules for finance, quality, data and compliance.</p></div></div>
      <p class="org-label">Your interface</p>
      <div class="org-row" style="--n:2">
        <div class="node"><p class="where">Italy</p><h3>Next Mind Solutions</h3><p>European client relationships, solution design, proposals, project coordination and acceptance. Can act as your European contracting entity.</p></div>
        <div class="node"><p class="where">United Arab Emirates</p><h3>Next Mind Consulting</h3><p>Clients outside Europe: strategy, market entry, transformation programmes, PMO and international business development.</p></div>
      </div>
      <p class="org-label">Delivery centres</p>
      <div class="org-row" style="--n:3">
        <div class="node"><p class="where">India</p><h3>Next Mind Platform</h3><p>Software architecture, the Group platform, AI and automation, integration, cybersecurity and support.</p></div>
        <div class="node"><p class="where">India</p><h3>Next Mind Engineering &amp; Production</h3><p>Two divisions with separate budgets and quality records: engineering and product development; manufacturing and industrial operations.</p></div>
        <div class="node"><p class="where">India</p><h3>Next Mind Trade &amp; Logistics</h3><p>Shipping planning, export documents, Incoterms, freight-forwarder coordination, tracking and supplier follow-up.</p></div>
      </div>
      <p class="org-label">Planned</p>
      <div class="org-row"><div class="node future"><p class="where">United States</p><h3>North America hub</h3><p>A market-facing company for North American clients, to be set up only when demand, revenue and local needs justify it. Until then, North American clients are served by Consulting or Solutions.</p></div></div>
    </div>
    <p class="note" style="margin-top:32px">The Group is being built in stages. A company is created only when there is a measurable business reason for it, not to create the appearance of scale.</p>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="head"><h2>Who you deal with</h2><p class="muted">Every client has one commercial owner. The units behind it work on defined work packages and never contact you outside the agreed process.</p></div>
    <div class="table-wrap"><table class="table stack">
      <thead><tr><th>If you are</th><th>Your interface</th><th>Who delivers</th></tr></thead>
      <tbody>
        <tr><td data-h="If you are">A European company</td><td data-h="Your interface">Next Mind Solutions, Italy: relationship, proposal, coordination, destination requirements</td><td data-h="Who delivers">Platform, Engineering &amp; Production and Trade &amp; Logistics, as the project needs</td></tr>
        <tr><td data-h="If you are">A company outside Europe</td><td data-h="Your interface">Next Mind Consulting, UAE: strategy, PMO and coordination of Group capabilities</td><td data-h="Who delivers">The relevant delivery centre; Solutions where European partners are involved</td></tr>
        <tr><td data-h="If you are">A company in North America</td><td data-h="Your interface">Consulting or Solutions today, depending on the project; the planned hub later</td><td data-h="Who delivers">The relevant delivery centre</td></tr>
      </tbody>
    </table></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="head"><h2>Why the work is split this way</h2></div>
    <div class="cols rule-top">
      <div><h3>Close to the client</h3><p>Italy and the UAE keep relationships, language, contracts and expectations local. You have one counterpart from the first meeting to acceptance.</p></div>
      <div><h3>Capability in one place</h3><p>Software, engineering, manufacturing and trade execution are concentrated in India instead of being rebuilt in each country, which keeps quality and methods consistent.</p></div>
      <div><h3>Controlled, not offshored</h3><p>The value is not only lower cost. It is technical capability combined with commercial coordination, quality control, visibility and one accountable project lead.</p></div>
    </div>
  </div>
</section>"""
    return page("group.html", "The Group", "How Next Mind Group is organised: Holding in Cyprus, Consulting in the UAE, Solutions in Italy and three delivery centres in India.", body, current="group.html")

SECTORS = [
 ("Industrial machinery and equipment", "Special-purpose machinery, production equipment, automation systems and assemblies.", "CAD and engineering packages, industrialisation, component production, supplier coordination, delivery abroad."),
 ("Material handling and intralogistics", "Handling equipment, intralogistics systems and industrial mobility.", "Engineering, industrial design, manufacturing, automation and software, spare parts and after-sales coordination."),
 ("Packaging, food-processing and line equipment", "Packaging machinery, food-processing equipment and production-line systems.", "Mechanical engineering, production support, spare parts, quality records, export documents."),
 ("Industrial automation and connected operations", "Companies digitalising engineering, production and supplier information.", "Workflow automation, engineering-document control, production visibility, reporting, AI use cases."),
 ("Precision components and mobility", "Tooling, fixtures, technical components and assemblies. Highly regulated supply chains only once quality systems and references are in place.", "Engineering services, prototypes, controlled production support."),
 ("Supply chain and trade", "Companies with many suppliers, cross-border flows and unreliable export processes.", "Supplier coordination, sourcing support, export documents, shipment visibility."),
 ("Renewable-energy equipment", "Selected equipment and infrastructure components, where technical fit and compliance are clear.", "Engineering, industrialisation, component supply, trade coordination."),
]

MARKETS = [
 ("Italy", "Industrial SMEs, machinery builders, component and packaging-equipment manufacturers", "Engineering feasibility, digital assessment, prototype, controlled sourcing or production support"),
 ("Selected European markets", "OEMs, technical manufacturers, automation and equipment producers", "Engineering packages, industrialisation, production capacity, project visibility"),
 ("UAE and GCC", "Industrial groups, project developers, technology companies, distributors and investors", "Strategy, PMO, market development, industrial digitalisation assessment"),
 ("India", "Industrial SMEs, exporters, machinery and component manufacturers", "Software and automation, engineering, export coordination, supplier development"),
 ("Africa and emerging markets", "Industrial project developers, local distributors, companies needing cross-border support", "Market-entry advice, sourcing support, trade coordination, partner-led"),
 ("North America (later)", "Advanced manufacturing, industrial technology, intralogistics, automation", "Strategic accounts and targeted partnerships before any local presence"),
]

def industries():
    sec = "".join(f'<div><h3>{a}</h3><p>{b}</p><p class="small muted"><strong>Typically needed:</strong> {c}</p></div>' for a, b, c in SECTORS)
    mk = "".join(f'<tr><td data-h="Market">{a}</td><td data-h="Who">{b}</td><td data-h="Usual first engagement">{c}</td></tr>' for a, b, c in MARKETS)
    body = hero("Industries", "Industrial companies with technical, operational or cross-border complexity.",
                "Industry matters, but the stronger signal is the type of problem: not enough coordination capacity, technical complexity, delivery across borders or several workstreams at once.") + f"""
<section class="section">
  <div class="wrap">
    <div class="head"><h2>Sectors we focus on</h2><p class="muted">We expand into new sectors only once we can show relevant references, technical competence and quality standards.</p></div>
    <div class="cols rule-top">{sec}</div>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="head"><h2>Who we serve first</h2><p class="muted">Industrial SMEs and mid-sized companies are the core: big enough to need more than one specialist, not big enough to build every capability in-house.</p></div>
    <div class="cols rule-top" style="--n:2">
      <div><h3>A good fit</h3><ul><li>Industrial SMEs and mid-market manufacturers</li><li>OEMs, machinery builders and component producers</li><li>Companies entering new markets or restructuring international operations</li><li>Technology-enabled industrial companies</li><li>Companies with fragmented supply, engineering or trade processes</li></ul></div>
      <div><h3>Usually not a fit</h3><ul><li>Purely price-driven procurement with no interest in coordination</li><li>Requests for broad capability without agreed scope or commercial terms</li><li>Low-value transactional orders</li></ul></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="head"><h2>Where we start</h2><p class="muted">We lead with the service that creates the lowest barrier and the clearest value, then expand only if it improves the outcome.</p></div>
    <div class="table-wrap"><table class="table stack"><thead><tr><th>Market</th><th>Who</th><th>Usual first engagement</th></tr></thead><tbody>{mk}</tbody></table></div>
  </div>
</section>"""
    return page("industries.html", "Industries", "Sectors and markets Next Mind Group serves: machinery, intralogistics, packaging, automation, components, supply chain and renewable-energy equipment.", body, current="industries.html")

def working():
    body = hero("Working with us", "Start small. Expand only when it helps you.",
                "Clients do not have to commit to a large programme before seeing what we deliver. Every engagement has a defined scope, an owner and a way to accept the result.") + """
<section class="section">
  <div class="wrap">
    <div class="head"><h2>How a relationship usually grows</h2><p class="muted">Each step happens only if the previous one delivered measurable value.</p></div>
    <ol class="journey">
      <li><h3>Focused first engagement</h3><p>An assessment, a feasibility study, a CAD package, a software pilot, a sourcing analysis or one shipment.</p></li>
      <li><h3>Validated project</h3><p>A larger piece of work built on what the first engagement showed.</p></li>
      <li><h3>Integrated solution</h3><p>Several services combined under one plan where the outcome needs them.</p></li>
      <li><h3>Recurring service</h3><p>Retained support, subscriptions, framework supply or logistics management.</p></li>
      <li><h3>Long-term account</h3><p>Regular reviews, a stable team and a shared roadmap.</p></li>
    </ol>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="head"><h2>Engagement models</h2><p class="muted">Prices depend on scope, risk and delivery obligations and are agreed per engagement.</p></div>
    <div class="cols rule-top">
      <div><h3>Assessment</h3><p>A diagnosis, report and roadmap for a fixed fee. Useful on its own, even if you do not continue with us.</p></div>
      <div><h3>Project or phase</h3><p>Defined outputs, paid by phase or milestone. Changes go through an agreed change process.</p></div>
      <div><h3>Fixed support</h3><p>Reserved capacity for a period, for example a project manager two days a week on site plus a weekly remote review.</p></div>
      <div><h3>Recurring package</h3><p>Repeated outputs at an agreed frequency, such as monthly reporting on three jobs or four technical reviews a month.</p></div>
      <div><h3>Integrated programme</h3><p>Several workstreams under one charter, one programme lead and one acceptance.</p></div>
      <div><h3>Production and supply</h3><p>Deposits, milestone payments and technical approval before production release; warranty limits agreed in the contract.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="head"><h2>Every project has</h2><p class="muted">Whatever its size.</p></div>
    <ul class="deliv">
      <li>One commercial owner</li><li>One project sponsor on your side</li><li>One project manager on ours</li><li>One approved scope and budget</li>
      <li>One risk register</li><li>One escalation path</li><li>One way of communicating with you</li><li>One acceptance process</li>
    </ul>
  </div>
</section>
<section class="section ink">
  <div class="wrap cta">
    <div><h2>What we need from you to start</h2></div>
    <div><ul><li>The result you need and why now</li><li>Constraints: time, budget, standards, locations</li><li>What already exists: documents, drawings, data, systems</li><li>Who decides and who will accept the work</li></ul>
    <div class="actions" style="margin-top:20px"><a class="btn" href="contact.html">Start a project</a></div></div>
  </div>
</section>"""
    return page("working-with-us.html", "Working with us", "Engagement models, how a relationship grows and what every Next Mind project includes.", body, current="working-with-us.html")

def trust():
    body = hero("Trust", "Your information, designs and decisions stay under control.",
                "How we handle confidentiality, intellectual property, data, AI, quality and third parties. We only state what is in place; certifications will be listed when they are obtained.") + """
<section class="section">
  <div class="wrap">
    <div class="cols rule-top">
      <div><h3>Confidentiality</h3><p>Confidentiality terms are agreed before you share technical documents. They also bind our employees, consultants, suppliers and subcontractors.</p></div>
      <div><h3>Your intellectual property</h3><p>Your drawings, specifications, data and custom code are governed by your contract. They never become Next Mind property by default and are never used for another client.</p></div>
      <div><h3>Our intellectual property</h3><p>General methods, reusable software modules and engineering libraries belong to the Group. Contracts state clearly what is yours and what we keep.</p></div>
      <div><h3>Data access</h3><p>Access is based on role and need. Customer information is not shared between units or partners without a contractual basis and an operational reason.</p></div>
      <div><h3>AI with human review</h3><p>AI output used in deliverables, engineering decisions, contracts or specifications is reviewed by a qualified person before release. AI does not make material decisions.</p></div>
      <div><h3>Quality gates</h3><p>Defined checks before releasing drawings, buying materials, starting production, shipping goods, deploying software or closing a project.</p></div>
      <div><h3>Qualified third parties</h3><p>Suppliers and partners are assessed for capability, quality, reliability, confidentiality and compliance before they join a project.</p></div>
      <div><h3>Trade compliance</h3><p>Counterparties, products and destinations are screened. We do not accept shipments where classification, end use or customer identity is unclear.</p></div>
      <div><h3>Ethics</h3><p>Zero tolerance for bribery and corruption. Commissions are documented and approved. Concerns can be raised without retaliation.</p></div>
    </div>
  </div>
</section>
<section class="section band">
  <div class="wrap cta">
    <div><h2>Ask for our terms before you share documents.</h2></div>
    <div><p>We send the confidentiality, IP and data terms that apply to your engagement before any technical exchange.</p><div class="actions"><a class="btn" href="contact.html">Ask for our terms</a></div></div>
  </div>
</section>"""
    return page("trust.html", "Trust", "Confidentiality, intellectual property, data handling, AI oversight, quality gates and compliance at Next Mind Group.", body, current="trust.html")

def careers():
    body = hero("Careers", "Work across business, digital, engineering and production.",
                "We are building teams in Italy, the UAE and India. People work on real industrial problems with clear responsibilities and colleagues in other disciplines.") + f"""
<section class="section">
  <div class="wrap">
    <div class="head"><h2>Where people work</h2></div>
    <div class="cols rule-top">
      <div><h3>Solutions · Italy</h3><p>Account management, solution design, project management and technical-commercial proposals for European clients.</p></div>
      <div><h3>Consulting · UAE</h3><p>Strategy, market entry, PMO and transformation programmes for clients outside Europe.</p></div>
      <div><h3>Platform · India</h3><p>Software development, integration, data, AI and automation, cybersecurity and support.</p></div>
      <div><h3>Engineering &amp; Production · India</h3><p>CAD, product development, industrialisation, manufacturing, quality and inspection.</p></div>
      <div><h3>Trade &amp; Logistics · India</h3><p>Export documentation, freight coordination, supplier follow-up and shipment tracking.</p></div>
      <div><h3>Group functions</h3><p>Finance, legal and compliance, quality, IT, people and brand, shared across the companies.</p></div>
    </div>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="head"><h2>How we hire</h2><p class="muted">The same standards in every country.</p></div>
    <ol class="journey">
      <li><h3>A written role</h3><p>Every opening states the outcomes expected in the first year and the skills that will be assessed, separating essential from trainable.</p></li>
      <li><h3>A practical exercise</h3><p>A work sample, case or trade test close to the real job, assessed by a specialist.</p></li>
      <li><h3>A structured panel</h3><p>The same core questions for every candidate. At least two trained assessors score independently before they discuss.</p></li>
      <li><h3>Clear communication</h3><p>Application confirmed within one business day and a status update at least every five business days while your process is active.</p></li>
    </ol>
    <p style="margin-top:32px"><a class="btn" href="contact.html?service=careers">Send us your profile</a></p>
  </div>
</section>"""
    return page("careers.html", "Careers", "Careers at Next Mind Group across Italy, the UAE and India.", body)

def contact():
    opts = [("strategy-growth", "Grow into a market"), ("digital-operations", "Digitalise a process"), ("engineering-industrialisation", "Engineer or redesign a part"),
            ("production", "Produce a batch"), ("trade-logistics", "Source or ship goods"), ("integrated-programmes", "Several of these at once"),
            ("not-sure", "Not sure yet"), ("careers", "Apply for a job")]
    choices = "".join(f'<label class="choice"><input type="radio" name="service" value="{v}" required> {t}</label>' for v, t in opts)
    body = hero("Start a project", "Describe the result you need.",
                "Five questions. You will get a structured brief you can copy or download and send to us, so the first conversation starts from your facts.") + f"""
<section class="section">
  <div class="wrap">
    <form class="form" id="brief-form" novalidate>
      <fieldset class="field"><legend>What do you need?</legend><div class="choices">{choices}</div><p class="error" id="err-service" hidden>Choose what you need.</p></fieldset>
      <div class="field"><label for="f-result">The result you need<span class="hint">What should be true when the work is finished?</span></label><textarea id="f-result" name="result" required></textarea><p class="error" id="err-result" hidden>Describe the result in a sentence or two.</p></div>
      <div class="field"><label for="f-have">What already exists<span class="hint">Drawings, samples, data, systems, suppliers, earlier studies.</span></label><textarea id="f-have" name="have"></textarea></div>
      <div class="field"><label for="f-when">When you need it</label><select id="f-when" name="when"><option value="">Choose</option><option>Within a month</option><option>In one to three months</option><option>In three to six months</option><option>Later than six months</option><option>No fixed date</option></select></div>
      <div class="cols" style="--n:2;gap:22px">
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name"></div>
        <div class="field"><label for="f-company">Company and country</label><input id="f-company" name="company" autocomplete="organization"></div>
      </div>
      <div><button class="btn" type="submit">Prepare my brief</button></div>
    </form>
    <div class="brief" id="brief" hidden tabindex="-1">
      <h2 style="font-size:28px">Your brief</h2>
      <pre id="brief-text"></pre>
      <div class="actions"><button class="btn" type="button" id="copy-brief">Copy brief</button><button class="btn line" type="button" id="download-brief">Download as text</button><button class="btn line" type="button" id="edit-brief">Edit answers</button></div>
      <p class="small muted" id="copy-status" role="status" style="margin-top:12px"></p>
    </div>
    <p class="note" style="margin-top:40px">This form is not yet connected to an inbox: your answers stay in your browser. Send the brief to your Next Mind contact. A direct submission will be added when the Group’s contact address is confirmed.</p>
  </div>
</section>"""
    return page("contact.html", "Start a project", "Describe the result you need and prepare a structured brief for Next Mind Group.", body)

def credits(site_dir):
    d = json.load(open(os.path.join(site_dir, "assets/img/photos/CREDITS.json")))
    rows = "".join(f'<li><a href="{esc(v["source"])}">Pexels photo {k}</a></li>' for k, v in d.items())
    body = hero("Credits", "Photo and font credits.", "Photographs are used under the Pexels License. The typeface is IBM Plex Sans, under the SIL Open Font License.") + f"""
<section class="section"><div class="wrap"><ul class="cols" style="--n:3;list-style:none;padding:0">{rows}</ul></div></section>"""
    return page("credits.html", "Credits", "Photo and font credits for the Next Mind Group website.", body)

def notfound():
    body = hero("Page not found", "This page does not exist.", "The address may have changed. Start from the home page or go straight to the services.") + """
<section class="section"><div class="wrap actions"><a class="btn" href="index.html">Go to the home page</a><a class="btn line" href="services/index.html">See the services</a></div></section>"""
    return page("404.html", "Page not found", "Page not found.", body)
