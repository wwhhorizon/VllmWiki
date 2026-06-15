# vllm-project/vllm#7519: [Feature]: Context Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#7519](https://github.com/vllm-project/vllm/issues/7519) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Context Parallelism

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As we can see, Google Gemini can support up to million tokens and to serve longer context length, we have to do context parallelism, which means, split the input matrix on sequence dimension to multi-GPUs. I myself have experience on context parallelism and vLLM (i did Whisper fork), and I am ready to support Context Parallelism development for vLLM. This issue will be long to explain the idea from my side. Context Parallelism is utilizing Blockwise Attention, https://arxiv.org/abs/2305.19370, which, - Each Q block must access all KV blocks to compute local attentions and LSEs, after that aggregate. Improvement of Blockwise Attention, - Ring Attention, only make sense for gpus > 2, https://arxiv.org/abs/2310.01889 - Tree Attention, topology aware, only make sense for multiple worlds aka multi-nodes, https://arxiv.org/abs/2408.04093 - Ring and Tree just to improve communication overhead, but still, each Q block must access all KV blocks and aggregate. ## Assume variables num_gpus = 2 batch_size = 1 num_head = 32 head_dim = 128 - Why only 2 gpus? Easy to draw at below. But can be any size of devices. - We also assumed one device only fit max 5...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Context Parallelism feature request;stale ### 🚀 The feature, motivation and pitch As we can see, Google Gemini can support up to million tokens and to serve longer context length, we have to do context parall...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: long to explain the idea from my side. Context Parallelism is utilizing Blockwise Attention, https://arxiv.org/abs/2305.19370, which, - Each Q block must access all KV blocks to compute local attentions and LSEs, after...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ica/context-parallelism-xformers/blob/master/playground/step-sdpa.ipynb Flash attention also returned LSE, should be able to the same blockwise. **During prefill, context parallelism use all GPUs, during step, only one...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tention Each GPU will calculate their own Blockwise Attention and can decide which communication need to use, 2. if num_gpus > 2 and multi nodes, use tree. 1. else, use ring. #### Data movement Now for each GPU, 1. [50k...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Context Parallelism feature request;stale ### 🚀 The feature, motivation and pitch As we can see, Google Gemini can support up to million tokens and to serve longer context length, we have to do context parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
