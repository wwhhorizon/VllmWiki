# vllm-project/vllm#18180: [Usage]: InfLLM qwen2.5

| 字段 | 值 |
| --- | --- |
| Issue | [#18180](https://github.com/vllm-project/vllm/issues/18180) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: InfLLM qwen2.5

### Issue 正文摘录

[qwen2.txt](https://github.com/user-attachments/files/20218515/qwen2.txt) ### Your current environment ```text The output of `python collect_env.py` ``` vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X NODE SYS SYS 0-27,56-83 0 N/A GPU1 NODE X SYS SYS 0-27,56-83 0 N/A GPU2 SYS SYS X NODE 28-55,84-111 1 N/A GPU3 SYS SYS NODE X 28-55,84-111 1 N/A Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node PHB = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU) PXB = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks NCCL_CUMEM_ENABLE=0 PYTORCH_NVML_BASED_CUDA_CHECK=1 TORCHINDUCTOR_COMPILE_THREADS=1 CUDA_MODULE_LOADING=LAZY VLLM v0.8.4 ### How would you like to use vllm I want to run inference of a [specific model](https://github.com/thunlp/InfLLM). Th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rent environment ```text The output of `python collect_env.py` ``` vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ent ```text The output of `python collect_env.py` ``` vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X NODE SYS SYS...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: InfLLM qwen2.5 usage [qwen2.txt](https://github.com/user-attachments/files/20218515/qwen2.txt) ### Your current environment ```text The output of `python collect_env.py` ``` vLLM Build Flags: CUDA Archs: Not Se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support cuda build_error env_dependency [...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
