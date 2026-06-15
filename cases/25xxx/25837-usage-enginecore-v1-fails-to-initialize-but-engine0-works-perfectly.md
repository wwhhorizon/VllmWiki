# vllm-project/vllm#25837: [Usage]: EngineCore v1 fails to initialize but Engine0 works perfectly

| 字段 | 值 |
| --- | --- |
| Issue | [#25837](https://github.com/vllm-project/vllm/issues/25837) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: EngineCore v1 fails to initialize but Engine0 works perfectly

### Issue 正文摘录

### Your current environment OS: WSL 2 on Windows 11 Python: 3.10 CUDA: 12.8 GPU: NVIDIA RTX A500 Laptop GPU Driver: 573.44 VLLM version: 0.10.2 ### How would you like to use vllm When trying to initialize a VLLM EngineCore v1 on WSL with the facebook/opt-125m model, the engine fails during startup. EngineCore v0 works fine on the same system. I have already tried limiting parallelism (export MAX_JOBS=1) and other job limits, but the error persists: Unable to register cuDNN/cuFFT/cuBLAS factory Steps to reproduce (minimal code snippet): ``` from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` Error log **OUTPUT USING ENGINE1**: 2025-09-28 15:47:00.704737: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2025-09-28 15:47:00.704813: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2025-09-28 15:47:00.758139: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attem...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: hon: 3.10 CUDA: 12.8 GPU: NVIDIA RTX A500 Laptop GPU Driver: 573.44 VLLM version: 0.10.2 ### How would you like to use vllm When trying to initialize a VLLM EngineCore v1 on WSL with the facebook/opt-125m model, the eng...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 5:47:17 [__init__.py:1815] Using max model len 2048 INFO 09-28 15:47:19 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192. (EngineCore_DP0 pid=17374) INFO 09-28 15:47:20 [core.py:654] Waitin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: usage ### Your current environment OS: WSL 2 on Windows 11 Python: 3.10 CUDA: 12.8 GPU: NVIDIA RTX A500 Laptop GPU Driver: 573.44 VLLM version: 0.10.2 ### How would you like to use vllm When trying to initialize a VLLM...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: or: Free memory on device (3.22/4.0 GiB) on startup is less than desired GPU memory utilization (0.9, 3.6 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. (EngineCore_DP0 pid=17374) Pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
