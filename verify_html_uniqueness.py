import os
from playwright.sync_api import sync_playwright

def verify_and_print_pages():
    project_root = "/Users/kyzl/updated_remake"
    exclude_dirs = {'.git', 'node_modules', '.expo', 'bin', 'assets', 'hooks', 'build'}
    allowed_extensions = {'.ts', '.tsx', '.sql'}
    
    files_to_print = []
    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in allowed_extensions:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, project_root)
                if "package.json" in rel_path or "tsconfig.json" in rel_path:
                    continue
                files_to_print.append((rel_path, full_path))
                
    # Create HTML
    pages_html = []
    for idx, (rel_path, full_path) in enumerate(files_to_print[:10]):
        with open(full_path, "r", encoding="utf-8") as f:
            code = f.read()
        pages_html.append(f"""
        <div class="page" id="page-{idx}">
            <h1>{rel_path}</h1>
            <pre class="code-block"><code>{code[:100]}</code></pre>
        </div>
        """)
        
    full_html = f"""
    <html>
    <head>
        <style>
            .page {{ page-break-after: always; height: 100vh; }}
            .code-block {{ background: #111; color: white; }}
        </style>
    </head>
    <body>
        {"".join(pages_html)}
    </body>
    </html>
    """
    
    with open("test_uniqueness.html", "w") as f:
        f.write(full_html)
        
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath('test_uniqueness.html')}")
        
        # Verify text of page 0 vs page 1 in the rendered DOM
        t0 = page.locator("#page-0 pre").inner_text()
        t1 = page.locator("#page-1 pre").inner_text()
        print("Page 0 code snippet:", t0[:50].strip())
        print("Page 1 code snippet:", t1[:50].strip())
        print("Are they different?", t0 != t1)
        
        browser.close()
        
    if os.path.exists("test_uniqueness.html"):
        os.remove("test_uniqueness.html")

verify_and_print_pages()