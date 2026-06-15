# vllm-project/vllm#6192: [Bug]: gemma-2-27b error loading with vllm.LLM

| 字段 | 值 |
| --- | --- |
| Issue | [#6192](https://github.com/vllm-project/vllm/issues/6192) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma-2-27b error loading with vllm.LLM

### Issue 正文摘录

### Your current environment ```text Address sizes: 43 bits physical, 48 bits virtual CPU(s): 128 On-line CPU(s) list: 0-127 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 Model name: AMD EPYC 7502 32-Core Processor Stepping: 0 Frequency boost: enabled CPU MHz: 2500.000 CPU max MHz: 2500.0000 CPU min MHz: 1500.0000 BogoMIPS: 5000.23 Virtualization: AMD-V L1d cache: 2 MiB L1i cache: 2 MiB L2 cache: 32 MiB L3 cache: 256 MiB NUMA node0 CPU(s): 0-31,64-95 NUMA node1 CPU(s): 32-63,96-127 Vulnerability Itlb multihit: Not affected Vulnerability L1tf: Not affected Vulnerability Mds: Not affected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STIBP protection Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vulnerability Spectre v2: Mitigation; Retpolines, IBPB conditional, STIBP always-on, RSB filling, PBRSB-eIBRS Not affected Vulnerability Srbds: Not affected...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: gemma-2-27b error loading with vllm.LLM bug ### Your current environment ```text Address sizes: 43 bits physical, 48 bits virtual CPU(s): 128 On-line CPU(s) list: 0
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: xsaveerptr rdpru wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sme...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ted Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STIBP protection Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STIBP protection Vulnerability Spec store bypass: Mit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
