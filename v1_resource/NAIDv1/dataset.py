
import torch
from torch.utils.data import Dataset

class NAID_Dataset(Dataset):
    def __init__(self, data, tokenizer, max_length=512, gt_row='TNCSI_SP',prompt_style=0):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.gt_row = gt_row # Choose between (TNCSI_SP || TNCSI)


    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        label = float(row[self.gt_row])

        text = f'''Given a certain paper, Title: {row['title']}\n Abstract: {row['abstract']}. \n Predict its normalized academic impact (between 0 and 1):'''
        inputs = self.tokenizer(text, max_length=self.max_length, padding='max_length', truncation=True, return_tensors="pt")

        return {
            'input_ids': inputs['input_ids'].squeeze(0),
            'attention_mask': inputs['attention_mask'].squeeze(0),
            'labels': torch.tensor(label, dtype=torch.float)
        }

