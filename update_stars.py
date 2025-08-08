#!/usr/bin/env python3
"""
Update starred repositories and regenerate README
This script is designed to run in GitHub Actions
"""
import os
import json
import subprocess
import sys
from datetime import datetime

def run_command(cmd):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running command: {cmd}")
            print(f"Error: {result.stderr}")
            return None
        return result.stdout
    except Exception as e:
        print(f"Exception running command: {e}")
        return None

def fetch_starred_repos():
    """Fetch all starred repositories using GitHub CLI"""
    print("Fetching starred repositories...")
    
    # Use GITHUB_TOKEN if available (for GitHub Actions)
    if 'GITHUB_TOKEN' in os.environ:
        print("Using GITHUB_TOKEN for authentication")
    
    # Fetch starred repos with pagination
    output = run_command("gh api user/starred --paginate")
    if not output:
        print("Failed to fetch starred repositories")
        return None
    
    try:
        repos = json.loads(output)
        print(f"Fetched {len(repos)} starred repositories")
        return repos
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return None

def categorize_repo(repo):
    """Categorize repository based on name, description, language, and topics"""
    categories = []
    
    name = (repo.get('full_name') or '').lower()
    desc = (repo.get('description') or '').lower()
    lang = repo.get('language') or ''
    topics = repo.get('topics') or []
    
    # Scientific Computing & Numerical Analysis
    if any(keyword in name + desc for keyword in ['fortran', 'numerical', 'finite element', 'fem', 'cfd', 'computational', 'solver', 'simulation', 'physics', 'mechanics']):
        categories.append('Scientific Computing & Numerical Analysis')
    
    # Machine Learning & AI
    if any(keyword in name + desc for keyword in ['machine learning', 'deep learning', 'neural', 'ai ', 'artificial intelligence', ' ml ', 'tensorflow', 'pytorch', 'keras', 'scikit']):
        categories.append('Machine Learning & AI')
    
    # Data Science & Analytics
    if any(keyword in name + desc for keyword in ['data science', 'analytics', 'pandas', 'numpy', 'visualization', 'jupyter', 'notebook', 'data analysis']):
        categories.append('Data Science & Analytics')
    
    # Web Development
    if any(keyword in name + desc for keyword in ['web', 'frontend', 'backend', 'react', 'vue', 'angular', 'node', 'django', 'flask', 'api', 'rest']):
        categories.append('Web Development')
    
    # DevOps & Infrastructure
    if any(keyword in name + desc for keyword in ['docker', 'kubernetes', 'ci/cd', 'devops', 'infrastructure', 'terraform', 'ansible', 'jenkins', 'github action']):
        categories.append('DevOps & Infrastructure')
    
    # Programming Languages & Compilers
    if any(keyword in name + desc for keyword in ['compiler', 'interpreter', 'language', 'parser', 'lexer', 'ast']):
        categories.append('Programming Languages & Compilers')
    
    # Tools & Utilities
    if any(keyword in name + desc for keyword in ['tool', 'utility', 'cli', 'command line', 'terminal', 'shell']):
        categories.append('Tools & Utilities')
    
    # Documentation & Learning Resources
    if any(keyword in name + desc for keyword in ['tutorial', 'guide', 'book', 'course', 'learning', 'documentation', 'example', 'awesome']):
        categories.append('Documentation & Learning Resources')
    
    # Mathematics & Statistics
    if any(keyword in name + desc for keyword in ['math', 'statistics', 'statistical', 'probability', 'algebra', 'calculus']):
        categories.append('Mathematics & Statistics')
    
    # Security & Cryptography
    if any(keyword in name + desc for keyword in ['security', 'crypto', 'encryption', 'authentication', 'vulnerability']):
        categories.append('Security & Cryptography')
    
    # Language-specific categories
    if lang in ['Fortran', 'FORTRAN']:
        categories.append('Fortran Projects')
    elif lang == 'Python':
        categories.append('Python Projects')
    elif lang == 'Jupyter Notebook':
        categories.append('Jupyter Notebooks')
    elif lang == 'C++':
        categories.append('C++ Projects')
    elif lang == 'Julia':
        categories.append('Julia Projects')
    elif lang in ['TypeScript', 'JavaScript']:
        categories.append('JavaScript/TypeScript Projects')
    
    # If no category found, add to Uncategorized
    if not categories:
        categories.append('Uncategorized')
    
    return categories

def process_repos(repos):
    """Process and categorize repositories"""
    from collections import defaultdict
    
    categorized = defaultdict(list)
    
    for repo in repos:
        # Extract relevant information
        repo_data = {
            'name': repo.get('full_name', 'Unknown'),
            'description': repo.get('description'),
            'language': repo.get('language'),
            'topics': repo.get('topics', []),
            'stars': repo.get('stargazers_count', 0),
            'url': repo.get('html_url', '#'),
            'archived': repo.get('archived', False),
            'fork': repo.get('fork', False)
        }
        
        # Categorize
        categories = categorize_repo(repo)
        for category in categories:
            categorized[category].append(repo_data)
    
    return dict(categorized)

def save_data(repos, categorized):
    """Save raw and categorized data"""
    # Save raw data
    with open('starred_repos_raw.json', 'w') as f:
        json.dump(repos, f, indent=2)
    print("Saved raw repository data")
    
    # Save categorized data
    with open('categorized_repos.json', 'w') as f:
        json.dump(categorized, f, indent=2)
    print("Saved categorized repository data")

def main():
    """Main update function"""
    print("=" * 50)
    print("Awesome Stars Update Script")
    print(f"Started at: {datetime.now()}")
    print("=" * 50)
    
    # Fetch starred repositories
    repos = fetch_starred_repos()
    if not repos:
        print("Failed to fetch repositories")
        sys.exit(1)
    
    # Categorize repositories
    print("Categorizing repositories...")
    categorized = process_repos(repos)
    
    # Print statistics
    print(f"\nStatistics:")
    print(f"  Total repositories: {len(repos)}")
    print(f"  Total categories: {len(categorized)}")
    for category, repo_list in sorted(categorized.items(), key=lambda x: len(x[1]), reverse=True)[:5]:
        print(f"  - {category}: {len(repo_list)} repos")
    
    # Save data
    save_data(repos, categorized)
    
    # Generate README
    print("\nGenerating README.md...")
    result = run_command("python3 generate_readme.py")
    if result:
        print("README.md generated successfully")
    else:
        print("Failed to generate README.md")
        sys.exit(1)
    
    print("\n✅ Update completed successfully!")
    print(f"Finished at: {datetime.now()}")

if __name__ == '__main__':
    main()