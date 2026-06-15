# vllm-project/vllm#3790: [Performance]: Why is it so slow to deploy the model using Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#3790](https://github.com/vllm-project/vllm/issues/3790) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Why is it so slow to deploy the model using Ray

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression ![image](https://github.com/vllm-project/vllm/assets/31993091/f8d08c31-c251-495c-8bbd-5e4c583cd9ae) The two nodes are on the same LAN, so it shouldn't be that slow in theory ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: Why is it so slow to deploy the model using Ray performance ### Proposal to improve performance _No response_ ### Report of performance regression ![image](https://github.com/vllm-project/vllm/assets/3199...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: roposal to improve performance _No response_ ### Report of performance regression ![image](https://github.com/vllm-project/vllm/assets/31993091/f8d08c31-c251-495c-8bbd-5e4c583cd9ae) The two nodes are on the same LAN, so...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
