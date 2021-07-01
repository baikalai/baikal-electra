# deeq-electra

- deeq-electra는 baikal.ai가 개발하고 있는 pre-trained ELECTRA(base) 모델입니다.
- 한국어 위키, 1990~2020 네이버 뉴스 등을 포함한 다양한 말뭉치를 정제하여 학습합니다.
- 모델은 huggingface에 deeq/delectra로 공개되어있어 transformers 라이브러리로 간편하게 사용할 수 있습니다.
- delectra는 wordpiece 토크나이저(BERT)를 그대로 사용합니다.

## files

- discriminator.py: Discriminator 사용 예시
- generator.py: Generator 사용 예시

## sample runs

- discriminator.py

입력: 서울은 한국의 국가(fake-token) 입니다.

```
['서울은', '한국의', '수도', '입니다', '.']
['서울은', '한국의', '국가', '입니다', '.']
[[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]]
```

- generator.py

입력: 대한민국은 민주 [MASK] 입니다.

```
{'sequence': '대한민국은 민주공화국 입니다.', 'score': 0.7041397094726562, 'token': 16831, 'token_str': '##공화국'}
{'sequence': '대한민국은 민주국가 입니다.', 'score': 0.03875487670302391, 'token': 5683, 'token_str': '##국가'}
{'sequence': '대한민국은 민주정부 입니다.', 'score': 0.026517674326896667, 'token': 2505, 'token_str': '##정부'}
{'sequence': '대한민국은 민주정당 입니다.', 'score': 0.022539861500263214, 'token': 7174, 'token_str': '##정당'}
{'sequence': '대한민국은 민주시민 입니다.', 'score': 0.012016055174171925, 'token': 4711, 'token_str': '##시민'}
```

## works to do

- deeqnlp 토크나이저를 사용한 모델
