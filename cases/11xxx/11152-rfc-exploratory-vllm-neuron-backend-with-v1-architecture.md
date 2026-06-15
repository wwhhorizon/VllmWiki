# vllm-project/vllm#11152: [RFC][Exploratory]: vLLM Neuron Backend with V1 Architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#11152](https://github.com/vllm-project/vllm/issues/11152) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][Exploratory]: vLLM Neuron Backend with V1 Architecture

### Issue 正文摘录

### Motivation. To leverage vLLM V1 architecture change, we are trying to propose a new integration apporach for the neuron backend that seamlessly integrate with vLLM, while maintaining high-performance and taking prefix-caching as first-class feature. ### Background (ref: https://github.com/vllm-project/vllm/issues/8779) vLLM is on a path toward 1/ full support for torch.compile, 2/ turn on chunked prefill, prefix caching, speculative decoding by default, 3/ support more than 60 model variants. While, current neuron backend is supported via the transformers-neuronx library, which has limited support to the combination of these feature. To support a wide range of model variants, vLLM has been maintaining the modular design with vllm.model_executor.layers module. This enables new model developers easily contribute to vLLM to support new model variants. For instance, Mistral team released pixtral-large model weights and brought pixtral-large model support with [Pixtral (](https://github.com/patrickvonplaten/vllm/commit/d394787e5268903a705850413e494ebf2ddcefb5)[vllm-project#8377](https://github.com/vllm-project/vllm/pull/8377)[)](https://github.com/patrickvonplaten/vllm/commit/d3947...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ect/vllm/issues/8779) vLLM is on a path toward 1/ full support for torch.compile, 2/ turn on chunked prefill, prefix caching, speculative decoding by default, 3/ support more than 60 model variants. While, current neuro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC][Exploratory]: vLLM Neuron Backend with V1 Architecture RFC ### Motivation. To leverage vLLM V1 architecture change, we are trying to propose a new integration apporach for the neuron backend that seamlessly integr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: torch.compile with openxla backend. For instance, we can implement copy_blocks with ```python class NeuronAttentionBackend: @torch.compile(backend="openxla") @staticmethod def copy_blocks( kv_caches: List[Tuple[torch.Te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s on a path toward 1/ full support for torch.compile, 2/ turn on chunked prefill, prefix caching, speculative decoding by default, 3/ support more than 60 model variants. While, current neuron backend is supported via t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [RFC][Exploratory]: vLLM Neuron Backend with V1 Architecture RFC ### Motivation. To leverage vLLM V1 architecture change, we are trying to propose a new integration apporach for the neuron backend that seamlessly integr...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
