# vllm-project/vllm#15222: [New Model]: jinaai/jina-reranker-v2-base-multilingual

| 字段 | 值 |
| --- | --- |
| Issue | [#15222](https://github.com/vllm-project/vllm/issues/15222) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: jinaai/jina-reranker-v2-base-multilingual

### Issue 正文摘录

### The model to consider. https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual ### The closest model vllm already supports. XLMRobertaForSequenceClassification ### What's your difficulty of supporting the model you want? The jinaai's XLMRoberta implementation is different from vllm's current implementation. When I try to using vllm to load jina-reranker-v2-base-multilingual . Exception occurred as following: ```python [rank0]: File "/home/xiayubin/.local/share/virtualenvs/test_project-krbMYW6A/lib/python3.11/site-packages/vllm/model_executor/models/roberta.py", line 224, in load_weights [rank0]: self.roberta.load_weights(bert_weights) [rank0]: File "/home/xiayubin/.local/share/virtualenvs/test_project-krbMYW6A/lib/python3.11/site-packages/vllm/model_executor/models/bert.py", line 381, in load_weights [rank0]: param = params_dict[name] [rank0]: ~~~~~~~~~~~^^^^^^ [rank0]: KeyError: 'emb_ln.weight' Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s] ``` The missing parameter `emb_ln.weight` is layer normalization layer in jinaai XLMRoberta refer to [code](https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual/blob/eed787badf7784e1a25c0eaa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: jinaai/jina-reranker-v2-base-multilingual new-model ### The model to consider. https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual ### The closest model vllm already supports. XLMRobertaForSequ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: del ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ing: ```python [rank0]: File "/home/xiayubin/.local/share/virtualenvs/test_project-krbMYW6A/lib/python3.11/site-packages/vllm/model_executor/models/roberta.py", line 224, in load_weights [rank0]: self.roberta.load_weigh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
