# vllm-project/vllm#32828: [Feature]: Qwen3-Next dual-stream execution in_proj_qkvz in_proj_ba

| 字段 | 值 |
| --- | --- |
| Issue | [#32828](https://github.com/vllm-project/vllm/issues/32828) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen3-Next dual-stream execution in_proj_qkvz in_proj_ba

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In TensorRT LLM, Qwen3-Next `in_proj_qkvz` and `in_proj_ba` are executed in dual stream. [code ref].(https://github.com/NVIDIA/TensorRT-LLM/blob/0434db5bf75dfd01fe575a79c27d9260b597f167/tensorrt_llm/_torch/models/modeling_qwen3_next.py#L777C26-L777C30) See TensorRT LLM nsys screenshot below. The two GEMM are executed in 2 streams in parallel. (Qwen3-Next-80B-A3B TP2 generation step BS=8) VLLM may do this as well. [code ref](https://github.com/vllm-project/vllm/blob/24a163ed77a4dba8f46221c945943f8a3ff7ee27/vllm/model_executor/models/qwen3_next.py#L455C39-L455C49) The actual speedup is not clear yet in terms of problem size (at which concurrency or ISL) but should give benefit to TPOT at low concurrency. (From a BS=8 nsys, hiding 5.05us proj gemm per layer in a 8.5ms gen step, about 1.03x speedup per step) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Qwen3-Next dual-stream execution in_proj_qkvz in_proj_ba feature request ### 🚀 The feature, motivation and pitch In TensorRT LLM, Qwen3-Next `in_proj_qkvz` and `in_proj_ba` are executed in dual stream. [code...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: of problem size (at which concurrency or ISL) but should give benefit to TPOT at low concurrency. (From a BS=8 nsys, hiding 5.05us proj gemm per layer in a 8.5ms gen step, about 1.03x speedup per step) ### Alternatives...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ext.py#L777C26-L777C30) See TensorRT LLM nsys screenshot below. The two GEMM are executed in 2 streams in parallel. (Qwen3-Next-80B-A3B TP2 generation step BS=8) VLLM may do this as well. [code ref](https://github.com/v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ature]: Qwen3-Next dual-stream execution in_proj_qkvz in_proj_ba feature request ### 🚀 The feature, motivation and pitch In TensorRT LLM, Qwen3-Next `in_proj_qkvz` and `in_proj_ba` are executed in dual stream. [code ref...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
