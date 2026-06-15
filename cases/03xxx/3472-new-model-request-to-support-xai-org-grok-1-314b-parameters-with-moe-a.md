# vllm-project/vllm#3472: [New Model]: Request to support xai-org/grok-1 (314B parameters with MOE architecture)

| 字段 | 值 |
| --- | --- |
| Issue | [#3472](https://github.com/vllm-project/vllm/issues/3472) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | moe;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [New Model]: Request to support xai-org/grok-1 (314B parameters with MOE architecture)

### Issue 正文摘录

### The model to consider. https://huggingface.co/xai-org/grok-1 With int8 quantization, this model can be hosted on 8 GPUs with 80GB memory, a node of H100 or A100. After a high-level look at the code, I am seeing xai has the model architecture implemented via JAX and its code couples model architecture and implementation details such as int8 quantization and sharing across GPUs. I saw a twitter post about the tricky implementation differences in Gemma's implementations. So, I wonder if someone familiar with JAX is planning to port it to PyTorch and validate, so that it can be integrate with vLLM with additional optimization for MOE architecture. ### The closest model vllm already supports. Mixtral 8x7B. ### What's your difficulty of supporting the model you want? - its source code is in JAX, instead of PyTorch - It requires quantization; otherwise, it won't work on most GPUs, including H100/A100. Here, I assume cpu offloading is not of considerations to avoid notable impact on efficiency - Its MOE component require additional optimization for inference efficiency

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [New Model]: Request to support xai-org/grok-1 (314B parameters with MOE architecture) new-model;stale ### The model to consider. https://huggingface.co/xai-org/grok-1 With int8 quantization, this model can be hosted on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Request to support xai-org/grok-1 (314B parameters with MOE architecture) new-model;stale ### The model to consider. https://huggingface.co/xai-org/grok-1 With int8 quantization, this model can be hosted on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: The model to consider. https://huggingface.co/xai-org/grok-1 With int8 quantization, this model can be hosted on 8 GPUs with 80GB memory, a node of H100 or A100. After a high-level look at the code, I am seeing xai has...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [New Model]: Request to support xai-org/grok-1 (314B parameters with MOE architecture) new-model;stale ### The model to consider. https://huggingface.co/xai-org/grok-1 With int8 quantization, this model can be hosted on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: Request to support xai-org/grok-1 (314B parameters with MOE architecture) new-model;stale ### The model to consider. https://huggingface.co/xai-org/grok-1 With int8 quantization, this model can be hosted on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
