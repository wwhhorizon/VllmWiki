# vllm-project/vllm#31623: [Bug] QKVParallelLinear layers leaking implementation details to compressed-tensors quantization_config targets

| 字段 | 值 |
| --- | --- |
| Issue | [#31623](https://github.com/vllm-project/vllm/issues/31623) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] QKVParallelLinear layers leaking implementation details to compressed-tensors quantization_config targets

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug > [!TIP] > Full workaround and analysis just below: https://github.com/sgl-project/sglang/issues/16295#issuecomment-3706926633 While loading a partially quantized MiniMax-M2.1 I get `KeyError: 'layers.56.self_attn.qkv_proj.weight'` ~~This seems to be a problem similar to https://github.com/vllm-project/vllm/issues/11790 which was fixed by this one-liner https://github.com/vllm-project/vllm/pull/11795/changes~~ The quantization recipe didn't touch the QKV weights (they were dequantized to BF16 for llm-compressor support) ```yaml default_stage: default_modifiers: AWQModifier: config_groups: mlp_experts_projections: # Include only MLP expert weights for 4-bit quantization targets: ["re:.*block_sparse_moe\\.experts\\.\\d+\\.(w1|w2|w3)$"] weights: num_bits: 4 type: int symmetric: true group_size: 32 strategy: group dynamic: false # actorder: group observer: memoryless_minmax mappings: - smooth_layer: re:.*post_attention_layernorm$ balance_layers: ["re:.*w1$", "re:.*w3$"] - smooth_layer: re:.*w3$ balance_layers: ["re:.*w2$"] duo_scaling: true ``` Raised also at SGLang: https://github.com/sgl-project/sglang/issues/16295 ### Before submi...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rallelLinear layers leaking implementation details to compressed-tensors quantization_config targets bug;stale ### Your current environment ### 🐛 Describe the bug > [!TIP] > Full workaround and analysis just below: http...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ://github.com/vllm-project/vllm/pull/11795/changes~~ The quantization recipe didn't touch the QKV weights (they were dequantized to BF16 for llm-compressor support) ```yaml default_stage: default_modifiers: AWQModifier:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: group observer: memoryless_minmax mappings: - smooth_layer: re:.*post_attention_layernorm$ balance_layers: ["re:.*w1$", "re:.*w3$"] - smooth_layer: re:.*w3$ balance_layers: ["re:.*w2$"] duo_scaling: true ``` Raised also...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: only MLP expert weights for 4-bit quantization targets: ["re:.*block_sparse_moe\\.experts\\.\\d+\\.(w1|w2|w3)$"] weights: num_bits: 4 type: int symmetric: true group_size: 32 strategy: group dynamic: f
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: : default_modifiers: AWQModifier: config_groups: mlp_experts_projections: # Include only MLP expert weights for 4-bit quantization targets: ["re:.*block_sparse_moe\\.experts\\.\\d+\\.(w1|w2|w3)$"] weights: num_bits: 4 t

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
