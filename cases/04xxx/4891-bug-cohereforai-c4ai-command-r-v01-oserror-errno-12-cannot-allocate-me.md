# vllm-project/vllm#4891: [Bug]: `CohereForAI/c4ai-command-r-v01`OSError: [Errno 12] Cannot allocate memory

| 字段 | 值 |
| --- | --- |
| Issue | [#4891](https://github.com/vllm-project/vllm/issues/4891) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `CohereForAI/c4ai-command-r-v01`OSError: [Errno 12] Cannot allocate memory

### Issue 正文摘录

### Your current environment ```text qdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid fsrm md_clear pconfig flush_l1d arch_capabilities Virtualization: VT-x L1d cache: 1.1 MiB (24 instances) L1i cache: 768 KiB (24 instances) L2 cache: 30 MiB (24 instances) L3 cache: 36 MiB (2 instances) NUMA node(s): 2 NUMA node0 CPU(s): 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46 NUMA node1 CPU(s): 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47 Vulnerability Gather data sampling: Mitigation; Microcode Vulnerability Itlb multihit: Not affected Vulnerability L1tf: Not affected Vulnerability Mds: Not affected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vulnerability Spectre v2: Mitigation; Enhanced / Automatic IBRS, IBPB conditional, RSB filling, PBRSB-eIBRS SW sequence Vulnerability Srbds: Not affected Vulnera...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Not affected Vulnerability Tsx async abort: Not affected Versions of relevant libraries: [pip3] flake8==7.0.0 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [ [pip3] torch==2.2.1 [pip3] torch-ac==1.4.0 [pip3] triton...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 2_bitalg tme avx512_vpopcntdq la57 rdpid fsrm md_clear pconfig flush_l1d arch_capabilities Virtualization: VT-x L1d cache: 1.1 MiB (24 instances) L1i cache: 768 KiB (24 instances) L2 cache: 30 MiB
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid fsrm md_clear pconfig flush_l1d arch_capabilities Virtualization: VT-x L1d cache: 1.1 MiB (24 instances) L1i cache: 768 KiB (24 instances) L2 cache:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eForAI/c4ai-command-r-v01`OSError: [Errno 12] Cannot allocate memory bug;stale ### Your current environment ```text qdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid fsrm md_clear pconfig flush_l1d arch_capa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] numpy==1.26.4 [ [pip3] torch==2.2.1 [pip3] torch-ac==1.4.0 [pip3] triton==2.2.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.19.3 pypi_0 pypi [conda] torch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
