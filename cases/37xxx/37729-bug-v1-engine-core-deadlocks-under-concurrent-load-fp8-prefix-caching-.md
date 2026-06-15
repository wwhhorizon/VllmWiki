# vllm-project/vllm#37729: [Bug]: V1 engine core deadlocks under concurrent load (fp8 + prefix caching + Qwen3.5)

| 字段 | 值 |
| --- | --- |
| Issue | [#37729](https://github.com/vllm-project/vllm/issues/37729) |
| 状态 | open |
| 标签 | bug |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 engine core deadlocks under concurrent load (fp8 + prefix caching + Qwen3.5)

### Issue 正文摘录

### Your current environment ``` CUDA Archs: 7.0 7.5 8.0 8.9 9.0 10.0 12.0; ROCm: Disabled GPU Topology: GPU0 NIC0 NIC1 NIC2 NIC3 NIC4 NIC5 NIC6 NIC7 NIC8 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X SYS SYS SYS SYS SYS PHB PHB PHB PHB 88-175 1 N/A NIC0 SYS X NODE NODE NODE NODE SYS SYS SYS SYS NIC1 SYS NODE X PHB PHB PHB SYS SYS SYS SYS NIC2 SYS NODE PHB X PHB PHB SYS SYS SYS SYS NIC3 SYS NODE PHB PHB X PHB SYS SYS SYS SYS NIC4 SYS NODE PHB PHB PHB X SYS SYS SYS SYS NIC5 PHB SYS SYS SYS SYS SYS X PHB PHB PHB NIC6 PHB SYS SYS SYS SYS SYS PHB X PHB PHB NIC7 PHB SYS SYS SYS SYS SYS PHB PHB X PHB NIC8 PHB SYS SYS SYS SYS SYS PHB PHB PHB X Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node PHB = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU) PXB = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks NIC Legend: NIC0: mlx5_0 NIC1: mlx5_1 NIC2:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: PHB X Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: V1 engine core deadlocks under concurrent load (fp8 + prefix caching + Qwen3.5) bug ### Your current environment ``` CUDA Archs: 7.0 7.5 8.0 8.9 9.0 10.0 12.0; ROCm: Disabled GPU Topology: GPU0 NIC0 NIC1 NIC2 NIC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: (fp8 + prefix caching + Qwen3.5) bug ### Your current environment ``` CUDA Archs: 7.0 7.5 8.0 8.9 9.0 10.0 12.0; ROCm: Disabled GPU Topology: GPU0 NIC0 NIC1 NIC2 NIC3 NIC4 NIC5 NIC6 NIC7 NIC8 CPU Affinity NUMA Affinity...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: V1 engine core deadlocks under concurrent load (fp8 + prefix caching + Qwen3.5) bug ### Your current environment ``` CUDA Archs: 7.0 7.5 8.0 8.9 9.0 10.0 12.0; ROCm: Disabled GPU Topology: GPU0 NIC0 NIC1 NIC2
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: brief spike, the engine freezes 4. No specific error triggers it — no OOM, no CUDA error, no validation error Engine log sequence showing the deadlock: ``` 13:57:45 Avg prompt throughput: 2598.6 tokens/s, Avg generation...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
