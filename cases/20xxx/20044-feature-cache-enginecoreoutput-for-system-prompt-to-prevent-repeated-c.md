# vllm-project/vllm#20044: [Feature]: Cache EngineCoreOutput for system prompt to prevent repeated calculation

| 字段 | 值 |
| --- | --- |
| Issue | [#20044](https://github.com/vllm-project/vllm/issues/20044) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Cache EngineCoreOutput for system prompt to prevent repeated calculation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch My company is prefixing a common system prompt to all requests we serve through vLLM. Currently, when we call add_request, we send a request with prompt_token_ids including the entire system prompt. Every time we schedule a request, we are forced to schedule these common system prompt tokens over and over again. The RFC I propose is, instead of passing the system prompt tokens per-request, we add a function add_system_prompt which schedules a dummy request whose prompt solely consists of the system prompt. We cache the resulting EngineCoreOutputs. Finally, when we start serving requests, we simply set num_computed_tokens to num_tokens_in_sys_prompt // block_size * block_size. To prevent evicting the system prompt KVCacheBlocks, we add a 'permanent' flag to the KVCacheBlock data structure, and set this flag in the add_system_prompt function. This feature would significantly help our inference for short context window (max_model_len=2048). We are wondering if our reasoning is sound, or if there are issues. @WoosukKwon @youkaichao @comaniac ### Alternatives _No response_ ### Additional context We expect to see a 36% decrease in latency when max...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: gineCoreOutput for system prompt to prevent repeated calculation feature request;stale ### 🚀 The feature, motivation and pitch My company is prefixing a common system prompt to all requests we serve through vLLM. Curren...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: No response_ ### Additional context We expect to see a 36% decrease in latency when max_model_len=2048. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 48. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: quests, we simply set num_computed_tokens to num_tokens_in_sys_prompt // block_size * block_size. To prevent evicting the system prompt KVCacheBlocks, we add a 'permanent' flag to the KVCacheBlock data structure, and se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ure would significantly help our inference for short context window (max_model_len=2048). We are wondering if our reasoning is sound, or if there are issues. @WoosukKwon @youkaichao @comaniac ### Alternatives _No respon...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
