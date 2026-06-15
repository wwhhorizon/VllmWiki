# vllm-project/vllm#15705: [Bug]: Qwen2.5: Sliding window for some but all layers is not supported. This model uses sliding window but `max_window_layers` = 28 is less than `num_hidden_layers` = 28. Please open an issue to discuss this feature.

| 字段 | 值 |
| --- | --- |
| Issue | [#15705](https://github.com/vllm-project/vllm/issues/15705) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5: Sliding window for some but all layers is not supported. This model uses sliding window but `max_window_layers` = 28 is less than `num_hidden_layers` = 28. Please open an issue to discuss this feature.

### Issue 正文摘录

### Your current environment For some reason, I can't run `collect_env.py` in my env. Sorry about that. :) But I'm sure this problem has nothing to do with the environment. My envinronment: vllm: 0.7.3 cuda: 12.4 transformers: 4.50.1 trl: 0.15.2 ### 🐛 Describe the bug My code using vllm: ```python llm = LLM(model=model_name_or_path, dtype="float16", tensor_parallel_size=tensor_parallel_size, max_num_seqs=batch_size, max_model_len=None if max_model_len == -1 else max_model_len, gpu_memory_utilization=0.9) sampling_params = SamplingParams(temperature=temperature, max_tokens=max_tokens) outputs = llm.generate(prompts, sampling_params) ``` When I want to generate response from `Qwen2.5-7B-Instruct`, I encounter `ValueError` raised by [this line](https://github.com/vllm-project/vllm/blob/fd5fd2690275e90865023a0bcac0047ecb3f3897/vllm/model_executor/models/qwen2.py#L274): ``` Sliding window for some but all layers is not supported. This model uses sliding window but `max_window_layers` = 28 is less than `num_hidden_layers` = 28. Please open an issue to discuss this feature. ``` The model I used is fine-tuned using `trl` library and flash-attention 2, with sliding window enabled. Looks li...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: g vllm: ```python llm = LLM(model=model_name_or_path, dtype="float16", tensor_parallel_size=tensor_parallel_size, max_num_seqs=batch_size, max_model_len=None if max_model_len == -1 else max_model_len, gpu_memory_utiliz
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m has nothing to do with the environment. My envinronment: vllm: 0.7.3 cuda: 12.4 transformers: 4.50.1 trl: 0.15.2 ### 🐛 Describe the bug My code using vllm: ```python llm = LLM(model=model_name_or_path, dtype="float16"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5: Sliding window for some but all layers is not supported. This model uses sliding window but `max_window_layers` = 28 is less than `num_hidden_layers` = 28. Please open an issue to discuss this feature. b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: eqs=batch_size, max_model_len=None if max_model_len == -1 else max_model_len, gpu_memory_utilization=0.9) sampling_params = SamplingParams(temperature=temperature, max_tokens=max_tokens) outputs = llm.generate(prompts,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
