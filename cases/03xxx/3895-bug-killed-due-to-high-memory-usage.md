# vllm-project/vllm#3895: [Bug]: killed due to high memory usage

| 字段 | 值 |
| --- | --- |
| Issue | [#3895](https://github.com/vllm-project/vllm/issues/3895) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: killed due to high memory usage

### Issue 正文摘录

### Your current environment NUMA node(s): 2 NUMA node0 CPU(s): 0-19,40-59 NUMA node1 CPU(s): 20-39,60-79 Vulnerability Gather data sampling: Mitigation; Microcode Vulnerability Itlb multihit: KVM: Mitigation: VMX disabled Vulnerability L1tf: Mitigation; PTE Inversion; VMX conditional cache flushes, SMT vulnerable Vulnerability Mds: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Mitigation; IBRS Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vulnerability Spectre v2: Mitigation; IBRS, IBPB conditional, STIBP conditional, RSB filling, PBRSB-eIBRS Not affected Vulnerability Srbds: Not affected Vulnerability Tsx async abort: Mitigation; Clear CPU buffers; SMT vulnerable Versions of relevant libraries: [pip3] lion-pytorch==0.1.2 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.25.1 [pip3] onnxruntime==1.15.1 [pip3] pytorch-ignite==0.4.12 [pip3] torch==2.1....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tion: VMX disabled Vulnerability L1tf: Mitigation; PTE Inversion; VMX conditional cache flushes, SMT vulnerable Vulnerability Mds: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Meltdown: Mitigation; PTI Vu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Mitigation; PTE Inversion; VMX conditional cache flushes, SMT vulnerable Vulnerability Mds: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;quantization;sampling;triton build_error;crash;nan_inf;oom dtype;env_dependency Your curren...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e==1.15.1 [pip3] pytorch-ignite==0.4.12 [pip3] torch==2.1.2 [pip3] torch-model-archiver==0.9.0 [pip3] torchaudio==2.1.0+cu121 [pip3] torchserve==0.9.0 [pip3] torchvision==0.16.0+cu121 [pip3] triton==2.1.0 [conda] lion-p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: killed due to high memory usage bug;stale ### Your current environment NUMA node(s): 2 NUMA node0 CPU(s): 0-19,40-59 NUMA node1 CPU(s): 20-39,60-79 Vulnerability Gather data sampling: Mitigation; Mic

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
