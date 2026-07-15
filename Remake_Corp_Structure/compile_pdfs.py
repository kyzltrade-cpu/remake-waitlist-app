import os
import csv
import re
from playwright.sync_api import sync_playwright

# Define the paths
BASE_DIR = "/Users/kyzl/Remake_Corp_Structure"
OUTPUT_DIR = "/Users/kyzl/Remake_Corp_Structure"

def read_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def parse_md_to_pages(content):
    # Split content by '## ' to separate into different pages
    parts = content.split("## ")
    pages = []
    
    # Page 1: Title and initial intro
    title_part = parts[0].strip()
    title = ""
    subtitle = ""
    body_html = ""
    
    lines = title_part.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            title = line[2:]
        elif line.startswith("*") and line.endswith("*"):
            subtitle = line[1:-1]
        elif line:
            # Simple markdown conversion for bold/italic/links
            line_html = format_inline_md(line)
            body_html += f'<p class="font-sans text-xs text-[#5C5350] mb-4 leading-relaxed">{line_html}</p>'
            
    pages.append({
        "is_cover": True,
        "title": title,
        "subtitle": subtitle,
        "content": body_html
    })
    
    # Subsequent pages
    for part in parts[1:]:
        part = part.strip()
        if not part:
            continue
        lines = part.split("\n")
        heading = lines[0].strip()
        body_html = ""
        
        in_list = False
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
                
            # Handle list items
            if line.startswith("* ") or line.startswith("- "):
                if not in_list:
                    body_html += '<ul class="space-y-3 mb-4">'
                    in_list = True
                item_content = format_inline_md(line[2:])
                # Check for checkbox list item
                if "[ ]" in line or "[-]" in line or "[x]" in line or "[X]" in line:
                    item_content = item_content.replace("[ ]", "").replace("[x]", "").replace("[X]", "").strip()
                    body_html += f'''
                    <li class="font-sans text-xs text-[#5C5350] flex items-start gap-2">
                        <span class="w-3 h-3 rounded border border-[#D98A96] flex-shrink-0 mt-0.5 bg-[#FFF0F5]"></span>
                        <span>{item_content}</span>
                    </li>'''
                else:
                    body_html += f'''
                    <li class="font-sans text-xs text-[#5C5350] flex items-start gap-2">
                        <span class="w-1.5 h-1.5 rounded-full bg-[#D98A96] flex-shrink-0 mt-1.5"></span>
                        <span>{item_content}</span>
                    </li>'''
            elif line.startswith("### "):
                if in_list:
                    body_html += '</ul>'
                    in_list = False
                subheading = format_inline_md(line[4:])
                body_html += f'<h3 class="font-sans text-[10px] tracking-[0.15em] uppercase text-[#D98A96] font-semibold mt-6 mb-2">{subheading}</h3>'
            elif line.startswith("---"):
                if in_list:
                    body_html += '</ul>'
                    in_list = False
                body_html += '<hr class="border-t border-[#EAE6E1] my-6" />'
            else:
                if in_list:
                    body_html += '</ul>'
                    in_list = False
                # Handle signature blocks
                if "SIGNATURE:" in line or "___________________________" in line or "Kyle Cheung" in line and len(line) < 30 and "_" in line:
                    body_html += f'<div class="mt-8 pt-4 border-t border-[#EAE6E1] w-48"><p class="font-serif italic text-sm text-[#2E2724]">{line.replace("___________________________", "").replace("SIGNATURE:", "").strip()}</p></div>'
                else:
                    line_html = format_inline_md(line)
                    # Specific callout classes
                    if line.startswith("⚠️") or line.startswith("*CFO Note:") or line.startswith("*CFO Directive:"):
                        body_html += f'<div class="p-4 bg-[#FFF5F7] border-l-2 border-[#D98A96] rounded-r-xl mb-4"><p class="font-sans text-xs text-[#2E2724] leading-relaxed">{line_html}</p></div>'
                    else:
                        body_html += f'<p class="font-sans text-xs text-[#5C5350] mb-4 leading-relaxed">{line_html}</p>'
                        
        if in_list:
            body_html += '</ul>'
            
        pages.append({
            "is_cover": False,
            "heading": heading,
            "content": body_html
        })
        
    return pages

def format_inline_md(text):
    # Bold **
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong class="font-semibold text-[#2E2724]">\1</strong>', text)
    # Italic *
    text = re.sub(r'\*(.*?)\*', r'<em class="italic text-[#2E2724]">\1</em>', text)
    # Underline/Link [text](url)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" class="text-[#D98A96] underline hover:text-[#C5A059]">\1</a>', text)
    # Emojis/Icons substitutions or wrappers
    return text

def compile_markdown_pdf(md_path, pdf_path):
    print(f"Compiling Markdown to PDF: {md_path} -> {pdf_path}")
    content = read_markdown(md_path)
    pages = parse_md_to_pages(content)
    
    html_pages = ""
    for idx, page in enumerate(pages):
        page_num = idx + 1
        total_pages = len(pages)
        
        if page.get("is_cover", False):
            # Cover Page or Intro Page
            content_html = f'''
            <div class="flex-grow flex flex-col justify-center max-w-xl">
                <div class="h-1 w-12 bg-[#D98A96] mb-8"></div>
                <h1 class="font-serif text-4xl font-light text-[#2E2724] leading-tight mb-3">{page["title"]}</h1>
                {f'<p class="font-sans text-xs tracking-[0.2em] uppercase text-[#D98A96] font-semibold mb-8">{page["subtitle"]}</p>' if page["subtitle"] else ""}
                <div class="border-t border-[#EAE6E1] pt-6 mt-4">
                    {page["content"]}
                </div>
            </div>'''
        else:
            # Standard Content Page
            content_html = f'''
            <div class="flex-grow">
                <h2 class="font-serif text-2xl font-light text-[#2E2724] border-b border-[#EAE6E1] pb-3 mb-6">{page["heading"]}</h2>
                <div class="content-body space-y-4">
                    {page["content"]}
                </div>
            </div>'''
            
        html_pages += f'''
        <div class="page">
            <!-- HEADER -->
            <div class="flex justify-between items-center border-b border-[#EAE6E1] pb-3 mb-6">
                <span class="font-serif italic text-base text-[#2E2724]">Remake</span>
                <span class="font-sans text-[8px] tracking-[0.25em] uppercase text-[#D98A96] font-semibold">Corporate Governance & Strategy</span>
            </div>
            
            <!-- BODY -->
            {content_html}
            
            <!-- FOOTER -->
            <div class="flex justify-between items-center border-t border-[#EAE6E1] pt-3 mt-6">
                <span class="font-sans text-[8px] tracking-[0.1em] text-[#A69B97]">REMAKE INC. | STANDALONE BUSINESS PLAN</span>
                <span class="font-sans text-[8px] tracking-[0.1em] text-[#A69B97] font-medium">Page {page_num} of {total_pages}</span>
            </div>
        </div>'''
        
    render_html_to_pdf(html_pages, pdf_path, landscape=False)

def compile_csv_pdf(csv_path, pdf_path, landscape=False):
    print(f"Compiling CSV to PDF: {csv_path} -> {pdf_path}")
    
    title = os.path.basename(csv_path).replace(".csv", "").replace("_", " ").title()
    if "Pnl" in title:
        title = "Remake Pro Forma P&L Forecast (SaaS Metrics)"
    elif "Cap Table" in title:
        title = "Remake Capitalization & Founder Equity Table"
    elif "Zero Cost" in title or "Zero_Cost" in title:
        title = "Remake Zero-Cost Technology Infrastructure Stack"
    elif "Chart Of Accounts Bootstrapped" in title:
        title = "Remake Bootstrapped Chart of Accounts (Sole Prop Phase)"
    elif "Chart Of Accounts" in title:
        title = "Remake Standard Chart of Accounts (C-Corp Phase)"
        
    rows = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                rows.append(row)
                
    if not rows:
        return
        
    headers = rows[0]
    data_rows = rows[1:]
    
    # Process potential footer/notes at the end of CSV
    notes = []
    filtered_data_rows = []
    for r in data_rows:
        if r and len(r) > 0 and (r[0].startswith("*") or r[0].strip() == ""):
            notes.append(" ".join(filter(None, r)))
        else:
            filtered_data_rows.append(r)
            
    table_headers_html = "".join([f'<th class="font-sans text-[9px] tracking-[0.15em] uppercase font-semibold text-[#D98A96] bg-[#FFF5F7] px-3 py-3 text-left border-b border-[#EAE6E1]">{h}</th>' for h in headers])
    
    table_rows_html = ""
    for idx, row in enumerate(filtered_data_rows):
        bg_class = "bg-[#FCFBF9]" if idx % 2 == 0 else "bg-[#FAF6F0]"
        row_cells = ""
        for cell in row:
            # Right-align numbers, left-align text
            is_num = re.match(r'^\s*[\$\d\.,%-]+\s*$', cell)
            align_class = "text-right font-mono" if is_num else "text-left"
            bold_class = "font-semibold text-[#2E2724]" if "TOTAL" in row or "Total" in row else "text-[#5C5350]"
            row_cells += f'<td class="px-3 py-3 text-xs border-b border-[#EAE6E1] {align_class} {bold_class}">{cell}</td>'
        table_rows_html += f'<tr class="{bg_class} hover:bg-[#FFF0F5] transition-colors duration-150">{row_cells}</tr>'
        
    notes_html = ""
    if notes:
        notes_html = f'''
        <div class="mt-6 p-4 bg-[#FFF5F7] border-l-2 border-[#D98A96] rounded-r-xl max-w-3xl">
            <h4 class="font-sans text-[9px] tracking-[0.15em] uppercase font-semibold text-[#D98A96] mb-2">Accountant Notes & Assumptions</h4>
            <ul class="space-y-1">
                {"".join([f'<li class="font-sans text-[10px] text-[#5C5350] list-none">{n}</li>' for n in notes])}
            </ul>
        </div>'''
        
    html_pages = f'''
    <div class="page {"landscape" if landscape else ""}">
        <!-- HEADER -->
        <div class="flex justify-between items-center border-b border-[#EAE6E1] pb-3 mb-6">
            <span class="font-serif italic text-base text-[#2E2724]">Remake</span>
            <span class="font-sans text-[8px] tracking-[0.25em] uppercase text-[#D98A96] font-semibold">Financial Treasury Ledger</span>
        </div>
        
        <!-- BODY -->
        <div class="flex-grow flex flex-col">
            <h1 class="font-serif text-3xl font-light text-[#2E2724] mb-2">{title}</h1>
            <p class="font-sans text-[9px] tracking-[0.2em] uppercase text-[#D98A96] font-semibold mb-6">Corporate Accounts and Financial Infrastructure</p>
            
            <div class="overflow-x-auto border border-[#EAE6E1] rounded-xl shadow-sm bg-[#FCFBF9]">
                <table class="min-w-full border-collapse">
                    <thead>
                        <tr>{table_headers_html}</tr>
                    </thead>
                    <tbody>
                        {table_rows_html}
                    </tbody>
                </table>
            </div>
            
            {notes_html}
        </div>
        
        <!-- FOOTER -->
        <div class="flex justify-between items-center border-t border-[#EAE6E1] pt-3 mt-6">
            <span class="font-sans text-[8px] tracking-[0.1em] text-[#A69B97]">REMAKE INC. | STARTUP FINANCIAL LEDGER</span>
            <span class="font-sans text-[8px] tracking-[0.1em] text-[#A69B97] font-medium">Page 1 of 1</span>
        </div>
    </div>'''
    
    render_html_to_pdf(html_pages, pdf_path, landscape=landscape)

def compile_sql_pdf(sql_path, pdf_path):
    print(f"Compiling SQL Database Schema to PDF: {sql_path} -> {pdf_path}")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql_content = f.read()
        
    # Format code comments and statement groupings
    formatted_code = html_escape(sql_content)
    # Simple syntax highlighting for SQL
    keywords = ["CREATE", "TABLE", "IF", "NOT", "EXISTS", "PRIMARY", "KEY", "DEFAULT", "UNIQUE", "REFERENCES", "CASCADE", "TIMESTAMP", "WITH", "TIME", "ZONE", "TEXT", "BOOLEAN", "UUID", "INT", "NUMERIC", "EXTENSION", "ON", "DELETE"]
    for kw in keywords:
        formatted_code = re.sub(rf'\b{kw}\b', f'<span class="text-[#E2C08D] font-semibold">{kw}</span>', formatted_code)
        
    # Types highlighting
    types = ["UUID", "TEXT", "BOOLEAN", "TIMESTAMP", "WITH TIME ZONE", "INT", "NUMERIC", "NUMERIC\(10, 6\)", "NUMERIC\(10, 2\)"]
    for t in types:
        formatted_code = re.sub(rf'\b{t}\b', f'<span class="text-[#84C1E8]">{t}</span>', formatted_code)
        
    # Comments highlighting
    formatted_code = re.sub(r'(--.*?)(?=\n|$)', r'<span class="text-[#8E908C] italic">\1</span>', formatted_code)
    
    html_pages = f'''
    <div class="page">
        <!-- HEADER -->
        <div class="flex justify-between items-center border-b border-[#EAE6E1] pb-3 mb-6">
            <span class="font-serif italic text-base text-[#2E2724]">Remake</span>
            <span class="font-sans text-[8px] tracking-[0.25em] uppercase text-[#D98A96] font-semibold">Technical Infrastructure Schema</span>
        </div>
        
        <!-- BODY -->
        <div class="flex-grow flex flex-col justify-between">
            <div>
                <h1 class="font-serif text-3xl font-light text-[#2E2724] mb-2">Remake Core Database Ledger</h1>
                <p class="font-sans text-[9px] tracking-[0.2em] uppercase text-[#D98A96] font-semibold mb-6">Database Schema & Entitlement Logic Architecture</p>
                
                <div class="p-4 bg-[#FFF5F7] border-l-2 border-[#D98A96] rounded-r-xl mb-6 max-w-xl">
                    <p class="font-sans text-xs text-[#2E2724] leading-relaxed">
                        <strong class="font-semibold text-[#D98A96]">CFO Mandate:</strong> We must track exact LLM token usage per user to calculate unit economics and ensure our $9.99/mo subscription has a profitable gross margin.
                    </p>
                </div>
                
                <!-- macOS-Style Code Window -->
                <div class="rounded-2xl border border-[#EAE6E1] shadow-lg overflow-hidden bg-[#1F1917] max-w-3xl">
                    <!-- Window Controls -->
                    <div class="flex items-center gap-1.5 px-4 py-3 bg-[#2D2421] border-b border-[#3A2F2B]">
                        <span class="w-3 h-3 rounded-full bg-[#EF5A5A]"></span>
                        <span class="w-3 h-3 rounded-full bg-[#E1A141]"></span>
                        <span class="w-3 h-3 rounded-full bg-[#53B753]"></span>
                        <span class="font-mono text-[10px] text-[#A69B97] ml-2 font-medium">schema.sql — Remake Backend Ledger</span>
                    </div>
                    <!-- Code Space -->
                    <pre class="p-6 font-mono text-[11px] leading-relaxed text-[#FAF6F0] overflow-x-auto font-light">{formatted_code}</pre>
                </div>
            </div>
        </div>
        
        <!-- FOOTER -->
        <div class="flex justify-between items-center border-t border-[#EAE6E1] pt-3 mt-6">
            <span class="font-sans text-[8px] tracking-[0.1em] text-[#A69B97]">REMAKE INC. | TECHNICAL LEDGER DEPLOYMENT</span>
            <span class="font-sans text-[8px] tracking-[0.1em] text-[#A69B97] font-medium">Page 1 of 1</span>
        </div>
    </div>'''
    
    render_html_to_pdf(html_pages, pdf_path, landscape=False)

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

def render_html_to_pdf(html_content, output_pdf_path, landscape=False):
    # Construct complete HTML page
    html_document = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            @page {{
                size: {"A4 landscape" if landscape else "A4"};
                margin: 0;
            }}
            body {{
                margin: 0;
                padding: 0;
                -webkit-print-color-adjust: exact;
                background-color: #FAF6F0;
                color: #2E2724;
                font-family: 'Plus Jakarta Sans', sans-serif;
            }}
            .page {{
                width: {"297mm" if landscape else "210mm"};
                height: {"210mm" if landscape else "297mm"};
                box-sizing: border-box;
                background-color: #FAF6F0;
                overflow: hidden;
                position: relative;
                page-break-after: always;
                padding: 24mm 20mm;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}
            .page.landscape {{
                width: 297mm;
                height: 210mm;
                padding: 18mm 18mm;
            }}
            .content-body h3 {{
                font-family: 'Plus Jakarta Sans', sans-serif;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    temp_html_path = "/tmp/temp_pdf_render.html"
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_document)
        
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        path = os.path.abspath(temp_html_path)
        page.goto(f"file://{path}")
        
        # Wait for CDN and google fonts
        page.wait_for_timeout(1800)
        
        page.pdf(
            path=output_pdf_path,
            format="A4",
            landscape=landscape,
            print_background=True,
            margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
        )
        browser.close()
        
    print(f"Generated successfully: {output_pdf_path}")

def run_all_compilations():
    print("Initiating full Remake PDF compilation suite...")
    
    # 1. Delaware Playbook (MD)
    compile_markdown_pdf(
        os.path.join(BASE_DIR, "Legal/Delaware_CCorp_Incorporation_Playbook.md"),
        os.path.join(OUTPUT_DIR, "Legal/Remake_Delaware_CCorp_Incorporation_Playbook.pdf")
    )
    
    # 2. Operating Agreement (MD)
    compile_markdown_pdf(
        os.path.join(BASE_DIR, "Legal/Operating_Agreement_SoleProp.md"),
        os.path.join(OUTPUT_DIR, "Legal/Remake_Operating_Agreement_SoleProp.pdf")
    )
    
    # 3. IRS 83(b) Election (MD)
    compile_markdown_pdf(
        os.path.join(BASE_DIR, "Legal/IRS_83b_Election_Template.md"),
        os.path.join(OUTPUT_DIR, "Legal/Remake_IRS_83b_Election_Template.pdf")
    )
    
    # 4. Founder IP Assignment (MD)
    compile_markdown_pdf(
        os.path.join(BASE_DIR, "Legal/Founder_IP_Assignment.md"),
        os.path.join(OUTPUT_DIR, "Legal/Remake_Founder_IP_Assignment_Agreement.pdf")
    )
    
    # 5. Contractor NDA (MD)
    compile_markdown_pdf(
        os.path.join(BASE_DIR, "Legal/Contractor_NDA_IP_Agreement.md"),
        os.path.join(OUTPUT_DIR, "Legal/Remake_Contractor_NDA_IP_Agreement.pdf")
    )
    
    # 6. Expense Reimbursement Policy (MD)
    compile_markdown_pdf(
        os.path.join(BASE_DIR, "Accounting/Expense_Reimbursement_Policy.md"),
        os.path.join(OUTPUT_DIR, "Accounting/Remake_Expense_Reimbursement_Policy.pdf")
    )
    
    # 7. Launch Checklist (MD)
    compile_markdown_pdf(
        os.path.join(BASE_DIR, "Launch_Checklist.md"),
        os.path.join(OUTPUT_DIR, "Remake_Launch_Checklist.pdf")
    )
    
    # 8. Org Chart Matrix (MD)
    compile_markdown_pdf(
        os.path.join(BASE_DIR, "Org_Chart_Matrix.md"),
        os.path.join(OUTPUT_DIR, "Remake_Org_Chart_Matrix.pdf")
    )
    
    # 9. Cap Table (CSV)
    compile_csv_pdf(
        os.path.join(BASE_DIR, "Cap_Table.csv"),
        os.path.join(OUTPUT_DIR, "Remake_Cap_Table.pdf")
    )
    
    # 10. Zero-Cost Infrastructure Tech Stack (CSV)
    compile_csv_pdf(
        os.path.join(BASE_DIR, "Zero_Cost_Stack.csv"),
        os.path.join(OUTPUT_DIR, "Remake_Zero_Cost_Tech_Stack.pdf")
    )
    
    # 11. Chart of Accounts Bootstrapped (CSV)
    compile_csv_pdf(
        os.path.join(BASE_DIR, "Chart_of_Accounts_Bootstrapped.csv"),
        os.path.join(OUTPUT_DIR, "Accounting/Remake_Chart_of_Accounts_Bootstrapped.pdf")
    )
    
    # 12. Chart of Accounts C-Corp (CSV)
    compile_csv_pdf(
        os.path.join(BASE_DIR, "Chart_of_Accounts.csv"),
        os.path.join(OUTPUT_DIR, "Accounting/Remake_Chart_of_Accounts_CCorp.pdf")
    )
    
    # 13. Pro Forma P&L (CSV) - LANDSCAPE
    compile_csv_pdf(
        os.path.join(BASE_DIR, "Accounting/Pro_Forma_PnL.csv"),
        os.path.join(OUTPUT_DIR, "Accounting/Remake_Pro_Forma_PnL.pdf"),
        landscape=True
    )
    
    # 14. SQL Schema (SQL)
    compile_sql_pdf(
        os.path.join(BASE_DIR, "app/db/schema.sql"),
        os.path.join(OUTPUT_DIR, "app/db/Remake_Database_Schema.pdf")
    )
    
    print("All 14 PDFs have been successfully compiled with our ultra-premium Gen Z pink and cream editorial styling!")

if __name__ == "__main__":
    run_all_compilations()
