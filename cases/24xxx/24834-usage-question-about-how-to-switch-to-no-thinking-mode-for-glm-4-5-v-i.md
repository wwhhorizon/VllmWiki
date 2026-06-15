# vllm-project/vllm#24834: [Usage]: Question about how to switch to no-thinking mode for GLM-4.5 V in vllm offline inference

| 字段 | 值 |
| --- | --- |
| Issue | [#24834](https://github.com/vllm-project/vllm/issues/24834) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Question about how to switch to no-thinking mode for GLM-4.5 V in vllm offline inference

### Issue 正文摘录

### Your current environment GPUs: 8× A100 80GB vllm: 0.10.1 ### How would you like to use vllm Hi team, thanks for vLLM! I’m running offline inference with GLM-4.5V (and the FP8 variant) via vllm.LLM.generate. I want to disable the model’s “Thinking Mode”. In the OpenAI-compatible server path, I know we can pass: ```extra_body={"chat_template_kwargs": {"enable_thinking": False}}```…but I’m not sure what’s the equivalent for offline inference (LLM.generate) where there is no extra_body. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llm offline inference usage;stale ### Your current environment GPUs: 8× A100 80GB vllm: 0.10.1 ### How would you like to use vllm Hi team, thanks for vLLM! I’m running offline inference with GLM-4.5V (and the FP8 varian...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: , thanks for vLLM! I’m running offline inference with GLM-4.5V (and the FP8 variant) via vllm.LLM.generate. I want to disable the model’s “Thinking Mode”. In the OpenAI-compatible server path, I know we can pass: ```ext...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e can pass: ```extra_body={"chat_template_kwargs": {"enable_thinking": False}}```…but I’m not sure what’s the equivalent for offline inference (LLM.generate) where there is no extra_body. ### Before submitting a new iss...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -4.5V (and the FP8 variant) via vllm.LLM.generate. I want to disable the model’s “Thinking Mode”. In the OpenAI-compatible server path, I know we can pass: ```extra_body={"chat_template_kwargs": {"enable_thinking": Fals...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: switch to no-thinking mode for GLM-4.5 V in vllm offline inference usage;stale ### Your current environment GPUs: 8× A100 80GB vllm: 0.10.1 ### How would you like to use vllm Hi team, thanks for vLLM! I’m running offlin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
