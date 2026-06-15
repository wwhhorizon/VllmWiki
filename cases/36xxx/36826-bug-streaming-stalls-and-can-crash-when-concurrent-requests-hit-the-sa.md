# vllm-project/vllm#36826: [Bug]: Streaming stalls and can crash when concurrent requests hit the same vLLM server

| 字段 | 值 |
| --- | --- |
| Issue | [#36826](https://github.com/vllm-project/vllm/issues/36826) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming stalls and can crash when concurrent requests hit the same vLLM server

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description** While streaming tokens from the OpenAI-compatible API, any second request to the same vLLM server causes a visible stall in the stream. Example during streaming: `curl http://localhost:8000/health` or starting another generation request while the first one is streaming. The stream pauses briefly and then continues. If the server receives many such requests during streaming, the engine can eventually crash with: ``` AsyncLLM output_handler failed /opt/pytorch/pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [6,0,0], thread: [0,0,0] Assertion `srcIndex , 'debug_dump_path': None, 'cache_dir': '/root/.cache/vllm/torch_compile_cache/5dbc8b65ab', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['none'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_mla_attention', 'vllm::unified_mla_attention_with_output', 'vllm::mamba_mixer2', 'vllm::mamba_mixer', 'vllm::short_conv', 'vllm::linear_attention', 'vllm::plamo2_mamba_mixer', 'vllm::gdn_attention_core', 'vllm::olmo_hybrid_gdn_full_forward', 'vllm::kda_attention',...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 515: indexSelectSmallIndex: block: [6,0,0], thread: [0,0,0] Assertion `srcIndex , 'debug_dump_path': None, 'cache_dir': '/root/.cache/vllm/torch_compile_cache/5dbc8b65ab', 'compile_cache_save_format': 'binary', 'backend...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Streaming stalls and can crash when concurrent requests hit the same vLLM server bug ### Your current environment ### 🐛 Describe the bug **Description** While streaming tokens from the OpenAI-compatible API, any...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: torch_compile_cache/5dbc8b65ab', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['none'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: True, 'use_inductor_graph_partition': False, 'pass_config': {'fuse_norm_quant': False, 'fuse_act_quant': True, 'fuse_attn_quant': False, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse_allreduce_rms': False}, 'max_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: AsyncLLM output_handler failed /opt/pytorch/pytorch/aten/src/ATen/native/cuda/Indexing.cu:1515: indexSelectSmallIndex: block: [6,0,0], thread: [0,0,0] Assertion `srcIndex , 'debug_dump_path': None, 'cache_dir': '/root/....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
