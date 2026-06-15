# vllm-project/vllm#27019: [New Model]: Add support for openPangu-Ultra-MoE-718B

| 字段 | 值 |
| --- | --- |
| Issue | [#27019](https://github.com/vllm-project/vllm/issues/27019) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Add support for openPangu-Ultra-MoE-718B

### Issue 正文摘录

### The model to consider. [https://ai.gitcode.com/ascend-tribe/openPangu-Ultra-MoE-718B-V1.1](url) The architecture of the openPangu-Ultra-MoE-718B-V1.1 adopts the mainstream Multi-head Latent Attention (MLA), Multi-Token Prediction (MTP), high MoE sparsity, and features several different designs: Depth-Scaled Sandwich-Norm and TinyInit: These techniques adjust the layer normalization structure and parameter initialization for improved training stability. EP-Group load balancing loss: This technique optimizes the load balancing loss, achieving better expert specialization. ### The closest model vllm already supports. The closest model is Deepseek_v3. ### What's your difficulty of supporting the model you want? Most related mainstream modules have been well implemented in vllm, but the Depth-Scaled Sandwich-Norm structure and EP-Group router still need some adaptation. Furthermore, more dense models in openPangu series will be added in the future. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [New Model]: Add support for openPangu-Ultra-MoE-718B new-model ### The model to consider. [https://ai.gitcode.com/ascend-tribe/openPangu-Ultra-MoE-718B-V1.1](url) The architecture of the openPangu-Ultra-MoE-718B-V1.1 a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: meter initialization for improved training stability. EP-Group load balancing loss: This technique optimizes the load balancing loss, achieving better expert specialization. ### The closest model vllm already supports....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: (MTP), high MoE sparsity, and features several different designs: Depth-Scaled Sandwich-Norm and TinyInit: These techniques adjust the layer normalization structure and parameter initialization for improved training sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s://ai.gitcode.com/ascend-tribe/openPangu-Ultra-MoE-718B-V1.1](url) The architecture of the openPangu-Ultra-MoE-718B-V1.1 adopts the mainstream Multi-head Latent Attention (MLA), Multi-Token Prediction (MTP), high MoE s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: Add support for openPangu-Ultra-MoE-718B new-model ### The model to consider. [https://ai.gitcode.com/ascend-tribe/openPangu-Ultra-MoE-718B-V1.1](url) The architecture of the openPangu-Ultra-MoE-718B-V1.1 a...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
