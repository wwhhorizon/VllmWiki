# vllm-project/vllm#4880: [Usage]: gpu memory usage when using tensor parallel 

| 字段 | 值 |
| --- | --- |
| Issue | [#4880](https://github.com/vllm-project/vllm/issues/4880) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: gpu memory usage when using tensor parallel 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm i try to use vllm to serve Qwen-32B-chat-AWQ in 3090(24G x 2). in my expectation, 24G memory could be enough in one gpu, so i use one GPU at first time, but failed then i try to use tensor parallel to serve the model and that work, but memeory usage over my expection: 18G for each GPU, total 36G, that much more beyond my expectation for one GPU, i want to know, if that is common in my expectation, 13-14G for each GPU is enough

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .py` ``` ### How would you like to use vllm i try to use vllm to serve Qwen-32B-chat-AWQ in 3090(24G x 2). in my expectation, 24G memory could be enough in one gpu, so i use one GPU at first time, but failed then i try...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: gpu memory usage when using tensor parallel usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm i try to use vllm to serve Qwen-32B-chat-AWQ i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
