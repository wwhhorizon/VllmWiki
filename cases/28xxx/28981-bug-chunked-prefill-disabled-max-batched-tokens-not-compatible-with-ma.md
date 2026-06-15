# vllm-project/vllm#28981: [Bug]: chunked prefill disabled & max batched tokens not compatible with max model length on non-X86 CPU Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#28981](https://github.com/vllm-project/vllm/issues/28981) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: chunked prefill disabled & max batched tokens not compatible with max model length on non-X86 CPU Backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For non-x86 CPU backends it seems chunked prefill isn’t supported `([arg_utils.py:1376] Chunked prefill is not supported for ARM and POWER, S390X and RISC-V CPUs; disabling it for V1 backend.)` and there isn’t code to update max_num_batched_tokens to be compatible with max_model_len ``` (APIServer pid=63635) pydantic_core._pydantic_core.ValidationError: 1 validation error for SchedulerConfig (APIServer pid=63635) Value error, max_num_batched_tokens (2048) is smaller than max_model_len (40960). This effectively limits the maximum sequence length to max_num_batched_tokens and makes vLLM reject longer sequences. Please increase max_num_batched_tokens or decrease max_model_len. [type=value_error, input_value=ArgsKwargs((), {'runner_t..., 'stream_interval': 1}), input_type=ArgsKwargs] ``` This means the user has to manually set this themselves. We should `self.max_num_batched_tokens = model_config.max_model_len` when chunked prefill is disabled. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs....

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ig (APIServer pid=63635) Value error, max_num_batched_tokens (2048) is smaller than max_model_len (40960). This effectively limits the maximum sequence length to max_num_batched_tokens and makes vLLM reject longer seque...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ]: chunked prefill disabled & max batched tokens not compatible with max model length on non-X86 CPU Backend bug;cpu ### Your current environment ### 🐛 Describe the bug For non-x86 CPU backends it seems chunked prefill...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: chunked prefill disabled & max batched tokens not compatible with max model length on non-X86 CPU Backend bug;cpu ### Your current environment ### 🐛 Describe the bug For non-x86 CPU backends it seems chunked pref...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: & max batched tokens not compatible with max model length on non-X86 CPU Backend bug;cpu ### Your current environment ### 🐛 Describe the bug For non-x86 CPU backends it seems chunked prefill isn’t supported `([arg_utils...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
