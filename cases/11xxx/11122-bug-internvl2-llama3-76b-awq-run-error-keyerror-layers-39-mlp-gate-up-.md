# vllm-project/vllm#11122: [Bug]: InternVL2-Llama3-76B-AWQ RUN ERROR KeyError: 'layers.39.mlp.gate_up_proj.qweight'

| 字段 | 值 |
| --- | --- |
| Issue | [#11122](https://github.com/vllm-project/vllm/issues/11122) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL2-Llama3-76B-AWQ RUN ERROR KeyError: 'layers.39.mlp.gate_up_proj.qweight'

### Issue 正文摘录

### Your current environment Neuron SDK Version: N/A vLLM Version: 0.6.4.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 GPU4 GPU5 GPU6 GPU7 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X PIX PXB PXB SYS SYS SYS SYS 0-95 N/A N/A GPU1 PIX X PXB PXB SYS SYS SYS SYS 0-95 N/A N/A GPU2 PXB PXB X PXB SYS SYS SYS SYS 0-95 N/A N/A GPU3 PXB PXB PXB X SYS SYS SYS SYS 0-95 N/A N/A GPU4 SYS SYS SYS SYS X PIX PXB PXB 0-95 N/A N/A GPU5 SYS SYS SYS SYS PIX X PXB PXB 0-95 N/A N/A GPU6 SYS SYS SYS SYS PXB PXB X PXB 0-95 N/A N/A GPU7 SYS SYS SYS SYS PXB PXB PXB X 0-95 N/A N/A Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node PHB = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU) PXB = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks NVIDIA_VISIBLE_DEVICES=all CUBLAS_VERSION=12.2.5.6 NVIDIA_REQ...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: InternVL2-Llama3-76B-AWQ RUN ERROR KeyError: 'layers.39.mlp.gate_up_proj.qweight' bug ### Your current environment Neuron SDK Version: N/A vLLM Version: 0.6.4.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Di...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 9.mlp.gate_up_proj.qweight' bug ### Your current environment Neuron SDK Version: N/A vLLM Version: 0.6.4.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 GP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ent Neuron SDK Version: N/A vLLM Version: 0.6.4.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 GPU4 GPU5 GPU6 GPU7 CPU Affinity NUMA Affinity GPU NUMA ID...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 9.3 NVIDIA_DRIVER_CAPABILITIES=compute,utility,video NVIDIA_PRODUCT_NAME=Triton Server CUDA_VERSION=12.2.2.009 CUDA_VISIBLE_DEVICES=0,1,2,3 CUDA_VISIBLE_DEVICES=0,1,2,3 CUDNN_VERSION=8.9.5.29 NVIDIA_TRITON_SERVER_VERSIO...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: uted_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization cuda;gemm;quantization;triton build_error;crash Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
