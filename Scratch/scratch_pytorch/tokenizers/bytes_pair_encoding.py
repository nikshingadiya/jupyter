from importlib.metadata import version
import tiktoken
# https://huggingface.co/docs/transformers/en/tokenizer_summary
tokenizer=tiktoken.get_encoding("gpt2")
print(tokenizer)

text = "Hello, world. This, is a test.<endoftext>"

integers=tokenizer.encode(text,allowed_special={"<endoftext>","<unk>"})

print(integers)

string=tokenizer.decode(integers)

print(string)