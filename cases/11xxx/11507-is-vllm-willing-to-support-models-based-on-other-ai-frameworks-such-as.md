# vllm-project/vllm#11507: Is vllm willing to support models based on other AI frameworks, such as mindspore?

| 字段 | 值 |
| --- | --- |
| Issue | [#11507](https://github.com/vllm-project/vllm/issues/11507) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is vllm willing to support models based on other AI frameworks, such as mindspore?

### Issue 正文摘录

Hello, we are MindSpore eco-developers! MindSpore is a new open source deep learning training/inference framework that could be used for mobile, edge and cloud scenarios.(You can get a more detailed introduction to MindSpore at: https://www.mindspore.cn/en) We want to add a MindSpore backend to vllm to expand the MindSpore ecosystem, and at the same time, also make the vllm ecosystem better. Our team has several software engineers with years of development experience, and we are supported by the team of MindSpore framework developers. We would like to know if your community accepts models based on MindSpore? and if it is possible, we can discuss the technical details further.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: o MindSpore at: https://www.mindspore.cn/en) We want to add a MindSpore backend to vllm to expand the MindSpore ecosystem, and at the same time, also make the vllm ecosystem better. Our team has several software enginee...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Is vllm willing to support models based on other AI frameworks, such as mindspore? usage Hello, we are MindSpore eco-developers! MindSpore is a new open source deep learning training/inference framework that could be us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
