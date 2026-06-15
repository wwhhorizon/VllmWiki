# vllm-project/vllm#13084: [Performance]:  Why Does the TPOT Increase with the Request Rate Increase?

| 字段 | 值 |
| --- | --- |
| Issue | [#13084](https://github.com/vllm-project/vllm/issues/13084) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:  Why Does the TPOT Increase with the Request Rate Increase?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I get a question. Why Does the TPOT Increase when the Request Rate Increase? Here is the parameter: "args": [ "--backend", "vllm", "--dataset-name", "sonnet", "--sonnet-input-len", "1024", "--sonnet-output-len", "6", "--sonnet-prefix-len", "50", "--num-prompts", "20", "--request-rate", "2", ], I checked the code and confirm that no request is scheduled. But TPOT(and ITL) increased when request-rate changes from 2 to 4 especially P99 TPOT. Besides，num-prompts influence TPOT too. When num-prompts changes from 20 to 200, ITL get unstable and fluctuated. Thus P99 TPOT get dramatically big. What other factors affect ITL? ### Your current environment (if you think it is necessary) _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Why Does the TPOT Increase with the Request Rate Increase? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on per...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Why Does the TPOT Increase with the Request Rate Increase? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on per...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: he Request Rate Increase? Here is the parameter: "args": [ "--backend", "vllm", "--dataset-name", "sonnet", "--sonnet-input-len", "1024", "--sonnet-output-len", "6", "--sonnet-prefix-len", "50", "--num-prompts", "20", "
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d. But TPOT(and ITL) increased when request-rate changes from 2 to 4 especially P99 TPOT. Besides，num-prompts influence TPOT too. When num-prompts changes from 20 to 200, ITL get unstable and fluctuated. Thus P99 TPOT g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
