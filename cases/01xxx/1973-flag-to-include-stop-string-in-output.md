# vllm-project/vllm#1973: Flag to include stop string in output

| 字段 | 值 |
| --- | --- |
| Issue | [#1973](https://github.com/vllm-project/vllm/issues/1973) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Flag to include stop string in output

### Issue 正文摘录

Currently vLLM cuts out the stop string from output text (https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py#L683-L689). Reason for this add: 1. In case there are multiple stop strings, we want to understand which stop string caused the stop of generation 2. This also matches the behavior of TGI

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
