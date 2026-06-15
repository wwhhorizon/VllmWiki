# vllm-project/vllm#5250: [Misc]: Why prometheus metric vllm:request_success_total doubles the value?

| 字段 | 值 |
| --- | --- |
| Issue | [#5250](https://github.com/vllm-project/vllm/issues/5250) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Why prometheus metric vllm:request_success_total doubles the value?

### Issue 正文摘录

### Anything you want to discuss about vllm. I am using the following script to display the vllm metric:request_success_total: `sum(increase(vllm:request_success_total{model_name="$MODEL_NAME"}[$__rate_interval])) by (finished_reason)` But each of my queries in the model is displayed on the graph in the amount of "2". It seems that the value is incremented twice by mistake with a single request. ![image](https://github.com/vllm-project/vllm/assets/21113432/b5b686de-02c8-416d-8797-4d368d00790b)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m metric:request_success_total: `sum(increase(vllm:request_success_total{model_name="$MODEL_NAME"}[$__rate_interval])) by (finished_reason)` But each of my queries in the model is displayed on the graph in the amount of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Why prometheus metric vllm:request_success_total doubles the value? bug;good first issue ### Anything you want to discuss about vllm. I am using the following script to display the vllm metric:request_success_to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
