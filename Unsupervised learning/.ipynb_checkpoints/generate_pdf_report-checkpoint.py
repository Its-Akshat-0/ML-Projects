import markdown
from xhtml2pdf import pisa
import os

# Define input and output filenames
input_filename = 'Business_Insight_Report.md'
output_filename = 'Business_Insight_Report.pdf'

# CSS for styling the PDF
css = """
<style>
    @page { size: A4; margin: 2cm; }
    body { font-family: Helvetica, sans-serif; font-size: 12pt; line-height: 1.5; color: #333; }
    h1 { color: #2c3e50; font-size: 24pt; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; margin-top: 0; }
    h2 { color: #e67e22; font-size: 18pt; margin-top: 20px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }
    h3 { color: #34495e; font-size: 14pt; margin-top: 15px; }
    p { margin-bottom: 10px; text-align: justify; }
    ul { margin-bottom: 10px; }
    li { margin-bottom: 5px; }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; margin-bottom: 15px; }
    th { background-color: #f2f2f2; border: 1px solid #ddd; padding: 8px; text-align: left; font-weight: bold; }
    td { border: 1px solid #ddd; padding: 8px; }
    tr:nth-child(even) { background-color: #f9f9f9; }
</style>
"""

def convert_md_to_pdf(source_md, output_pdf):
    # Read Markdown content
    with open(source_md, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert Markdown to HTML
    # We include 'tables' extension to handle the markdown table correctly
    html_content = markdown.markdown(md_text, extensions=['tables'])

    # Combine CSS and HTML
    full_html = f"<html><head>{css}</head><body>{html_content}</body></html>"

    # Write PDF
    with open(output_pdf, "wb") as result_file:
        pisa_status = pisa.CreatePDF(
            src=full_html,
            dest=result_file
        )

    if pisa_status.err:
        print(f"Error converting {source_md} to PDF")
    else:
        print(f"Successfully created {output_pdf}")

if __name__ == "__main__":
    if os.path.exists(input_filename):
        print(f"Found {input_filename}, starting conversion...")
        convert_md_to_pdf(input_filename, output_filename)
    else:
        print(f"Error: {input_filename} not found.")
