# vllm-project/vllm#13087: [Bug]: The first streaming chunks are empty when the stop field is set

| 字段 | 值 |
| --- | --- |
| Issue | [#13087](https://github.com/vllm-project/vllm/issues/13087) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The first streaming chunks are empty when the stop field is set

### Issue 正文摘录

### Your current environment - vllm==0.6.6.post1 - FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 - Python 3.9 ### 🐛 Describe the bug When I set the stop arg to anything other than None (which is the default) I got the first streaming chunks as null!! ``` data: {"id":"chatcmpl-e4eb908a00044330868ed9072a59526a","object":"chat.completion.chunk","created":1737893394,"model":"ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-e4eb908a00044330868ed9072a59526a","object":"chat.completion.chunk","created":1737893394,"model":"ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-e4eb908a00044330868ed9072a59526a","object":"chat.completion.chunk","created":1737893394,"model":"ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-e4eb908a00044330868ed9072a59526a","object":"chat.completion.chunk","created":1737893394,"model":"ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-IN...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug;stale ### Your current environment - vllm==0.6.6.post1 - FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 - Python 3.9 ### 🐛 Describe the bug When I set the stop arg to anything other than None (which is the default) I go...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 868ed9072a59526a","object":"chat.completion.chunk","created":1737893394,"model":"ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: created":1737893394,"model":"ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-e4eb908a000443...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ug]: The first streaming chunks are empty when the stop field is set bug;stale ### Your current environment - vllm==0.6.6.post1 - FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 - Python 3.9 ### 🐛 Describe the bug When I se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
