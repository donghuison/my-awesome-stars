# 🌟 My Awesome Stars 사용 가이드

> GitHub Starred Repositories를 카테고리별로 자동 관리하는 완벽한 솔루션

## 📖 목차

1. [소개](#-소개)
2. [주요 기능](#-주요-기능)
3. [초기 설정](#-초기-설정)
4. [사용 방법](#-사용-방법)
5. [자동화 활성화](#-자동화-활성화)
6. [카테고리 커스터마이징](#-카테고리-커스터마이징)
7. [문제 해결](#-문제-해결)
8. [고급 기능](#-고급-기능)

---

## 🎯 소개

**My Awesome Stars**는 GitHub에서 star를 준 repository들을 자동으로 카테고리별로 분류하고 관리해주는 도구입니다.

### 왜 필요한가요?

- ✅ **자동 분류**: 311개의 starred repos를 16개 카테고리로 자동 정리
- ✅ **매일 업데이트**: GitHub Actions로 자동 동기화
- ✅ **시각화**: 통계와 배지로 한눈에 파악
- ✅ **검색 가능**: 카테고리별로 빠르게 찾기

### Repository 정보

- **URL**: https://github.com/donghuison/my-awesome-stars
- **총 Stars**: 311개
- **카테고리**: 16개
- **업데이트 주기**: 매일 00:00 UTC

---

## ✨ 주요 기능

### 1. 자동 카테고리 분류

Repository는 다음 기준으로 자동 분류됩니다:

| 카테고리 | 설명 | 개수 |
|---------|------|------|
| 🔬 Scientific Computing | 과학 계산, 수치 해석 | 103 |
| 🔢 Fortran Projects | Fortran 언어 프로젝트 | 101 |
| 🐍 Python Projects | Python 관련 프로젝트 | 63 |
| 🤖 Machine Learning & AI | 인공지능, 머신러닝 | 41 |
| 📓 Jupyter Notebooks | Jupyter 노트북 | 36 |
| 📚 Documentation | 문서, 학습 자료 | 31 |

### 2. 자동 업데이트

- **GitHub Actions**: 매일 자동 실행
- **수동 실행**: 언제든지 가능
- **변경 감지**: 새로운 star 자동 반영

### 3. 아름다운 README

- 📊 통계 대시보드
- 🏷️ 카테고리별 배지
- 📑 목차 자동 생성
- ⭐ Star 수 표시

---

## 🚀 초기 설정

### Step 1: Repository 접속

1. 브라우저에서 https://github.com/donghuison/my-awesome-stars 접속
2. 우측 상단의 ⭐ **Star** 버튼 클릭 (선택사항)
3. 📋 **Fork** 버튼으로 자신의 계정에 복사 (커스터마이징시)

### Step 2: 로컬 환경 설정 (선택사항)

로컬에서 직접 실행하려면:

```bash
# 1. Repository 클론
git clone https://github.com/donghuison/my-awesome-stars.git
cd my-awesome-stars

# 2. Python 환경 확인
python3 --version  # 3.8 이상 필요

# 3. GitHub CLI 설치 확인
gh --version  # 설치 안되어있으면 brew install gh
```

---

## 📱 사용 방법

### 방법 1: 웹에서 보기 (가장 쉬움)

1. https://github.com/donghuison/my-awesome-stars 접속
2. README.md에서 원하는 카테고리 클릭
3. Repository 목록 확인 및 클릭하여 이동

### 방법 2: 수동으로 업데이트 실행

#### GitHub 웹에서:

1. Repository 페이지 → **Actions** 탭 클릭
2. 왼쪽 메뉴에서 **"Update Starred Repositories"** 선택
3. 오른쪽의 **"Run workflow"** 버튼 클릭
4. **"Run workflow"** 확인 버튼 클릭

#### 터미널에서:

```bash
# GitHub CLI 사용
gh workflow run update-stars.yml
```

### 방법 3: 로컬에서 실행

```bash
# my-awesome-stars 디렉토리에서
python3 update_stars.py
```

---

## ⚙️ 자동화 활성화

### GitHub Actions 확인

자동화가 제대로 작동하는지 확인:

1. **Actions** 탭 접속
2. 녹색 체크 ✅ 확인
3. 실패시 🔴 클릭하여 로그 확인

### 업데이트 주기 변경

`.github/workflows/update-stars.yml` 파일 수정:

```yaml
on:
  schedule:
    # 매일 오전 9시 (한국시간)
    - cron: '0 0 * * *'  # UTC 00:00 = KST 09:00
    
    # 매주 월요일 오전 9시
    # - cron: '0 0 * * 1'
    
    # 매달 1일 오전 9시  
    # - cron: '0 0 1 * *'
```

---

## 🎨 카테고리 커스터마이징

### 새 카테고리 추가하기

`update_stars.py` 파일의 `categorize_repo()` 함수 수정:

```python
# 새 카테고리 추가 예시
if any(keyword in name + desc for keyword in ['blockchain', 'crypto', 'web3']):
    categories.append('Blockchain & Web3')
```

### 카테고리 이모지 변경

`generate_readme.py` 파일의 `CATEGORY_EMOJIS` 수정:

```python
CATEGORY_EMOJIS = {
    'Scientific Computing & Numerical Analysis': '🔬',  # 변경
    'Machine Learning & AI': '🤖',
    'Blockchain & Web3': '⛓️',  # 새로 추가
    # ...
}
```

### 표시 개수 조정

`generate_readme.py`에서 수정:

```python
# 카테고리당 표시 개수 (기본: 30)
display_repos = sorted_repos[:30]  # 50개로 변경시: [:50]
```

---

## 🔧 문제 해결

### 일반적인 문제들

#### 1. GitHub Actions 실패

**증상**: Actions 탭에 빨간색 X 표시

**해결**:
```bash
# 로그 확인
gh run list --limit 1
gh run view [run-id]

# 수동으로 재실행
gh workflow run update-stars.yml
```

#### 2. 권한 오류

**증상**: "Permission denied" 메시지

**해결**:
1. Settings → Actions → General
2. "Workflow permissions" 섹션
3. "Read and write permissions" 선택
4. Save

#### 3. Repository 누락

**증상**: 특정 starred repo가 보이지 않음

**해결**:
```bash
# 수동 업데이트 실행
python3 update_stars.py

# 또는 GitHub에서
gh api user/starred | grep "repository-name"
```

---

## 🚀 고급 기능

### 1. GitHub Pages 배포

정적 웹사이트로 배포:

1. Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: "main" / "root"
4. Save

### 2. API 활용

```python
# 프로그래밍 방식으로 데이터 활용
import json

with open('categorized_repos.json', 'r') as f:
    data = json.load(f)
    
# 특정 카테고리 repos 가져오기
ml_repos = data.get('Machine Learning & AI', [])
for repo in ml_repos[:5]:
    print(f"- {repo['name']}: {repo['stars']} stars")
```

### 3. 통계 분석

```python
# 언어별 통계
from collections import Counter

languages = []
for category, repos in data.items():
    for repo in repos:
        if repo.get('language'):
            languages.append(repo['language'])

language_stats = Counter(languages)
print(f"Top languages: {language_stats.most_common(5)}")
```

### 4. 백업 생성

```bash
# 데이터 백업
cp categorized_repos.json backup_$(date +%Y%m%d).json

# Git 태그로 버전 관리
git tag -a v1.0 -m "Initial categorization"
git push origin v1.0
```

---

## 📊 통계 대시보드

### 현재 상태

- **총 Repositories**: 311개
- **카테고리 수**: 16개
- **마지막 업데이트**: 자동 갱신
- **주요 언어**: Fortran (86), Python (63), Jupyter (36)

### 성장 추적

Actions 실행 기록으로 성장 추적:

```bash
# 실행 기록 보기
gh run list --workflow=update-stars.yml --limit 30

# 특정 날짜 기록
gh run list --created "2024-01-01..2024-12-31"
```

---

## 💡 팁과 트릭

### 빠른 검색

브라우저에서 `Ctrl+F` (Mac: `Cmd+F`)로 repository 검색

### 카테고리 건너뛰기

목차의 카테고리 링크 클릭으로 빠른 이동

### 로컬 검색 도구

```bash
# 특정 키워드 포함 repos 찾기
cat README.md | grep -i "machine learning"

# JSON에서 직접 검색
jq '.["Machine Learning & AI"][] | select(.stars > 1000)' categorized_repos.json
```

---

## 🤝 기여하기

개선 아이디어가 있다면:

1. Fork 생성
2. 기능 브랜치 생성 (`git checkout -b feature/AmazingFeature`)
3. 변경사항 커밋 (`git commit -m 'Add AmazingFeature'`)
4. 브랜치 푸시 (`git push origin feature/AmazingFeature`)
5. Pull Request 생성

---

## 📝 라이선스

MIT License - 자유롭게 사용 가능

---

## 🙋 도움말

### 자주 묻는 질문

**Q: 얼마나 자주 업데이트되나요?**
A: 매일 UTC 00:00 (한국시간 오전 9시)에 자동 업데이트됩니다.

**Q: Private repository도 포함되나요?**
A: 아니요, public starred repositories만 포함됩니다.

**Q: 다른 사람의 stars도 관리할 수 있나요?**
A: Fork 후 `update_stars.py`에서 사용자명을 변경하면 가능합니다.

### 연락처

- GitHub Issues: https://github.com/donghuison/my-awesome-stars/issues
- 개선 제안: Pull Request 환영

---

*마지막 업데이트: 2024년 1월*