import jsonlines
import pandas as pd
import random

data_path = "blossom-math-v2/blossom-math-v2-10k.jsonl"
out_path = "blossom-math-v2/blossom-math-v2-7500-zh.jsonl"

with jsonlines.open(data_path, "r") as reader:
    with jsonlines.open(out_path, "w") as writer:
        for i, obj in enumerate(reader, start=1):
            if obj["dataset"] in ["GSM8K"]:
                continue
            elif obj["dataset"] in ["Math23K", "GSM8K-CN"]:
                query = obj["input"]
                think = obj["output"]
                ans = obj["answer"]
                message = {"messages": [{"role": "user", "content": query}, {"role": "assistant", "content": f"[unused16]{think}[unused17]{ans}"}]}
                writer.write(message)

# split train(7400) and test(100) examples
df = pd.read_json(out_path, lines=True)
print(df.head())
# train-validation-test splitting
sample_index = list(range(len(df)))
random.seed(2022)
random.shuffle(sample_index)
train_index = sample_index[0:7400]
test_index = sample_index[7400:]
test_df = df.iloc[test_index, :]
train_df = df.iloc[train_index, :]
with jsonlines.open('blossom-math-v2/train.jsonl', mode='w') as writer:
    writer.write_all(train_df.to_dict(orient='records'))
with jsonlines.open('blossom-math-v2/test.jsonl', mode='w') as writer:
    writer.write_all(test_df.to_dict(orient='records'))
