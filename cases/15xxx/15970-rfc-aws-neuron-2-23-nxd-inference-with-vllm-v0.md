# vllm-project/vllm#15970: [RFC]: AWS Neuron 2.23 NxD Inference with vLLM V0

| 字段 | 值 |
| --- | --- |
| Issue | [#15970](https://github.com/vllm-project/vllm/issues/15970) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: AWS Neuron 2.23 NxD Inference with vLLM V0

### Issue 正文摘录

### Motivation. AWS Neuron has released the [NeuronX Distributed (NxD) Inference](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-inference/index.html) library, a PyTorch-based solution that has performance optimizations relevant to AWS Trainium and Inferentia instances. NxD Inference is the path forward for optimized inference on Neuron. The [Transformers NeuronX (TNx)](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/transformers-neuronx/index.html) library will soon reach the end of support. This RFC integrates NxD Inference into vLLM and adds minor features to TNx. The integration currently targets vLLM’s V0 architecture, with plans to migrate to V1 Architecture. These changes streamline Neuron Serving with vLLM while maintaining while maintaining compatibility and performance for inference workloads on AWS Trainium and Inferentia. AWS Neuron is committed to supporting vLLM and is planning an engineering roadmap with deeper integration. We will share the next RFC with the vLLM community for feedback once it’s ready. **We are adding the following features to the current RFC:** 1. NeuronX Distributed (NxD) Inference Support 2. Speculative D...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ference Support 2. Speculative Decoding 3. Dynamic On-device Sampling 4. Quantized Model Support (limited to TNx) 4. Multi-Modal Support (Llama-3.2) 5. Multi-LoRA Serving **Note:** The changes will be isolated to Neuron...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pport 2. Speculative Decoding 3. Dynamic On-device Sampling 4. Quantized Model Support (limited to TNx) 4. Multi-Modal Support (Llama-3.2) 5. Multi-LoRA Serving **Note:** The changes will be isolated to Neuron-specific...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Multi-LoRA Serving **Note:** The changes will be isolated to Neuron-specific logic and will not impact other platforms. ### Proposed Change. 1. NeuronX Distributed (NxD) Inference Support 1. Allow customers to select a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: adds minor features to TNx. The integration currently targets vLLM’s V0 architecture, with plans to migrate to V1 Architecture. These changes streamline Neuron Serving with vLLM while maintaining while maintaining compa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: to the current RFC:** 1. NeuronX Distributed (NxD) Inference Support 2. Speculative Decoding 3. Dynamic On-device Sampling 4. Quantized Model Support (limited to TNx) 4. Multi-Modal Support (Llama-3.2) 5. Multi-LoRA Ser...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
