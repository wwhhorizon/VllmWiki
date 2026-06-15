# vllm-project/vllm#17429: [Bug]: fused moe lose weight_loader in verl

| 字段 | 值 |
| --- | --- |
| Issue | [#17429](https://github.com/vllm-project/vllm/issues/17429) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: fused moe lose weight_loader in verl

### Issue 正文摘录

### Your current environment vllm == 0.8.4 ### 🐛 Describe the bug In vLLM 0.8.4, for the Qwen3-MoE model, verl still faces the issue we mentioned before: the weight_loader does not exist. We initially thought this was unique to DeepseekV3ForCausalLM, but now we confirm it’s likely a problem with FusedMoE, affecting all MoE-related models. This is our current [workaround](https://github.com/volcengine/verl/blob/main/verl/utils/vllm_utils.py), but I think it needs to be fixed in vLLM. Any suggestions? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vironment vllm == 0.8.4 ### 🐛 Describe the bug In vLLM 0.8.4, for the Qwen3-MoE model, verl still faces the issue we mentioned before: the weight_loader does not exist. We initially thought this was unique to DeepseekV3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: fused moe lose weight_loader in verl bug;stale ### Your current environment vllm == 0.8.4 ### 🐛 Describe the bug In vLLM 0.8.4, for the Qwen3-MoE model, verl still faces the issue we mentioned before: the weight_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: fused moe lose weight_loader in verl bug;stale ### Your current environment vllm == 0.8.4 ### 🐛 Describe the bug In vLLM 0.8.4, for the Qwen3-MoE model, verl still faces the issue we mentioned before: the weight_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
