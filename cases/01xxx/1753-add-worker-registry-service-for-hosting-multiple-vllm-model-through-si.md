# vllm-project/vllm#1753: Add worker registry service for hosting multiple vllm model through single api gateway

| 字段 | 值 |
| --- | --- |
| Issue | [#1753](https://github.com/vllm-project/vllm/issues/1753) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add worker registry service for hosting multiple vllm model through single api gateway

### Issue 正文摘录

I have been using vllm integration from fastchat to host multiple vllm models. However, it does not offer the full capability of vllm. e.g. It does not support beam search. I would like to propose to add a system like the one in the FastChat to to serve vllm workers so that all its capabilities are exposed e.g. greedy search, beam search, return of log_probs, etc. I have done modifying the chat completion endpoint. However, it is specifically written for vllm workers, not the transformers model_workers. The preliminary code can be found at https://github.com/tjtanaa/fastchat-serve/tree/vllm-api-expose-tj Custom OpenAI API server with best_of, use_beam_search https://github.com/tjtanaa/fastchat-serve/blob/vllm-api-expose-tj/src/fastchat_serve/openai_api_server_vllm.py Modified vllm worker to support greedy search and beam search. https://github.com/tjtanaa/fastchat-serve/blob/vllm-api-expose-tj/src/fastchat_serve/vllm_worker.py Would this be helpful to have in this vllm repository? I have opened an issue at https://github.com/lm-sys/FastChat/issues/2709 as I am not sure which repository is better to store this feature.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: stchat to host multiple vllm models. However, it does not offer the full capability of vllm. e.g. It does not support beam search. I would like to propose to add a system like the one in the FastChat to to serve vllm wo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: I have done modifying the chat completion endpoint. However, it is specifically written for vllm workers, not the transformers model_workers. The preliminary code can be found at https://github.com/tjtanaa/fastchat-serv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Add worker registry service for hosting multiple vllm model through single api gateway I have been using vllm integration from fastchat to host multiple vllm models. However, it does not offer the full capability of vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
