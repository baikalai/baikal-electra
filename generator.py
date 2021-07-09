# coding: utf-8

from transformers import pipeline

# 모델과 태스크만 주어지면 바로 실행
nlp = pipeline("fill-mask", model="deeq/delectra-generator")
text = "대한민국은 민주 [MASK] 입니다."
result = nlp(text)

for r in result:
    print(r)
