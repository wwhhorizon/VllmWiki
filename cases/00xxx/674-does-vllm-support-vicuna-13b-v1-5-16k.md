# vllm-project/vllm#674: Does vllm support vicuna-13b-v1.5-16k ?

| 字段 | 值 |
| --- | --- |
| Issue | [#674](https://github.com/vllm-project/vllm/issues/674) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Does vllm support vicuna-13b-v1.5-16k ?

### Issue 正文摘录

The model seems to loop in its outputs I'm using: vllm 0.1.2 transformers 4.31.0 launched through the FastChat (commit [b0462aa](https://github.com/lm-sys/FastChat/commit/b0462aa6f028af2065a1691e83a563eccc43ea20) )/vllm wrapper (worker) Any idea on what's going on? Thanks.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Does vllm support vicuna-13b-v1.5-16k ? feature request The model seems to loop in its outputs I'm using: vllm 0.1.2 transformers 4.31.0 launched through the FastChat (commit [b0462aa](https://github.com/lm-sys/FastChat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Does vllm support vicuna-13b-v1.5-16k ? feature request The model seems to loop in its outputs I'm using: vllm 0.1.2 transformers 4.31.0 launched through the FastChat (commit [b0462aa](https://github.com/lm-sys/FastChat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
