# vllm-project/vllm#26775: [Bug]: ModelRegistry.inspect_model_cls shows that Qwen3ForCausalLM is not pooling model

| 字段 | 值 |
| --- | --- |
| Issue | [#26775](https://github.com/vllm-project/vllm/issues/26775) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ModelRegistry.inspect_model_cls shows that Qwen3ForCausalLM is not pooling model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug but the doc says that Qwen3ForCausalLM is embedding model ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ModelRegistry.inspect_model_cls shows that Qwen3ForCausalLM is not pooling model bug;stale ### Your current environment ### 🐛 Describe the bug but the doc says that Qwen3ForCausalLM is embedding model ### Befor
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: y.inspect_model_cls shows that Qwen3ForCausalLM is not pooling model bug;stale ### Your current environment ### 🐛 Describe the bug but the doc says that Qwen3ForCausalLM is embedding model ### Before submitting a new is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
