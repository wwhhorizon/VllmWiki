# vllm-project/vllm#5712: [Usage]: Is this an error ? "async_llm_engine.py:154] Aborted request cmpl-xxxxx"

| 字段 | 值 |
| --- | --- |
| Issue | [#5712](https://github.com/vllm-project/vllm/issues/5712) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Is this an error ? "async_llm_engine.py:154] Aborted request cmpl-xxxxx"

### Issue 正文摘录

### Your current environment ```text Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.18.1 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] nomkl 3.0 0 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.18.1 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] triton 2.1.0 pypi_0 pypiROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.0 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 CPU Affinity NUMA Affinity GPU0 X SYS 0-23,48-71 0 GPU1 SYS X 24-47,72-95 1 Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node PHB = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU) PXB = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks (vllm) [jack@localhost model_product]$ ``` ### How would you...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed request cmpl-xxxxx" usage;stale ### Your current environment ```text Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.18.1 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] nomkl 3.0 0 h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [conda] triton 2.1.0 pypi_0 pypiROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.0 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 CPU Affinity NU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Is this an error ? "async_llm_engine.py:154] Aborted request cmpl-xxxxx" usage;stale ### Your current environment ```text Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.18.1 [pi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.18.1 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] nomkl 3.0 0 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main [conda] numpy 1.26.4 pypi_0 pypi [conda]
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: = Connection traversing a bonded set of # NVLinks (vllm) [jack@localhost model_product]$ ``` ### How would you like to use vllm I keep seeing the output of the vllm that : async_llm_engine.py:154] Aborted request cmpl-x...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
