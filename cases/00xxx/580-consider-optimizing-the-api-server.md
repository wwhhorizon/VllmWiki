# vllm-project/vllm#580: Consider optimizing the API server

| 字段 | 值 |
| --- | --- |
| Issue | [#580](https://github.com/vllm-project/vllm/issues/580) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Consider optimizing the API server

### Issue 正文摘录

Consider optimizing the FastAPI/OpenAI API server in vLLM as the server is widely used and seems to have a lot of overhead. On 1xA100 Llama 13B, the `LLM` class reaches 90~100% GPU utilization, while the API server can only utilize 50% Related: https://github.com/vllm-project/vllm/discussions/459

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: M as the server is widely used and seems to have a lot of overhead. On 1xA100 Llama 13B, the `LLM` class reaches 90~100% GPU utilization, while the API server can only utilize 50% Related: https://github.com/vllm-projec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: the server is widely used and seems to have a lot of overhead. On 1xA100 Llama 13B, the `LLM` class reaches 90~100% GPU utilization, while the API server can only utilize 50% Related: https://github.com/vllm-project/vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
