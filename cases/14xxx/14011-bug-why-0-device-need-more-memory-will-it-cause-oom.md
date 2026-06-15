# vllm-project/vllm#14011: [Bug]: Why 0 device need more memory? will it cause OOM?

| 字段 | 值 |
| --- | --- |
| Issue | [#14011](https://github.com/vllm-project/vllm/issues/14011) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Why 0 device need more memory? will it cause OOM?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash Fri Feb 28 11:23:46 2025 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 4 NVIDIA L20 On | 00000000:87:00.0 Off | 0 | | N/A 41C P0 80W / 350W | 45040MiB / 46068MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 5 NVIDIA L20 On | 00000000:88:00.0 Off | 0 | | N/A 40C P0 77W / 350W | 40998MiB / 46068MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 6 NVIDIA L20 On | 00000000:89:00.0 Off | 0 | | N/A 43C P0 83W / 350W | 40998MiB / 46068MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+------...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --------------------------------------------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+-----------------...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ----------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M |...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Why 0 device need more memory? will it cause OOM? bug;stale ### Your current environment ### 🐛 Describe the bug ```bash Fri Feb 28 11:23:46 2025 +------------------------------------------------------------------...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Why 0 device need more memory? will it cause OOM? bug;stale ### Your current environment ### 🐛 Describe the bug ```bash Fri Feb 28 11:23:46 2025 +------------------------------------------------------------------...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel cuda oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
