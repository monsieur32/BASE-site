import os
import re

def parse_markdown(md_text):
    html_lines = []
    in_list = False
    
    for line in md_text.split('\n'):
        line = line.strip()
        
        # Replace bold and italic
        line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
        line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
        
        if line.startswith('# '):
            if in_list: html_lines.append('</ul>'); in_list = False
            html_lines.append(f'<h1 style="margin-bottom: 1rem; color: var(--emerald);">{line[2:]}</h1>')
        elif line.startswith('## '):
            if in_list: html_lines.append('</ul>'); in_list = False
            html_lines.append(f'<h2 style="margin-top: 2rem; margin-bottom: 1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;">{line[3:]}</h2>')
        elif line.startswith('### '):
            if in_list: html_lines.append('</ul>'); in_list = False
            html_lines.append(f'<h3 style="margin-top: 1.5rem; margin-bottom: 0.75rem; color: #38bdf8;">{line[4:]}</h3>')
        elif line.startswith('- '):
            if not in_list: html_lines.append('<ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.7; color: var(--muted);">'); in_list = True
            html_lines.append(f'<li style="margin-bottom: 0.5rem;">{line[2:]}</li>')
        elif line == '---':
            if in_list: html_lines.append('</ul>'); in_list = False
            html_lines.append('<hr style="border: none; border-top: 1px solid var(--border); margin: 2rem 0;">')
        elif line == '':
            pass # ignore blank lines between paragraphs for simplicity, or handle if needed
        else:
            if in_list: html_lines.append('</ul>'); in_list = False
            html_lines.append(f'<p style="margin-bottom: 1rem; line-height: 1.7; color: var(--muted);">{line}</p>')
            
    if in_list: html_lines.append('</ul>')
    return '\n'.join(html_lines)


def main():
    root_dir = r"c:\Users\32ngu\Desktop\BASE-site-main"
    index_path = os.path.join(root_dir, "index.html")
    
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()
        
    head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', index_html, re.DOTALL)
    nav_match = re.search(r'(<nav id="navbar">.*?</nav>)', index_html, re.DOTALL)
    footer_match = re.search(r'(<footer>.*?</html>)', index_html, re.DOTALL)
    
    head = head_match.group(1)
    nav = nav_match.group(1)
    footer = footer_match.group(1)
    
    # Adjust nav links
    nav = nav.replace('href="#', 'href="index.html#')
    
    # Files
    tiktok_md = os.path.join(root_dir, "tiktok-phonefarm-project", "tiktok_phonefarm_portfolio.md")
    n8n_md = os.path.join(root_dir, "n8nflow-realestate", "n8n_realestate_portfolio.md")
    
    with open(tiktok_md, "r", encoding="utf-8") as f: tiktok_text = f.read()
    with open(n8n_md, "r", encoding="utf-8") as f: n8n_text = f.read()
    
    tiktok_html_content = parse_markdown(tiktok_text)
    n8n_html_content = parse_markdown(n8n_text)
    
    template = """{head}
<body>
    {nav}
    <main style="padding-top: 100px; padding-bottom: 50px; min-height: calc(100vh - 100px);">
        <div class="container" style="max-width: 800px; margin: 0 auto; padding: 20px;">
            <a href="index.html#portfolio" style="color: var(--emerald); text-decoration: none; display: inline-block; margin-bottom: 30px; font-weight: 500;">
                <i class="fas fa-arrow-left"></i> Back to Portfolio
            </a>
            <div class="portfolio-content" style="background: var(--bg2); padding: 40px; border-radius: 12px; border: 1px solid var(--border);">
                {content}
            </div>
        </div>
    </main>
    {footer}
"""
    
    # Write Tiktok
    tiktok_page = template.format(head=head.replace("<title>", "<title>TikTok PhoneFarm | "), nav=nav, content=tiktok_html_content, footer=footer)
    with open(os.path.join(root_dir, "tiktok-portfolio.html"), "w", encoding="utf-8") as f:
        f.write(tiktok_page)
        
    # Write N8n
    n8n_page = template.format(head=head.replace("<title>", "<title>Real Estate n8n Pipeline | "), nav=nav, content=n8n_html_content, footer=footer)
    with open(os.path.join(root_dir, "realestate-portfolio.html"), "w", encoding="utf-8") as f:
        f.write(n8n_page)
        
    print("Generated HTML pages.")

if __name__ == "__main__":
    main()
