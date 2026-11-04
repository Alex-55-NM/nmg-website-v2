"""Services overview and six service pages."""
from layout import page, photo, esc

S = [
 dict(slug="strategy-growth", name="Strategy &amp; Growth", photo=("39205088", "Team discussing a strategy sketched on a board"),
  h1="Decide where to grow before you commit the organisation.",
  lead="Market analysis, go-to-market, portfolio and new-country entry for industrial companies, with a roadmap someone is responsible for carrying out.",
  fit=["You want to export or enter a new country, but have no validated target segment or channel.",
       "Sales depend on a few historic relationships and a few people.",
       "You have several growth ideas and not enough people or money to pursue all of them.",
       "Growth plans have been written before, but nobody turned them into work packages."],
  do=[("Market and segment analysis", "Demand signals, competitors, customer requirements and the cost of serving each market, with assumptions kept separate from verified evidence."),
      ("Go-to-market", "Target accounts, channels, positioning, sales process and the people who will run them."),
      ("Portfolio and business model", "The offer, its value to the client, the revenue logic and what delivery will require."),
      ("International expansion", "Entry routes, local partners and operating constraints, screened for payment, regulatory and logistics risk.")],
  get=["Prioritised opportunity list", "Comparison of entry routes", "Commercial plan with owners", "Execution roadmap", "Success measures agreed with you", "Handover pack with open actions"],
  who=[("Solutions · Italy", "Leads for European clients and coordinates the work."), ("Consulting · UAE", "Leads outside Europe and contributes analysis and international development.")],
  start="Market and growth assessment: two to three candidate markets or segments compared, with a recommendation to enter, wait or drop.",
  related=["digital-operations", "integrated-programmes"]),
 dict(slug="digital-operations", name="Digital Operations", photo=("442152", "Field engineer working on a laptop beside network cabling"),
  h1="One controlled workflow instead of spreadsheets and email approvals.",
  lead="Process assessment, workflow design, integration, automation and AI, built with the people who do the work and measured after go-live.",
  fit=["The same data is typed into several systems or spreadsheets.",
       "Approvals get lost in email and nobody knows who must act next.",
       "Reports arrive too late to change anything.",
       "You are considering AI but have no data model or owner for the process."],
  do=[("Process assessment", "The actual process, data owners and recurring bottlenecks, mapped from real records."),
      ("Workflow design", "Roles, data fields, approval rules and the decisions the workflow must support."),
      ("Integration and automation", "Agreed systems connected and repeatable steps automated, tested with representative records and exceptions."),
      ("Adoption and control", "User testing, training for process owners, monitoring of exceptions and adoption.")],
  get=["Process and data map", "Workflow specification", "Tested integrations", "Dashboard for the process owner", "User guide and controls", "Adoption measures against your baseline"],
  who=[("Solutions · Italy", "Leads requirements and adoption with your team."), ("Platform · India", "Develops, integrates and supports the software.")],
  start="Workflow diagnostic and pilot: one process mapped end to end, a pilot boundary and the criteria that decide whether to roll it out.",
  related=["integrated-programmes", "production"]),
 dict(slug="engineering-industrialisation", name="Engineering &amp; Industrialisation", photo=("9616959", "Hands working over a set of technical drawings"),
  h1="From a physical part or a concept to a design you can manufacture.",
  lead="Reverse engineering, CAD, drawings, bills of materials, design for manufacture and assembly, prototypes and validation, released as one controlled package.",
  fit=["A part must be reproduced, but the only reference is a worn sample.",
       "Drawings are incomplete, or revisions are hard to trace.",
       "Manufacturing problems are discovered at the supplier, too late.",
       "A concept needs to become a prototype and then a producible product."],
  do=[("Requirements and capture", "Function, interfaces, materials and acceptance requirements clarified; geometry captured where useful."),
      ("Design and engineering", "3D models, 2D drawings, tolerances and bills of materials under revision control."),
      ("Industrialisation", "Design for manufacture and assembly, process choices and supplier feasibility."),
      ("Validation and release", "Checks planned, results recorded and issues resolved before technical release.")],
  get=["Requirements baseline", "Controlled CAD models and drawings", "Bill of materials", "Industrialisation plan", "Prototype or verification evidence", "Engineering Release Pack"],
  who=[("Solutions · Italy", "Aligns requirements and acceptance with your technical authority."), ("Engineering & Production · India", "Develops the technical solution and prototypes.")],
  start="Engineering feasibility or a single-part release: one component taken to a verified drawing set and bill of materials.",
  related=["production", "trade-logistics"]),
 dict(slug="production", name="Production", photo=("8865187", "CNC machine spindle with coolant lines"),
  h1="A confirmed route from released design to inspected batch.",
  lead="Manufacturing readiness, process routes, qualified capacity, machining, fabrication, assembly, inspection and ramp-up, with records that support acceptance.",
  fit=["A validated prototype must become a repeatable first batch.",
       "Supplier capacity or lead times are uncertain.",
       "Inspection records do not support your acceptance decision.",
       "Deviations are handled informally between people."],
  do=[("Readiness", "Drawing maturity, critical characteristics, materials and required volumes checked before anything is ordered."),
      ("Capacity and sourcing", "Process routes, qualified capacity and supplier responsibilities defined."),
      ("Build and inspect", "Machining, fabrication, welding, assembly and inspections coordinated against agreed criteria."),
      ("Ramp-up and handover", "Deviations reviewed, the process stabilised and production records handed over.")],
  get=["Readiness checklist", "Production and capacity plan", "Inspection plan", "Inspection and test reports", "Non-conformity records and dispositions", "Production Release Pack"],
  who=[("Solutions · Italy", "Coordinates timing and acceptance for European clients."), ("Engineering & Production · India", "Manufactures or activates qualified capacity.")],
  start="Manufacturing readiness review: the gaps between your design and a repeatable batch, listed and assigned before any material is bought.",
  related=["engineering-industrialisation", "trade-logistics"]),
 dict(slug="trade-logistics", name="Trade &amp; Logistics", photo=("9850156", "Port crane handling cargo at a quay"),
  h1="Goods, documents and suppliers on one visible route.",
  lead="Supply planning, supplier follow-up, export documents and freight coordination with competent operators, from origin to the agreed delivery terms.",
  fit=["Several suppliers must feed one delivery and their dates do not agree.",
       "Shipment documents are incomplete or arrive late.",
       "Responsibility for goods changes hands without anyone noticing.",
       "Import, Incoterms and insurance questions are answered case by case."],
  do=[("Supply planning", "Quantities, lead times and delivery milestones aligned across suppliers."),
      ("Supplier follow-up", "Commitments tracked and gaps escalated with the responsible supplier."),
      ("Shipment readiness", "Packing, documentation, freight booking and customs interfaces coordinated with competent operators."),
      ("Delivery and closure", "Milestones followed, receipt confirmed and quantity or document discrepancies closed.")],
  get=["Supply schedule", "Supplier action log", "Shipment document checklist", "Tracking report", "Delivery confirmation", "Closure record"],
  who=[("Trade & Logistics · India", "Coordinates the flows, documents and freight partners."), ("Solutions · Italy", "Remains your contact for European deliveries and destination requirements.")],
  start="Shipment and sourcing plan for one order: milestones, documents and who is responsible at each handover.",
  related=["production", "integrated-programmes"]),
 dict(slug="integrated-programmes", name="Integrated Programmes", photo=("7691694", "Project team reviewing drawings around a table"),
  h1="Several workstreams, one plan, one acceptance.",
  lead="When the outcome needs engineering, digital, production and supply together, one programme lead connects them through shared milestones, interfaces and acceptance criteria.",
  fit=["Each team has a plan, but the plans do not connect.",
       "One team’s delay surfaces weeks later in another team’s work.",
       "Nobody clearly owns the final handover.",
       "You want one counterpart responsible for the whole result."],
  do=[("Frame the programme", "Objectives, scope boundaries, decision rights and measurable acceptance criteria."),
      ("Connect capabilities", "Lead and supporting units assigned around the required outputs, with interfaces mapped."),
      ("Control execution", "Milestones, interfaces, changes, risks and evidence managed through one integrated plan."),
      ("Accept and hand over", "Deliverables verified with you; documentation, ownership and open actions transferred.")],
  get=["Programme charter", "Responsibility and interface map", "Integrated delivery plan", "Common risk and change log", "Steering reports", "Acceptance and handover pack"],
  who=[("Solutions · Italy or Consulting · UAE", "Provides the programme lead and PMO, depending on where you are."), ("Platform, Engineering & Production, Trade & Logistics", "Join only where the outcome needs them.")],
  start="Programme charter: scope, sponsor, decision rights, units involved and the integrated plan, approved before execution starts.",
  related=["engineering-industrialisation", "digital-operations"]),
]
BY = {s["slug"]: s for s in S}

def service_page(s):
    fit = "".join(f"<li>{x}</li>" for x in s["fit"])
    do = "".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in s["do"])
    get = "".join(f"<li>{x}</li>" for x in s["get"])
    who = "".join(f'<div class="node"><p class="where">{esc(a)}</p><p>{esc(b)}</p></div>' for a, b in s["who"])
    rel = " · ".join(f'<a href="{r}.html">{BY[r]["name"]}</a>' for r in s["related"])
    body = f"""
<section class="page-hero split">
  <div class="wrap">
    <div>
      <p class="crumbs"><a href="../index.html">Home</a> / <a href="index.html">Services</a> / {s['name']}</p>
      <h1>{s['h1']}</h1>
      <p class="lead">{s['lead']}</p>
    </div>
    {photo('../', s['photo'][0], s['photo'][1], eager=True, sizes="(max-width: 900px) 100vw, 42vw")}
  </div>
</section>
<section class="section">
  <div class="wrap head" style="margin-bottom:0;align-items:start">
    <h2>When this helps</h2>
    <ul class="fit">{fit}</ul>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="head"><h2>What we do</h2><p class="muted">You can buy one of these activities or several connected ones. The scope is agreed with you before work starts.</p></div>
    <div class="cols rule-top" style="--n:4">{do}</div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="head"><h2>What you receive</h2><p class="muted">Documents you can review, keep and use after we hand over. Results such as time or cost savings are measured against your own starting point.</p></div>
    <ul class="deliv">{get}</ul>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="head"><h2>Who delivers</h2><p class="muted">One company is your contract and your contact. The others work behind it on defined work packages.</p></div>
    <div class="who">{who}</div>
  </div>
</section>
<section class="section ink">
  <div class="wrap cta">
    <div><h2>How it usually starts</h2><p class="lead" style="margin-top:16px">{s['start']}</p></div>
    <div><div class="actions"><a class="btn" href="../contact.html?service={s['slug']}">Discuss this service</a><a class="btn line" href="../approach.html">How we work</a></div>
    <p class="small" style="margin-top:24px">Often combined with {rel}.</p></div>
  </div>
</section>"""
    plain = s["name"].replace("&amp;", "&")
    return page(f"services/{s['slug']}.html", plain, f"{plain}: " + s["lead"].replace("&amp;", "&"), body, current="services/index.html")

def overview():
    rows = "".join(f"""
<div class="offer">
  <h3><a href="{s['slug']}.html">{s['name']}</a></h3>
  <p>{s['lead']}</p>
  <p class="first">{s['start'].split(':')[0]}<span>{s['start'].split(':',1)[1].strip()}</span></p>
</div>""" for s in S)
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Home</a> / Services</p>
    <h1>Six services. Buy one, or connect them.</h1>
    <p class="lead">Each service has its own first deliverable. When a result needs more than one discipline, Integrated Programmes put them under one plan and one acceptance.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="col-labels" aria-hidden="true"><span>Service</span><span>What it covers</span><span>Usual first engagement</span></div>
    <div class="offers">{rows}</div>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="head"><h2>Three ways the offer is organised</h2><p class="muted">The level depends on your need, budget and how far you want to go. We do not push clients toward the largest one.</p></div>
    <div class="cols rule-top">
      <div><h3>A focused service</h3><p>One defined piece of work: an assessment, a CAD package, a software module, a prototype, a production order or one shipment.</p></div>
      <div><h3>An integrated solution</h3><p>Two or more services combined to solve a broader problem, such as engineering and production, or consulting and software.</p></div>
      <div><h3>A strategic account</h3><p>Long-term support across several workstreams: retained consulting, subscriptions, recurring production and logistics, with regular performance reviews.</p></div>
    </div>
  </div>
</section>"""
    return page("services/index.html", "Services", "Strategy & Growth, Digital Operations, Engineering & Industrialisation, Production, Trade & Logistics and Integrated Programmes.", body, current="services/index.html")

def build():
    out = {"services/index.html": overview()}
    for s in S:
        out[f"services/{s['slug']}.html"] = service_page(s)
    return out
