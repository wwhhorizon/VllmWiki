# vllm-project/vllm#17069: [Feature]: GGUF support for GLM4

| 字段 | 值 |
| --- | --- |
| Issue | [#17069](https://github.com/vllm-project/vllm/issues/17069) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GGUF support for GLM4

### Issue 正文摘录

### 🚀 The feature, motivation and pitch GLM4 is a powerful LLM by THUDM. ### Alternatives I could run with BF16 with 9B model but that requires larger VRAM usage. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: GGUF support for GLM4 feature request;stale ### 🚀 The feature, motivation and pitch GLM4 is a powerful LLM by THUDM. ### Alternatives I could run with BF16 with 9B model but that requires larger VRAM usage. #...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: h GLM4 is a powerful LLM by THUDM. ### Alternatives I could run with BF16 with 9B model but that requires larger VRAM usage. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: powerful LLM by THUDM. ### Alternatives I could run with BF16 with 9B model but that requires larger VRAM usage. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already sear...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
