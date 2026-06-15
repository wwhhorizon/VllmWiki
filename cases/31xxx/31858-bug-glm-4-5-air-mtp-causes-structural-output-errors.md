# vllm-project/vllm#31858: [Bug]: GLM-4.5-Air + MTP causes structural output errors

| 字段 | 值 |
| --- | --- |
| Issue | [#31858](https://github.com/vllm-project/vllm/issues/31858) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5-Air + MTP causes structural output errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying GLM-4.5-Air with MTP (Multi-Token Prediction) and sending requests with structural output (like JSON schema), the output content does not conform to the schema constraints. Specifically, the observed behavior is that extra tokens appear before the structured output content. For example, the output starts with `A{` or ` ```{ ` instead of directly starting with `{`. When MTP is disabled, GLM-4.5-Air produces correct results. When deploying with SGLang with MTP enabled, the output is also correct. **Initial suspicion**: Tokens predicted by MTP that don't meet the structured output requirements are not being rolled back properly. **Additional note**: When deploying Qwen3-Next-80B with MTP, this issue does not seem to occur - all test requests I sent returned correctly formatted results. **How to reproduce** Deployment command: ```bash vllm serve \ /path/to/GLM-4.5-Air \ --served-model-name "glm-4.5-air" \ --enable-export-parallel \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.85 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --max-num-seqs 32 \ --max-model-len 65536 \ --rea...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: are not being rolled back properly. **Additional note**: When deploying Qwen3-Next-80B with MTP, this issue does not seem to occur - all test requests I sent returned correctly formatted results. **How to reproduce** De...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: GLM-4.5-Air + MTP causes structural output errors bug;stale ### Your current environment ### 🐛 Describe the bug When deploying GLM-4.5-Air with MTP (Multi-Token Prediction) and sending requests with structural ou...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uto-tool-choice \ --tool-call-parser glm45 \ --structured-outputs-config.backend guidance \ --host 0.0.0.0 \ --port 20080 ``` Request example (the prompt intentionally includes extra guidance to make the issue easier to...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ll test requests I sent returned correctly formatted results. **How to reproduce** Deployment command: ```bash vllm serve \ /path/to/GLM-4.5-Air \ --served-model-name "glm-4.5-air" \ --enable-export-parallel \ --tensor-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ema), the output content does not conform to the schema constraints. Specifically, the observed behavior is that extra tokens appear before the structured output content. For example, the output starts with `A{` or ` ``...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
