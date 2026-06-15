# vllm-project/vllm#24839: [Usage]: The Intel/AMD x86 Pre-built Docker image (v0.10.2) cannot be run

| 字段 | 值 |
| --- | --- |
| Issue | [#24839](https://github.com/vllm-project/vllm/issues/24839) |
| 状态 | closed |
| 标签 | rocm;usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The Intel/AMD x86 Pre-built Docker image (v0.10.2) cannot be run

### Issue 正文摘录

### Your current environment Machine has 64GB RAM. ```text Collecting environment information... CPU family: 6 Model: 165 Thread(s) per core: 1 Core(s) per socket: 8 Socket(s): 1 Stepping: 3 BogoMIPS: 7200.00 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon nopl xtopology tsc_reliable nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves arat md_clear flush_l1d arch_capabilities Hypervisor vendor: VMware Virtualization type: full L1d cache: 256 KiB (8 instances) L1i cache: 256 KiB (8 instances) L2 cache: 2 MiB (8 instances) L3 cache: 6 MiB (1 instance) NUMA node(s): 1 NUMA node0 CPU(s): 0-7 Vulnerability Gather data sampling: Unknown: Dependent on hypervisor status Vulnerability Itlb multihit: KVM: Mitigation: VMX unsupported Vulnerability L1tf: Not affected Vulnerability Mds: Not affected Vulnerabili...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]: The Intel/AMD x86 Pre-built Docker image (v0.10.2) cannot be run rocm;usage ### Your current environment Machine has 64GB RAM. ```text Collecting environment information... CPU family: 6 Model:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Usage]: The Intel/AMD x86 Pre-built Docker image (v0.10.2) cannot be run rocm;usage ### Your current environment Machine has 64GB RAM. ```text Collecting environment information... CPU family: 6 Model: 165 Thread(s) per...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ent environment Machine has 64GB RAM. ```text Collecting environment information... CPU family: 6 Model: 165 Thread(s) per core: 1 Core(s) per socket: 8 Socket(s): 1 Step
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Reg file data sampling: Not affected Vulnerability Retbl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .0+cpu [pip3] torchvision==0.21.0+cpu [pip3] transformers==4.54.0 [pip3] triton==3.2.0 [conda] No relevant packages ============================== vLLM Info ============================== ROCM Version : Could not collec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
