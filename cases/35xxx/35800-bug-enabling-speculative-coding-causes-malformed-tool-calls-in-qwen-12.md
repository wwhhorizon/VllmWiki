# vllm-project/vllm#35800: [Bug]: Enabling speculative coding causes malformed Tool Calls in Qwen 122B MXFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#35800](https://github.com/vllm-project/vllm/issues/35800) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enabling speculative coding causes malformed Tool Calls in Qwen 122B MXFP4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After enabling speculative decoding on Qwen 122B MXFP4 on RTX 6000, I am frequently seeing malformed tool calls, which implies that guided decoding for tool calls is not functioning when speculative decoding is enabled. It is unclear per the docs whether it is expected that Speculative Decoding disables Guided Decoding, or whether this is a bug. The docs do indicate that speculative decoding outputs mathematically identical tokens when enabled, which gives me the impression that the two features should work together, and there is no note in the feature incompatibility section to indicate these features are incompatible https://docs.vllm.ai/en/latest/features/speculative_decoding/#known-feature-incompatibility Launch options: ``` vllm serve olka-fi/Qwen3.5-122B-A10B-MXFP4 \ --max-num-seqs 128 \ --max-model-len 262144 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_xml \ --port 11434 \ --reasoning-parser qwen3 \ --served-model-name qwen/qwen3.5-122B \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens": 5}' ``` To reproduce, simply try using this model with speculative decoding enabled with any agent, y...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;opera...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: g]: Enabling speculative coding causes malformed Tool Calls in Qwen 122B MXFP4 bug ### Your current environment ### 🐛 Describe the bug After enabling speculative decoding on Qwen 122B MXFP4 on RTX 6000, I am frequently...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: cribe the bug After enabling speculative decoding on Qwen 122B MXFP4 on RTX 6000, I am frequently seeing malformed tool calls, which implies that guided decoding for tool calls is not functioning when speculative decodi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Enabling speculative coding causes malformed Tool Calls in Qwen 122B MXFP4 bug ### Your current environment ### 🐛 Describe the bug After enabling speculative decoding on Qwen 122B MXFP4 on RTX 6000, I am frequent...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quantization;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
