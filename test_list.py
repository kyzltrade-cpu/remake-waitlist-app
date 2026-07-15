import os
from playwright.sync_api import sync_playwright

def test_pages_uniqueness():
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
                
    print(f"Found {len(files_to_print)} total files to print.")
    for idx, (rel_path, full_path) in enumerate(files_to_print[:10]):
        print(f"File {idx+1}: {rel_path}")

test_pages_uniqueness()