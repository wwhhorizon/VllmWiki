# vllm-project/vllm#10197: [New Model]: https://huggingface.co/jinaai/jina-clip-v1

| 字段 | 值 |
| --- | --- |
| Issue | [#10197](https://github.com/vllm-project/vllm/issues/10197) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: https://huggingface.co/jinaai/jina-clip-v1

### Issue 正文摘录

### The model to consider. https://huggingface.co/jinaai/jina-clip-v1 ### The closest model vllm already supports. CLIP ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: https://huggingface.co/jinaai/jina-clip-v1 new-model;stale ### The model to consider. https://huggingface.co/jinaai/jina-clip-v1 ### The closest model vllm already supports. CLIP ### What's your difficulty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: https://huggingface.co/jinaai/jina-clip-v1 new-model;stale ### The model to consider. https://huggingface.co/jinaai/jina-clip-v1 ### The closest model vllm already supports. CLIP ### What's your difficulty...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
