# vllm-project/vllm#35920: [Bug]: UMA Memory Profiling Misattributes OS Page Cache and Fails in Concurrent Deployments

| 字段 | 值 |
| --- | --- |
| Issue | [#35920](https://github.com/vllm-project/vllm/issues/35920) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | crash |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: UMA Memory Profiling Misattributes OS Page Cache and Fails in Concurrent Deployments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Bug Report: UMA Memory Profiling Misattributes OS Page Cache and Fails in Concurrent Deployments (Race Condition) **vLLM version** All versions including latest. **System Info** Hardware: UMA (Unified Memory Architecture) systems such as NVIDIA Jetson (Orin), DGX Spark, Thor, or any system sharing system RAM with GPU VRAM. **What happened?** When launching models on a UMA system using the `--gpu-memory-utilization` parameter, the final calculated available KV Cache capacity is severely under-allocated. When launching multiple models concurrently (e.g., three ` **Proposed Fix** In `utils/mem_utils.py` and `gpu_worker.py`, when operating on recognized UMA platforms (`current_platform.get_device_capability()`), the memory profiling logic needs an overhaul: * The `MemorySnapshot` logic needs to account for reclaimable OS Page Cache (`psutil.virtual_memory().cached`). Alternatively, the loading logic should aggressively flush (`os.posix_fadvise` / `O_DIRECT`) the loaded tensor files from the kernel cache instantly after loading so that the snapshot calculates true remaining allocatable VRAM. * The global profiling math `(Global Sy...

## 现有链接修复摘要

#35929 fix(memory): resolve UMA concurrent profiling race condition and page cache leak

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Page Cache and Fails in Concurrent Deployments (Race Condition) **vLLM version** All versions including latest. **System Info** Hardware: UMA (Unified Memory Architecture) systems such as NVIDIA Jetson (Orin), DGX Spark...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ersions including latest. **System Info** Hardware: UMA (Unified Memory Architecture) systems such as NVIDIA Jetson (Orin), DGX Spark, Thor, or any system sharing system RAM with GPU VRAM. **What happened?** When launch...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: the `--gpu-memory-utilization` parameter, the final calculated available KV Cache capacity is severely under-allocated. When launching multiple models concurrently (e.g., three ` **Proposed Fix** In `utils/mem_utils.py`...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: UMA Memory Profiling Misattributes OS Page Cache and Fails in Concurrent Deployments bug ### Your current environment ### 🐛 Describe the bug ### Bug Report: UMA Memory Profiling Misattributes OS Page Cache and Fa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tem sharing system RAM with GPU VRAM. **What happened?** When launching models on a UMA system using the `--gpu-memory-utilization` parameter, the final calculated available KV Cache capacity is severely under-allocated...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35929](https://github.com/vllm-project/vllm/pull/35929) | closes_keyword | 0.95 | fix(memory): resolve UMA concurrent profiling race condition and page cache leak | Resolves #35920 - Fixes crashes related to concurrent vLLM loading on Orin/Thor/Spark UMA nodes. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
