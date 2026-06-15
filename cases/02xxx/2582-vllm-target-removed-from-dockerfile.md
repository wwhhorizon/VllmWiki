# vllm-project/vllm#2582: `vllm` target removed from Dockerfile

| 字段 | 值 |
| --- | --- |
| Issue | [#2582](https://github.com/vllm-project/vllm/issues/2582) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `vllm` target removed from Dockerfile

### Issue 正文摘录

The `vllm` target was removed from the Dockerfile with [this commit](https://github.com/vllm-project/vllm/commit/6e01e8c1c8ea323d30e3f57050469b2df66b56c6#). I was always building it to this target until now (rather than using `vllm-openai` target. Was this an intentional change?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `vllm` target removed from Dockerfile The `vllm` target was removed from the Dockerfile with [this commit](https://github.com/vllm-project/vllm/commit/6e01e8c1c8ea323d30e3f57050469b2df66b56c6#). I was always building it...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
