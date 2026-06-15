# vllm-project/vllm#30631: [Bug]: GPU has redundant outputs when running Qwen3-Next-MTP in batched inferring.

| 字段 | 值 |
| --- | --- |
| Issue | [#30631](https://github.com/vllm-project/vllm/issues/30631) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU has redundant outputs when running Qwen3-Next-MTP in batched inferring.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When we run: ```python prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is" ] sampling_params = SamplingParams(temperature=0.0, top_p=0.95, top_k=40, max_tokens=20) llm = LLM(model="/home/model/Qwen3-Next-80B-A3B-Instruct", tensor_parallel_size=4, enforce_eager=True, distributed_executor_backend="mp", gpu_memory_utilization=0.7, speculative_config={ "method": "qwen3_next_mtp", "num_speculative_tokens": 1, }, max_model_len=4096, enable_prefix_caching=False) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` The outputs of gpu are: ```text Prompt: 'Hello, my name is', Generated text: ' [Your Name], and I am a 20-year-old student from [Your Country]. I' Prompt: 'The president of the United States is', Generated text: ' 2024 is the president of the United States of America. The president of the United' Prompt: 'The capital of France is', Generated text: ' the of capital isThe the of capital isThe the of capital is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: sation has redundant outputs. `vllm-ascned` also has same bug, it is descibed in https://github.com/vllm-project/vllm-ascend/issues/4930. ### Before submitting a new issue... - [x] Make sure you already searched for rel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPU has redundant outputs when running Qwen3-Next-MTP in batched inferring. bug ### Your current environment ### 🐛 Describe the bug When we run: ```python prompts = [ "Hello, my name is", "The president of the Un...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: =4, enforce_eager=True, distributed_executor_backend="mp", gpu_memory_utilization=0.7, speculative_config={ "method": "qwen3_next_mtp", "num_speculative_tokens": 1, }, max_m
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 30. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: max_model_len=4096, enable_prefix_caching=False) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generat...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
