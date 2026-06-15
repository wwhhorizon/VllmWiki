# vllm-project/vllm#18059: [Bug]: Mistral3ForConditionalGeneration does not support LoRA yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#18059](https://github.com/vllm-project/vllm/issues/18059) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral3ForConditionalGeneration does not support LoRA yet.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug According to [https://docs.vllm.ai/en/latest/models/supported_models.html#id5](https://docs.vllm.ai/en/latest/models/supported_models.html#id5), Mistral3ForConditionalGeneration is supposed to support LORA with VLLM. However, when running the w4a16 quantized version of the model via the official docker image `vllm/vllm-openai:latest` in a docker-compose setup using this command: `--port=80 --host=0.0.0.0 --model RedHatAI/Mistral-Small-3.1-24B-Instruct-2503-quantized.w4a16 --chat-template /root/chat_templates/mistral_small_prompt_template.jinja --tool-call-parser mistral --enable-auto-tool-choice --max_model_len 16384 --enable-lora --lora-modules my-lora=$HOME/.cache/huggingface/hub/models--xxxxxxxxxx` I get `ValueError: Mistral3ForConditionalGeneration does not support LoRA yet.` on startup and VLLM refuses to launch. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: sed to support LORA with VLLM. However, when running the w4a16 quantized version of the model via the official docker image `vllm/vllm-openai:latest` in a docker-compose setup using this command: `--port=80 --host=0.0.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: p using this command: `--port=80 --host=0.0.0.0 --model RedHatAI/Mistral-Small-3.1-24B-Instruct-2503-quantized.w4a16 --chat-template /root/chat_templates/mistral_small_prompt_template.jinja --tool-call-parser mistral --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug According to [https://docs.vllm.ai/en/latest/models/supported_models.html#id5](https://docs.vllm.ai/en/latest/models/supported_models.html#id5), Mistral3ForConditionalGeneration is supposed to sup...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n is supposed to support LORA with VLLM. However, when running the w4a16 quantized version of the model via the official docker image `vllm/vllm-openai:latest` in a docker-compose setup using this command: `--port=80 --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
