# vllm-project/vllm#27401: [Bug]: Deepseek3.2 exp awq seems to not work on new vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#27401](https://github.com/vllm-project/vllm/issues/27401) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek3.2 exp awq seems to not work on new vllm

### Issue 正文摘录

### Your current environment env:OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.14.0-284.25.1.el9_2.x86_64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H800 GPU 1: NVIDIA H800 GPU 2: NVIDIA H800 GPU 3: NVIDIA H800 GPU 4: NVIDIA H800 GPU 5: NVIDIA H800 GPU 6: NVIDIA H800 GPU 7: NVIDIA H800 Nvidia driver version : 550.90.07 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.10.2 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.10.2 /usr/lib/x86_64-linux-gnu/libcudn...

## 现有链接修复摘要

#27411 Fix: Improve layer skipping and FusedMoE handling in AWQMarlin

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.4.1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: occup_llc cqm_mbm_tota l cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req hfi avx512vbmi umi p pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: DA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H800 GPU 1: NVIDIA H800 GPU 2: NVIDIA H800 GPU 3: NVIDIA H800 GPU 4: NVIDIA H800 GPU 5: NVIDIA H800 GPU 6: NVIDIA H8...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27411](https://github.com/vllm-project/vllm/pull/27411) | closes_keyword | 0.95 | Fix: Improve layer skipping and FusedMoE handling in AWQMarlin | Fix layer skipping logic and improve handling of FusedMoE layers for compatibility with deepseek3.2 AWQ layers in awq_marlin.py. #27401 ## Test Plan Test loading the deepseek3.2 A |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
