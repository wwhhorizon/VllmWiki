# vllm-project/vllm#41360: [Bug]: Qwen3-30B-A3B on B200 (TP=8) — K must be divisible by blockK in flashinfer convert_to_block_layout (unquantized MoE oracle path)

| 字段 | 值 |
| --- | --- |
| Issue | [#41360](https://github.com/vllm-project/vllm/issues/41360) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-30B-A3B on B200 (TP=8) — K must be divisible by blockK in flashinfer convert_to_block_layout (unquantized MoE oracle path)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading `Qwen/Qwen3-30B-A3B` on 8x B200 with TP=8, all 8 TP workers fail at engine init with an `AssertionError` from flashinfer's `convert_to_block_layout`: ``` AssertionError: K must be divisible by blockK ``` The model's per-expert weight K-dim does not divide the `block_k` chosen by vLLM's flashinfer trtllm block-layout conversion path. The error fires in the **unquantized** MoE oracle path — i.e., the model is loaded without an explicit quantization argument and routed through `flashinfer_utils.convert_moe_weights_to_flashinfer_trtllm_block_layout`. ### Stack trace (from one of the 8 workers — identical on all) ``` (Worker_TP6 pid=11321) ERROR 04-29 00:05:12 [multiproc_executor.py:870] File ".../vllm/model_executor/layers/fused_moe/oracle/unquantized.py", line 315, in convert_to_unquantized_kernel_format File ".../vllm/model_executor/layers/quantization/utils/flashinfer_utils.py", line 195, in convert_moe_weights_to_flashinfer_trtllm_block_layout tmp_weights2 = convert_to_block_layout(tmp_weights2.view(torch.uint8), block_k) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File ".../flashinfer/fused_moe/...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: e divisible by blockK in flashinfer convert_to_block_layout (unquantized MoE oracle path) bug ### Your current environment ### 🐛 Describe the bug When loading `Qwen/Qwen3-30B-A3B` on 8x B200 with TP=8, all 8 TP workers...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: divide the `block_k` chosen by vLLM's flashinfer trtllm block-layout conversion path. The error fires in the **unquantized** MoE oracle path — i.e., the model is loaded without an explicit quantization argument and rout...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Qwen3-30B-A3B on B200 (TP=8) — K must be divisible by blockK in flashinfer convert_to_block_layout (unquantized MoE oracle path) bug ### Your current environment ### 🐛 Describe the bug When loading `Qwen/Qwen3-30...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3-30B-A3B on B200 (TP=8) — K must be divisible by blockK in flashinfer convert_to_block_layout (unquantized MoE oracle path) bug ### Your current environment ### 🐛 Describe the bug When loading `Qwen/Qwen3-30...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Qwen3-30B-A3B on B200 (TP=8) — K must be divisible by blockK in flashinfer convert_to_block_layout (unquantized MoE oracle path) bug ### Your current environment ### 🐛 Describe the bug When loading `Qwen/Qwen3-30...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
