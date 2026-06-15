# vllm-project/vllm#25926: [Usage]: Error when loading TIGER-Lab/VLM2Vec-Qwen2VL-2B

| 字段 | 值 |
| --- | --- |
| Issue | [#25926](https://github.com/vllm-project/vllm/issues/25926) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Error when loading TIGER-Lab/VLM2Vec-Qwen2VL-2B

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference for TIGER-Lab/VLM2Vec-Qwen2VL-2b. I don't know how to initialize it with vllm. I am doing like: llm = LLM( model="TIGER-Lab/VLM2Vec-Qwen2VL-2b", runner="pooling", trust_remote_code=True, ) But get failure "There is no module or parameter named 'base_model' in Qwen2VLForConditionalGeneration" when load weights. It looks there are some config setting issues which cause weight key name mismatch. Thanks in advance for any advice to debug this! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Error when loading TIGER-Lab/VLM2Vec-Qwen2VL-2B usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference for TIGER-Lab/VLM2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: looks there are some config setting issues which cause weight key name mismatch. Thanks in advance for any advice to debug this! ### Before submitting a new issue... - [x] Make sure you already searched for relevant iss...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t looks there are some config setting issues which cause weight key name mismatch. Thanks in advance for any advice to debug this! ### Before submitting a new issue... - [x] Make sure you already searched for relevant i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
