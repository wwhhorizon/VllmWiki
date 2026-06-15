# vllm-project/vllm#11621: [Usage]: Can AsyncEngineArgs load multiple lora modules？

| 字段 | 值 |
| --- | --- |
| Issue | [#11621](https://github.com/vllm-project/vllm/issues/11621) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can AsyncEngineArgs load multiple lora modules？

### Issue 正文摘录

### Your current environment `vllm==0.6.5` ### How would you like to use vllm I only know loading a lora module example in online API is: ``` lora_request = LoRARequest( lora_name="glm4-lora", lora_int_id=1, lora_local_path=LORA_PATH, ) async for output in engine.generate(inputs=inputs, sampling_params=sampling_params, request_id=f"{time.time()}", lora_request=lora_request): (...) ``` If I have other lora modules, such as lora2, lora3, can I load them together with glm4-lora? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Can AsyncEngineArgs load multiple lora modules？ usage;stale ### Your current environment `vllm==0.6.5` ### How would you like to use vllm I only know loading a lora module example in online API is: ``` lora_req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ra? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
