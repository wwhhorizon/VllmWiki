# vllm-project/vllm#15127: [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError

| 字段 | 值 |
| --- | --- |
| Issue | [#15127](https://github.com/vllm-project/vllm/issues/15127) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.5.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.31.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 6 2024, 20:22:13) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.136-tegra-aarch64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Orin (nvgpu) Nvidia driver version: N/A cuDNN version: Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_adv.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_cnn.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_engines_precompiled.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_graph.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_heuristic.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_ops.so.9.4.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment Collecting environment information... PyTorch version: 2.5.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (aarch64) GCC version:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.5.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM us...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: environment information... PyTorch version: 2.5.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: adError bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.5.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: dio==2.5.0 [pip3] torchvision==0.20.0 [pip3] transformers==4.48.0 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.6.post1 vLLM Build Flags: CUDA A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
