# Sales site - Docu (A) and Beacon (B)

Two public pages replacing the Substack sample pages, served as static files by nginx.

- `/` - The Tender Alert for Small Contractors - Sample (Beacon, GBP, Stripe checkout)
- `/freight-invoice-audit` - Freight Invoice Audit & Cost Reconciliation (Docu, USD list prices, enquiry form)
- `/worked-example` - the full worked example (sample invoice ANF-INV-2026-004918)

## Price source: Stripe (live)

Beacon plans, all verified active in Stripe on 2026-11-10:

- Starter GBP 24/month - https://buy.stripe.com/eVq7sLalD2mA0pod1N9EI03
- Starter GBP 240/year - https://buy.stripe.com/5kQ8wP79r9P22xwf9V9EI00
- Professional GBP 59/month - https://buy.stripe.com/8x27sL8dve5ic864vh9EI01
- Professional GBP 590/year - https://buy.stripe.com/7sY28rctL8KYb42f9V9EI02
- Business GBP 89/month - https://buy.stripe.com/bJe14nfFX8KY9ZYe5R9EI05
- Business GBP 890/year - https://buy.stripe.com/3cI14nctLbXa8VUf9V9EI04

Docu prices are not in Stripe (no Docu product exists there). They are the published
list prices from the service documentation: USD 149 / 299 / 549 per month (50 / 150 / 300
packets) and a single audit at USD 199 (up to 20 packets, one carrier, one rate card).

## Form

Both pages post to https://formcarry.com/s/VxTz_0yxAnA (Formcarry form "Docu and Beacon
enquiries", email notifications to yhaoo3111@gmail.com).

## Deploy

uppcoder autobuild from the public GitHub repo. The Dockerfile serves the static files
with nginx on port 80; clean URLs come from try_files ($uri $uri.html).
