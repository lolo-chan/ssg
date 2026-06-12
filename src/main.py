from website import static_to_public, generate_pages_recursive
import sys

def main():
    basepath = sys.argv[0]
    if not basepath:
        basepath = '/'
    static_to_public("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()