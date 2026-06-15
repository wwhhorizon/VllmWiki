# vllm-project/vllm#13464: [Bug]: Memory leak in 0.6 and 0.7 when setting "max_tokens=1"

| 字段 | 值 |
| --- | --- |
| Issue | [#13464](https://github.com/vllm-project/vllm/issues/13464) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Memory leak in 0.6 and 0.7 when setting "max_tokens=1"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug from vllm import LLM, SamplingParams llm=LLM(model='qwen/Qwen2.5-0.5B-Instruct', trust_remote_code=True) sampling_params = SamplingParams(max_tokens=1) while True: result = llm.generate("Hello world, ", sampling_params) pass pass ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug from vllm import LLM, SamplingParams llm=LLM(model='qwen/Qwen2.5-0.5B-Instruct', trust_remote_code=True) sampling_params = SamplingParams(max_tokens=1) while True: result = llm.generate("Hello wor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stale ### Your current environment ### 🐛 Describe the bug from vllm import LLM, SamplingParams llm=LLM(model='qwen/Qwen2.5-0.5B-Instruct', trust_remote_code=True) sampling_params = SamplingParams(max_tokens=1) while Tru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ass ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Memory leak in 0.6 and 0.7 when setting "max_tokens=1" bug;stale ### Your current environment ### 🐛 Describe the bug from vllm import LLM, SamplingParams llm=LLM(model='qwen/Qwen2.5-0.5B-Instruct', trust_remote_c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
