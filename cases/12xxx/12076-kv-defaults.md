# vllm-project/vllm#12076: kv defaults

| 字段 | 值 |
| --- | --- |
| Issue | [#12076](https://github.com/vllm-project/vllm/issues/12076) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> kv defaults

### Issue 正文摘录

Q1: What is the default quantization method used when ```kv_cache_dtype = fp8``` is used while serving a standard checkpoint and what is the granularity - per tensor, per token? Q2: What is the default FP8 format used when the kv_cache_dtype = fp8? E4M3 or E5M2? All information was in the documentation: Thanks for the clarification! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: kv defaults usage Q1: What is the default quantization method used when ```kv_cache_dtype = fp8``` is used while serving a standard checkpoint and what is the granularity - per tensor, per token? Q2: What is the default...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ion! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is the granularity - per tensor, per token? Q2: What is the default FP8 format used when the kv_cache_dtype = fp8? E4M3 or E5M2? All information was in the documentation: Thanks for the clarification! ### Before submitt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
