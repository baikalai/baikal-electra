from transformers import ElectraForPreTraining, ElectraTokenizerFast
import torch

discriminator = ElectraForPreTraining.from_pretrained("deeq/delectra")
tokenizer = ElectraTokenizerFast.from_pretrained("deeq/delectra")

sentence = "서울은 한국의 수도 입니다."
fake_sentence = "서울은 미국의 수도 입니다."

print(tokenizer.tokenize(sentence))
fake_tokens = tokenizer.tokenize(fake_sentence)
print(fake_tokens)

fake_inputs = tokenizer.encode(fake_sentence, return_tensors="pt")
discriminator_outputs = discriminator(fake_inputs)
predictions = torch.round((torch.sign(discriminator_outputs[0]) + 1) / 2)

print(predictions.tolist())
