# vllm-project/vllm#19630: [Perf]: Support non-contiguous input for `dynamic_scaled_int8_quant` and `dynamic_per_token_scaled_fp8_quant`

| 字段 | 值 |
| --- | --- |
| Issue | [#19630](https://github.com/vllm-project/vllm/issues/19630) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Perf]: Support non-contiguous input for `dynamic_scaled_int8_quant` and `dynamic_per_token_scaled_fp8_quant`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch From https://github.com/vllm-project/vllm/pull/19452 We temporally force input to be contiguous, which may cause a high copy overhead when input is not contiguous. I'm trying to work on this to support non-contiguous input for the quant kernel. Scope: - `dynamic_scaled_int8_quant` - `dynamic_per_token_scaled_fp8_quant` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Perf]: Support non-contiguous input for `dynamic_scaled_int8_quant` and `dynamic_per_token_scaled_fp8_quant` feature request ### 🚀 The feature, motivation and pitch From https://github.com/vllm-project/vllm/pull/19452...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Perf]: Support non-contiguous input for `dynamic_scaled_int8_quant` and `dynamic_per_token_scaled_fp8_quant` feature request ### 🚀 The feature, motivation and pitch From https://github.com/vllm-project/vllm/pull/19452...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: amic_scaled_int8_quant` and `dynamic_per_token_scaled_fp8_quant` feature request ### 🚀 The feature, motivation and pitch From https://github.com/vllm-project/vllm/pull/19452 We temporally force input to be contiguous, w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
