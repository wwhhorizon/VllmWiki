# vllm-project/vllm#1426: StableLM-3B Support

| 字段 | 值 |
| --- | --- |
| Issue | [#1426](https://github.com/vllm-project/vllm/issues/1426) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> StableLM-3B Support

### Issue 正文摘录

[StableLM-3B](https://huggingface.co/stabilityai/stablelm-3b-4e1t) is the most powerful 3B LLM yet. Adding support in vLLM (with awq quantization) would help many working in latency-sensitive use-cases where bigger LLMs are too slow.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: StableLM-3B Support new-model [StableLM-3B](https://huggingface.co/stabilityai/stablelm-3b-4e1t) is the most powerful 3B LLM yet. Adding support in vLLM (with awq quantization) would help many working in latency-sensiti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -4e1t) is the most powerful 3B LLM yet. Adding support in vLLM (with awq quantization) would help many working in latency-sensitive use-cases where bigger LLMs are too slow.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: dding support in vLLM (with awq quantization) would help many working in latency-sensitive use-cases where bigger LLMs are too slow.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
