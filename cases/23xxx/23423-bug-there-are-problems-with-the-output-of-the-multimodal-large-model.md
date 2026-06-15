# vllm-project/vllm#23423: [Bug]: There are problems with the output of the Multimodal large model

| 字段 | 值 |
| --- | --- |
| Issue | [#23423](https://github.com/vllm-project/vllm/issues/23423) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: There are problems with the output of the Multimodal large model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug A multimodal large model (qwen-vl-32b-awq) was deployed using vllm 0.9.2. After uploading an image, the model has a certain probability of returning an empty value or a series of \n. When an exception occurs, the return speed is very fast. However, the vllm backend did not report any errors, and the API could also return normally. What is the reason behind this? Is it related to vllm or to the model itself? How to solve ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: There are problems with the output of the Multimodal large model bug;stale ### Your current environment ### 🐛 Describe the bug A multimodal large model (qwen-vl-32b-awq) was deployed using vllm 0.9.2. After uploa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: en an exception occurs, the return speed is very fast. However, the vllm backend did not report any errors, and the API could also return normally. What is the reason behind this? Is it related to vllm or to the model i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lve ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: There are problems with the output of the Multimodal large model bug;stale ### Your current environment ### 🐛 Describe the bug A multimodal large model (qwen-vl-32b-awq) was deployed using vllm 0.9.2. After uploadin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
