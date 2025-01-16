import torch
from torch.utils.data import Dataset, DataLoader
import tiktoken


class GPTDataSetV1(Dataset):
    def __init__(self, texts, tokenizer,max_length,stride=0):
        self.texts = texts
        self.tokenizer = tokenizer
        self.input_ids = []
        self.target_ids = []
        token_ids=tokenizer.encode(texts,allowed_special={"<endoftext>","<unk>"})

        for i in range(0,len(token_ids)-max_length+1,stride):
            input_chunk_id=token_ids[i:i+max_length]
            target_chunk_id=token_ids[i+1:i+max_length+1]
            self.input_ids.append(torch.tensor(input_chunk_id))
            self.target_ids.append(torch.tensor(target_chunk_id))
    
    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]



def create_dataloader_v1(txt,batch_size=4,max_length=256,stride=128,shuffle=True,drop_last=True,num_workers=0):
    tokenizer=tiktoken.get_encoding("gpt2")
    dataset=GPTDataSetV1(txt,tokenizer,max_length,stride)
    dataloader=DataLoader(dataset=dataset,
                         batch_size=batch_size,
                         shuffle=shuffle,
                         drop_last=drop_last,
                         num_workers=num_workers)
    return dataloader   


with open("the-verdict.txt", "r", encoding="utf-8") as f:
	raw_text = f.read()

data_loader=create_dataloader_v1(raw_text,batch_size=4,max_length=256,stride=128,shuffle=False,drop_last=True,num_workers=0)

data_iter=iter(data_loader)

first_batch=next(data_iter)

print("\nFirst Batch:", first_batch)

second_batch = next(data_iter)
print("Second Batch:", second_batch)


dataloader_final = create_dataloader_v1(raw_text, batch_size=8, max_length=4, stride=4, shuffle=False)
data_iter_final = iter(dataloader_final)
inputs, targets = next(data_iter_final)
print("\nInputs:\n", inputs)
print("\nTargets:\n", targets)
