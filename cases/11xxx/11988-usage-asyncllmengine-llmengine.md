# vllm-project/vllm#11988: [Usage]: AsyncLLMEngine比离线的LLMEngine推理速度更慢

| 字段 | 值 |
| --- | --- |
| Issue | [#11988](https://github.com/vllm-project/vllm/issues/11988) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: AsyncLLMEngine比离线的LLMEngine推理速度更慢

### Issue 正文摘录

### Your current environment vllm-0.6.5 ### How would you like to use vllm ```python request_id = str(uuid.uuid4().hex) contents_generator = llm.generate( model_inputs, sampling_params, request_id=request_id, lora_request=LoRARequest( lora_name, lora_id, os.path.join(hps.lora_dir, lora_name) ) ) final_output = None async for request_output in contents_generator: final_output = request_output print(final_output.outputs[0].text) contents = final_output.outputs[0].text ``` 使用AsyncLLMEngine进行推理时，花费时间cost time: 6.88584303855896 ```python contents = llm.generate( model_inputs, sampling_params, lora_request=LoRARequest( lora_name, lora_id, os.path.join(hps.lora_dir, lora_name) ) ) contents = [content.outputs[0].text for content in contents] ``` 使用LLMEngine进行推理时，花费时间cost time2.119072675704956 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 956 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d = str(uuid.uuid4().hex) contents_generator = llm.generate( model_inputs, sampling_params, request_id=request_id, lora_request=LoRARequest( lora_name, lora_id, os.path.join(hps.lora_dir, lora_name) ) ) final_output = N...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: environment vllm-0.6.5 ### How would you like to use vllm ```python request_id = str(uuid.uuid4().hex) contents_generator = llm.generate( model_inputs, sampling_params, request_id=request_id, lora_request=LoRARequest( l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
