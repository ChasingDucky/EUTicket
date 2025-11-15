#!/usr/bin/env python3
"""
Vue.js to Markdown Migration Script for Wiki.js
Converts Vue single-file components to Markdown format

Usage:
    python migrate_vue_to_markdown.py

Requirements:
    pip install beautifulsoup4 lxml html2text
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import html2text

# Directories
VUE_DIR = Path("src/views/countries")
OUTPUT_DIR = Path("wiki_content/countries")

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# HTML to Markdown converter settings
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False
h.ignore_emphasis = False
h.body_width = 0  # Don't wrap lines
h.unicode_snob = True
h.skip_internal_links = False


def extract_template(vue_content):
    """Extract <template> content from Vue SFC"""
    match = re.search(r'<template>(.*?)</template>', vue_content, re.DOTALL)
    if match:
        return match.group(1)
    return ""


def clean_vue_directives(html):
    """Remove Vue-specific directives and attributes"""
    # Remove v-for, v-if, :key, etc.
    html = re.sub(r'\s+v-[a-z-]+="[^"]*"', '', html)
    html = re.sub(r'\s+:[a-z-]+="[^"]*"', '', html)
    html = re.sub(r'\s+@[a-z-]+="[^"]*"', '', html)
    # Remove scoped class attributes
    html = re.sub(r'\s+data-v-[a-z0-9]+', '', html)
    return html


def convert_info_boxes(html):
    """Convert custom info-box divs to Markdown blockquotes"""
    # Replace info-box divs with blockquotes for better Markdown rendering
    html = re.sub(
        r'<div class="info-box tip">',
        '<blockquote class="tip">',
        html
    )
    html = re.sub(
        r'<div class="info-box warning">',
        '<blockquote class="warning">',
        html
    )
    html = re.sub(
        r'<div class="info-box">',
        '<blockquote>',
        html
    )
    html = html.replace('</div>', '</blockquote>')
    return html


def clean_markdown(markdown):
    """Clean up converted Markdown"""
    # Remove empty lines (more than 2 consecutive)
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)

    # Fix blockquote formatting
    markdown = re.sub(r'>\s*\*\*(.+?)\*\*', r'> **\1**', markdown)

    # Ensure proper spacing around headers
    markdown = re.sub(r'([^\n])\n(#{1,6} )', r'\1\n\n\2', markdown)

    # Fix list spacing
    markdown = re.sub(r'(\n- .+)\n([^-\n])', r'\1\n\n\2', markdown)

    return markdown.strip()


def add_metadata(title, markdown_content):
    """Add Wiki.js metadata frontmatter"""
    metadata = f"""---
title: {title}
description: Complete guide to {title.replace(' Railway Guide', '')} train travel
published: true
date: 2024-03-15T00:00:00.000Z
tags: railway, travel, {title.lower().split()[0]}
editor: markdown
---

"""
    return metadata + markdown_content


def convert_vue_to_markdown(vue_file_path):
    """Convert a single Vue file to Markdown"""
    print(f"Converting {vue_file_path.name}...")

    # Read Vue file
    with open(vue_file_path, 'r', encoding='utf-8') as f:
        vue_content = f.read()

    # Extract template content
    template_html = extract_template(vue_content)
    if not template_html:
        print(f"  ⚠️  No template found in {vue_file_path.name}")
        return None

    # Clean Vue directives
    template_html = clean_vue_directives(template_html)

    # Parse HTML
    soup = BeautifulSoup(template_html, 'lxml')

    # Extract title from h1
    h1 = soup.find('h1')
    title = h1.get_text() if h1 else vue_file_path.stem

    # Get main content (skip wrapper divs)
    country_guide = soup.find('div', class_='country-guide')
    if country_guide:
        content_html = str(country_guide)
    else:
        content_html = template_html

    # Convert info boxes
    content_html = convert_info_boxes(content_html)

    # Convert HTML to Markdown
    markdown = h.handle(content_html)

    # Clean up Markdown
    markdown = clean_markdown(markdown)

    # Add metadata
    markdown = add_metadata(title, markdown)

    # Generate output filename
    country_name = vue_file_path.stem.lower()
    output_file = OUTPUT_DIR / f"{country_name}.md"

    # Write Markdown file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"  ✅ Created {output_file}")
    return output_file


def main():
    """Main migration function"""
    print("=" * 60)
    print("Vue.js to Markdown Migration for Wiki.js")
    print("=" * 60)
    print()

    # Find all Vue files in countries directory
    vue_files = list(VUE_DIR.glob("*.vue"))

    if not vue_files:
        print(f"❌ No Vue files found in {VUE_DIR}")
        return

    print(f"Found {len(vue_files)} Vue files to convert")
    print()

    converted = []
    failed = []

    for vue_file in sorted(vue_files):
        # Skip Index.vue
        if vue_file.name == "Index.vue":
            print(f"Skipping {vue_file.name} (index page)")
            continue

        try:
            output_file = convert_vue_to_markdown(vue_file)
            if output_file:
                converted.append(output_file)
        except Exception as e:
            print(f"  ❌ Error: {e}")
            failed.append(vue_file.name)

    print()
    print("=" * 60)
    print("Migration Summary")
    print("=" * 60)
    print(f"✅ Successfully converted: {len(converted)} files")
    if failed:
        print(f"❌ Failed: {len(failed)} files")
        for name in failed:
            print(f"   - {name}")
    print()
    print(f"📁 Output directory: {OUTPUT_DIR.absolute()}")
    print()
    print("Next steps:")
    print("1. Review generated Markdown files in wiki_content/countries/")
    print("2. Import to Wiki.js via Admin → Tools → Import")
    print("   OR manually copy-paste content to Wiki.js editor")
    print("3. Adjust formatting as needed in Wiki.js editor")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Migration cancelled by user")
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
