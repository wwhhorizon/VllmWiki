# vllm-project/vllm#14701: [Bug]: vLLM CPU inference does not use AVX512 on AVX512-capable CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#14701](https://github.com/vllm-project/vllm/issues/14701) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM CPU inference does not use AVX512 on AVX512-capable CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running with with a Xeon 3175X which is an AVX512 capable CPU as seen in the lscpu flags, I can see that it does not throttle to the AVX512 clocks and therefore VLLM isn't using AVX512. Is there a env flag I have to set to enable AVX512? Is it because it is running in WSL? This is the lscpu output: ```text Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 56 On-line CPU(s) list: 0-55 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) W-3175X CPU @ 3.10GHz CPU family: 6 Model: 85 Thread(s) per core: 2 Core(s) per socket: 28 Socket(s): 1 Stepping: 4 BogoMIPS: 6200.11 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse s se2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology tsc_r eliable nonstop_tsc cpuid pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movb e popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch inv pcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi ept vpid ept_ad fsgsbase tsc_adjust bmi1 hl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eliable nonstop_tsc cpuid pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movb e popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch inv pcid_single pti ssbd ibrs ibp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ? Is it because it is running in WSL? This is the lscpu output: ```text Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 56 On-line C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: On-line CPU(s) list: 0-55 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) W-3175X CPU @ 3.10GHz CPU family: 6 Model: 85 Thread(s) per core: 2 Core(s) per socket: 28 Socket(s): 1 Stepping:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: SMT Host state unknown Meltdown: Mitigation; PTI Mmio stale data: Mitigation; Clear CPU buffers; SMT Host state unknown Reg file data sampling: Not affected Retbleed: Mitigation; IBRS Spec rstack overflow: Not affected...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
