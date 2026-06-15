# vllm-project/vllm#13466: [Bug]: Mamba should return states in fp32

| 字段 | 值 |
| --- | --- |
| Issue | [#13466](https://github.com/vllm-project/vllm/issues/13466) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mamba should return states in fp32

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug There's a difference in the precision of SSM states. - Authors' implementation uses `weight_type`, which is usually fp32: https://github.com/state-spaces/mamba/blob/v2.2.4/csrc/selective_scan/selective_scan.cpp#L313 - vLLM implementation uses `input_t`, which can be 16bit: https://github.com/vllm-project/vllm/blob/v0.7.2/csrc/mamba/mamba_ssm/selective_scan_fwd.cu#L131 This difference seems lowering the quality of generated texts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: N/A ### 🐛 Describe the bug There's a difference in the precision of SSM states. - Authors' implementation uses `weight_type`, which is usually fp32: https://github.com/state-spaces/mamba/blob/v2.2.4/csrc/selective_scan/...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nt environment N/A ### 🐛 Describe the bug There's a difference in the precision of SSM states. - Authors' implementation uses `weight_type`, which is usually fp32: https://github.com/state-spaces/mamba/blob/v2.2.4/csrc/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: environment N/A ### 🐛 Describe the bug There's a difference in the precision of SSM states. - Authors' implementation uses `weight_type`, which is usually fp32: https://github.com/state-spaces/mamba/blob/v2.2.4/csrc/sel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Mamba should return states in fp32 bug;stale ### Your current environment N/A ### 🐛 Describe the bug There's a difference in the precision of SSM states. - Authors' implementation uses `weight_type`, which is usu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
