# vllm-project/vllm#2650: Proposal: Adding more Prometheus metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#2650](https://github.com/vllm-project/vllm/issues/2650) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Proposal: Adding more Prometheus metrics

### Issue 正文摘录

Once #2316 is merged, I'm willing to contribute the following metrics which I believe would be helpful for monitoring the usage of vllm. | # | Metric | Type | Labels | Description | | --- | --- | --- | --- | --- | | 1. | vllm:request_success | Counter | finish_reason=`stop\|length` | Count of successfully processed requests. | | 2. | vllm:request_params_max_tokens | Histogram | | Value of max_tokens request parameter. | | 3. | vllm:request_params_n | Histogram | | Value of n request parameter. | | 4. | vllm:request_total_tokens | Histogram | | Total sequence length of request (input tokens + generated tokens). | | 5. | vllm:request_prompt_tokens | Histogram | | Number of prefill tokens processed. | | 6. | vllm:request_generation_tokens | Histogram | | Number of generation tokens processed. | **Notes:** metrics 5. and 6. already exist but as counters (`vllm:prompt_tokens_total` and `vllm:generation_tokens_total`). I think a Histogram is more meaningful. For backward compatibility, we can keep both types (counters and histograms). Please let me know what you think.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ype | Labels | Description | | --- | --- | --- | --- | --- | | 1. | vllm:request_success | Counter | finish_reason=`stop\|length` | Count of successfully processed requests. | | 2. | vllm:request_params_max_tokens | His...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
