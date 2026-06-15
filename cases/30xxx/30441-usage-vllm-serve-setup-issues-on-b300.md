# vllm-project/vllm#30441: [Usage]: vllm serve setup issues on B300

| 字段 | 值 |
| --- | --- |
| Issue | [#30441](https://github.com/vllm-project/vllm/issues/30441) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm serve setup issues on B300

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Amazon Linux 2023.9.20251208 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : Could not collect CMake version : version 3.22.2 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.14 (main, Nov 12 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] (64-bit runtime) Python platform : Linux-6.1.158-180.294.amzn2023.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA B300 SXM6 AC GPU 1: NVIDIA B300 SXM6 AC GPU 2: NVIDIA B300 SXM6 AC GPU 3: NVIDIA B300 SXM6 AC GPU 4: NVIDIA B300 SXM6 AC GPU 5: NVIDIA B30...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: OS : Amazon Linux 2023.9.20251208 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : Could not collect CMake version : version 3.22.2 Libc version : glibc-2.34 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.14 (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.0.0.19 [pip3] nvidia-cuda-cupti==13.0.48 [pip3] nvidia-cuda-nvrtc==13.0.48 [...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx_vnni avx512_bf16 wbnoinvd ida arat avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid cld...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: The output of `python collect_env.py` ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Amazon Linux 2023.9.20251208 (x86_64) GCC vers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
