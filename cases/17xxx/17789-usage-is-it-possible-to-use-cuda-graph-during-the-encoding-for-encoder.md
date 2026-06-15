# vllm-project/vllm#17789: [Usage]: Is it possible to use CUDA Graph during the encoding for encoder-decoder models?

| 字段 | 值 |
| --- | --- |
| Issue | [#17789](https://github.com/vllm-project/vllm/issues/17789) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is it possible to use CUDA Graph during the encoding for encoder-decoder models?

### Issue 正文摘录

### Your current environment vLLM v0.8.3 ### How would you like to use vllm I understand that CUDA Graph is already supported during decoding for encoder-decoder models. Is it possible to also apply CUDA Graph during encoding? #7631 ![Image](https://github.com/user-attachments/assets/9dbe1c1c-d67d-4070-89f2-11ce3023be8a) ![Image](https://github.com/user-attachments/assets/f070a099-66ba-4959-b64c-1e09b3291b4b) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Is it possible to use CUDA Graph during the encoding for encoder-decoder models? usage;stale ### Your current environment vLLM v0.8.3 ### How would you like to use vllm I understand that CUDA Graph is already s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Usage]: Is it possible to use CUDA Graph during the encoding for encoder-decoder models? usage;stale ### Your current environment vLLM v0.8.3 ### How would you like to use vllm I understand that CUDA Graph is already su...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Is it possible to use CUDA Graph during the encoding for encoder-decoder models? usage;stale ### Your current environment vLLM v0.8.3 ### How would you like to use vllm I understand that CUDA Graph is already supported...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
