# vllm-project/vllm#618: cannot import name 'LLM' from 'vllm' (unknown location)

| 字段 | 值 |
| --- | --- |
| Issue | [#618](https://github.com/vllm-project/vllm/issues/618) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> cannot import name 'LLM' from 'vllm' (unknown location)

### Issue 正文摘录

I am building vllm from source, and I am unable to import LLM from vllm. > from vllm import LLM, SamplingParams

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cannot import name 'LLM' from 'vllm' (unknown location) I am building vllm from source, and I am unable to import LLM from vllm. > from vllm import LLM, SamplingParams

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
