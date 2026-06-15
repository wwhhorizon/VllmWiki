# vllm-project/vllm#2571: Slow build speed with punica after #1804

| 字段 | 值 |
| --- | --- |
| Issue | [#2571](https://github.com/vllm-project/vllm/issues/2571) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Slow build speed with punica after #1804

### Issue 正文摘录

After #1804, the build speed of vLLM becomes significantly slower. Most of the time was spent on `/home/zhuohan/vllm/vllm/csrc/punica/bgmv/bgmv_all.cu`. Should we turn off punica by default? cc @Yard1

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Slow build speed with punica after #1804 After #1804, the build speed of vLLM becomes significantly slower. Most of the time was spent on `/home/zhuohan/vllm/vllm/csrc/punica/bgmv/bgmv_all.cu`. Should we turn off punica...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
