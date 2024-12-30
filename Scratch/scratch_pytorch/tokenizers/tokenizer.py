import urllib.request
import re

url = ("https://raw.githubusercontent.com/rasbt/"
	   "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
	   "the-verdict.txt")

#   Download .txt file into directory
# file_path = "the-verdict.txt"
# urllib.request.urlretrieve(url, file_path)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
	raw_text = f.read()

print("Total number of character:", len(raw_text))
print(raw_text[:99])

#           Tokenization 
# Split text on whitespace characters
text = "Hello, world. This, is a test."
result = re.split(r"(\s)", text)
print("\n", result)

# Split text on whitespace, commas, and periods
result = re.split(r"([,.]|\s)", text)
print("\n", result)

# Optional, remove redundant whitespace characters
result = [item for item in result if item.strip()]
print("\n", result)

# Split text to handle more such as question marks, quotation marks, and double-dashes.
text = "Hello, world. Is this-- a test?"
result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
result = [item.strip() for item in result if item.strip()] # fully removes whitespaces
print("\n", result, " \n Token Count:", len(result))

# Basic Tokenizer applied to full short story, "the-verdict.txt"
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print("\n Sample of Tokenized output: \n", preprocessed[:30], "\n Full Token Count:", len(preprocessed))