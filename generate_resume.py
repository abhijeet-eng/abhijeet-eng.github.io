from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_PATH = "Abhijeet_Khandelwal_Resume.pdf"


PROFILE = {
    "name": "Abhijeet Khandelwal",
    "title": "AI Engineering Manager | ML Engineer",
    "location": "Austin, Texas Metropolitan Area",
    "phone": "+1-385-515-8567",
    "email": "abhijeetkhandelwal@outlook.com",
    "linkedin": "https://www.linkedin.com/in/abhijeet-khandelwal-9a034728/",
    "portfolio": "https://abhijeet-eng.github.io/",
    "summary": (
        "AI engineering manager and machine learning engineer with 12+ years of experience designing and "
        "scaling production AI, analytics, and data platforms. Brings hands-on depth in enterprise GenAI "
        "systems together with organizational leadership and business execution, including building an "
        "Intel Foundry-wide GenAI platform embedded in day-to-day engineering and manufacturing workflows and delivering systems tied to "
        "measurable productivity gains, savings, and modernized engineering workflows."
    ),
    "highlights": [
        ("Foundry-wide", "Daily GenAI platform usage across Intel Foundry"),
        ("10% gain", "Productivity improvement from GenAI workflows"),
        ("~$100M", "Yearly savings supported by delivered applications"),
    ],
    "experience": [
        {
            "company": "Intel Corporation",
            "role": "AI Engineering Manager | ML Engineer",
            "period": "April 2019 - Present",
            "location": "Austin, Texas Metropolitan Area",
            "bullets": [
                "Directed strategy, architecture, and delivery of GenAI, machine learning, analytics, and computer vision solutions for semiconductor manufacturing.",
                "Built and scaled Intel Foundry's GenAI platform into a Foundry-wide enterprise system supporting day-to-day engineering and manufacturing workflows.",
                "Designed multi-source knowledge discovery and retrieval workflows across SharePoint, Word documents, and factory systems to improve knowledge access, root cause analysis, and decision support.",
                "Partnered with business stakeholders, factory engineers, data scientists, and software teams to align roadmap, adoption, governance, and value realization, contributing to a 10% improvement in factory productivity.",
                "Led a 12-person team of engineers and data scientists while remaining hands-on in architecture reviews, platform design, technical direction, and mentoring.",
                "Delivered 3 production ML and analytics applications supporting roughly $100M in yearly manufacturing savings.",
                "Built CNN-based defect detection, localization, and quality prediction systems that contributed to $30M in yearly savings and improved developer productivity by 15% through cloud modernization.",
                "Developed large-scale Python, Airflow, and Modin ETL frameworks that standardized health metrics across Intel products and sites, saving work equivalent to 4 full-time employees.",
            ],
        },
        {
            "company": "EXL Services",
            "role": "Analytics Consultant",
            "period": "August 2018 - March 2019",
            "location": "Pittsburgh, Pennsylvania",
            "bullets": [
                "Developed analytical dashboards and ad hoc reporting workflows in Tableau, Alteryx, and SQL to support business decision-making.",
                "Built unsupervised models for customer segmentation and outlier detection, improving visibility into mortgage risk and delinquency trends.",
            ],
        },
        {
            "company": "Tata Consultancy Services",
            "role": "Analyst / Software Developer",
            "period": "July 2013 - July 2017",
            "location": "India",
            "bullets": [
                "Applied clustering-based machine learning techniques to fraud detection work for an audit organization.",
                "Developed tax collection modules for an African Revenue Services client using Java, SQL, JavaScript, and HTML.",
            ],
        },
    ],
    "skills": [
        ("AI & ML", "GenAI, RAG, enterprise search, AI agents, machine learning, computer vision, LangChain, LangGraph, AutoGen, PGVector, TensorFlow, PyTorch, Spark"),
        ("Languages", "Python, SQL, R, Scala, Java, JavaScript, HTML, Perl"),
        ("Platform", "Platform architecture, Airflow, Docker, Git, CI/CD, Ansible, Kafka, Sentry"),
        ("Analytics", "Power BI, Dash, Tableau, JMP, predictive analytics, data visualization"),
        ("Data Stores", "HBase, MongoDB, Azure Blob, MySQL, SQL Server, Redis"),
    ],
    "education": [
        "Master of Science in Information Systems, Concentration in Data Analytics - University at Buffalo, School of Management (2018)",
        "Bachelor of Science in Mechanical Engineering - Rajiv Gandhi Technical University (2013)",
    ],
    "certifications": (
        "SAS Base Programmer, ITIL V3 Foundation, Six Sigma Yellow Belt, Deep Learning Specialization, and MLOps Specialization"
    ),
    "publication": {
        "title": (
            "A virtual defect metrology system utilizing photolithography scanner topography maps to "
            "quantitatively detect gross defects, perform in-line yield prediction, and identify defect generating tools"
        ),
        "venue": "SPIE Proceedings 13426",
        "year": "2025",
        "url": "https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502264724243383",
    },
    "recognition": (
        "2 Group Recognition Awards, 16 Intel Division Recognition Awards, Intel Excellent Achievement Award, "
        "Superior Department Award, and 25+ peer recognitions"
    ),
}


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="HeaderName",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=24,
            textColor=colors.HexColor("#111827"),
            alignment=TA_LEFT,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="HeaderTitle",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=colors.HexColor("#0f766e"),
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="HeaderMeta",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=11.2,
            textColor=colors.HexColor("#4b5563"),
            alignment=TA_RIGHT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10.2,
            leading=12,
            textColor=colors.HexColor("#0f766e"),
            alignment=TA_LEFT,
            spaceBefore=5,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.0,
            leading=11.5,
            textColor=colors.HexColor("#1f2937"),
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyMuted",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.2,
            textColor=colors.HexColor("#4b5563"),
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Role",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.1,
            leading=11.8,
            textColor=colors.HexColor("#111827"),
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="RoleMeta",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.0,
            textColor=colors.HexColor("#6b7280"),
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ImpactValue",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=16,
            textColor=colors.HexColor("#111827"),
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ImpactLabel",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8.3,
            leading=10.3,
            textColor=colors.HexColor("#4b5563"),
            alignment=TA_LEFT,
        )
    )
    return styles


def add_section(story, title, styles):
    story.append(Spacer(1, 0.06 * inch))
    story.append(Paragraph(title, styles["SectionTitle"]))
    story.append(
        HRFlowable(
            width="100%",
            thickness=0.8,
            lineCap="round",
            color=colors.HexColor("#d7dde3"),
            spaceBefore=1,
            spaceAfter=4,
        )
    )


def bullet_list(bullets, styles):
    items = []
    for bullet in bullets:
        para = Paragraph(bullet, styles["Body"])
        items.append(ListItem(para, leftIndent=0))
    return ListFlowable(
        items,
        bulletType="bullet",
        leftIndent=12,
        bulletFontName="Helvetica",
        bulletFontSize=7.0,
        spaceBefore=1,
        spaceAfter=3,
    )


def build_resume():
    styles = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.5 * inch,
    )

    story = []

    left_header = Paragraph(
        f'{PROFILE["name"]}<br/><font size="10.5" color="#0f766e"><b>{PROFILE["title"]}</b></font>',
        styles["HeaderName"],
    )
    right_header = Paragraph(
        (
            f'{PROFILE["location"]}<br/>'
            f'{PROFILE["phone"]}<br/>'
            f'<link href="mailto:{PROFILE["email"]}">{PROFILE["email"]}</link><br/>'
            f'<link href="{PROFILE["linkedin"]}">LinkedIn</link> | '
            f'<link href="{PROFILE["portfolio"]}">Portfolio</link>'
        ),
        styles["HeaderMeta"],
    )
    header_table = Table([[left_header, right_header]], colWidths=[4.6 * inch, 2.25 * inch], hAlign="LEFT")
    header_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(header_table)
    story.append(Spacer(1, 0.08 * inch))
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.2,
            lineCap="round",
            color=colors.HexColor("#0f766e"),
            spaceBefore=0,
            spaceAfter=10,
        )
    )

    add_section(story, "Executive Summary", styles)
    story.append(Paragraph(PROFILE["summary"], styles["Body"]))

    highlight_cells = []
    for value, label in PROFILE["highlights"]:
        cell = Paragraph(
            f'<font size="14"><b>{value}</b></font><br/><font size="8.3" color="#4b5563">{label}</font>',
            styles["Body"],
        )
        highlight_cells.append(cell)
    highlight_table = Table([highlight_cells], colWidths=[2.23 * inch, 2.23 * inch, 2.23 * inch], hAlign="LEFT")
    highlight_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f6faf9")),
                ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#d4ebe7")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d4ebe7")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(Spacer(1, 0.09 * inch))
    story.append(highlight_table)

    add_section(story, "Professional Experience", styles)
    for entry in PROFILE["experience"]:
        block = [
            Paragraph(f'{entry["company"]} - {entry["role"]}', styles["Role"]),
            Paragraph(f'{entry["period"]} | {entry["location"]}', styles["RoleMeta"]),
            bullet_list(entry["bullets"], styles),
        ]
        story.append(KeepTogether(block))

    skills_block = []
    add_section(skills_block, "Core Expertise", styles)
    skill_rows = []
    for label, value in PROFILE["skills"]:
        skill_rows.append(
            [
                Paragraph(f"<b>{label}</b>", styles["Body"]),
                Paragraph(value, styles["Body"]),
            ]
        )
    skill_table = Table(skill_rows, colWidths=[1.28 * inch, 5.95 * inch], hAlign="LEFT")
    skill_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LINEBELOW", (0, 0), (-1, -2), 0.25, colors.HexColor("#d7dde3")),
            ]
        )
    )
    skills_block.append(skill_table)
    story.append(KeepTogether(skills_block))

    education_block = []
    add_section(education_block, "Education", styles)
    for line in PROFILE["education"]:
        education_block.append(Paragraph(line, styles["Body"]))
    education_block.append(Spacer(1, 0.03 * inch))
    education_block.append(Paragraph(f'<b>Certifications:</b> {PROFILE["certifications"]}', styles["Body"]))
    story.append(KeepTogether(education_block))

    add_section(story, "Publication", styles)
    pub = PROFILE["publication"]
    pub_text = (
        f'{pub["title"]}<br/>'
        f'<font color="#4b5563">{pub["venue"]} - {pub["year"]} - '
        f'<link href="{pub["url"]}">Reference</link></font>'
    )
    story.append(Paragraph(pub_text, styles["Body"]))

    add_section(story, "Recognition", styles)
    story.append(Paragraph(PROFILE["recognition"], styles["Body"]))

    doc.build(story)


if __name__ == "__main__":
    build_resume()
