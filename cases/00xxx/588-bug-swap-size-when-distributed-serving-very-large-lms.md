# vllm-project/vllm#588: BUG: swap_size - when distributed serving very large LMs

| 字段 | 值 |
| --- | --- |
| Issue | [#588](https://github.com/vllm-project/vllm/issues/588) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> BUG: swap_size - when distributed serving very large LMs

### Issue 正文摘录

Hi I run into another issue: "RuntimeError: Aborted due to the lack of CPU swap space. Please increase the swap space to avoid this error." What is this problem?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
