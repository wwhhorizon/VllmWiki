# vllm-project/vllm#36481: [Performance]: 2-stage custom allreduce (TP4) bandwidth lagging behind NCCL for large message sizes

| 字段 | 值 |
| --- | --- |
| Issue | [#36481](https://github.com/vllm-project/vllm/issues/36481) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: 2-stage custom allreduce (TP4) bandwidth lagging behind NCCL for large message sizes

### Issue 正文摘录

### Proposal to improve performance @hanzhi713 , in your previous reply in https://github.com/vllm-project/vllm/issues/4770 and https://github.com/vllm-project/vllm/pull/2760 you mentioned that for GPUs connected via PCIe (not crossing CPU) , Custom allreduce should perform better than NCCL. However, **I'm now encountering an issue where the 2-stage TP4 bandwidth is worse than NCCL**. Could you help take a look? >1、It's more performant than NCCL when either there are only two PCIe GPUs (they can be connected to the PCIe root complex directly or with a PCIe switch), or there are multiple PCIe GPUs connected to the same PCIe switch. 2、However, in your case you have a PCIe switch connecting to each group of 4 GPUs. Given the much better switching performance, my implementation may work and provide performance improvements. 1. **Hardware**: 4× RTX 4090 (connected via PCIe 4.0, not crossing CPU sockets) 2. **Driver**: Open-source driver (used to force-enable P2P, as 4090 does not support P2P by default; the modification successfully enables direct P2P communication between GPUs) 3. **P2P bandwidth**: Verified that peer-to-peer transfers achieve near PCIe 4.0 x16 theoretical bandwidth (...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: CIe 4.0 x16 theoretical bandwidth (~32 GB/s). The topology and bandwidth tests confirm this（**Unidirectional P2P bandwidth = 26.33GB/s**）. ```PowerShell [P2P (Peer-to-Peer) GPU Bandwidth Latency Test] Device: 0, NVIDIA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion may work and provide performance improvements. 1. **Hardware**: 4× RTX 4090 (connected via PCIe 4.0, not crossing CPU sockets) 2. **Driver**: Open-source driver (used to force-enable P2P, as 4090 does not support P...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /vllm-project/vllm/pull/2760 you mentioned that for GPUs connected via PCIe (not crossing CPU) , Custom allreduce should perform better than NCCL. However, **I'm now encountering an issue where the 2-stage TP4 bandwidth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
