# vllm-project/vllm#42432: [Bug]: deepseek v4 failed to work on R6000 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#42432](https://github.com/vllm-project/vllm/issues/42432) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseek v4 failed to work on R6000 GPU

### Issue 正文摘录

### Your current environment ``` Collecting environment information... BIOS Model name: INTEL(R) XEON(R) GOLD 6548Y+ CPU @ 2.3GHz BIOS CPU family: 2 CPU family: 6 Model: 207 Thread(s) per core: 1 Core(s) per socket: 16 Socket(s): 1 Stepping: 2 BogoMIPS: 5000.00 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscplm constant_tsc arch_perfmon rep_good nopl xtopology tsc_reliable nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves user_shstk avx_vnni avx512_bf16 wbnoinvd arat avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid cldemote movdiri movdir64b fsrm md_clear serialize amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities Hypervisor vendor: VMware Virtualization type: full L1d cache: 768...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: 512bw avx512vl xsaveopt xsavec xgetbv1 xsaves user_shstk avx_vnni avx512_bf16 wbnoinvd arat avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid cldemote movdiri m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: _reliable nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch ssbd ibrs ibpb stibp ibrs_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: 00] Detected quantization_config.scale_fmt=ue8m0; enabling UE8M0 for DeepGEMM. (APIServer pid=396885) INFO 05-12 14:40:19 [model.py:568] Resolved architecture: DeepseekV4ForCausalLM (APIServer pid=396885) INFO 05-12 14:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: l_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, quantization=deepseek_v4_fp8, quantization_config=None, enforce_eager=True, enable_return_routed_e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscplm constant_tsc arch_perfmon rep_good nopl xtopology tsc_reliable nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe po...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
