# vllm-project/vllm#18630: [Bug]: lora_filesystem_resolver wont work

| 字段 | 值 |
| --- | --- |
| Issue | [#18630](https://github.com/vllm-project/vllm/issues/18630) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: lora_filesystem_resolver wont work

### Issue 正文摘录

### Your current environment ok ### 🐛 Describe the bug I'm trying to use the plugin lora_filesystem_resolver, so that LoRAs are automatically loaded based on request. I'm using the following: `export MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct-AWQ docker run \ --ipc=host \ --runtime nvidia \ -e VLLM_USE_V1=1 \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=${MODEL_ID_GPU}" \ --env "VLLM_ALLOW_RUNTIME_LORA_UPDATING=True" \ --env "VLLM_PLUGINS=lora_filesystem_resolver" \ --env "VLLM_LORA_RESOLVER_CACHE_DIR=/root/lora" \ -v "VLLM_LOGGING_LEVEL=${VLLM_LOGGING_LEVEL}" \ -v "${HF_HOME}:/root/.cache/huggingface" \ -v "/teamspace/studios/this_studio/lora:/root/lora" \ -v "$(pwd):/app" \ ubicloud/vllm-openai:latest \ --model ${MODEL_ID} \ --quantization awq \ --dtype float16 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --chat-template /vllm-workspace/examples/tool_chat_template_hermes.jinja \ --gpu-memory-utilization 0.29 \ --max-lora-rank 256 \ --enable-lora \ --served-model-name qwen-qwen25-vl-3b-instruct-awq ` **note: I'm using ubicloud/vllm-openai because vllm/vllm-openai was not loading the plugin.** It seems t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: utomatically loaded based on request. I'm using the following: `export MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct-AWQ docker run \ --ipc=host \ --runtime nvidia \ -e VLLM_USE_V1=1 \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: m using the following: `export MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct-AWQ docker run \ --ipc=host \ --runtime nvidia \ -e VLLM_USE_V1=1 \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -v "$(pwd):/app" \ ubicloud/vllm-openai:latest \ --model ${MODEL_ID} \ --quantization awq \ --dtype float16 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --chat-template /vllm-workspace/examples/tool_chat_te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=${MODEL_ID_GPU}" \ --env "VLLM_ALLOW_RUNTIME_LORA_UPDATING=True" \ --env "VLLM_PLUGINS=lora_filesystem_resolver" \ --env "VLL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ora_filesystem_resolver, so that LoRAs are automatically loaded based on request. I'm using the following: `export MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct-AWQ docker run \ --ipc=host \ --runtime nvidia \ -e VLLM_USE_V1=1 \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
