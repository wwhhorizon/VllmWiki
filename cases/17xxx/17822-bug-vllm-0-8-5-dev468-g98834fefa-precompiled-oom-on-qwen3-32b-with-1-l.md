# vllm-project/vllm#17822: [Bug]: vllm 0.8.5.dev468+g98834fefa.precompiled OOM on Qwen3-32B with 1 lora module

| 字段 | 值 |
| --- | --- |
| Issue | [#17822](https://github.com/vllm-project/vllm/issues/17822) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.8.5.dev468+g98834fefa.precompiled OOM on Qwen3-32B with 1 lora module

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Environment vLLM Version: 0.8.5.dev468+g98834fefa.precompiled Model: Qwen3-32B Scenario: LoRA module enabled Description When running Qwen3-32B with a LoRA module enabled, the system experiences an Out of Memory (OOM) error. Reproduction Steps Attempt to run Qwen3-32B with LoRA module Observe OOM error Observations Without LoRA module: Model starts successfully With VLLM_USE_V1=0: Model starts successfully With VLLM_USE_V1=1: OOM error occurs Attempted Mitigations Adjusted max-num-seqs Modified gpu_memory_utilization No successful resolution observed System Configuration No specific details provided about hardware/GPU configuration Possible Impact This issue prevents using the Qwen3-32B model with LoRA in vLLM 0.8.5.dev Suggested Next Steps Investigate memory allocation differences when LoRA is enabled Check compatibility between Qwen3-32B, LoRA implementation, and current vLLM version Verify if this is a regression in the latest development build Additional Information Needed GPU model and memory Full command used to start the model Complete error log Reproducibility Consistent OOM when VLLM_USE_V1=1 and LoRA enabled /cc @vllm-p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: vllm 0.8.5.dev468+g98834fefa.precompiled OOM on Qwen3-32B with 1 lora module bug;stale ### Your current environment ### 🐛 Describe the bug Environment vLLM Version: 0.8.5.dev468+g98834fefa.precompiled Model: Qwen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm 0.8.5.dev468+g98834fefa.precompiled OOM on Qwen3-32B with 1 lora module bug;stale ### Your current environment ### 🐛 Describe the bug Environment vLLM Version: 0.8.5.dev468+g98834fefa.precompiled Model: Qwen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ge) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: t OOM when VLLM_USE_V1=1 and LoRA enabled /cc @vllm-project/maintainers Reproducible: Yes Severity: High (Blocks model usage) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: .5.dev468+g98834fefa.precompiled OOM on Qwen3-32B with 1 lora module bug;stale ### Your current environment ### 🐛 Describe the bug Environment vLLM Version: 0.8.5.dev468+g98834fefa.precompiled Model: Qwen3-32B Scenario:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
