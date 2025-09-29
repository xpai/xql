---
configs:
- config_name: default
  data_files:
  - path: blossom-math-v2-10k.jsonl
    split: train
license: Apache License 2.0
tags:
- finetune
- chat
- math
- zh
- blossom
tasks:
- text-generation
- chat
---


### Clone with HTTP
```bash
git clone https://www.modelscope.cn/datasets/AI-ModelScope/blossom-math-v2.git
```

迁移来源: https://www.huggingface.co/datasets/Azure99/blossom-math-v2

sdk下载:
```python
from modelscope import MsDataset

dataset = MsDataset.load('AI-ModelScope/blossom-math-v2').to_hf_dataset()
print(dataset)

"""
Dataset({
    features: ['id', 'input', 'output', 'answer', 'dataset'],
    num_rows: 10004
})
"""
```