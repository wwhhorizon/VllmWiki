# vllm-project/vllm#40260: [Bug]: Incompatible dimension when using Mistral Small 4

| 字段 | 值 |
| --- | --- |
| Issue | [#40260](https://github.com/vllm-project/vllm/issues/40260) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incompatible dimension when using Mistral Small 4

### Issue 正文摘录

### Your current environment I'm working of this commit of vllm: 6b2b7bd0ebd43ef756632d2142ce974929f05d8f ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 24 2026, 22:47:08) [Clang 22.1.1 ] (64-bit runtime) Python platform : Linux-6.17.0-1014-nvidia-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GB10 Nvidia driver version : 580.142 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ======== OS : Ubuntu 24.04.4 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 3.28.3 Libc version : glibc-2.39 ===============
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti ecv afp wfxt Model name: Cortex-A725 Model: 1 Thread(s) per core: 1 Core(s) per socket: 10 S
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Incompatible dimension when using Mistral Small 4 bug ### Your current environment I'm working of this commit of vllm: 6b2b7bd0ebd43ef756632d2142ce974929f05d8f ``` Collecting environment information... ==========...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.7 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0.88 [p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: : 6b2b7bd0ebd43ef756632d2142ce974929f05d8f ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (aarch64) GCC version : (Ubuntu 13.3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
