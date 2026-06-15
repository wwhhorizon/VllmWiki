# vllm-project/vllm#16336: [Installation]: run error on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#16336](https://github.com/vllm-project/vllm/issues/16336) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: run error on B200

### Issue 正文摘录

### Your current environment ```text INFO 04-09 11:11:59 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.8.0.dev20250408+cu128 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: version 4.0.0 Libc version: glibc-2.39 Python version: 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.8.0-57-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.8.93 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B200 GPU 7: NVIDIA B200 Nvidia driver version: 570.124.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 224 On-line CPU(s) list: 0-223 Vendor ID: GenuineI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: run error on B200 installation;stale ### Your current environment ```text INFO 04-09 11:11:59 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Installation]: run error on B200 installation;stale ### Your current environment ```text INFO 04-09 11:11:59 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.8.0.dev20250408+cu128 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS: U...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -nvjitlink-cu12==12.8.61 [pip3] nvidia-nvtx-cu12==12.8.55 [pip3] pytorch-triton==3.3.0+git96316ce5 [pip3] pyzmq==26.4.0 [pip3] torch==2.8.0.dev20250408+cu128 [pip3] torchaudio==2.6.0.dev20250408+cu128 [pip3] torchvision...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
