"""Home page."""
from layout import page, photo

ROUTE_WIDE = """
<svg class="route route-wide" viewBox="0 0 850 400" role="img" aria-labelledby="route-t route-d">
<title id="route-t">How a request travels through Next Mind</title>
<desc id="route-d">Your need reaches one interface company: Solutions in Italy for European clients, Consulting in the UAE elsewhere. It is delivered by Platform, Engineering and Production, and Trade and Logistics in India, then checked against agreed criteria before you accept the result.</desc>
<path class="track" d="M30 200 H770"/>
<path class="line draw" pathLength="1" d="M30 200 H230" style="animation-duration:.7s"/>
<path class="line draw" pathLength="1" d="M230 200 C285 200 295 80 350 80 H630 C685 80 695 200 770 200" style="animation-delay:.9s;animation-duration:1.8s"/>
<path class="line draw" pathLength="1" d="M230 200 H770" style="animation-delay:.9s;animation-duration:1.8s"/>
<path class="line draw" pathLength="1" d="M230 200 C285 200 295 320 350 320 H630 C685 320 695 200 770 200" style="animation-delay:.9s;animation-duration:1.8s"/>
<g class="fade" style="animation-delay:.2s"><circle class="stop key" cx="30" cy="200" r="11"/><text class="label" x="18" y="168">Your need</text></g>
<g class="fade" style="animation-delay:.8s"><circle class="stop" cx="230" cy="200" r="11"/>
<text class="label" x="246" y="168" text-anchor="end">One interface</text>
<text class="note" x="236" y="236" text-anchor="end">Solutions · Italy</text>
<text class="note" x="236" y="256" text-anchor="end">Consulting · UAE</text></g>
<g class="fade" style="animation-delay:1.5s"><circle class="stop" cx="470" cy="80" r="10"/><text class="label" x="380" y="62">Platform</text><text class="note" x="380" y="106">Software, AI and automation</text></g>
<g class="fade" style="animation-delay:1.7s"><circle class="stop" cx="470" cy="200" r="10"/><text class="label" x="380" y="182">Engineering &amp; Production</text><text class="note" x="380" y="226">Design, prototypes, manufacturing</text></g>
<g class="fade" style="animation-delay:1.9s"><circle class="stop" cx="470" cy="320" r="10"/><text class="label" x="380" y="302">Trade &amp; Logistics</text><text class="note" x="380" y="346">Sourcing, documents, shipping</text></g>
<g class="fade" style="animation-delay:2.1s"><text class="place" x="380" y="388">Delivery centres in India</text></g>
<g class="fade" style="animation-delay:2.7s"><circle class="stop key" cx="770" cy="200" r="13"/><path d="M763 200 l5 5 l9 -10" fill="none" stroke="#0A1A33" stroke-width="2.5"/>
<text class="label" x="770" y="168" text-anchor="middle">Accepted result</text>
<text class="note" x="770" y="236" text-anchor="middle">Checked against</text>
<text class="note" x="770" y="254" text-anchor="middle">agreed criteria</text></g>
</svg>"""

ROUTE_TALL = """
<svg class="route route-tall" viewBox="0 0 360 560" role="img" aria-labelledby="route-tt route-td">
<title id="route-tt">How a request travels through Next Mind</title>
<desc id="route-td">Your need reaches one interface company, is delivered by three delivery centres in India and is checked against agreed criteria before you accept the result.</desc>
<path class="line draw" pathLength="1" d="M40 30 V190" style="animation-duration:.8s"/>
<path class="line draw" pathLength="1" d="M40 190 C40 215 22 215 22 240 V420 C22 445 40 445 40 470" style="animation-delay:.8s;animation-duration:1.4s"/>
<path class="line draw" pathLength="1" d="M40 190 V470" style="animation-delay:.8s;animation-duration:1.4s"/>
<path class="line draw" pathLength="1" d="M40 190 C40 215 58 215 58 240 V420 C58 445 40 445 40 470 V530" style="animation-delay:.8s;animation-duration:1.6s"/>
<g class="fade" style="animation-delay:.2s"><circle class="stop key" cx="40" cy="30" r="11"/><text class="label" x="84" y="37">Your need</text></g>
<g class="fade" style="animation-delay:.7s"><circle class="stop" cx="40" cy="130" r="10"/><text class="label" x="84" y="124">One interface</text><text class="note" x="84" y="146">Solutions · Italy, Consulting · UAE</text></g>
<g class="fade" style="animation-delay:1.3s"><circle class="stop" cx="22" cy="270" r="8"/><text class="label" x="84" y="272">Platform</text></g>
<g class="fade" style="animation-delay:1.5s"><circle class="stop" cx="40" cy="330" r="8"/><text class="label" x="84" y="332">Engineering &amp; Production</text></g>
<g class="fade" style="animation-delay:1.7s"><circle class="stop" cx="58" cy="390" r="8"/><text class="label" x="84" y="392">Trade &amp; Logistics</text><text class="place" x="84" y="420">Delivery centres in India</text></g>
<g class="fade" style="animation-delay:2.3s"><circle class="stop key" cx="40" cy="530" r="12"/><path d="M34 530 l4 4 l8 -9" fill="none" stroke="#0A1A33" stroke-width="2.5"/><text class="label" x="84" y="526">Accepted result</text><text class="note" x="84" y="548">Checked against agreed criteria</text></g>
</svg>"""

OFFERS = [
    ("strategy-growth", "Strategy &amp; Growth", "Decide where to grow before you commit people and money.",
     "Market and growth assessment", "Priorities, options compared, an execution roadmap"),
    ("digital-operations", "Digital Operations", "Replace spreadsheets, email approvals and late reports with one controlled workflow.",
     "Workflow diagnostic and pilot", "Process map, pilot scope, adoption criteria"),
    ("engineering-industrialisation", "Engineering &amp; Industrialisation", "Turn a physical part, a concept or incomplete drawings into a design you can manufacture.",
     "Engineering Release Pack", "Verified CAD, drawings, bill of materials, validation evidence"),
    ("production", "Production", "Move from prototype to a first batch with a confirmed route and inspection records.",
     "Manufacturing readiness review", "Gap list, process route, inspection plan"),
    ("trade-logistics", "Trade &amp; Logistics", "Get goods, documents and suppliers to the right place on the agreed date.",
     "Shipment and sourcing plan", "Milestones, document checklist, responsibilities"),
    ("integrated-programmes", "Integrated Programmes", "Run several workstreams toward one outcome, with one plan and one acceptance.",
     "Programme charter", "Scope, decision rights, integrated plan, interface map"),
]

PHASES = [
    ("Assess", "We look at your company as it really runs: numbers, sales, operations, systems and people."),
    ("Design", "We turn the diagnosis into a strategy and a roadmap you can fund."),
    ("Plan", "Every initiative gets owners, a schedule, a budget, risks and a way to measure it."),
    ("Deliver", "The right teams execute: software, engineering, production, logistics."),
    ("Measure", "Results are compared with the starting baseline, not with promises."),
    ("Improve", "What works becomes routine. What does not is corrected or stopped."),
]

def build():
    offers = "".join(f"""
<div class="offer">
  <h3><a href="services/{slug}.html">{name}</a></h3>
  <p>{line}</p>
  <p class="first">{first}<span>{gets}</span></p>
</div>""" for slug, name, line, first, gets in OFFERS)
    phases = "".join(f"<li><h3>{n}</h3><p>{t}</p></li>" for n, t in PHASES)
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <h1>From industrial need to accepted result, on one route.</h1>
    <div class="hero-copy">
      <p class="lead">Next Mind Group connects strategy, software, engineering, production and international trade. You deal with one company; we coordinate the specialists behind it and stay until the work is accepted.</p>
      <div class="actions"><a class="btn" href="contact.html">Describe the result you need</a><a class="btn line" href="approach.html">See how we work</a></div>
    </div>
    <div class="hero-visual">{ROUTE_WIDE}{ROUTE_TALL}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head">
      <h2>Start with one defined piece of work.</h2>
      <p class="muted">Each service can be bought on its own. The first engagement has a fixed scope and a deliverable you can judge, so you can test how we work before committing to more.</p>
    </div>
    <div class="col-labels" aria-hidden="true"><span>Service</span><span>When it helps</span><span>What you get first</span></div>
    <div class="offers">{offers}</div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="head">
      <h2>How a project runs.</h2>
      <p class="muted">Six phases, each with defined inputs from you and documents from us. You can join at any phase: a technical package, for example, starts at Plan.</p>
    </div>
    <ol class="phases">{phases}</ol>
    <p style="margin-top:40px"><a href="approach.html">What you provide and receive in each phase</a></p>
  </div>
</section>

<section class="section ink">
  <div class="wrap">
    <div class="head">
      <h2>Who does what.</h2>
      <p class="lead">The Holding owns and governs. Consulting and Solutions own the client relationship. Platform, Engineering &amp; Production and Trade &amp; Logistics deliver.</p>
    </div>
    <div class="roles">
      <div class="role"><p class="where">Italy</p><h3>Next Mind Solutions</h3><ul><li>Your interface if you are in Europe</li><li>Proposal, project coordination and acceptance</li><li>European contracting entity when you need one</li></ul></div>
      <div class="role"><p class="where">United Arab Emirates</p><h3>Next Mind Consulting</h3><ul><li>Your interface outside Europe: GCC, Middle East, Africa</li><li>Strategy, PMO and international development</li><li>Leads proposals that span several units</li></ul></div>
      <div class="role"><p class="where">India</p><h3>Three delivery centres</h3><ul><li><strong>Platform</strong>: software, AI, automation, integration</li><li><strong>Engineering &amp; Production</strong>: CAD, industrialisation, prototypes, manufacturing</li><li><strong>Trade &amp; Logistics</strong>: sourcing, export documents, freight coordination</li></ul></div>
    </div>
    <p class="note" style="margin-top:32px">Next Mind Holding in Cyprus owns the brand, methods and shared technology and sets common rules for every company. A North American hub is planned once demand justifies it. <a href="group.html">How the Group is organised</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head"><h2>Rules we work by.</h2><p class="muted">They decide who you talk to, who answers for the result and what happens to your information.</p></div>
    <ul class="principles">
      <li><strong>One client, one commercial owner.</strong><span>No other unit quotes or contacts you outside the agreed process.</span></li>
      <li><strong>One project, one sponsor, one scope.</strong><span>One budget, one risk register, one escalation path and one acceptance process.</span></li>
      <li><strong>Evidence before release.</strong><span>Drawings, batches, software and shipments pass agreed checks before they reach you.</span></li>
      <li><strong>Your data and designs stay yours.</strong><span>Ownership and use are set in your contract, never assumed by us.</span></li>
    </ul>
  </div>
</section>

<section class="section band">
  <div class="wrap cta">
    <div><h2>Tell us what has to change.</h2></div>
    <div>
      <p>Describe the result you need, your constraints and what you already have. The first conversation sets the scope, the people involved and the first deliverable.</p>
      <div class="actions"><a class="btn" href="contact.html">Start a project</a><a class="btn line" href="working-with-us.html">Ways to work with us</a></div>
    </div>
  </div>
</section>
"""
    return page("index.html", "From industrial need to accepted result",
                "Next Mind Group connects strategy, software, engineering, production and international trade through one accountable interface.",
                body, current=None)
