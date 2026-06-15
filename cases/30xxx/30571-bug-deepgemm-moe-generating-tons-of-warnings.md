# vllm-project/vllm#30571: [Bug]: DeepGEMM MoE generating tons of warnings

| 字段 | 值 |
| --- | --- |
| Issue | [#30571](https://github.com/vllm-project/vllm/issues/30571) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepGEMM MoE generating tons of warnings

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running models with DeepGEMM currently leads to tons of these warnings in the output, during both startup and inference: ``` (EngineCore_DP3 pid=1608190) WARNING 12-12 11:54:11 [vllm.py:1394] Current vLLM config is not set. (EngineCore_DP3 pid=1608190) INFO 12-12 11:54:11 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=2048. ``` This is because `deep_gemm_moe_fp8` constructs a new `FusedMoEModularKernel` each time it's called. `FusedMoEModularKernel.__init__()` calls `get_current_vllm_config()`, and since the config is not set at runtime, it constructs a new `VllmConfig`, triggering the warnings. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ngs bug ### Your current environment ### 🐛 Describe the bug Running models with DeepGEMM currently leads to tons of these warnings in the output, during both startup and inference: ``` (EngineCore_DP3 pid=1608190) WARNI...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: DeepGEMM MoE generating tons of warnings bug ### Your current environment ### 🐛 Describe the bug Running models with DeepGEMM currently leads to tons of these warnings in the output, during both startup and infer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: LLM config is not set. (EngineCore_DP3 pid=1608190) INFO 12-12 11:54:11 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=2048. ``` This is because `deep_gemm_moe_fp8` constructs a new `FusedMoEM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ed with max_num_batched_tokens=2048. ``` This is because `deep_gemm_moe_fp8` constructs a new `FusedMoEModularKernel` each time it's called. `FusedMoEModularKernel.__init__()` calls `get_current_vllm_config()`, and sinc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
