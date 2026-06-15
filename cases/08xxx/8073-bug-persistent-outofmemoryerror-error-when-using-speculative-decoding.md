# vllm-project/vllm#8073: [Bug]: Persistent OutOfMemoryError error when using speculative decoding 

| 字段 | 值 |
| --- | --- |
| Issue | [#8073](https://github.com/vllm-project/vllm/issues/8073) |
| 状态 | closed |
| 标签 | bug;speculative-decoding;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Persistent OutOfMemoryError error when using speculative decoding 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I get an out of memory error when using speculative decoding (SD). This happens in the middle of generation or after several batches completed successfully. I have tried reducing `max_model_len`, `max_num_batched_tokens` and `gpu_memory_utilization`, but to no avail. **Usage** ```python llm = LLM("nvidia/Llama-3.1-Minitron-4B-Width-Base", enable_prefix_caching=True, block_size=3, gpu_memory_utilization=0.8, max_num_batched_tokens=11000, max_model_len=11000, speculative_model="ibm-fms/llama3-8b-accelerator", num_speculative_tokens=1, use_v2_block_manager=True) sampling_params = SamplingParams(temperature=0.5, top_p=0.2, max_tokens=1) formatted_prompts = ["array of len 10000 to 400000, each around 100-200 tokens"] from outlines import models, generate model = models.VLLM(llm) generator = generate.choice(model, ["yes", "no"]) predictions = generator(formatted_prompts, sampling_params=sampling_params) ``` In contrast, when SD is disabled, runs always complete even at high max_model_len`, `max_num_batched_tokens` and `gpu_memory_utilization`. ```python llm = LLM("nvidia/Llama-3.1-Minitron-4B-Width-Base", enable_prefix_caching=True, bl...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Persistent OutOfMemoryError error when using speculative decoding bug;speculative-decoding;stale ### Your current environment ### 🐛 Describe the bug I get an out of memory error when using speculative decoding (S...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ation or after several batches completed successfully. I have tried reducing `max_model_len`, `max_num_batched_tokens` and `gpu_memory_utilization`, but to no avail. **Usage** ```python llm = LLM("nvidia/Llama-3.1-Minit...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: M("nvidia/Llama-3.1-Minitron-4B-Width-Base", enable_prefix_caching=True, block_size=3, gpu_memory_utilization=0.8, max_num_batched_tokens=11000, max_model_len=11000, speculative_model="ibm-fms/llama3-8b-accelerator", nu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: fter several batches completed successfully. I have tried reducing `max_model_len`, `max_num_batched_tokens` and `gpu_memory_utilization`, but to no avail. **Usage** ```python llm = LLM("nvidia/Llama-3.1-Minitron-4B-Wid...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _v2_block_manager=True) ``` **Error trace** ```python OutOfMemoryError: CUDA out of memory. Tried to allocate 1.86 GiB. GPU 0 has a total capacity of 21.99 GiB of which 337.38 MiB is free. Process 30125 has 21.64 GiB me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
