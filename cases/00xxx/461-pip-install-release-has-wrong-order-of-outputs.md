# vllm-project/vllm#461: pip install release has wrong order of outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#461](https://github.com/vllm-project/vllm/issues/461) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> pip install release has wrong order of outputs

### Issue 正文摘录

When using `pip install vllm` that version of the library does not have this [PR](#402) merged. Which is a breaking change because the outputs do not match the order of the inputs due to the async nature. When I install from source, the behaviour is correct and I get the right order of outputs.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pip install release has wrong order of outputs bug When using `pip install vllm` that version of the library does not have this [PR](#402) merged. Which is a breaking change because the outputs do not match the order of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
