# vllm-project/vllm#11092: [Usage]: Why is QWen VL's dynamic loading of LoRA so slow in execution?

| 字段 | 值 |
| --- | --- |
| Issue | [#11092](https://github.com/vllm-project/vllm/issues/11092) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why is QWen VL's dynamic loading of LoRA so slow in execution?

### Issue 正文摘录

### Your current environment Environment： vllm==0.6.4.post1 A800 Performance： Without loading LoRA, it averages 1 second; with LoRA loading, it averages 3 seconds ### How would you like to use vllm request_id = str(uuid.uuid4().hex) sampling_params = SamplingParams(max_tokens=1024) lora_request = LoRARequest("1234567", int("1234567"), "/qwenvl/sft/output/qwen2-vl-7b-instruct/v2-20241202-150642/checkpoint-280") result_generator = engine_vllm.generate( prompt=llm_inputs, sampling_params=sampling_params, request_id=request_id, lora_request=lora_request ) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Why is QWen VL's dynamic loading of LoRA so slow in execution? usage ### Your current environment Environment： vllm==0.6.4.post1 A800 Performance： Without loading LoRA, it averages 1 second; with LoRA loading,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: LoRA loading, it averages 3 seconds ### How would you like to use vllm request_id = str(uuid.uuid4().hex) sampling_params = SamplingParams(max_tokens=1024) lora_request = LoRARequest("1234567", int("1234567"), "/qwenvl/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
