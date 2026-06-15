# vllm-project/vllm#18157: [Bug]: `vllm serve` with various models on v0 crashes during chat completion request

| 字段 | 值 |
| --- | --- |
| Issue | [#18157](https://github.com/vllm-project/vllm/issues/18157) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `vllm serve` with various models on v0 crashes during chat completion request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Is [OpenAI Chat Completion Client For Multimodal](https://docs.vllm.ai/en/latest/getting_started/examples/openai_chat_completion_client_for_multimodal.html) with `vllm serve llava-hf/llava-1.5-7b-hf` and `vllm serve llava-hf/llava-v1.6-mistral-7b-hf` on v0 (in my case CPU platform) expected to work? Right now the server crashes for me when the script makes the chat completion request. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: `vllm serve` with various models on v0 crashes during chat completion request bug;stale ### Your current environment ### 🐛 Describe the bug Is [OpenAI Chat Completion Client For Multimodal](https://docs.vllm.ai/e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding cache;c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ]: `vllm serve` with various models on v0 crashes during chat completion request bug;stale ### Your current environment ### 🐛 Describe the bug Is [OpenAI Chat Completion Client For Multimodal](https://docs.vllm.ai/en/la...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: uted_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding cache;cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf;slowdown dtype...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
