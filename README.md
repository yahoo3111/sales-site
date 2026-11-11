# Sales site (Anderson Sam)

Two sample sales pages plus a worked example, served by a dependency-free
Python static server (`app.py`). Deployed on uppcoder from this repository.

- `/` - B track: tender alerts for small contractors
- `/freight-invoice-audit` - A track: freight invoice audit and cost reconciliation
- `/worked-example` - the full worked example for the audit output
- `/robots.txt`, `/sitemap.xml`, `/og-image.png` - SEO and link-preview files

Forms POST to formcarry; payments are Stripe payment links. Published prices
must stay aligned with the Stripe products the buttons point at:
B track GBP 24/59/89 (monthly) and 240/590/890 (yearly); A track USD
149/299/549 (monthly) and 1490/2990/5490 (yearly).
