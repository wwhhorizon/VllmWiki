# vllm-project/vllm#27499: [Bug]: GPU Hang on RX 7800 XT when QWEN3-VL multimodal activated

| 字段 | 值 |
| --- | --- |
| Issue | [#27499](https://github.com/vllm-project/vllm/issues/27499) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU Hang on RX 7800 XT when QWEN3-VL multimodal activated

### Issue 正文摘录

### Your current environment I built docker image for vllm 0.11.0 and 0.11.1 and run it with ```Qwen/Qwen3-VL-2B-Instruct``` and ```Qwen/Qwen3-VL-4B-Instruct``` When ```mutimodal``` activated ``` --limit-mm-per-prompt.image 1 --limit-mm-per-prompt.video 1 --limit-mm-per-prompt.audio 1 ``` I got error ```GPU Hang``` ``` vllm-qwen-vl | DEBUG 10-24 19:45:52 [plugins/__init__.py:32] No plugins for group vllm.platform_plugins found. vllm-qwen-vl | DEBUG 10-24 19:45:52 [platforms/__init__.py:36] Checking if TPU platform is available. vllm-qwen-vl | DEBUG 10-24 19:45:52 [platforms/__init__.py:55] TPU platform is not available because: No module named 'libtpu' vllm-qwen-vl | DEBUG 10-24 19:45:52 [platforms/__init__.py:61] Checking if CUDA platform is available. vllm-qwen-vl | DEBUG 10-24 19:45:52 [platforms/__init__.py:88] Exception happens when checking CUDA platform: NVML Shared Library Not Found vllm-qwen-vl | DEBUG 10-24 19:45:52 [platforms/__init__.py:105] CUDA platform is not available because: NVML Shared Library Not Found vllm-qwen-vl | DEBUG 10-24 19:45:52 [platforms/__init__.py:112] Checking if ROCm platform is available. vllm-qwen-vl | DEBUG 10-24 19:45:52 [platforms/__init__.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: L multimodal activated bug;rocm ### Your current environment I built docker image for vllm 0.11.0 and 0.11.1 and run it with ```Qwen/Qwen3-VL-2B-Instruct``` and ```Qwen/Qwen3-VL-4B-Instruct``` When ```mutimodal``` activ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: GPU Hang on RX 7800 XT when QWEN3-VL multimodal activated bug;rocm ### Your current environment I built docker image for vllm 0.11.0 and 0.11.1 and run it with ```Qwen/Qwen3-VL-2B-Instruct``` and ```Qwen/Qwen3-VL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: : 1}, 'max_num_batched_tokens': 4096, 'max_num_seqs': 1, 'enable_chunked_prefill': True, 'compilation_config': {'level': None, 'mode': 3, 'debug_dump_path': None, 'cache_dir': '', 'backend': 'inductor', 'custom_ops': []...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: .0.0', 'model': 'Qwen/Qwen3-VL-2B-Instruct', 'trust_remote_code': True, 'dtype': 'float16', 'max_model_len': 4096, 'disable_cascade_attn': True, 'gpu_memory_utilization': 0.85, 'limit_mm_per_prompt': {'image': 1, 'video...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ': {'level': None, 'mode': 3, 'debug_dump_path': None, 'cache_dir': '', 'backend': 'inductor', 'custom_ops': [], 'splitting_ops': [], 'use_inductor': None, 'compile_sizes': None, 'inductor_compile_config': {'enable_auto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
