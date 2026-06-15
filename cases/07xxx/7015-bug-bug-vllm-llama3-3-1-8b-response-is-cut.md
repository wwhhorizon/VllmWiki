# vllm-project/vllm#7015: [Bug]: [Bug]: vllm llama3/3.1-8b response is cut 

| 字段 | 值 |
| --- | --- |
| Issue | [#7015](https://github.com/vllm-project/vllm/issues/7015) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [Bug]: vllm llama3/3.1-8b response is cut 

### Issue 正文摘录

### 🐛 Describe the bug When calling llama3 using vllm message is always truncated Here is the response I have tried to play with different parameters but couldn't found any way to solve this issue. any suggestions?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: [Bug]: vllm llama3/3.1-8b response is cut bug ### 🐛 Describe the bug When calling llama3 using vllm message is always truncated Here is the response I have tried to play with different parameters but couldn't fou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
