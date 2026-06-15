# vllm-project/vllm#37992: [Bug]: RuntimeError triton error during profile_run with Qwen3.5-MoE vision encoder on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#37992](https://github.com/vllm-project/vllm/issues/37992) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError triton error during profile_run with Qwen3.5-MoE vision encoder on ROCm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Environment** - Model: `amd/Qwen3.5-397B-A17B-MTP-PTPC-FP8` - ROCm: MI325X (gfx942) **Command** ```bash vllm serve amd/Qwen3.5-397B-A17B-MTP-PTPC-FP8 \ --tensor-parallel-size 8 \ --dtype auto \ --enforce-eager \ --no-enable-chunked-prefill \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' \ --gpu-memory-utilization 0.95 \ --port 8008 ``` **Error message** The server crashes during engine initialization at the memory-profiling stage (`profile_run`), before any user request is served. The profiling run creates dummy multimodal inputs and forwards them through the Qwen3.5 vision encoder (ViT). All 8 TP workers fail simultaneously with the same error: ``` Traceback (most recent call last): File "/workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 944, in worker_busy_loop output = func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 120, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/workspace/vllm/vllm/v1/worker/gpu_worker.py", line 370, in determine_available_memory self.model_runner.profile_run() F...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: RuntimeError triton error during profile_run with Qwen3.5-MoE vision encoder on ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug **Environment** - Model: `amd/Qwen3.5-397B-A17B-MTP-PTPC-FP8` - RO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Error triton error during profile_run with Qwen3.5-MoE vision encoder on ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug **Environment** - Model: `amd/Qwen3.5-397B-A17B-MTP-PTPC-FP8` - ROCm: MI325X (gf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: RuntimeError triton error during profile_run with Qwen3.5-MoE vision encoder on ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug **Environment** - Model: `amd/Qwen3.5-397B-A17B-MTP-PTPC-FP8` - RO...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _order_ops/triton_kernel_wrap.py", line 2049, in __call__ return tracing_triton_hopifier_singleton.call_triton_kernel( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: scribe the bug **Environment** - Model: `amd/Qwen3.5-397B-A17B-MTP-PTPC-FP8` - ROCm: MI325X (gfx942) **Command** ```bash vllm serve amd/Qwen3.5-397B-A17B-MTP-PTPC-FP8 \ --tensor-parallel-size 8 \ --dtype auto \ --enforc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
