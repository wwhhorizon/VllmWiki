# vllm-project/vllm#41874: [Bug]: AttributeError when loading Mamba2ForCausalLM with BitsAndBytes quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#41874](https://github.com/vllm-project/vllm/issues/41874) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError when loading Mamba2ForCausalLM with BitsAndBytes quantization

### Issue 正文摘录

### Your current environment The output of python collect_env.py ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Pop!_OS 22.04 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Dec 2 2025, 19:47:35) [Clang 21.1.4 ] (64-bit runtime) Python platform : Linux-6.16.3-76061603-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3080 Ti Nvidia driver version : 580.82.07 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N...

## 现有链接修复摘要

#41875 [Bugfix] Enable BitsAndBytes support for Mamba-2

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========== OS : Pop!_OS 22.04 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.3.5 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: AttributeError when loading Mamba2ForCausalLM with BitsAndBytes quantization bug ### Your current environment The output of python collect_env.py ```text Collecting environment information... uv is set ==========...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: noinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm d...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41875](https://github.com/vllm-project/vllm/pull/41875) | closes_keyword | 0.95 | [Bugfix] Enable BitsAndBytes support for Mamba-2 | Fixes: #41874 ## Test Plan To verify this change, I performed in-flight 4-bit quantization on a memory-constrained consumer GPU (RTX 3080 Ti 12GB). Test command: ```ba |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
