# vllm-project/vllm#9342: [Bug]: vllm crashes when preemption of priority scheduling is triggered on vllm-0.6.3.dev173+g36ea7907.d20241011

| 字段 | 值 |
| --- | --- |
| Issue | [#9342](https://github.com/vllm-project/vllm/issues/9342) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm crashes when preemption of priority scheduling is triggered on vllm-0.6.3.dev173+g36ea7907.d20241011

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As I mentioned in https://github.com/vllm-project/vllm/issues/9272, even if the priority is propagated successfully, vllm always crashes as long as preemption happens. I just tested with vllm-0.6.3.dev173+g36ea7907.d20241011. The only change I made is following fix and some logs: https://github.com/vllm-project/vllm/pull/9277 Could you please help to check it? Reproduce procedure: 1. Start vllm: ``` python3 -m vllm.entrypoints.openai.api_server --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \ --host 0.0.0.0 --port 8080 --seed 42 --trust-remote-code --scheduling-policy priority \ --tensor-parallel-size 2 --max-num-seqs 10 --enable_chunked_prefill False ``` 2. Use openai client to make a 15 concurrent load. 3. Use another openai client to send some requests with priority -100. 4. As long as preemption is triggered, vllm crashes: ``` INFO 10-11 06:51:31 engine.py:292] Added request chat-29ccd21f37fb4a8ea96c1c8c189a6a49. INFO 10-11 06:51:31 engine.py:294] tonyaw:Added request -100. INFO 10-11 06:51:31 scheduler.py:1025] tonyaw: len(prefills.seq_groups) = 0 INFO 10-11 06:51:31 scheduler...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ity scheduling is triggered on vllm-0.6.3.dev173+g36ea7907.d20241011 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As I mentioned in https://github.com/vllm-project/vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: vllm: ``` python3 -m vllm.entrypoints.openai.api_server --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \ --host 0.0.0.0 --port 8080 --seed 42 --trust-remote-code --scheduling-policy priority \ --tensor-para...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ev173+g36ea7907.d20241011 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As I mentioned in https://github.com/vllm-project/vllm/issues/9272, even if the priority is pro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: successfully, vllm always crashes as long as preemption happens. I just tested with vllm-0.6.3.dev173+g36ea7907.d20241011. The only change I made is following fix and some logs: https://github.com/vllm-project/vllm/pull...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: hub.com/vllm-project/vllm/pull/9277 Could you please help to check it? Reproduce procedure: 1. Start vllm: ``` python3 -m vllm.entrypoints.openai.api_server --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
