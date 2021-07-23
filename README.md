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
['서울은', '한국의', '나라', '입니다', '.']
[[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]]
```

- generator.py

입력: 대한민국은 민주 [MASK] 입니다.

```
{'sequence': '대한민국은 민주국가 입니다.', 'score': 0.48309803009033203, 'token': 5683, 'token_str': '##국가'}
{'sequence': '대한민국은 민주공화국 입니다.', 'score': 0.26447364687919617, 'token': 16831, 'token_str': '##공화국'}
{'sequence': '대한민국은 민주사회 입니다.', 'score': 0.08608758449554443, 'token': 2641, 'token_str': '##사회'}
{'sequence': '대한민국은 민주 국가 입니다.', 'score': 0.06539660692214966, 'token': 2184, 'token_str': '국가'}
{'sequence': '대한민국은 민주국 입니다.', 'score': 0.012030140496790409, 'token': 1108, 'token_str': '##국'}
```

## works to do

- deeqnlp 토크나이저를 사용한 모델
