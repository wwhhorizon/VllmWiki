# vllm-project/vllm#3457: [Usage]: When I set tensor_parallel_size as 2 and worker_use_ray will be automatically true, Ray will stop when INFO ray.init() 

| 字段 | 值 |
| --- | --- |
| Issue | [#3457](https://github.com/vllm-project/vllm/issues/3457) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: When I set tensor_parallel_size as 2 and worker_use_ray will be automatically true, Ray will stop when INFO ray.init() 

### Issue 正文摘录

### Your current environment NUMA node(s): 1 NUMA node0 CPU(s): 0-47 Vulnerability Gather data sampling: Unknown: Dependent on hypervisor status Vulnerability Itlb multihit: Not affected Vulnerability L1tf: Not affected Vulnerability Mds: Not affected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vulnerability Spectre v2: Mitigation; Enhanced IBRS, IBPB conditional, RSB filling, PBRSB-eIBRS SW sequence Vulnerability Srbds: Not affected Vulnerability Tsx async abort: Mitigation; TSX disabled Versions of relevant libraries: [pip3] numpy==1.26.3 [pip3] optree==0.10.0 [pip3] torch==2.1.2 [pip3] torchaudio==2.2.0 [pip3] torchelastic==0.2.2 [pip3] torchvision==0.17.0 [pip3] triton==2.1.0 [conda] blas 1.0 mkl [conda] ffmpeg 4.3 hf484d3e_0 pytorch [conda] libjpeg-turbo 2.0.0 h9bf148f_0 pytorch [conda]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t affected Vulnerability Tsx async abort: Mitigation; TSX disabled Versions of relevant libraries: [pip3] numpy==1.26.3 [pip3] optree==0.10.0 [pip3] torch==2.1.2 [pip3] torchaudio==2.2.0 [pip3] torchelastic==0.2.2 [pip3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rag.init. Log info: WARNING 03-18 03:37:09 config.py:618] Casting torch.bfloat16 to torch.float16. INFO 03-18 03:37:09 config.py:433] Custom all-reduce kernels are temporarily disabled due to stability issues. We will r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mkl [conda] ffmpeg 4.3 hf484d3e_0 pytorch [conda] libjpeg-turbo 2.0.0 h9bf148f_0 pytorch [conda] mkl 2023.1.0 h213fc3f_46344 [conda] mkl-service 2.4.0 py3
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: udio==2.2.0 [pip3] torchelastic==0.2.2 [pip3] torchvision==0.17.0 [pip3] triton==2.1.0 [conda] blas 1.0 mkl [conda] ffmpeg 4.3 hf484d3e_0 pytorch [conda] libjpeg-turbo 2.0.0 h9bf14

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
