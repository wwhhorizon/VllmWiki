# vllm-project/vllm#14233: [Bug]: ValueError: The vocabulary does not allow us to build a sequence that matches the input regex

| 字段 | 值 |
| --- | --- |
| Issue | [#14233](https://github.com/vllm-project/vllm/issues/14233) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: The vocabulary does not allow us to build a sequence that matches the input regex

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using guided decoding with choices it gives below error. ValueError: The vocabulary does not allow us to build a sequence that matches the input regex model_id = "../../Mistral-Small-Instruct-2409" llm = LLM(model=model_id, quantization="bitsandbytes", load_format="bitsandbytes", # dtype='auto', max_lora_rank=32, max_model_len = 5192+64, gpu_memory_utilization=0.65, tensor_parallel_size=1, enforce_eager=True) for prompt in tqdm(list(zip(prompts))): params = SamplingParams(temperature=0.0, max_tokens=64, stop=[tokenizer.eos_token, '[INST]', '[/INST]']) guided_decoding_params = GuidedDecodingParams(choice=inv_list) params.guided_decoding = guided_decoding_params ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: = "../../Mistral-Small-Instruct-2409" llm = LLM(model=model_id, quantization="bitsandbytes", load_format="bitsandbytes", # dtype='auto', max_lora_rank=32, max_model_len = 5192+64, gpu_memory_utilization=0.65, tensor_par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: build a sequence that matches the input regex model_id = "../../Mistral-Small-Instruct-2409" llm = LLM(model=model_id, quantization="bitsandbytes", load_format="bitsandbytes", # dtype='auto', max_lora_rank=32, max_model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lary does not allow us to build a sequence that matches the input regex model_id = "../../Mistral-Small-Instruct-2409" llm = LLM(model=model_id, quantization="bitsandbytes", load_format="bitsandbytes", # dtype='auto', m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: ValueError: The vocabulary does not allow us to build a sequence that matches the input regex bug;stale ### Your current environment ### 🐛 Describe the bug When using guided decoding with choices it gives below e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: y does not allow us to build a sequence that matches the input regex bug;stale ### Your current environment ### 🐛 Describe the bug When using guided decoding with choices it gives below error. ValueError: The vocabulary...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
