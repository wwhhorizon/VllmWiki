# vllm-project/vllm#2059: mixtral-8x7B-Instruct-v0.1 giving garbage output on long prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#2059](https://github.com/vllm-project/vllm/issues/2059) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> mixtral-8x7B-Instruct-v0.1 giving garbage output on long prompts

### Issue 正文摘录

Having some trouble pinpointing if its my prompts that is causing this, but often on long-ish prompts (5k+ tokens), the output is either completely unrelated (as in the attached image), or just a word/pair-of-words/phrase being repeated endlessly. Is anybody else facing the same issue?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ord/pair-of-words/phrase being repeated endlessly. Is anybody else facing the same issue?
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: st a word/pair-of-words/phrase being repeated endlessly. Is anybody else facing the same issue?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
