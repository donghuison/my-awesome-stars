#!/usr/bin/env python3
"""
Generate awesome-stars README.md from categorized repositories
"""
import json
from datetime import datetime
import re

# Emoji mapping for categories
CATEGORY_EMOJIS = {
    'Scientific Computing & Numerical Analysis': '🔬',
    'Machine Learning & AI': '🤖',
    'Fortran Projects': '🔢',
    'Python Projects': '🐍',
    'Jupyter Notebooks': '📓',
    'Documentation & Learning Resources': '📚',
    'Programming Languages & Compilers': '⚙️',
    'JavaScript/TypeScript Projects': '📜',
    'C++ Projects': '⚡',
    'Julia Projects': '🔮',
    'Tools & Utilities': '🛠️',
    'Web Development': '🌐',
    'Data Science & Analytics': '📊',
    'Mathematics & Statistics': '📐',
    'Security & Cryptography': '🔒',
    'DevOps & Infrastructure': '🚀',
    'Uncategorized': '📦'
}

def load_data():
    """Load categorized repository data"""
    with open('categorized_repos.json', 'r') as f:
        return json.load(f)

def generate_badge(text, color='blue'):
    """Generate a shield.io badge"""
    text = text.replace(' ', '%20').replace('-', '--')
    return f"![{text}](https://img.shields.io/badge/{text}-{color})"

def format_repo_entry(repo):
    """Format a single repository entry"""
    name = repo.get('name', 'Unknown')
    desc = repo.get('description', '')
    lang = repo.get('language', '')
    stars = repo.get('stars', 0)
    url = repo.get('url', '#')
    topics = repo.get('topics', [])
    
    # Repository name with link
    entry = f"- [{name}]({url})"
    
    # Add stars if significant
    if stars > 100:
        entry += f" ⭐ {stars:,}"
    
    # Add language badge
    if lang:
        lang_color = {
            'Python': 'blue',
            'JavaScript': 'yellow',
            'TypeScript': 'blue',
            'C++': 'orange',
            'Fortran': 'purple',
            'FORTRAN': 'purple',
            'Julia': 'purple',
            'TeX': 'green',
            'MATLAB': 'red'
        }.get(lang, 'gray')
        entry += f" {generate_badge(lang, lang_color)}"
    
    # Add description
    if desc:
        if len(desc) > 150:
            desc = desc[:147] + "..."
        entry += f" - {desc}"
    
    return entry

def generate_readme(categorized):
    """Generate the complete README.md content"""
    readme = []
    
    # Header
    readme.append("# 🌟 My Awesome Stars")
    readme.append("")
    readme.append("> A curated list of my GitHub starred repositories organized by categories")
    readme.append("")
    
    # Stats badges
    total_repos = sum(len(repos) for repos in categorized.values())
    readme.append(f"![Total Stars](https://img.shields.io/badge/Total%20Stars-{total_repos}-brightgreen)")
    readme.append(f"![Categories](https://img.shields.io/badge/Categories-{len(categorized)}-blue)")
    readme.append(f"![Last Updated](https://img.shields.io/badge/Last%20Updated-{datetime.now().strftime('%Y--%m--%d')}-orange)")
    readme.append("")
    
    # Description
    readme.append("## 📖 About")
    readme.append("")
    readme.append("This repository contains a categorized collection of all my GitHub starred repositories.")
    readme.append("It's automatically updated daily to keep track of new stars and maintain organization.")
    readme.append("")
    
    # Statistics
    readme.append("## 📊 Statistics")
    readme.append("")
    readme.append("| Category | Count |")
    readme.append("|----------|-------|")
    
    # Sort categories by count
    sorted_cats = sorted(categorized.items(), key=lambda x: len(x[1]), reverse=True)
    for category, repos in sorted_cats[:10]:
        emoji = CATEGORY_EMOJIS.get(category, '📁')
        readme.append(f"| {emoji} {category} | {len(repos)} |")
    readme.append("")
    
    # Table of Contents
    readme.append("## 📑 Table of Contents")
    readme.append("")
    
    # Group categories
    main_categories = ['Scientific Computing & Numerical Analysis', 'Machine Learning & AI', 
                      'Documentation & Learning Resources', 'Web Development']
    language_categories = ['Fortran Projects', 'Python Projects', 'Jupyter Notebooks',
                          'C++ Projects', 'Julia Projects', 'JavaScript/TypeScript Projects']
    
    readme.append("### 🎯 Main Categories")
    for cat in main_categories:
        if cat in categorized:
            emoji = CATEGORY_EMOJIS.get(cat, '📁')
            anchor = cat.lower().replace(' ', '-').replace('&', 'and')
            readme.append(f"- [{emoji} {cat}](#{anchor}) ({len(categorized[cat])} repos)")
    readme.append("")
    
    readme.append("### 💻 Language-Based")
    for cat in language_categories:
        if cat in categorized:
            emoji = CATEGORY_EMOJIS.get(cat, '📁')
            anchor = cat.lower().replace(' ', '-').replace('&', 'and')
            readme.append(f"- [{emoji} {cat}](#{anchor}) ({len(categorized[cat])} repos)")
    readme.append("")
    
    other_cats = [c for c in categorized.keys() 
                  if c not in main_categories and c not in language_categories]
    if other_cats:
        readme.append("### 📚 Other Categories")
        for cat in other_cats:
            emoji = CATEGORY_EMOJIS.get(cat, '📁')
            anchor = cat.lower().replace(' ', '-').replace('&', 'and')
            readme.append(f"- [{emoji} {cat}](#{anchor}) ({len(categorized[cat])} repos)")
        readme.append("")
    
    readme.append("---")
    readme.append("")
    
    # Categories sections
    for category, repos in sorted_cats:
        emoji = CATEGORY_EMOJIS.get(category, '📁')
        readme.append(f"## {emoji} {category}")
        readme.append("")
        readme.append(f"*{len(repos)} repositories*")
        readme.append("")
        
        # Sort repos by stars
        sorted_repos = sorted(repos, key=lambda x: x.get('stars', 0), reverse=True)
        
        # Limit to top 30 per category for readability
        display_repos = sorted_repos[:30]
        for repo in display_repos:
            readme.append(format_repo_entry(repo))
        
        if len(repos) > 30:
            readme.append("")
            readme.append(f"<details>")
            readme.append(f"<summary>View {len(repos) - 30} more...</summary>")
            readme.append("")
            for repo in sorted_repos[30:]:
                readme.append(format_repo_entry(repo))
            readme.append("</details>")
        
        readme.append("")
        readme.append("[⬆ Back to Top](#-my-awesome-stars)")
        readme.append("")
        readme.append("---")
        readme.append("")
    
    # Footer
    readme.append("## 🤖 Automation")
    readme.append("")
    readme.append("This repository is automatically updated daily using GitHub Actions.")
    readme.append("The update script fetches all starred repositories and reorganizes them based on:")
    readme.append("- Programming language")
    readme.append("- Repository topics")
    readme.append("- Description keywords")
    readme.append("")
    readme.append("## 📝 License")
    readme.append("")
    readme.append("This repository is available under the MIT License.")
    readme.append("")
    readme.append("---")
    readme.append("")
    readme.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    
    return "\n".join(readme)

def main():
    """Main function"""
    print("Loading categorized repository data...")
    categorized = load_data()
    
    print(f"Found {len(categorized)} categories")
    print("Generating README.md...")
    
    readme_content = generate_readme(categorized)
    
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print("✅ README.md generated successfully!")
    print(f"   Total categories: {len(categorized)}")
    print(f"   Total repositories: {sum(len(repos) for repos in categorized.values())}")

if __name__ == '__main__':
    main()