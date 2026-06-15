# vllm-project/vllm#17738: [Bug]: Interrupting inference with ctrl-c causes future requests to hang

| 字段 | 值 |
| --- | --- |
| Issue | [#17738](https://github.com/vllm-project/vllm/issues/17738) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Interrupting inference with ctrl-c causes future requests to hang

### Issue 正文摘录

Has happened for quite some time, and seems to happen with most models (like Qwen 3 8B) ### 🐛 Describe the bug ```python llm = vllm.LLM(model="Qwen/Qwen3-8B") for i in range(100): llm.generate(["bees"]) ``` interrupt with ctrl-c and observe later calls to ```python llm.generate(["bees"]) ``` hang and never finish. It should ideally be able to be interrupted with ctrl-c and still run on future calls, like any other python program. It seems to be something about entering an inconsistent state. I can workaround this by listening for a key to be pressed and then throwing an exception to break, but it would be nice to not have to rely on that. I found https://github.com/vllm-project/vllm/issues/17273 which is sorta relevant. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ug;stale Has happened for quite some time, and seems to happen with most models (like Qwen 3 8B) ### 🐛 Describe the bug ```python llm = vllm.LLM(model="Qwen/Qwen3-8B") for i in range(100): llm.generate(["bees"]) ``` int...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Interrupting inference with ctrl-c causes future requests to hang bug;stale Has happened for quite some time, and seems to happen with most models (like Qwen 3 8B) ### 🐛 Describe the bug ```python llm = vllm.LLM(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
