# vllm-project/vllm#35031: [Bug]: MTP Speculative Decoding with NVFP4: Weight Shape Mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#35031](https://github.com/vllm-project/vllm/issues/35031) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MTP Speculative Decoding with NVFP4: Weight Shape Mismatch

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-37-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.1.115 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX PRO 6000 Blackwell Workstation Edition GPU 1: NVIDIA RTX 6000 Ada Generation Nvidia driver version : 580.126.09 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info =============...

## 现有链接修复摘要

#35041 [Bug Fix] MTP Speculative Decoding with NVFP4: Weight Shape Mismatch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 3.28.3 Libc version : glibc-2.39 =================
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: MTP Speculative Decoding with NVFP4: Weight Shape Mismatch bug ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: MTP Speculative Decoding with NVFP4: Weight Shape Mismatch bug ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version :...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: DA runtime version : 13.1.115 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX PRO 6000 Blackwell Workstation Edition GPU 1: NVIDIA RTX 6000 Ada Generation Nvidia driver version : 580.126.09...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.4 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35041](https://github.com/vllm-project/vllm/pull/35041) | closes_keyword | 0.95 | [Bug Fix] MTP Speculative Decoding with NVFP4: Weight Shape Mismatch | Fixes #35031 ### Summary The `eh_proj` layer in multiple MTP (Multi-Token Prediction) model files was defined as a plain `nn.Linear`, which does not participate in vLLM's quantiz |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
