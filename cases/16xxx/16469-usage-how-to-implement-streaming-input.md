# vllm-project/vllm#16469: [Usage]: How to implement Streaming Input

| 字段 | 值 |
| --- | --- |
| Issue | [#16469](https://github.com/vllm-project/vllm/issues/16469) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to implement Streaming Input

### Issue 正文摘录

### Your current environment Suppose the situation of dual talking, where each infer step needs the previous step's token and an extra token from outside(prepared from user's audio trunk). I want to add a outside-input-generator in sampling params's extra_args, so I can do some logic in sampler to produce a combined token for next step. but I encounted this error: ``` Traceback (most recent call last): File "/var/lib/container/zhanyu/llm/dual-talking/tests/qwen_vllm_test.py", line 66, in main(args) File "/var/lib/container/zhanyu/llm/dual-talking/tests/qwen_vllm_test.py", line 58, in main process_requests(engine, test_prompts) File "/var/lib/container/zhanyu/llm/dual-talking/tests/qwen_vllm_test.py", line 38, in process_requests engine.add_request(str(request_id), prompt, sampling_params) File "/var/lib/container/zhanyu/llm/vllm/vllm/v1/engine/llm_engine.py", line 198, in add_request self.engine_core.add_request(request) File "/var/lib/container/zhanyu/llm/vllm/vllm/v1/engine/core_client.py", line 514, in add_request self._send_input(EngineCoreRequestType.ADD, request) File "/var/lib/container/zhanyu/llm/vllm/vllm/v1/engine/core_client.py", line 498, in _send_input msg = (request_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to implement Streaming Input usage;stale ### Your current environment Suppose the situation of dual talking, where each infer step needs the previous step's token and an extra token from outside(prepared fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ent call last): File "/var/lib/container/zhanyu/llm/dual-talking/tests/qwen_vllm_test.py", line 66, in main(args) File "/var/lib/container/zhanyu/llm/dual-talking/tests/qwen_vllm_test.py", line 58, in main process_reque...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: st recent call last): File "/var/lib/container/zhanyu/llm/dual-talking/tests/qwen_vllm_test.py", line 66, in main(args) File "/var/lib/container/zhanyu/llm/dual-talking/tests/qwen_vllm_test.py", line 58, in main process...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
