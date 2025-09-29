from openai import OpenAI
import jsonlines
import pandas as pd

test_path = "blossom-math-v2/test.jsonl"

client = OpenAI(
    api_key='',
    base_url=f'http://localhost:8000/v1',
)
model = client.models.list().data[0].id
print(f'model: {model}')

res = []
with jsonlines.open(test_path, "r") as reader:
    for obj in reader:
        messages = [obj["messages"][0]]
        resp = client.chat.completions.create(model=model, messages=messages, temperature=0.6)
        query = messages[0]['content']
        response = resp.choices[0].message.content
        ans = response.split("</think>")[-1].strip()
        gold_ans = obj["messages"][1]["content"].split("[unused17]")[-1]
        correct = 1 if int(ans) == int(gold_ans) else 0
        res.append([query, response, ans, correct])

df = pd.DataFrame(res, columns=["query", "response", "answer", "correct"])
print(df["correct"].mean())
df.to_csv("output/test_ans.csv", index=False)
