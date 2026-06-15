# vllm-project/vllm#5351: [Bug]: TorchSDPAMetadata is out of date

| 字段 | 值 |
| --- | --- |
| Issue | [#5351](https://github.com/vllm-project/vllm/issues/5351) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TorchSDPAMetadata is out of date

### Issue 正文摘录

### Your current environment alexr@roxy:~$ python collect_env.py Collecting environment information... PyTorch version: 2.0.0+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.26.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.5.119 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3070 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: GenuineIntel Model name: Intel(R) Core(TM) i7-10700K CPU @ 3.80GHz CPU family: 6 Model: 165 Thread(s) per core: 2 Core(s) per socket: 8 Socket(s): 1 Stepping: 5 CPU max MHz: 5100.0000 C...

## 现有链接修复摘要

#5402 [Bugfix] Add device assertion to TorchSDPA

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: y:~$ python collect_env.py Collecting environment information... PyTorch version: 2.0.0+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.0.0+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: [Bug]: TorchSDPAMetadata is out of date bug ### Your current environment alexr@roxy:~$ python collect_env.py Collecting environment information... PyTorch version: 2.0.0+cu117 Is debug build: False CUDA used to build Py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nvironment alexr@roxy:~$ python collect_env.py Collecting environment information... PyTorch version: 2.0.0+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec rstack overflow: Not affected V...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5402](https://github.com/vllm-project/vllm/pull/5402) | closes_keyword | 0.95 | [Bugfix] Add device assertion to TorchSDPA | Fix #5351 Added a device assertion to avoid using TorchSDPA with NVIDIA GPUs. --- <details> <!-- inside this <details> section, markdown rendering does not work, so we u |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
