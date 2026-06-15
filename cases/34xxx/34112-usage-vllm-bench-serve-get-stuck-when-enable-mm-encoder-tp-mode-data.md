# vllm-project/vllm#34112: [Usage]: vllm bench serve get stuck when enable `--mm-encoder-tp-mode data`

| 字段 | 值 |
| --- | --- |
| Issue | [#34112](https://github.com/vllm-project/vllm/issues/34112) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm bench serve get stuck when enable `--mm-encoder-tp-mode data`

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.9.0+cpu Is debug build: False OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version: Could not collect CMake version: version 4.2.1 Libc version: glibc-2.35 Python version: 3.11.14 (main, Oct 21 2025, 18:24:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.19.90-vhulk2211.3.0.h1804.eulerosv2r10.aarch64-aarch64-with-glibc2.35 CPU: Architecture: aarch64 CPU op-mode(s): 64-bit Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Vendor ID: HiSilicon Model name: Kunpeng-920 Model: 0 Thread(s) per core: 1 Core(s) per cluster: 48 Socket(s): - Cluster(s): 4 Stepping: 0x1 BogoMIPS: 200.00 Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs L1d cache: 12 MiB (192 instances) L1i cache: 12 MiB (192 instances) L2 cache: 96 MiB (192 instances) L3 cache: 192 MiB (8 instances) NUMA node(s): 8 NUMA node0 CPU(s): 0-23 NUMA node1 CPU(s): 24-47 NUMA node2 CPU(s): 48-71 NUMA node3 CPU(s): 72-95 NUMA node4 CPU(s): 96-119 NUMA node5 CPU(s): 120-143 NUMA node6 CPU(s): 144-167 NUMA node7 CPU(s): 168-191 Vulnerab...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ncoder-tp-mode data` usage ### Your current environment ```text PyTorch version: 2.9.0+cpu Is debug build: False OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version: Could...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: list: 0-191 Vendor ID: HiSilicon Model name: Kunpeng-920 Model: 0 Thread(s) per core: 1 Core(s) per cluster: 48 Socket(s): - Cluster(s):
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Torch version: 2.9.0+cpu Is debug build: False OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version: Could not collect CMake version: version 4.2.1 Libc version: glibc-2.35...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: npu==2.9.0 [pip3] torchvision==0.24.0 [pip3] transformers==4.57.6 [pip3] triton-ascend==3.2.0 [pip3] zmq==0.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] pyzmq 27.1.0 pypi_0 pypi [conda] sentence-transformers
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl Vulnera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
