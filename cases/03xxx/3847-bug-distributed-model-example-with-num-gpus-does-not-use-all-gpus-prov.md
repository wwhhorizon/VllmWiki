# vllm-project/vllm#3847: [Bug]: distributed model example with num_gpus does not use all gpus provided by the ray actor

| 字段 | 值 |
| --- | --- |
| Issue | [#3847](https://github.com/vllm-project/vllm/issues/3847) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: distributed model example with num_gpus does not use all gpus provided by the ray actor

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ``` Versions of relevant libraries: [pip3] mypy-extensions==0.4.3 [pip3] numpy==1.23.5 [pip3] torch==2.0.1+cu118 [pip3] torchvision==0.15.2+cu118 [pip3] triton==2.0.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 NIC0 NIC1 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X NV12 NODE NODE 0-23 0 N/A GPU1 NV12 X SYS SYS 24-47 1 N/A NIC0 NODE SYS X NODE NIC1 NODE SYS NODE X Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node PHB = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU) PXB = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks NIC Legend: NIC0: mlx5_0 NIC1: mlx5_1 ``` ### 🐛 Describe the bug I am running llama 70b and...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rrent environment ```text The output of `python collect_env.py` ``` ``` Versions of relevant libraries: [pip3] mypy-extensions==0.4.3 [pip3] numpy==1.23.5 [pip3] torch==2.0.1+cu118 [pip3] torchvision==0.15.2+cu118 [pip3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: torchvision==0.15.2+cu118 [pip3] triton==2.0.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled G...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: distributed model example with num_gpus does not use all gpus provided by the ray actor bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ``` Versions of relevant libraries:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: xample with num_gpus does not use all gpus provided by the ray actor bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ``` Versions of relevant libraries: [pip3] mypy-extensions==0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 1.23.5 [pip3] torch==2.0.1+cu118 [pip3] torchvision==0.15.2+cu118 [pip3] triton==2.0.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
