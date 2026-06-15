# vllm-project/vllm#1319: openbuddy-llama2 bug

| 字段 | 值 |
| --- | --- |
| Issue | [#1319](https://github.com/vllm-project/vllm/issues/1319) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> openbuddy-llama2 bug

### Issue 正文摘录

path = "./openbuddy-llama2-13b-v11.1-bf16" prompts = ["hello"] llm = LLM(model=path, tokenizer=path, trust_remote_code=True, tensor_parallel_size=2, dtype="auto", tokenizer_mode="slow", load_format="pt") outputs = llm.generate(prompts) text = outputs[0].outputs[0].text text is : hd2022 Mohammed Ali Jinnah Democratic Republic Sudan (

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: openbuddy-llama2 bug path = "./openbuddy-llama2-13b-v11.1-bf16" prompts = ["hello"] llm = LLM(model=path, tokenizer=path, trust_remote_code=True, tensor_parallel_size=2, dtype="auto", tokenizer_mode="slow", load_format=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: openbuddy-llama2 bug path = "./openbuddy-llama2-13b-v11.1-bf16" prompts = ["hello"] llm = LLM(model=path, tokenizer=path, trust_remote_code=True, tensor_parallel_size=2, dtype="auto", tokenizer_mode="slow", load_format=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
