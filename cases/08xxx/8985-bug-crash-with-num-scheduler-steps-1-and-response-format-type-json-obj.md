# vllm-project/vllm#8985: [Bug]: Crash with num-scheduler-steps > 1 and response_format type json object

| 字段 | 值 |
| --- | --- |
| Issue | [#8985](https://github.com/vllm-project/vllm/issues/8985) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash with num-scheduler-steps > 1 and response_format type json object

### Issue 正文摘录

### Your current environment vllm container v0.6.2 (vllm/vllm-openai:v0.6.2) Models: LLama-3-70b-Instruct, LLama-3-8b-Instruct, Qwen-2.5-32b-Instruct GPUs: A100, A30 ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using --num-scheduler-steps 8 and request with "response_format": { "type": "json_object" }, vllm raise an error and crash after that. The error log: ``` Compiling FSM index for all state transitions: 100%|██████████████████████| 3/3 [00:02<00:00, 1.14it/s] INFO 10-01 02:39:08 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. ERROR 10-01 02:39:08 engine.py:157] AssertionError('Logits Processors are not supported in multi-step decoding') ERROR 10-01 02:39:08 engine.py:157] Traceback (most recent call last): ERROR 10-01 02:39:08 engine.py:157] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 155, in start ERROR 10-01 02:39:08 engine.py:157] self.run_engine_loop() ERROR 10-01 02:39:08 engine.py:157] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/...

## 现有链接修复摘要

#9892 [Bugfix][Frontend] Reject guided decoding in multistep mode

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Crash with num-scheduler-steps > 1 and response_format type json object bug ### Your current environment vllm container v0.6.2 (vllm/vllm-openai:v0.6.2) Models: LLama-3-70b-Instruct, LLama-3-8b-Instruct, Qwen-2.5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: LLama-3-70b-Instruct, LLama-3-8b-Instruct, Qwen-2.5-32b-Instruct GPUs: A100, A30 ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using --num-scheduler-steps 8 and request with "response_format": { "type"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Crash with num-scheduler-steps > 1 and response_format type json object bug ### Your current environment vllm container v0.6.2 (vllm/vllm-openai:v0.6.2) Models: LLama-3-70b-Instruct, LLama-3-8b-Instruct, Qwen-2.5...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [00:02<00:00, 1.14it/s] INFO 10-01 02:39:08 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/routing...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9892](https://github.com/vllm-project/vllm/pull/9892) | closes_keyword | 0.95 | [Bugfix][Frontend] Reject guided decoding in multistep mode | FIX #8985 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
