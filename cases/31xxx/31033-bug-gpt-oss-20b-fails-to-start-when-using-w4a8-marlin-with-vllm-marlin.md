# vllm-project/vllm#31033: [Bug]: gpt-oss-20b fails to start when using W4A8 Marlin with VLLM_MARLIN_INPUT_DTYPE=int8

| 字段 | 值 |
| --- | --- |
| Issue | [#31033](https://github.com/vllm-project/vllm/issues/31033) |
| 状态 | closed |
| 标签 | bug;gpt-oss |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-20b fails to start when using W4A8 Marlin with VLLM_MARLIN_INPUT_DTYPE=int8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When starting gpt-oss-20b w4a8 specifically with the int8 marlin backend, I see a kernel selection error. This is likely intentional due to kernel limitations with the shapes in the model, but wanted to post an issue to track. ``` VLLM_MARLIN_INPUT_DTYPE=int8 vllm serve openai/gpt-oss-20b --enforce-eager (APIServer pid=4251) INFO 12-19 10:05:15 [api_server.py:1262] vLLM API server version 0.13.0rc2.dev72+gf355ad541 (APIServer pid=4251) INFO 12-19 10:05:15 [utils.py:253] non-default args: {'model_tag': 'openai/gpt-oss-20b', 'model': 'openai/gpt-oss-20b', 'enforce_eager': True} (APIServer pid=4251) INFO 12-19 10:05:16 [model.py:514] Resolved architecture: GptOssForCausalLM Parse safetensors files: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00 , 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['all'], 'splitting_ops': [], 'compile_mm_encoder': False, 'compile_sizes': [], 'compile_ranges_split_points': [2048], 'inductor_compile_config': {'enable_auto_functionalized...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nvironment ### 🐛 Describe the bug When starting gpt-oss-20b w4a8 specifically with the int8 marlin backend, I see a kernel selection error. This is likely intentional due to kernel limitations with the shapes in the mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: gpt-oss-20b fails to start when using W4A8 Marlin with VLLM_MARLIN_INPUT_DTYPE=int8 bug;gpt-oss ### Your current environment ### 🐛 Describe the bug When starting gpt-oss-20b w4a8 specifically with the int8 marlin backen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gpt-oss-20b fails to start when using W4A8 Marlin with VLLM_MARLIN_INPUT_DTYPE=int8 bug;gpt-oss ### Your current environment ### 🐛 Describe the bug When starting gpt-oss-20b w4a8 specifically with the int8 marlin...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: _attn_quant': False, 'eliminate_noops': False, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse_allreduce_rms': False}, 'max_cudagraph_capture_size': 0, 'dynamic_shapes_config': {'type': , 'evaluate_guards': False},...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: onfig': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': , 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': [], 'cudagrap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
