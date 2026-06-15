# vllm-project/vllm#5502: [Usage]: RAG system

| 字段 | 值 |
| --- | --- |
| Issue | [#5502](https://github.com/vllm-project/vllm/issues/5502) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: RAG system

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run a RAG system using vLLM. Is it supported or not. I want to use the vLLM to use a llm model, pass the relevant docs to it and get the answer from it. I can't define a prompt template with the context and question. Can someone help me with this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: using vLLM. Is it supported or not. I want to use the vLLM to use a llm model, pass the relevant docs to it and get the answer from it. I can't define a prompt template with the context and question. Can someone help me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
