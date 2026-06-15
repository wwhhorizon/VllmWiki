# vllm-project/vllm#619: cannot import name 'LLM' from 'vllm' (unknown location)

| 字段 | 值 |
| --- | --- |
| Issue | [#619](https://github.com/vllm-project/vllm/issues/619) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> cannot import name 'LLM' from 'vllm' (unknown location)

### Issue 正文摘录

on running `from vllm import LLM, SamplingParams` I get the error above. I am building the package from source, because the pip version has a bug for my usecase. How do I resolve this?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cannot import name 'LLM' from 'vllm' (unknown location) on running `from vllm import LLM, SamplingParams` I get the error above. I am building the package from source, because the pip version has a bug for my usecase. H...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
