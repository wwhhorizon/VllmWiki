# vllm-project/vllm#6064: [Bug]: benchmark_serving.py cannot calculate Median TTFT correctly

| 字段 | 值 |
| --- | --- |
| Issue | [#6064](https://github.com/vllm-project/vllm/issues/6064) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark_serving.py cannot calculate Median TTFT correctly

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Virtualization: VT-x L1d cache: 1.9 MiB (40 instances) L1i cache: 1.3 MiB (40 instances) L2 cache: 50 MiB (40 instances) L3 cache: 60 MiB (2 instances) NUMA node(s): 2 NUMA node0 CPU(s): 0-19,40-59 NUMA node1 CPU(s): 20-39,60-79 Vulnerability Itlb multihit: Not affected Vulnerability L1tf: Not affected Vulnerability Mds: Not affected Vulnerability Meltdown: Not affected Vulnerability Spec store bypass: Vulnerable Vulnerability Spectre v1: Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers Vulnerability Spectre v2: Vulnerable, IBPB: disabled, STIBP: disabled Vulnerability Srbds: Not affected Vulnerability Tsx async abort: Not affected Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] sentence-transformers==2.2.2 [pip3] torch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformers==4.40.2 [pip3] transformers-stream-generator==0.0.4 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.0.post1 vLLM Build Flags: CUDA Archs: Not Set...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Not affected Vulnerability Tsx async abort: Not affected Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] sentence-transformers==2.2.2 [pip3] torch==2.3.0 [pip3] torchvision==0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.0.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: D...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: benchmark_serving.py cannot calculate Median TTFT correctly bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` Virtualization: VT-x L1d cache: 1.9 MiB (40 instances) L1i cach...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.40.2 [pip3] transformers-stream-generator==0.0.4 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: est rate, The Median TTFT obtained by benchmark_serving is always 0. ![dsfp8-100-1000](https://github.com/vllm-project/vllm/assets/49669092/ab3ef671-f12a-469f-b9e4-895aeee74723) When request rate is low, Median TTFT is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
