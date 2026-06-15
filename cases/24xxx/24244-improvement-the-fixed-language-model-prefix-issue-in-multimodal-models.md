# vllm-project/vllm#24244: [Improvement]: The fixed "language_model" prefix issue in multimodal models

| 字段 | 值 |
| --- | --- |
| Issue | [#24244](https://github.com/vllm-project/vllm/issues/24244) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Improvement]: The fixed "language_model" prefix issue in multimodal models

### Issue 正文摘录

### Your current environment vllm 0.10.1.1 vllm ascend 0.10.0 ### 🐛 Describe the bug For multimodal models, the prefix is fixed as "language_model". [qwen2_5_vl.py#L906](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen2_5_vl.py#L906) This may limit extensibility in downstream components. Could we change it to None or expose it as an argument of `__init__` to improve extensibility? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Improvement]: The fixed "language_model" prefix issue in multimodal models bug;stale ### Your current environment vllm 0.10.1.1 vllm ascend 0.10.0 ### 🐛 Describe the bug For multimodal models, the prefix is fixed as "l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ty? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ement]: The fixed "language_model" prefix issue in multimodal models bug;stale ### Your current environment vllm 0.10.1.1 vllm ascend 0.10.0 ### 🐛 Describe the bug For multimodal models, the prefix is fixed as "language...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
