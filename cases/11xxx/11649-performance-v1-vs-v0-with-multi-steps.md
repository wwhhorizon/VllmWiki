# vllm-project/vllm#11649: [Performance]: V1 vs V0 with multi-steps

| 字段 | 值 |
| --- | --- |
| Issue | [#11649](https://github.com/vllm-project/vllm/issues/11649) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: V1 vs V0 with multi-steps

### Issue 正文摘录

### Proposal to improve performance N/A ### Report of performance regression For V1: python -m vllm.entrypoints.openai.api_server --model NousResearch/Meta-Llama-3.1-8B-Instruct --tensor-parallel-size 8 --max-num-seqs 32 --max-model-len 4096 --disable-sliding-window --return-tokens-as-token-ids --port 8080 --enable-prefix-caching --enable-chunked-prefill --disable-log-requests --disable-log-stats For V0: python -m vllm.entrypoints.openai.api_server --model NousResearch/Meta-Llama-3.1-8B-Instruct --tensor-parallel-size 8 --max-num-seqs 32 --max-model-len 4096 --num-scheduler-steps 32 --multi-step-stream-outputs --disable-sliding-window --return-tokens-as-token-ids --port 8080 --enable-prefix-caching --enable-chunked-prefill --disable-log-requests --disable-log-stats run the following script: time curl -XPOST -s http://127.0.0.1:8080/v1/chat/completions -H 'content-type: application/json' -H 'Authorization: Bearer 1234' -d '{"model": "NousResearch/Meta-Llama-3.1-8B-Instruct", "messages": [{"role": "user", "content": "Explain in detail 5 important events of WW2."}], "stream": true, "logprobs": true, "temperature": 0.0, "seed": 42}' | grep 'data: ' | wc -l V1 result: 1545 real 0m6.946...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: V1 vs V0 with multi-steps performance;stale ### Proposal to improve performance N/A ### Report of performance regression For V1: python -m vllm.entrypoints.openai.api_server --model NousResearch/Meta-Llam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mance regression For V1: python -m vllm.entrypoints.openai.api_server --model NousResearch/Meta-Llama-3.1-8B-Instruct --tensor-parallel-size 8 --max-num-seqs 32 --max-model-len 4096 --disable-sliding-window --return-tok...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tale ### Proposal to improve performance N/A ### Report of performance regression For V1: python -m vllm.entrypoints.openai.api_server --model NousResearch/Meta-Llama-3.1-8B-Instruct --tensor-parallel-size 8 --max-num-s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Instruct", "messages": [{"role": "user", "content": "Explain in detail 5 important events of WW2."}], "stream": true, "logprobs": true, "temperature": 0.0, "seed": 42}' | grep 'data: ' | wc -l V1 result: 1545 real 0m6.9...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on For V1: python -m vllm.entrypoints.openai.api_server --model NousResearch/Meta-Llama-3.1-8B-Instruct --tensor-parallel-size 8 --max-num-seqs 32 --max-model-len 4096 --disable-sliding-window --return-tokens-as-token-i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
