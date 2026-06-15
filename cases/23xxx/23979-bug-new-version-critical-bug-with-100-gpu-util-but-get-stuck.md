# vllm-project/vllm#23979: [Bug]: new version critical bug with 100% gpu util but get stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#23979](https://github.com/vllm-project/vllm/issues/23979) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: new version critical bug with 100% gpu util but get stuck

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by Anaconda, Inc. | (main, Jun 5 2025, 13:09:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.14.0-29-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX 5000 Ada Generation GPU 1: NVIDIA RTX 5000 Ada Generation Nvidia driver version : 575.64.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK avai...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Bug]: new version critical bug with 100% gpu util but get stuck bug;stale ### Your current environment ``` Collecting environment information... ============================== System Info ==============================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 |...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: new version critical bug with 100% gpu util but get stuck bug;stale ### Your current environment ``` Collecting environment information... ============================== System Info ==============================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: dio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.56.0 [pip3] triton==3.3.1 [conda] numpy 2.2.6 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.6.80
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
