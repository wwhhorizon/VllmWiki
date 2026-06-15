# vllm-project/vllm#10155: [Installation]: VLLM does not support TPU v5p-16 (Multi-Host) with Ray Cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#10155](https://github.com/vllm-project/vllm/issues/10155) |
| 状态 | closed |
| 标签 | installation;tpu;ray |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: VLLM does not support TPU v5p-16 (Multi-Host) with Ray Cluster

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING:root:libtpu.so and TPU device found. Setting PJRT_DEVICE=TPU. INFO 11-04 16:11:44 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. PyTorch version: 2.6.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.30.5 Libc version: glibc-2.31 Python version: 3.10.15 (main, Oct 17 2024, 02:58:23) [GCC 10.2.1 20210110] (64-bit runtime) Python platform: Linux-5.19.0-1022-gcp-x86_64-with-glibc2.31 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 52 bits physical, 57 bits virtual CPU(s): 208 On-line CPU(s) list: 0-207 Thread(s) per...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: VLLM does not support TPU v5p-16 (Multi-Host) with Ray Cluster installation;tpu;ray ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNIN
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx_vnni avx512_bf16 arat avx512vbmi umip avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq la57 rdpid cldemote movdiri movdir64b fsrm m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ```text The output of `python collect_env.py` Collecting environment information... WARNING:root:libtpu.so and TPU device found. Setting PJRT_DEVICE=TPU. INFO 11-04 16:11:44 importing.py:15] Triton not installed or not...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl Vuln...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ions will not be available. PyTorch version: 2.6.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
