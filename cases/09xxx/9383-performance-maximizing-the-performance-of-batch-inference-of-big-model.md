# vllm-project/vllm#9383: [Performance]: Maximizing the performance of batch inference of big models on vllm 0.6.3 

| 字段 | 值 |
| --- | --- |
| Issue | [#9383](https://github.com/vllm-project/vllm/issues/9383) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Maximizing the performance of batch inference of big models on vllm 0.6.3 

### Issue 正文摘录

### Misc discussion on performance Hi all, I'm having trouble with maximizing the performance of batch inference of big models on vllm 0.6.3 (Llama 3.1 70b, 405b, Mistral large) My command to run the server is this: "python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-Large-Instruct-2407 --tensor-parallel-size 4 --guided-decoding-backend lm-format-enforcer --enable-chunked-prefill --enable-prefix-caching " Specifically, I'm running on 4xA100 80GB hardware I launch requests with a large min_tokens and max_tokens value (30,000) I do n = 8 to get 8 responses and to run them in parallel It appears that despite the same min and max token values, that my Avg generation throughput starts very high (~100+) and scales down slowly overtime to a crawl (I was seeing 4 tokens/s before I stopped the generation with mistral large). This is making it take a prohibitively long time to get outputs. I used to have max_tokens set to a very high value but min_tokens set low, and the model usually gave short outputs but was able to consistently keep high tok/s I need to get outputs in a reasonable time. Setting n lower cripples my t/s and this doesn't appear to be a GPU memory issue...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Performance]: Maximizing the performance of batch inference of big models on vllm 0.6.3 performance;stale ### Misc discussion on performance Hi all, I'm having trouble with maximizing the performance of batch inference...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: m-format-enforcer --enable-chunked-prefill --enable-prefix-caching " Specifically, I'm running on 4xA100 80GB hardware I launch requests with a large min_tokens and max_tokens value (30,000) I do n = 8 to get 8 response...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: performance of batch inference of big models on vllm 0.6.3 performance;stale ### Misc discussion on performance Hi all, I'm having trouble with maximizing the performance of batch inference of big models on vllm 0.6.3 (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hunked-prefill --enable-prefix-caching " Specifically, I'm running on 4xA100 80GB hardware I launch requests with a large min_tokens and max_tokens value (30,000) I do n = 8 to get 8 responses and to run them in paralle...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s that despite the same min and max token values, that my Avg generation throughput starts very high (~100+) and scales down slowly overtime to a crawl (I was seeing 4 tokens/s before I stopped the generation with mistr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
