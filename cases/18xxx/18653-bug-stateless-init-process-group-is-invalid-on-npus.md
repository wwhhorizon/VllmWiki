# vllm-project/vllm#18653: [Bug]: stateless_init_process_group is invalid on NPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#18653](https://github.com/vllm-project/vllm/issues/18653) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: stateless_init_process_group is invalid on NPUs

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.5.1 Is debug build: False OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 4.0.0 Libc version: glibc-2.35 Python version: 3.10.17 (main, Apr 30 2025, 16:00:31) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.19.90-89.11.v2401.ky10.aarch64-aarch64-with-glibc2.35 CPU: Architecture: aarch64 CPU op-mode(s): 64-bit Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Vendor ID: HiSilicon BIOS Vendor ID: HiSilicon Model name: Kunpeng-920 BIOS Model name: HUAWEI Kunpeng 920 5250 Model: 0 Thread(s) per core: 1 Core(s) per socket: 48 Socket(s): 4 Stepping: 0x1 Frequency boost: disabled CPU max MHz: 2600.0000 CPU min MHz: 200.0000 BogoMIPS: 200.00 Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs L1d cache: 12 MiB (192 instances) L1i cache: 12 MiB (192 instances) L2 cache: 96 MiB (192 instances) L3 cache: 192 MiB (8 instances) NUMA node(s): 8 NUMA node0 CPU(s): 0-23 NUMA node1 CPU(s): 24-47 NUMA node2 CPU(s): 48-71 NUMA node3 CPU(s): 72-95 NUMA node4 CPU(s):...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: s_group is invalid on NPUs bug ### Your current environment ``` PyTorch version: 2.5.1 Is debug build: False OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ` PyTorch version: 2.5.1 Is debug build: False OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 4.0.0 Libc version: glibc-2.35 P...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ) print(f"[Rank {rank}] Received: {recv_tensor}") assert torch.allclose(recv_tensor, torch.ones(4, 4, device="cuda")), "Data mismatch!" if __name__ == "__main__": # 配置参数 master_address = "127.0.0.1" # 本地测试用回环地址 master_p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: # Your current environment ``` PyTorch version: 2.5.1 Is debug build: False OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 4.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl Vulnera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
