# vllm-project/vllm#19278: [New Model]: jinaai/jina-colbert-v2

| 字段 | 值 |
| --- | --- |
| Issue | [#19278](https://github.com/vllm-project/vllm/issues/19278) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: jinaai/jina-colbert-v2

### Issue 正文摘录

### The model to consider. https://huggingface.co/jinaai/jina-colbert-v2 ### The closest model vllm already supports. https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual ### What's your difficulty of supporting the model you want? When trying to serve the model with `vllm serve jinaai/jina-colbert-v2 --port 8001 --trust-remote-code` I get the following error: ERROR 06-06 11:18:00 [core.py:500] AttributeError: module 'transformers_modules.jinaai.xlm-roberta-flash-implementation.2b6bc3f30750b3a9648fe9b63448c09920efe9be.modeling_xlm_roberta' has no attribute 'XLMRobertaForPreTraining'. Did you mean: 'XLMRobertaPreTrainingHeads'? The error occurs because vLLM is trying to find the class XLMRobertaForPreTraining in the custom modeling_xlm_roberta.py from the jinaai/xlm-roberta-flash-implementation repo, but that class does not exist there. The Transformers implementation for this model is not yet compatible with vLLM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked ques...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: jinaai/jina-colbert-v2 stale ### The model to consider. https://huggingface.co/jinaai/jina-colbert-v2 ### The closest model vllm already supports. https://huggingface.co/jinaai/jina-reranker-v2-base-multili...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: LM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: jinaai/jina-colbert-v2 stale ### The model to consider. https://huggingface.co/jinaai/jina-colbert-v2 ### The closest model vllm already supports. https://huggingface.co/jinaai/jina-reranker-v2-base-multili...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
