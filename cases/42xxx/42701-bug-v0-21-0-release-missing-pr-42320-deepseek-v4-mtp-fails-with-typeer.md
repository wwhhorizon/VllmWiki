# vllm-project/vllm#42701: [Bug] v0.21.0 release missing PR #42320 — DeepSeek-V4 MTP fails with `TypeError: missing required positional argument: post_mix`

| 字段 | 值 |
| --- | --- |
| Issue | [#42701](https://github.com/vllm-project/vllm/issues/42701) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] v0.21.0 release missing PR #42320 — DeepSeek-V4 MTP fails with `TypeError: missing required positional argument: post_mix`

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-1069-nvidia-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 580.95.05 cuDNN version : Could not collect HIP runtime v...

## 现有链接修复摘要

#41083 [Quantization] add humming mxfp4 moe backend | #41536 add fused mhc_post_pre kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt: post_mix` bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41083](https://github.com/vllm-project/vllm/pull/41083) | mentioned | 0.45 | [Quantization] add humming mxfp4 moe backend | s any deepseek-v4 mtp deployment on v0.21.0 today (e.g. evaluating pr #41083's humming w4a8 moe backend, which requires v0.21.0+ for `--moe-backend humming` cli support but also n… |
| [#41536](https://github.com/vllm-project/vllm/pull/41536) | mentioned | 0.45 | add fused mhc_post_pre kernel | (self, x, positions, input_ids) -> torch.tensor: ... # v0.21.0 (post #41536, broken) def forward(self, x, positions, input_ids, post_mix, res_mix, residual) -> torch.tensor: |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
