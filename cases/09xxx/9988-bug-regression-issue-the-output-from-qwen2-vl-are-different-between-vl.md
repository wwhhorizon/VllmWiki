# vllm-project/vllm#9988: [Bug]: [Regression Issue] The output from Qwen2 VL are different between vLLM v0.6.3-post1 and vLLM v0.6.1-post2

| 字段 | 值 |
| --- | --- |
| Issue | [#9988](https://github.com/vllm-project/vllm/issues/9988) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [Regression Issue] The output from Qwen2 VL are different between vLLM v0.6.3-post1 and vLLM v0.6.1-post2

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The bug is for the same input to the model in Qwen/Qwen2-VL (7B and 72B) on vLLM v0.6.3-post1 and v0.6.1-post1 are different. Moreover, the vLLM services will easily die from hitting the same slicing issue error as https://github.com/vllm-project/vllm/issues/9848 https://github.com/vllm-project/vllm/issues/9963 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [Regression Issue] The output from Qwen2 VL are different between vLLM v0.6.3-post1 and vLLM v0.6.1-post2 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The bug...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: [Regression Issue] The output from Qwen2 VL are different between vLLM v0.6.3-post1 and vLLM v0.6.1-post2 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The bug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nt. Moreover, the vLLM services will easily die from hitting the same slicing issue error as https://github.com/vllm-project/vllm/issues/9848 https://github.com/vllm-project/vllm/issues/9963 ### Before submitting a new...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 963 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: en2 VL are different between vLLM v0.6.3-post1 and vLLM v0.6.1-post2 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The bug is for the same input to the model in Qwen/Q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
