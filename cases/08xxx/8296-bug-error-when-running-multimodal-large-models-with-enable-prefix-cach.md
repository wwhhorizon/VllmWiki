# vllm-project/vllm#8296: [Bug]: Error when running multimodal large models with --enable-prefix-caching

| 字段 | 值 |
| --- | --- |
| Issue | [#8296](https://github.com/vllm-project/vllm/issues/8296) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error when running multimodal large models with --enable-prefix-caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I was using vllm to launch the Qwen2-VL model service, I configured the parameter --enable-prefix-caching. An error occurred when the service requested the second image. It seems that during the current use, this parameter is not compatible with multimodal large models. Do we have plans to fix this bug for compatibility in the future? ![下载](https://github.com/user-attachments/assets/4921b87d-cabb-4faa-945b-14ebc4f1478d) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error when running multimodal large models with --enable-prefix-caching bug;stale ### Your current environment ### 🐛 Describe the bug When I was using vllm to launch the Qwen2-VL model service, I configured the p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: or when running multimodal large models with --enable-prefix-caching bug;stale ### Your current environment ### 🐛 Describe the bug When I was using vllm to launch the Qwen2-VL model service, I configured the parameter -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 8d) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
