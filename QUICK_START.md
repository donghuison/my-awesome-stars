# 🚀 My Awesome Stars - 빠른 시작 가이드

## 📌 5분 만에 시작하기

### 1️⃣ Repository 확인
👉 https://github.com/donghuison/my-awesome-stars

### 2️⃣ 카테고리별 Stars 보기
README.md에서 원하는 카테고리 클릭!

### 3️⃣ 수동 업데이트 (필요시)
```bash
gh workflow run update-stars.yml
```

---

## 📊 현재 통계

```
📚 총 311개 Repositories
📁 16개 카테고리로 분류
🔄 매일 자동 업데이트
```

---

## 🎯 주요 카테고리

### 과학 계산 (103개)
- Fortran 기반 수치해석
- 유한요소법 (FEM)
- 전산유체역학 (CFD)

### 머신러닝 & AI (41개)
- TensorFlow/PyTorch
- Deep Learning 모델
- AI 도구 및 프레임워크

### Python 프로젝트 (63개)
- 데이터 분석 도구
- 웹 프레임워크
- 자동화 스크립트

---

## ⚡ 자주 사용하는 명령어

### 업데이트 확인
```bash
# 최근 실행 기록
gh run list --limit 5

# 상태 확인
gh workflow list
```

### 로컬 실행
```bash
cd my-awesome-stars
python3 update_stars.py
```

### 통계 보기
```bash
# 카테고리별 개수
cat README.md | grep "repositories*" | head -10
```

---

## 🔧 간단 커스터마이징

### 카테고리 추가
`update_stars.py` 파일에서:
```python
# 새 카테고리 추가
if 'golang' in name.lower():
    categories.append('Go Projects')
```

### 업데이트 시간 변경
`.github/workflows/update-stars.yml`:
```yaml
schedule:
  - cron: '0 0 * * *'  # 매일 UTC 00:00
```

---

## ❓ 도움이 필요하면

1. [상세 가이드](NOTION_GUIDE.md) 확인
2. [GitHub Issues](https://github.com/donghuison/my-awesome-stars/issues) 문의
3. 직접 수정 후 Pull Request

---

*자동 업데이트 중! 매일 새로운 Stars가 추가됩니다* ✨