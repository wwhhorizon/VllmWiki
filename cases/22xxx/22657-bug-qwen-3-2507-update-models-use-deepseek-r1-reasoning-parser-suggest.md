# vllm-project/vllm#22657: [Bug]: Qwen 3 2507 update models use `deepseek_r1` reasoning parser - suggest renaming

| 字段 | 值 |
| --- | --- |
| Issue | [#22657](https://github.com/vllm-project/vllm/issues/22657) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen 3 2507 update models use `deepseek_r1` reasoning parser - suggest renaming

### Issue 正文摘录

### Your current environment v0.10.1+gptoss ### 🐛 Describe the bug The Qwen 3 2507 update models (e.x. `Qwen/Qwen3-4B-Thinking-2507-FP8`) require the `deepseek_r1 reasoning parser. The older models (e.x. `Qwen/Qwen3-32B-FP8`) require the `qwen3` reasoning parser. This is a confusing inconsistency, and one of the two should be updated (or a third parser should be added). See: #22507 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen 3 2507 update models use `deepseek_r1` reasoning parser - suggest renaming bug;stale ### Your current environment v0.10.1+gptoss ### 🐛 Describe the bug The Qwen 3 2507 update models (e.x. `Qwen/Qwen3-4B-Thin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: he bug The Qwen 3 2507 update models (e.x. `Qwen/Qwen3-4B-Thinking-2507-FP8`) require the `deepseek_r1 reasoning parser. The older models (e.x. `Qwen/Qwen3-32B-FP8`) require the `qwen3` reasoning parser. This is a confu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 07 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: update models use `deepseek_r1` reasoning parser - suggest renaming bug;stale ### Your current environment v0.10.1+gptoss ### 🐛 Describe the bug The Qwen 3 2507 update models (e.x. `Qwen/Qwen3-4B-Thinking-2507-FP8`) req...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
