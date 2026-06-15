# vllm-project/vllm#39010: [Bug]: Hang During CUDA Graph Capture on ROCM in 0.19

| 字段 | 值 |
| --- | --- |
| Issue | [#39010](https://github.com/vllm-project/vllm/issues/39010) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hang During CUDA Graph Capture on ROCM in 0.19

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Attempting to serve any model (tested with devstral small 2) fails and stops at Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 71%|███████ | 36/51 [00:22 , 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['+sparse_attn_indexer', 'none'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_mla_attention', 'vllm::unified_mla_attention_with_output', 'vllm::mamba_mixer2', 'vllm::mamba_mixer', 'vllm::short_conv', 'vllm::linear_attention', 'vllm::plamo2_mamba_mixer', 'vllm::gdn_attention_core', 'vllm::olmo_hybrid_gdn_full_forward', 'vllm::kda_attention', 'vllm::sparse_attn_indexer', 'vllm::rocm_aiter_sparse_attn_indexer', 'vllm::unified_kv_cache_update', 'vllm::unified_mla_kv_cache_update'], 'compile_mm_encoder': False, 'cudagraph_mm_encoder': False, 'encoder_cudagraph_token_budgets': [], 'encoder_cudagraph_max_images_per_batch': 0, 'compile_sizes': [], 'compile_ranges_endpoints': [2048], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'size_asserts': False, 'alignment_asserts': False, 'scal...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: with devstral small 2) fails and stops at Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 71%|███████ | 36/51 [00:22 , 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend':...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: t environment ### 🐛 Describe the bug Attempting to serve any model (tested with devstral small 2) fails and stops at Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 71%|███████ | 36/51 [00:22 , 'debug_dump_path...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: mp_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['+sparse_attn_indexer', 'none'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 1%|███████ | 36/51 [00:22 , 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['+sparse_attn_indexer', 'none'], 'splitting_ops': ['vllm::unified_attent...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: True, 'use_inductor_graph_partition': False, 'pass_config': {'fuse_norm_quant': False, 'fuse_act_quant': False, 'fuse_attn_quant': False, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse_allreduce_rms': False}, 'max_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
