# vllm-project/vllm#16732: [Feature]: return graceful inference text input validation errors as part of output (without throwing an exception) - to enable skipping / handling bad examples after the processing of good ones

| 字段 | 值 |
| --- | --- |
| Issue | [#16732](https://github.com/vllm-project/vllm/issues/16732) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: return graceful inference text input validation errors as part of output (without throwing an exception) - to enable skipping / handling bad examples after the processing of good ones

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Originally posted at: - https://github.com/vllm-project/vllm/discussions/16730 ``` File "...", line ..., in model_outputs = model.generate( File "/home/inferencer/.local/lib/python3.10/site-packages/vllm/utils.py", line 1131, in inner return fn(*args, **kwargs) File "/home/inferencer/.local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 457, in generate self._validate_and_add_requests( File "/home/inferencer/.local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1317, in _validate_and_add_requests self._add_request( File "/home/inferencer/.local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1335, in _add_request self.llm_engine.add_request( File "/home/inferencer/.local/lib/python3.10/site-packages/vllm/v1/engine/llm_engine.py", line 186, in add_request request = self.processor.process_inputs(request_id, prompt, params, File "/home/inferencer/.local/lib/python3.10/site-packages/vllm/v1/engine/processor.py", line 209, in process_inputs self._validate_model_inputs(processed_inputs, lora_request) File "/home/inferencer/.local/lib/python3.10/site-packages/vllm/v1/engine/processor.py", line 308, in _validate...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: , line ..., in model_outputs = model.generate( File "/home/inferencer/.local/lib/python3.10/site-packages/vllm/utils.py", line 1131, in
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ipping / handling bad examples after the processing of good ones feature request;stale ### 🚀 The feature, motivation and pitch Originally posted at: - https://github.com/vllm-project/vllm/discussions/16730 ``` File "......
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
