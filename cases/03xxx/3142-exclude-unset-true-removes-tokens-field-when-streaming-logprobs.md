# vllm-project/vllm#3142: exclude_unset=True removes tokens field when streaming logprobs.

| 字段 | 值 |
| --- | --- |
| Issue | [#3142](https://github.com/vllm-project/vllm/issues/3142) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> exclude_unset=True removes tokens field when streaming logprobs.

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/54d3544784ff20e7038abf72793eaf734e727269/vllm/entrypoints/openai/serving_completion.py#L99 with `exclude_unset=True`. ``` data: {"id":"cmpl-6a6c465165c94d83bede2e6c8d33300c","created":12380229,"model":"google/gemma-7b-it","choices":[{"index":0,"text":"Hello","logprobs":{"top_logprobs":[{"Hello":-0.006023823 749274015}]},"finish_reason":null}]} data: {"id":"cmpl-6a6c465165c94d83bede2e6c8d33300c","created":12380229,"model":"google/gemma-7b-it","choices":[{"index":0,"text":"!","logprobs":{"top_logprobs":[{"!":-1.317667841911316," ,":-0.3176678419113159}]},"finish_reason":null}]} data: {"id":"cmpl-6a6c465165c94d83bede2e6c8d33300c","created":12380229,"model":"google/gemma-7b-it","choices":[{"index":0,"text":" 👋","logprobs":{"top_logprobs":[{"▁👋":-0.0000207422017 4108632}]},"finish_reason":null}]} data: {"id":"cmpl-6a6c465165c94d83bede2e6c8d33300c","created":12380229,"model":"google/gemma-7b-it","choices":[{"index":0,"text":"\n\n","logprobs":{"top_logprobs":[{"\n\n":-0.10709359496 831894}]},"finish_reason":"length"}]} data: {"id":"cmpl-6a6c465165c94d83bede2e6c8d33300c","created":12380229,"model":"google/gemma-7b-it","choices":[{"index":0,"text":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: data: {"id":"cmpl-6a6c465165c94d83bede2e6c8d33300c","created":12380229,"model":"google/gemma-7b-it","choices":[{"index":0,"text":"Hello","logprobs":{"top_logprobs":[{"Hello":-0.006023823 749274015}]},"finish_reason":nul...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: data: [DONE] ``` with `exclude_unset=False`. ``` curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{"model": "google/gemma-7b-it", "prompt": " user\nHello \n model\n", "max_tokens": 4, "s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: mpl-6a6c465165c94d83bede2e6c8d33300c","created":12380229,"model":"google/gemma-7b-it","choices":[{"index":0,"text":"Hello","logprobs":{"top_logprobs":[{"Hello":-0.006023823 749274015}]},"finish_reason":null}]}
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: o reason, `exclude_unset=False` is much more reasonable response for the request.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
