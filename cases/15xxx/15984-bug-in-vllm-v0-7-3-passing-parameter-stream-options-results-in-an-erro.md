# vllm-project/vllm#15984: [Bug]: In vllm v0.7.3, passing parameter "stream_options" results in an error.

| 字段 | 值 |
| --- | --- |
| Issue | [#15984](https://github.com/vllm-project/vllm/issues/15984) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: In vllm v0.7.3, passing parameter "stream_options" results in an error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deploy model using vLLM v0.7.3 with CPU resources. I get an error when calling the v1/chat/completions API with the parameter "stream_options": {"include_usage": true}. ![Image](https://github.com/user-attachments/assets/7c93c65b-8f8b-413e-816b-8e84285c8357) **From which version does the vllm-cpu version support this parameter?** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r-attachments/assets/7c93c65b-8f8b-413e-816b-8e84285c8357) **From which version does the vllm-cpu version support this parameter?** ### Before submitting a new issue... - [x] Make sure you already searched for relevant...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ?** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ;stale ### Your current environment ### 🐛 Describe the bug I deploy model using vLLM v0.7.3 with CPU resources. I get an error when calling the v1/chat/completions API with the parameter "stream_options": {"include_usag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vllm v0.7.3, passing parameter "stream_options" results in an error. bug;stale ### Your current environment ### 🐛 Describe the bug I deploy model using vLLM v0.7.3 with CPU resources. I get an error when calling the v1/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
