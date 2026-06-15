# vllm-project/vllm#32765: [Feature]: Support gemma3 Models in eagle3 Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#32765](https://github.com/vllm-project/vllm/issues/32765) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support gemma3 Models in eagle3 Speculative Decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It looks there is no support in eagle3 speculative decoding for gemma3 models: `` NFO PyProcess W-162-chat-film-stdout: Value error, Eagle3 is only supported for ['llama', 'qwen', 'minicpm', 'gpt_oss'] models. Got self.target_model_config.hf_text_config.model_type='gemma3_text' [type=value_error, input_value=ArgsKwargs((), {'method':..., _api_process_rank=0)}), input_type=ArgsKwargs] INFO PyProcess W-162-chat-film-stdout: For further information visit https://errors.pydantic.dev/2.12/v/value_error `` Is it possible to add it? Thanks! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Feature]: Support gemma3 Models in eagle3 Speculative Decoding feature request;stale ### 🚀 The feature, motivation and pitch It looks there is no support in eagle3 speculative decoding for gemma3 models: `` NFO PyProce...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support gemma3 Models in eagle3 Speculative Decoding feature request;stale ### 🚀 The feature, motivation and pitch It looks there is no support in eagle3 speculative decoding for gemma3 models: `` NFO PyProce...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Support gemma3 Models in eagle3 Speculative Decoding feature request;stale ### 🚀 The feature, motivation and pitch It looks there is no support in eagle3 speculative decoding for gemma3 models: `` NFO PyProce...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
