# vllm-project/vllm#3760: [Bug]: Issue with using min_tokens from recent build

| 字段 | 值 |
| --- | --- |
| Issue | [#3760](https://github.com/vllm-project/vllm/issues/3760) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue with using min_tokens from recent build

### Issue 正文摘录

### Your current environment My current environment setup is : ``` Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] triton 2.1.0 pypi_0 pypiROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X 0,2 0 N/A Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node PHB = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU) PXB = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks ``` ### 🐛 Describe the bug Currently, I am trying to use vllm for the task of summarization and I was getting the error of min_tokens not being present in the `SamplingParams` API. Hence, I wanted to install fr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Issue with using min_tokens from recent build bug;stale ### Your current environment My current environment setup is : ``` Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [conda] triton 2.1.0 pypi_0 pypiROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 CPU Affinity NUMA Affi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] triton 2.1.0
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 132, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-9q0l22qz/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 448, in get_requires_for_build_editab...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Issue with using min_tokens from recent build bug;stale ### Your current environment My current environment setup is : ``` Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
