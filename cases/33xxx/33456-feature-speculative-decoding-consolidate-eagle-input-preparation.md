# vllm-project/vllm#33456: [Feature][Speculative Decoding]: Consolidate EAGLE Input Preparation

| 字段 | 值 |
| --- | --- |
| Issue | [#33456](https://github.com/vllm-project/vllm/issues/33456) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Speculative Decoding]: Consolidate EAGLE Input Preparation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, EAGLE's prepare_inputs happens in many steps owned by different callers, such as: - prepare_next_token_ids (_padded) - called by gpu_model_runner - prepare_input_ids (_padded) - called by gpu_model_runner - set_inputs_first_pass - called in propose() Ideally, these should be consolidated into a prepare_inputs() method that is called in propose() and handles all the complexity. This would also allow us to write directly into the buffers used as inputs to the EAGLE model, saving some redundant work that reshapes and updates data before copying it into the buffers. This would require significantly refactoring the interface of the proposer classes, since currently there is a lot of model runner state used in the prepare_* methods. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature][Speculative Decoding]: Consolidate EAGLE Input Preparation feature request;stale ### 🚀 The feature, motivation and pitch Currently, EAGLE's prepare_inputs happens in many steps owned by different callers, such...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ent callers, such as: - prepare_next_token_ids (_padded) - called by gpu_model_runner - prepare_input_ids (_padded) - called by gpu_model_runner - set_inputs_first_pass - called in propose() Ideally, these should be con...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
