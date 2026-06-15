# vllm-project/vllm#3135: [feature request] Consider implementing triton="2.0.0" version of prefix_prefill.py

| 字段 | 值 |
| --- | --- |
| Issue | [#3135](https://github.com/vllm-project/vllm/issues/3135) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [feature request] Consider implementing triton="2.0.0" version of prefix_prefill.py

### Issue 正文摘录

In [context_flashattention_nopad.py](https://github.com/ModelTC/lightllm/blob/main/lightllm/models/llama/triton_kernel/context_flashattention_nopad.py)，it implement two version of context_attention_fwd kernel. Are there any plans to implement triton="2.0.0" version of prefix_prefill.py?

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [feature request] Consider implementing triton="2.0.0" version of prefix_prefill.py In [context_flashattention_nopad.py](https://github.com/ModelTC/lightllm/blob/main/lightllm/models/llama/triton_kernel/context_flashatt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: refix_prefill.py In [context_flashattention_nopad.py](https://github.com/ModelTC/lightllm/blob/main/lightllm/models/llama/triton_kernel/context_flashattention_nopad.py)，it implement two version of context_attention_fwd...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [feature request] Consider implementing triton="2.0.0" version of prefix_prefill.py In [context_flashattention_nopad.py](https://github.com/ModelTC/lightllm/blob/main/lightllm/models/llama/triton_kernel/context_flashatt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [feature request] Consider implementing triton="2.0.0" version of prefix_prefill.py In [context_flashattention_nopad.py](https://github.com/ModelTC/lightllm/blob/main/lightllm/models/llama/triton_kernel/context_flashatt...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
