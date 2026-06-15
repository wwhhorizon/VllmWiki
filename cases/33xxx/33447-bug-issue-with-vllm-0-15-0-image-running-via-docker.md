# vllm-project/vllm#33447: [Bug]: Issue with vllm 0.15.0 image - running via docker

| 字段 | 值 |
| --- | --- |
| Issue | [#33447](https://github.com/vllm-project/vllm/issues/33447) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue with vllm 0.15.0 image - running via docker

### Issue 正文摘录

### Your current environment ``` $ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-1091-nvidia-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.1.80 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B200 GPU 7: NVIDIA B200 Nvidia driver version : 580.105.08 cuDNN version : Could not collect HIP runtime...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: Issue with vllm 0.15.0 image - running via docker bug ### Your current environment ``` $ python collect_env.py Collecting environment information... ============================== System Info ====================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: urrent environment ``` $ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
