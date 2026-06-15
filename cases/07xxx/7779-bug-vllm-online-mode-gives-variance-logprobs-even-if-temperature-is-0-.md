# vllm-project/vllm#7779: [Bug]: vllm online mode gives variance logprobs even if temperature is 0 with same prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#7779](https://github.com/vllm-project/vllm/issues/7779) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm online mode gives variance logprobs even if temperature is 0 with same prompt

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For vllm online mode, I observed the logprob is slightly different with same prompt, same openai client parameter and temperature is 0 for different outputs. Please see two examples at the bottom of this message. It may cause unexpected output sometimes. What I want is a deterministic and consistent output for a same prompt in multiple runs. The openai client parameter in use is: ``` 024-08-22 07:45:26: openai_client_call: model_kwargs={'model': 'hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4', 'stream': False, 'max_tokens': 10240, 'temperature': 0, 'n': 1, 'seed': 42, 'extra_body': {'top_k': 1}, 'logprobs': True, 'top_logprobs': 5} ``` Interesting thing here is if I use offline mode, the logprob is always same regardless how many times run. What's the difference between offline mode and online mode? Any suggestion for this issue? Thanks in advance! First token generated twice. Although the order is same, but logprob isn't 100% same. ``` 2024-08-22 07:44:53: LOGPROBS in json= 2024-08-22 07:44:53: [ { "token": "Based", "logprob": 0.29491642842156046, "top_logprobs": [ { "token": "Based", "logprob": "-1.221063256263733(0.29491...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: with same prompt, same openai client parameter and temperature is 0 for different outputs. Please see two examples at the bottom of this message. It may cause unexpected output sometimes. What I want is a deterministic...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 024-08-22 07:45:26: openai_client_call: model_kwargs={'model': 'hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4', 'stream': False, 'max_tokens': 10240, 'temperature': 0, 'n': 1, 'seed': 42, 'extra_body': {'top_k': 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: client parameter in use is: ``` 024-08-22 07:45:26: openai_client_call: model_kwargs={'model': 'hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4', 'stream': False, 'max_tokens': 10240, 'temperature': 0, 'n': 1, 'seed...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: del': 'hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4', 'stream': False, 'max_tokens': 10240, 'temperature': 0, 'n': 1, 'seed': 42, 'extra_body': {'top_k': 1}, 'logprobs': True, 'top_logprobs': 5} ``` Interesting t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: this message. It may cause unexpected output sometimes. What I want is a deterministic and consistent output for a same prompt in multiple runs. The openai client parameter in use is: ``` 024-08-22 07:45:26: openai_clie...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
