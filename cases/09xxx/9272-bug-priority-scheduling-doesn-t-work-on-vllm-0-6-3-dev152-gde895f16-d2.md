# vllm-project/vllm#9272: [Bug]: priority scheduling doesn't work on vllm-0.6.3.dev152+gde895f16.d20241010

| 字段 | 值 |
| --- | --- |
| Issue | [#9272](https://github.com/vllm-project/vllm/issues/9272) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: priority scheduling doesn't work on vllm-0.6.3.dev152+gde895f16.d20241010

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It looks like priority sent by client isn't passed from multiprocessing/engine.py to vllm.engine.llm_engine.LLMEngine correctly. And it leads to priority can't work: https://github.com/vllm-project/vllm/blob/94bf9ae4e9b8199636668ccbe4dabcdc3b9e5ae6/vllm/engine/multiprocessing/engine.py#L279C13-L279C24 ```python self.engine.add_request( request_id=request_id, prompt=request.prompt, params=request.params, lora_request=request.lora_request, trace_headers=request.trace_headers, prompt_adapter_request=request.prompt_adapter_request) ### <<< priority=request.priority) is missed. ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .6.3.dev152+gde895f16.d20241010 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It looks like priority sent by client isn't passed from multiprocessing/engine.py to vllm.engin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ocessing/engine.py#L279C13-L279C24 ```python self.engine.add_request( request_id=request_id, prompt=request.prompt, params=request.params, lora_request=request.lora_request, trace_headers=request.trace
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
