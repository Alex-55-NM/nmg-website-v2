"""How we work: the six-phase execution framework (from the Consulting UAE framework)."""
from layout import page

# phase: (name, summary, [(step, you provide, we do, you receive)])
PHASES = [
 ("Assess", "We build a complete picture of the company as it really runs, so the strategy starts from facts rather than impressions.", [
  ("Company and governance", "Company profile, organisation chart, ownership and decision roles, products and markets served, main clients.",
   "Document review, management interviews, governance and business-model mapping, positioning review.",
   "Corporate assessment, business model canvas, governance map, SWOT."),
  ("Finance", "Three to five years of accounts, revenue by client and product, fixed and variable costs, job margins, price lists, receivables and payables.",
   "Revenue, margin, EBITDA, cash-flow and working-capital analysis; pricing and profitability by client, product and job.",
   "Financial diagnostic, margin analysis, cash-flow review, pricing review, financial baseline."),
  ("Sales", "Client list, sales history, quotes won and lost, CRM export, pipeline, agents and distributors.",
   "Pipeline and funnel analysis, CRM data quality, conversion, retention and cross-selling potential.",
   "Commercial assessment, pipeline report, customer ABC analysis, opportunity matrix."),
  ("Operations", "Layout, routings, bills of materials, cycle and set-up times, quality and scrap data, suppliers, lead times, stock and shipping costs.",
   "Process mapping, capacity and OEE baseline, bottleneck, inventory, supplier and logistics analysis.",
   "Process flow map, capacity model, bottleneck map, supplier risk matrix."),
  ("Technology", "Software list, ERP/CRM/MES/PLM exports, critical spreadsheets, server and cloud set-up, backup and access policies.",
   "System map, digital maturity score, cybersecurity review, automation and AI use cases, integration gaps.",
   "IT system map, digital maturity matrix, cybersecurity risk report, automation backlog."),
  ("People", "Organisation chart, job descriptions, roles and KPIs, training plans, turnover, interviews with managers.",
   "Skills matrix, role and responsibility mapping, leadership and training-needs review.",
   "Skills matrix, RACI draft, organisation gap report, training needs."),
 ]),
 ("Design", "The diagnosis becomes a strategy: where to grow, what to digitalise, what to fix in operations, how to sell and what it will cost.", [
  ("Growth", "Diagnostic report, current markets, target clients, capacity, management goals, growth budget.",
   "Market and segment analysis, product opportunities, partnerships, international scenarios.",
   "Growth strategy plan, market opportunity matrix, expansion scenarios."),
  ("Digital", "Technology assessment, current systems, manual workflows, IT priorities and budget, available data.",
   "Target architecture, data strategy, automation and AI roadmap, integration and cybersecurity plan.",
   "Digital roadmap, target IT architecture, AI roadmap, automation backlog."),
  ("Operations", "Operations assessment, quality problems, lead times, operating costs, investment plans.",
   "Lean roadmap, capacity planning, warehouse and supply-chain redesign, quality improvement.",
   "Operational improvement plan, capacity plan, supplier strategy."),
  ("Commercial", "Commercial assessment, CRM, pipeline, price lists and margins, lost quotes.",
   "Go-to-market and sales-process design, pricing, key-account and retention plans.",
   "Commercial strategy, sales playbook, pricing framework, key-account plan."),
  ("Organisation", "People assessment, current structure, staff budget, HR constraints.",
   "Target organisation, governance model, delegation matrix, KPIs by role.",
   "Target operating model, organisation chart, RACI, delegation matrix."),
  ("Investment", "Available budget, cash flow, supplier quotes, acceptable risk.",
   "CAPEX and OPEX analysis, ROI and payback modelling, business cases, prioritisation.",
   "Investment plan, ROI model, business-case portfolio."),
 ]),
 ("Plan", "The approved strategy is broken down into work packages with owners, milestones, budget, risks and acceptance criteria.", [
  ("Project governance", "Approved roadmap, internal sponsor, stakeholders, approved budget, time constraints.",
   "Project charter, work breakdown structure, RACI, communication plan, reporting model.",
   "Project charter, WBS, RACI matrix, governance calendar."),
  ("Resources", "Staff availability, internal skills, calendar, existing partners.",
   "Skill matching, capacity allocation, make-or-buy, allocation of Next Mind units.",
   "Resource plan, team structure, work-package map."),
  ("Risks", "Known risks, legal and IT constraints, supplier dependencies, past problems.",
   "Risk identification and scoring, mitigation, contingency and escalation procedure.",
   "Risk register, risk matrix, mitigation and contingency plans."),
  ("Procurement", "Current suppliers and contracts, technical specifications, purchasing budget and policy.",
   "RFQ and RFP preparation, supplier shortlist and comparison, service levels.",
   "Procurement plan, supplier scorecard, RFQ/RFP package."),
  ("Technology", "System access, user requirements, data to migrate, required integrations.",
   "Solution architecture, functional and technical specifications, migration, test and go-live plans.",
   "Solution architecture, test plan, go-live checklist."),
  ("Change", "Affected users and roles, known resistance, training plans.",
   "Change impact analysis, stakeholder engagement, training and adoption measures.",
   "Change management plan, training calendar, adoption plan."),
 ]),
 ("Deliver", "The responsible units execute while one coordinator keeps the client, the plan and the units aligned.", [
  ("Coordination", "Approved plan, available sponsor, timely decisions, deliverable approvals.",
   "Operational PMO, steering meetings, status reporting, issue and decision tracking.",
   "Weekly status report, issue log, decision log, steering pack."),
  ("Software", "Functional requirements, key users, data, system access, acceptance criteria.",
   "Analysis, design, development, configuration, integration, testing, training, release.",
   "Software release, test report, user manual, acceptance report."),
  ("Engineering", "Specifications, existing drawings, samples, materials, quality standards.",
   "CAD design, reverse engineering, bill of materials, design review, prototype support.",
   "3D models, 2D drawings, BOM, technical package."),
  ("Manufacturing", "Approved drawings, BOM, quantities, tolerances, quality and packaging requirements.",
   "Production planning, machining, welding, assembly, inspection, testing, packaging.",
   "Inspection and test reports, packing list, completion report."),
  ("Trade and logistics", "Delivery address, Incoterms, product codes, goods value, customs requirements, insurance.",
   "Supplier coordination, purchase orders, shipment booking, customs documents, tracking.",
   "Shipping and customs documents, tracking report, delivery confirmation."),
  ("AI and automation", "Manual processes, recurring documents, templates, datasets, validation rules.",
   "Use-case implementation, workflow automation, document processing, testing with users.",
   "Automation workflow, AI test report, user guide."),
 ]),
 ("Measure", "Results are compared with the baseline set in the assessment, so improvement is measured rather than claimed.", [
  ("Financial", "Updated revenue, margins, costs, cash flow, budget against actual.", "ROI tracking, variance and cost analysis.", "Financial dashboard, ROI report."),
  ("Commercial", "Updated CRM, pipeline, quotes, orders, lost clients.", "Pipeline, conversion and retention tracking.", "Sales dashboard, pipeline review."),
  ("Operational", "Production, OEE, cycle and set-up times, scrap, deliveries.", "OEE, scrap, productivity and delivery review.", "Operations dashboard, OEE report."),
  ("Project", "Activity updates, approvals, open issues, change requests.", "Milestone, budget, risk and change control.", "PMO dashboard, milestone report."),
  ("Digital and AI", "User logs, usage data, errors, user feedback, automation logs.", "Adoption, data-quality, accuracy and time-saving analysis.", "Adoption report, AI performance report."),
 ]),
 ("Improve", "The project becomes a routine: problems found, owners assigned, results reviewed every quarter and every year.", [
  ("Continuous improvement", "Updated KPIs, scrap and non-conformity data, operator suggestions.", "Root-cause analysis, kaizen workshops, standardisation, follow-up.", "Improvement plan, kaizen board, updated procedures."),
  ("Knowledge", "Procedures, manuals, technical documents, lessons learned.", "Knowledge-base design, procedure standardisation, document control.", "Knowledge base, procedure library, lessons-learned record."),
  ("Reviews", "Quarterly and annual results, open problems, new priorities.", "Quarterly business review and annual strategic review.", "Review report, updated roadmap and targets."),
 ]),
]

def build():
    blocks = []
    for i, (name, summary, steps) in enumerate(PHASES, 1):
        det = "".join(f"""
<details class="step"><summary>{s}</summary><div class="step-body">
  <div><h4>You provide</h4><p>{a}</p></div>
  <div><h4>We do</h4><p>{b}</p></div>
  <div><h4>You receive</h4><p>{c}</p></div>
</div></details>""" for s, a, b, c in steps)
        blocks.append(f"""
<section class="phase{' first' if i == 1 else ''}" id="{name.lower()}" aria-labelledby="ph-{i}">
  <div><span class="num" aria-hidden="true">{i}</span><h2 id="ph-{i}">{name}</h2><p class="muted">{summary}</p></div>
  <div>{det}</div>
</section>""")
    from pages_home import PHASES as SHORT
    toc = "".join(f'<li><h3><a href="#{n.lower()}">{n}</a></h3><p>{t}</p></li>' for n, t in SHORT)
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / How we work</p>
    <h1>Six phases. Every input and output named.</h1>
    <p class="lead">Each phase lists what we ask from you, what we do with it and the documents you receive. Nothing moves to the next phase until its outputs are reviewed with you.</p>
  </div>
</section>
<section class="section band" style="padding-top:clamp(48px,6vw,80px)">
  <div class="wrap"><ol class="phases">{toc}</ol></div>
</section>
<div class="wrap" style="padding-bottom:var(--space)">{''.join(blocks)}</div>
<section class="section ink">
  <div class="wrap cta">
    <div><h2>You do not have to start at phase one.</h2></div>
    <div><p>A company with a clear technical need can start at Plan or Deliver, for example with an engineering package or a pilot workflow. We agree the entry point in the first conversation.</p>
    <div class="actions"><a class="btn" href="contact.html">Start a project</a><a class="btn line" href="working-with-us.html">Engagement models</a></div></div>
  </div>
</section>"""
    return page("approach.html", "How we work",
                "The Next Mind execution framework: six phases from assessment to continuous improvement, with the inputs, activities and documents of each step.",
                body, current="approach.html")
