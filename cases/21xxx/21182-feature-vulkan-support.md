# vllm-project/vllm#21182: [Feature]: Vulkan support

| 字段 | 值 |
| --- | --- |
| Issue | [#21182](https://github.com/vllm-project/vllm/issues/21182) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Vulkan support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I started hacking on vLLM recently for RamaLama and other reasons to see what the hardware support is like compared to llama.cpp. The one big noticeable gap is Vulkan support. It would solve a bunch of problems around vLLM not running great on commodity hardware: https://github.com/containers/ramalama/pull/1677 ### Alternatives Use llama.cpp ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Vulkan support feature request;unstale ### 🚀 The feature, motivation and pitch I started hacking on vLLM recently for RamaLama and other reasons to see what the hardware support is like compared to llama.cpp....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a and other reasons to see what the hardware support is like compared to llama.cpp. The one big noticeable gap is Vulkan support. It would solve a bunch of problems around vLLM not running great on commodity hardware: h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
