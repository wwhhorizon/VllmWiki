# vllm-project/vllm#31718: [Installation]: cuda error when install from source

| 字段 | 值 |
| --- | --- |
| Issue | [#31718](https://github.com/vllm-project/vllm/issues/31718) |
| 状态 | open |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: cuda error when install from source

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Rocky Linux release 8.10 (Green Obsidian) (x86_64) GCC version : (GCC) 12.2.1 20221121 (Red Hat 12.2.1-7) Clang version : Could not collect CMake version : version 3.26.5 Libc version : glibc-2.28 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 | packaged by conda-forge | (main, Oct 22 2025, 23:25:55) [GCC 14.3.0] (64-bit runtime) Python platform : Linux-4.18.0-553.22.1.el8_10.x86_64-x86_64-with-glibc2.28 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.2.91 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX 6000 Ada Generation GPU 1: NVIDIA RTX 6000 Ada Generation GPU 2: NVIDIA RTX 6000 Ada Generation GPU 3: NVIDIA RTX 6000 Ada Generation Nvidia driver version : 550.127.05 cu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: cuda error when install from source installation;stale ### Your current environment ```text Collecting environment information... ============================== System Info =======================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Installation]: cuda error when install from source installation;stale ### Your current environment ```text Collecting environment information... ============================== System Info ==============================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ion;stale ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Rocky Linux release 8.10 (Green Obsidian) (x86_64) GCC...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
