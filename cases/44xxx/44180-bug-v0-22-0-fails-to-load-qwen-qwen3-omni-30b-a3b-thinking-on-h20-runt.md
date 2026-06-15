# vllm-project/vllm#44180: [Bug]: v0.22.0 fails to load Qwen/Qwen3-Omni-30B-A3B-Thinking on H20: RuntimeError: cu_seqlens_q must be on CUDA

| 字段 | 值 |
| --- | --- |
| Issue | [#44180](https://github.com/vllm-project/vllm/issues/44180) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.22.0 fails to load Qwen/Qwen3-Omni-30B-A3B-Thinking on H20: RuntimeError: cu_seqlens_q must be on CUDA

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.36 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.2 (main, Apr 8 2026, 01:58:00) [GCC 12.2.0] (64-bit runtime) Python platform : Linux-5.15.152.bsk.10-amd64-x86_64-with-glibc2.36 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H20 Nvidia driver version : Could not collect cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.14.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.14.0 /usr/lib/x86_64...

## 现有链接修复摘要

#44264 [Bugfix][Model] Qwen3-Omni: move cu_seqlens to GPU before VIT attention

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.36 =====================
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.11.post2 [pip3] numpy==2.3.5 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cccl==13.3.3.3.1 [pip3] nvidia-cuda-crt==13....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: v0.22.0 fails to load Qwen/Qwen3-Omni-30B-A3B-Thinking on H20: RuntimeError: cu_seqlens_q must be on CUDA bug ### Your current environment ``` Collecting environment information... ==============================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: wen3-Omni-30B-A3B-Thinking on H20: RuntimeError: cu_seqlens_q must be on CUDA bug ### Your current environment ``` Collecting environment information... ============================== System Info =======================...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44264](https://github.com/vllm-project/vllm/pull/44264) | closes_keyword | 0.95 | [Bugfix][Model] Qwen3-Omni: move cu_seqlens to GPU before VIT attention | Fixes #44180. During `profile_run` the multimodal `grid_thw` arrives on CPU, so the `cu_seqlens` tensor built from it inherits the CPU device. Passing this CPU tensor into the F |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
