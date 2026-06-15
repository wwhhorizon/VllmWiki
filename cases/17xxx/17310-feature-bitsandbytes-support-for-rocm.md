# vllm-project/vllm#17310: [Feature]: Bitsandbytes support for ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#17310](https://github.com/vllm-project/vllm/issues/17310) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Bitsandbytes support for ROCm

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As Bitsandbytes has (still alpha) support for Bitsandbytes on other arches than CUDA: https://huggingface.co/docs/bitsandbytes/main/en/non_cuda_backends Hence, support for ROCm (and other arches) in vLLM would be super nice. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Bitsandbytes support for ROCm feature request;stale ### 🚀 The feature, motivation and pitch As Bitsandbytes has (still alpha) support for Bitsandbytes on other arches than CUDA: https://huggingface.co/docs/bi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Bitsandbytes support for ROCm feature request;stale ### 🚀 The feature, motivation and pitch As Bitsandbytes has (still alpha) support for Bitsandbytes on other arches than CUDA: https://huggingface.co/docs/bi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: hes than CUDA: https://huggingface.co/docs/bitsandbytes/main/en/non_cuda_backends Hence, support for ROCm (and other arches) in vLLM would be super nice. ### Alternatives _No response_ ### Additional context _No respons...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: still alpha) support for Bitsandbytes on other arches than CUDA: https://huggingface.co/docs/bitsandbytes/main/en/non_cuda_backends Hence, support for ROCm (and other arches) in vLLM would be super nice. ### Alternative...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
