# vllm-project/vllm#27570: [Bug]: Qwen2.5 ViT Incorrect QKV Split When projection_size != hidden_size in Tensor Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#27570](https://github.com/vllm-project/vllm/issues/27570) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5 ViT Incorrect QKV Split When projection_size != hidden_size in Tensor Parallelism

### Issue 正文摘录

### Your current environment ``` vllm 0.10.1.1 torch 2.7.1 ``` ### 🐛 Describe the bug When using Qwen2.5 ViT with tensor parallelism, the QKV projection tensor is being split incorrectly when `projection_size` differs from `hidden_size`. The code currently splits the QKV tensor using `hidden_size // tp_size`: https://github.com/vllm-project/vllm/blob/a663f6ae64c88f0a708d3cb66b9918a659a6e868/vllm/model_executor/models/qwen2_5_vl.py#L366 https://github.com/vllm-project/vllm/blob/a663f6ae64c88f0a708d3cb66b9918a659a6e868/vllm/model_executor/models/qwen2_5_vl.py#L294-L296 This causes incorrect tensor dimensions when `projection_size != hidden_size`. For example, our model's `hidden_size` is 1280 and `projection_size` is 1536. Each rank's tensor has size 576 (192*3, TP 8). The tensor is split by `1280 / 8 = 160` instead of `1536 / 8 = 192`. The qkv concat result has the wrong order. To fix this, modify the tensor splitting logic to use `projection_size` instead of `hidden_size` when calculating chunk sizes for tensor parallelism. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: correct QKV Split When projection_size != hidden_size in Tensor Parallelism bug;stale ### Your current environment ``` vllm 0.10.1.1 torch 2.7.1 ``` ### 🐛 Describe the bug When using Qwen2.5 ViT with tensor parallelism,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5 ViT Incorrect QKV Split When projection_size != hidden_size in Tensor Parallelism bug;stale ### Your current environment ``` vllm 0.10.1.1 torch 2.7.1 ``` ### 🐛 Describe the bug When using Qwen2.5 ViT wit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: QKV Split When projection_size != hidden_size in Tensor Parallelism bug;stale ### Your current environment ``` vllm 0.10.1.1 torch 2.7.1 ``` ### 🐛 Describe the bug When using Qwen2.5 ViT with tensor parallelism, the QKV...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
