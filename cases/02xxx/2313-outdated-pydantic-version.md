# vllm-project/vllm#2313: Outdated Pydantic Version

| 字段 | 值 |
| --- | --- |
| Issue | [#2313](https://github.com/vllm-project/vllm/issues/2313) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Outdated Pydantic Version

### Issue 正文摘录

OpenAI's Python library now allows for Pydantic versions >= 1.9.0, < 3 (see openai [requirements](https://github.com/openai/openai-python/blob/f1c7d714914e3321ca2e72839fe2d132a8646e7f/pyproject.toml#L12C27-L12C27)). Would it be possible to bump the pinned version for vLLM to match?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Outdated Pydantic Version OpenAI's Python library now allows for Pydantic versions >= 1.9.0, < 3 (see openai [requirements](https://github.com/openai/openai-python/blob/f1c7d714914e3321ca2e72839fe2d132a8646e7f/pyproject...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
