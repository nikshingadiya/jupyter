import tiktoken


with open("the-verdict.txt", "r", encoding="utf-8") as f:
	raw_text = f.read()

tokenizer = tiktoken.get_encoding("gpt2")

enc_text = tokenizer.encode(raw_text)
print(len(enc_text)) # 5145

enc_sample=enc_text[:50]

context_size=4

x=enc_text[:context_size]
y=enc_text[1:context_size+1]

for i in range(1,context_size+1):
    context=enc_text[:i]
    target=enc_text[i]

    print(context,target)

print()


for i in range(1, context_size + 1):
	context = enc_sample[:i]
	desired = enc_sample[i]
	print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))