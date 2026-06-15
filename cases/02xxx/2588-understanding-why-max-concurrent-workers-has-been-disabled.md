# vllm-project/vllm#2588: Understanding why max_concurrent_workers has been disabled

| 字段 | 值 |
| --- | --- |
| Issue | [#2588](https://github.com/vllm-project/vllm/issues/2588) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Understanding why max_concurrent_workers has been disabled

### Issue 正文摘录

I have previously used a vllm version that supported `--max-parallel-loading-workers` being set. This translates to `max_concurrent_workers` [here](https://github.com/vllm-project/vllm/blob/3a7dd7e367277c47472912e84375fa912df07328/vllm/engine/llm_engine.py#L956). I was wondering why it has been disabled [here](https://github.com/vllm-project/vllm/blob/3a7dd7e367277c47472912e84375fa912df07328/vllm/engine/llm_engine.py#L963).

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y max_concurrent_workers has been disabled I have previously used a vllm version that supported `--max-parallel-loading-workers` being set. This translates to `max_concurrent_workers` [here](https://github.com/vllm-proj...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
