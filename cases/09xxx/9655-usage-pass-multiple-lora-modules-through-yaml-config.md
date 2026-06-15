# vllm-project/vllm#9655: [Usage]: Pass multiple LoRA modules through YAML config

| 字段 | 值 |
| --- | --- |
| Issue | [#9655](https://github.com/vllm-project/vllm/issues/9655) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Pass multiple LoRA modules through YAML config

### Issue 正文摘录

### How would you like to use vllm I would like to pass multiple LoRA modules to the vLLM engine, but currently I'm receiving error while parsing the `lora_modules` property. The `LoRAParserAction` class receives a `Sequence[str]` in case you want to use multiple LoRA modules. I have a YAML config file in which I declare the vLLM engine arguments, like this: ``` model: ai-models/Meta-Llama-3.1-8B-Instruct-rev-5206a32 tokenizer_mode: auto dtype: half lora_modules: "ai-models/adv_perizia_exp7_run6=ai-models/adv_perizia_exp7_run6" max_num_batched_tokens: 32768 max_num_seqs: 192 gpu_memory_utilization: 0.95 tensor_parallel_size: max_model_len: 32768 ``` In that way (`name=path` for the LoRA module), all works and I'm able to perform inference with LoRA (I set `enable_lora` argument later in the code, not in the YAML file). Now I would like to pass multiple `lora_modules`, but I'm receiving parsing error in every different ways I tried: `lora_modules: "ai-models/adv_perizia_exp7_run6=ai-models/adv_perizia_exp7_run6 ai-models/perizia_exp7_run3=ai-models/perizia_exp7_run3"` (blanks space between LoRA modules) ``` lora_modules: - "ai-models/adv_perizia_exp7_run6=ai-models/adv_perizia_exp7...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Pass multiple LoRA modules through YAML config usage;stale ### How would you like to use vllm I would like to pass multiple LoRA modules to the vLLM engine, but currently I'm receiving error while parsing the `...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: l: ai-models/Meta-Llama-3.1-8B-Instruct-rev-5206a32 tokenizer_mode: auto dtype: half lora_modules: "ai-models/adv_perizia_exp7_run6=ai-models/adv_perizia_exp7_run6" max_num_batched_tokens: 32768 max_num_seqs: 192 gpu_me...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Pass multiple LoRA modules through YAML config usage;stale ### How would you like to use vllm I would like to pass multiple LoRA modules to the vLLM engine, but currently I'm receiving error while parsing the `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
