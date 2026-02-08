from datetime import date

from django.core.management.base import BaseCommand

from core.models import CreditRating, Insight, TeamMember, Methodology, FAQItem


class Command(BaseCommand):
    help = 'Seed Transparency Analytics data'

    def handle(self, *args, **options):
        # Clear existing data
        CreditRating.objects.all().delete()
        Insight.objects.all().delete()
        TeamMember.objects.all().delete()
        Methodology.objects.all().delete()
        FAQItem.objects.all().delete()

        # Credit Ratings - Current (from real site)
        current_ratings = [
            ('Microsoft', 'Technology \u2013 Software/Diversified', 'AAA', 'Stable'),
            ('Accenture Plc.', 'Technology \u2013 Services', 'AA-', 'Stable'),
            ('Costco Wholesale Corporation', 'Retail', 'AA-', 'Stable'),
            ('Merck & Co, Inc', 'Healthcare \u2013 Pharmaceuticals', 'A+', 'Stable'),
            ('Comcast Corporation', 'Media & Communications', 'A-', 'Stable'),
            ('Halliburton Company', 'Oilfield Services', 'A-', 'Stable'),
            ('Dover Corporation', 'Industrials', 'BBB+', 'Stable'),
            ('Stryker Corporation', 'Healthcare \u2013 Products', 'BBB+', 'Stable'),
            ('Westlake Corporation', 'Chemicals', 'BBB', 'Stable'),
            ('Martin Marietta Materials', 'Basic Materials', 'BBB', 'Stable'),
            ('Conagra Brands Inc.', 'Consumer \u2013 Foods', 'BBB-', 'Stable'),
            ('Perdoceo Education Corporation', 'Education', 'BBB-', 'Stable'),
            ('Wyndham', 'Lodging', 'BB+', 'Stable'),
            ('Tenet Healthcare Corp', 'Healthcare \u2013 Services', 'BB', 'Stable'),
            ('TTM Technologies, Inc', 'Technology \u2013 Hardware & Components', 'BB', 'Positive'),
            ('Varex Imaging Corporation', 'Healthcare \u2013 Technology', 'B+', 'Stable'),
            ('ACCO Brands Corporation', 'Consumer \u2013 Products', 'B', 'Stable'),
            ('Holley Inc.', 'Automotive Suppliers', 'B', 'Stable'),
            ('USA Today', 'Media & Marketing', 'B-', 'Stable'),
            ('B&G Foods Inc.', 'Consumer \u2013 Foods', 'B-', 'Stable'),
        ]
        for i, (issuer, industry, rating, outlook) in enumerate(current_ratings):
            CreditRating.objects.create(
                issuer=issuer, industry=industry, rating=rating,
                outlook=outlook, is_previous=False, order=i,
            )

        # Credit Ratings - Previous
        CreditRating.objects.create(
            issuer='Beacon Roofing Supply, Inc.', industry='Distribution',
            rating='BB', outlook='Stable', is_previous=True, order=0,
        )

        # Insights (from real site) - (title, author, date, slug, description, external_url)
        insights_data = [
            ('Trends Point to Increased Private Credit Transparency',
             'Reetika Anand', date(2025, 10, 28),
             'trends-point-to-increased-private-credit-transparency',
             'Private credit has experienced rapid growth over the past decade, often outside the scope of traditional regulatory frameworks.',
             ''),
            ('Tokenization and Private Credit: How Well do Worlds Collide?',
             'Yashi Yadav', date(2025, 9, 15),
             'block-chain-09-2025',
             'Analysis of blockchain technology reshaping private credit. Explores how tokenized debt converts traditional lending into on-chain digital assets.',
             'https://www.transparency-analytics.com/s/TA-Tokenized-Debt.pdf'),
            ('The Rise of Private Credit in a High-Rate Environment: Opportunity or Risk?',
             'Reetika Anand', date(2025, 9, 15),
             'direct-lending-innovation-07-2025',
             'Examines direct lending growth to middle market and larger companies, exploring the asset class\u2019s risk-return profile and positive borrower effects.',
             'https://www.transparency-analytics.com/s/Rise-of-Private-Credit-09-2025.pdf'),
            ('Private Credit Liquidity: Implications for Product Expansion',
             'Michael Brawer', date(2025, 8, 15),
             'private-credit-liquidity',
             'Discusses State Street and Apollo\u2019s private credit ETF collaboration and its implications for market liquidity and product expansion.',
             'https://www.transparency-analytics.com/s/Private-Credit-Liquidity-08-2025.pdf'),
            ('Direct Lending: Lower Rates Would Add Cushion to Metrics, but Growth Support More Significant',
             'Peter Krukovsky', date(2025, 8, 15),
             'direct-lending-lower-rates',
             'Analyzes potential FOMC rate reductions and their effects on borrower credit profiles, addressing limited cash flow cushions.',
             'https://www.transparency-analytics.com/s/Direct-Lending-08-2025.pdf'),
            ('Direct Lending: Innovation Expanding Access to Credit and Supporting Growth',
             'Peter Krukovsky', date(2025, 7, 15),
             'direct-lending-innovation',
             'Explores positive effects of direct lending for borrower companies within the growing private credit sector.',
             'https://www.transparency-analytics.com/s/Direct-Lending-07-2025.pdf'),
        ]
        for title, author, d, slug, description, ext_url in insights_data:
            Insight.objects.create(
                title=title, author=author, date=d,
                slug=slug, description=description, content='',
                external_url=ext_url,
            )

        # Team Members (from real site)
        team_data = [
            ('Michael Brawer', 'CEO',
             'Financial services executive with expertise in risk management and operations.',
             'https://www.linkedin.com/in/michael-brawer-60800714',
             'https://images.squarespace-cdn.com/content/v1/676f0347d4bf61676db08489/42743796-a80b-4753-a575-e8a34d40fd58/Michael.webp',
             1),
            ('Philip Galgano', 'Head of Analytics',
             'Experienced financial services professional with expertise in credit and capital markets.',
             'https://www.linkedin.com/in/philipgalgano/',
             'https://images.squarespace-cdn.com/content/v1/676f0347d4bf61676db08489/ea682e1a-21f5-4621-8ef7-8e343b294c28/Philip.webp',
             2),
            ('Kristin Costello', 'Chief Compliance Officer',
             'Experienced financial services and regulatory professional.',
             'https://www.linkedin.com/in/kristin-costello-9152b017a/',
             'https://images.squarespace-cdn.com/content/v1/676f0347d4bf61676db08489/a9166bed-b0cd-4f1e-ac92-fe13d74d7d31/Kristen.webp',
             3),
            ('Chris Tolles', 'COO',
             'Experienced Silicon Valley executive, entrepreneur & 3X co-founder.',
             'https://www.linkedin.com/in/tolles/',
             'https://images.squarespace-cdn.com/content/v1/676f0347d4bf61676db08489/05029ab2-c2ce-408a-823e-9f8a684fcc58/Chris.webp',
             4),
        ]
        for name, title, bio, linkedin, photo, order in team_data:
            TeamMember.objects.create(
                name=name, title=title, bio=bio,
                linkedin_url=linkedin, photo_url=photo, order=order,
            )

        # Methodologies (from real site)
        methodology_data = [
            ('Corporate Issuer Credit Rating',
             'Applied across all major NAIC sectors, the corporate issuer credit rating framework combines quantitative metrics with seasoned analyst judgment to produce ratings at both the issuer and issue level.',
             1),
            ('Real Estate SASB Rating Methodology',
             'Used for transactions involving a single borrower and a single asset, or a concentrated pool of fewer than 10 loans, the SASB framework assesses structural features, loan-to-value ratios, and property-level performance.',
             2),
            ('Project Finance Credit Rating Methodology',
             'Applicable to debt issued by special-purpose entities, the project finance framework evaluates transactions that develop and operate specific projects. Sectors include infrastructure, transportation, energy, and industrial assets, emphasizing long-term cash flow stability and structural resilience.',
             3),
            ('Credit Tenant Lease Rating Methodology',
             'Designed for commercial real estate transactions, the CTL framework focuses on tenant credit quality, lease cash flow durability, structural protections, and loss-given-default metrics to derive ratings.',
             4),
            ('ABL Rating Framework',
             'Focused on loans or credit facilities secured by receivables, inventory, or equipment, the ABL framework applies across industries and accommodates a broad suite of asset types.',
             5),
            ('Rating Scales',
             'Explore the frameworks used in our rating methodology.',
             6),
        ]
        for title, description, order in methodology_data:
            Methodology.objects.create(
                title=title, description=description, order=order,
            )

        # FAQ Items (from real site - verbatim)
        faq_data = [
            ('How quickly are ratings issued once all required documentation and analysis are complete?',
             'Because our analysis is based largely on quantitative modeling, Transparency Analytics can provide initial, indicative ratings and scenario planning in real-time through our automated credit ratings portal. From there full ratings can be purchased, following the execution of an engagement letter and receipt of all relevant deal documentation.'),
            ('Are your credit ratings actively utilized in live transactions?',
             'Transparency Analytics\u2019 ratings can be utilized in live transactions; however, please note that we are not registered as a Nationally Recognized Statistical Rating Organization (NRSRO) with the U.S. Securities and Exchange Commission.'),
            ('What types of credit do you rate?',
             'Transparency Analytics provides ratings across a broad spectrum of private credit transactions. This includes corporate issuers and instruments in their capital structures, asset-based finance deals backed by receivables, inventory, equipment, and real estate; stand-alone credits such as credit tenant leases, ground leases, and project finance transactions.'),
            ('Will I be able to use this in investor materials?',
             'Transparency Analytics Credit Ratings & Reports are designed to support investor discussions, IC memos, and diligence. Our credit ratings are provided as an analytical opinion and are not intended for regulatory purposes.'),
            ('Do your processes follow NAIC and SEC guidelines?',
             'Yes. Transparency Analytics\u2019 systems, methodologies, and workflows are designed to align with widely accepted regulatory frameworks, including those established by the NAIC and SEC, with a strong emphasis on transparency and auditability.'),
            ('Are you a registered Nationally Recognized Statistic Ratings Organization (NRSRO)?',
             'Transparency Analytics is not currently registered as a Nationally Recognized Statistical Rating Organization (NRSRO) with the U.S. Securities and Exchange Commission. However, our methodologies, systems, and procedures are designed to reflect the discipline, documentation standards, and scoring rigor consistent with NRSRO requirements.'),
            ('How does Transparency Analytics differ from other, legacy rating agencies?',
             'Transparency Analytics is built on a fundamentally different foundation tailored to the unique demands of private credit markets. Unlike legacy agencies that often rely heavily on qualitative assessments, our methodologies prioritize transparency and quantitative rigor.'),
            ('Is the platform fully automated?',
             'Transparency Analytics\u2019 credit analysis is approximately 85% quantitatively derived and fully automated indicative ratings based on quantitative modeling can be run in real-time.'),
            ('Who is Transparency Analytics and who is the platform built for?',
             'Transparency Analytics is purpose-built to meet the evolving needs of the private credit ecosystem. Our platform offers scalable, transparent credit ratings and risk evaluation tools specifically designed for underwriters, credit professionals, insurance companies, asset managers, and deal teams operating in private credit markets.'),
            ('What do I need to get started?',
             'If you have the proposed terms for your corporate debt instrument, you can gain access to Transparency Analytics\u2019 automated ratings portal to receive an initial indicative rating.'),
        ]
        for i, (question, answer) in enumerate(faq_data):
            FAQItem.objects.create(
                question=question, answer=answer, order=i,
            )

        self.stdout.write(self.style.SUCCESS(
            f'Seeded: {CreditRating.objects.count()} ratings, '
            f'{Insight.objects.count()} insights, '
            f'{TeamMember.objects.count()} team members, '
            f'{Methodology.objects.count()} methodologies, '
            f'{FAQItem.objects.count()} FAQs'
        ))
