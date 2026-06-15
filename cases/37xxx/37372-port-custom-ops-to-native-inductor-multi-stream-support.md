# vllm-project/vllm#37372: Port custom ops to native Inductor multi-stream support

| 字段 | 值 |
| --- | --- |
| Issue | [#37372](https://github.com/vllm-project/vllm/issues/37372) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Port custom ops to native Inductor multi-stream support

### Issue 正文摘录

Native multi-stream in torch.compile will be supported soon. We should clean the custom op implementation like https://github.com/vllm-project/vllm/pull/36795 when native multi-stream support is available in the next pytorch release.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ops to native Inductor multi-stream support Native multi-stream in torch.compile will be supported soon. We should clean the custom op implementation like https://github.com/vllm-project/vllm/pull/36795 when native mult...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
