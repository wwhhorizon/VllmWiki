# vllm-project/vllm#40354: [Bug]: Ampere sm_86 can't load W4A16 quant at TP=2 when a layer's output dim halves to <64 (Marlin min_thread_n block)

| 字段 | 值 |
| --- | --- |
| Issue | [#40354](https://github.com/vllm-project/vllm/issues/40354) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ampere sm_86 can't load W4A16 quant at TP=2 when a layer's output dim halves to <64 (Marlin min_thread_n block)

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-110-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 Nvidia driver version : 595.58.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True =============...

## 现有链接修复摘要

#40361 [Kernel][Bugfix] Marlin W4A16: pad sub-tile output dims on load

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug]: Ampere sm_86 can't load W4A16 quant at TP=2 when a layer's output dim halves to <64 (Marlin min_thread_n block) bug ### Your current environment Collecting environment information... ==============================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: read_n block) bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Ampere sm_86 can't load W4A16 quant at TP=2 when a layer's output dim halves to <64 (Marlin min_thread_n block) bug ### Your current environment Collecting environment information... =============================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.7 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.9.1.4 [pip3] nvidia-cuda-cupti-cu12==12.9.79 [pip3] nvidia-cuda-nvrtc-c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40361](https://github.com/vllm-project/vllm/pull/40361) | closes_keyword | 0.95 | [Kernel][Bugfix] Marlin W4A16: pad sub-tile output dims on load | Closes #35924 (generically, not Qwen3.5-GDN-specific) Related: #40354 ## Testing - `test_marlin_gemm_sub_tile_n_pad[{32,48,96}]` (new) in `tests/kernels/quantization/test_marli |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
