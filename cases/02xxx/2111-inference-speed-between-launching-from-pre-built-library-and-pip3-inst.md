# vllm-project/vllm#2111: Inference speed between launching from pre-built library and pip3 install -e .

| 字段 | 值 |
| --- | --- |
| Issue | [#2111](https://github.com/vllm-project/vllm/issues/2111) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Inference speed between launching from pre-built library and pip3 install -e .

### Issue 正文摘录

Hi, I am wondering if there is difference in inference speed between launching vllm from pre-built library and that of 'pip3 install -e .' . Will installing using 'pip3 install -e .' have some speed degradation?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Inference speed between launching from pre-built library and pip3 install -e . Hi, I am wondering if there is difference in inference speed between launching vllm from pre-built library and that of 'pip3 install -e .' ....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
