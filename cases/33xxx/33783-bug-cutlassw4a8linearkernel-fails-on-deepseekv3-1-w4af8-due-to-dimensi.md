# vllm-project/vllm#33783: [Bug]: CutlassW4A8LinearKernel fails on DeepSeekV3.1 W4AF8 due to dimension alignment (K=7168, N=2112 not divisible by 128)

| 字段 | 值 |
| --- | --- |
| Issue | [#33783](https://github.com/vllm-project/vllm/issues/33783) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CutlassW4A8LinearKernel fails on DeepSeekV3.1 W4AF8 due to dimension alignment (K=7168, N=2112 not divisible by 128)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### **Description** When serving a **DeepSeek-V3.1** model quantized via `llm-compressor` (AWQ W4A8, `compressed-tensors` format), vLLM fails to initialize the model. The error is caused by a shape mismatch in the `CutlassW4A8LinearKernel`, which strictly requires both **K** and **N** dimensions to be multiples of **128**. In DeepSeek-V3's architecture, specific MoE or attention projections result in dimensions (e.g., ) that do not satisfy this alignment constraint. --- ### **Environment** * **vLLM Version:** 0.15.0 (Commit/Patch: `147`) * **Model:** DeepSeek-V3.1 (Quantized to W4A8 AWQ via `llm-compressor`) * **Quantization Format:** `compressed-tensors` (Weights: INT4, Group_size: 128; Activations: FP8 Dynamic) * **Hardware:** 8 x GPUs (TP=8, EP enabled) --- ### **Model Configuration (`config.json`)** Key parameters that contribute to the tensor shapes: ```json { "model_type": "deepseek_v3", "hidden_size": 7168, "intermediate_size": 18432, "moe_intermediate_size": 2048, "n_routed_experts": 256, "quantization_config": { "quant_method": "compressed-tensors", "format": "pack-quantized", "config_groups": { "group_0": { "input_activ...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: imensions to be multiples of **128**. In DeepSeek-V3's architecture, specific MoE or attention projections result in dimensions (e.g., ) that do not satisfy this alignment constraint. --- ### **Environment** * **vLLM Ve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ibe the bug ### **Description** When serving a **DeepSeek-V3.1** model quantized via `llm-compressor` (AWQ W4A8, `compressed-tensors` format), vLLM fails to initialize the model. The error is caused by a shape mismatch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t), vLLM fails to initialize the model. The error is caused by a shape mismatch in the `CutlassW4A8LinearKernel`, which strictly requires both **K** and **N** dimensions to be multiples of **128**. In DeepSeek-V3's arch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Describe the bug ### **Description** When serving a **DeepSeek-V3.1** model quantized via `llm-compressor` (AWQ W4A8, `compressed-tensors` format), vLLM fails to initialize the model. The error is caused by a shape mism...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ons to be multiples of **128**. In DeepSeek-V3's architecture, specific MoE or attention projections result in dimensions (e.g., ) that do not satisfy this alignment constraint. --- ### **Environment** * **vLLM Version:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
