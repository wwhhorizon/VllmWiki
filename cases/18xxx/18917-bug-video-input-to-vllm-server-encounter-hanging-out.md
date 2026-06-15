# vllm-project/vllm#18917: [Bug]: video input to vllm server encounter hanging out

| 字段 | 值 |
| --- | --- |
| Issue | [#18917](https://github.com/vllm-project/vllm/issues/18917) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: video input to vllm server encounter hanging out

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.11 (main, Dec 11 2024, 16:28:39) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.11.0-25-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.0.140 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX 5000 Ada Generation GPU 1: NVIDIA RTX 5000 Ada Generation Nvidia driver version : 550.144.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ==========================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ==============
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: r hanging out bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.11 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
