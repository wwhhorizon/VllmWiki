# vllm-project/vllm#1312: vllm cutoff the output

| 字段 | 值 |
| --- | --- |
| Issue | [#1312](https://github.com/vllm-project/vllm/issues/1312) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm cutoff the output

### Issue 正文摘录

We deployed the Baichuan2_13B model based on the VLLM framework. However, response truncation often occurs when an interface is invoked, see the following figure. The max_tokens of the request parameter is sent to 2500. According to the output tokens statistics, the maximum value is not reached either. Do you know what the problem is? request: ![image](https://github.com/vllm-project/vllm/assets/27138295/11fbc08a-8c59-4754-86d4-df77d94cce63) response: ![image](https://github.com/vllm-project/vllm/assets/27138295/9b5933a8-c392-4822-94c8-bbd44bcf86e7)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vllm cutoff the output bug;stale We deployed the Baichuan2_13B model based on the VLLM framework. However, response truncation often occurs when an interface is invoked, see the following figure. The max_tokens of the r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm cutoff the output bug;stale We deployed the Baichuan2_13B model based on the VLLM framework. However, response truncation often occurs when an interface is invoked, see the following figure. The max_tokens of the r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
