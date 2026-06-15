# vllm-project/vllm#1999: Fail to install the old version with the provided command, report error

| 字段 | 值 |
| --- | --- |
| Issue | [#1999](https://github.com/vllm-project/vllm/issues/1999) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Fail to install the old version with the provided command, report error

### Issue 正文摘录

fail to install the old version: pip install https://github.com/vllm-project/vllm/releases/download/v0.2.2/vllm-0.2.2+cu118-cp310-cp310-manylinu**x1_x86_64.whl ### ERROR: vllm-0.2.2+cu118-cp310-cp310-manylinux1_x86_64.whl is not a supported wheel on this platform.**

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Fail to install the old version with the provided command, report error fail to install the old version: pip install https://github.com/vllm-project/vllm/releases/download/v0.2.2/vllm-0.2.2+cu118-cp310-cp310-manylinu**x...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
