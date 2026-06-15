# vllm-project/vllm#8500: [Bug]: vllm-cpu docker gguf: AttributeError: '_OpNamespace' '_C' object has no attribute 'ggml_dequantize'

| 字段 | 值 |
| --- | --- |
| Issue | [#8500](https://github.com/vllm-project/vllm/issues/8500) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm-cpu docker gguf: AttributeError: '_OpNamespace' '_C' object has no attribute 'ggml_dequantize'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug First, I followed [this instruction](https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#cpu-backend-quick-start-dockerfile) and built my docker image. Then I started my container with the below `docker-compose.yml` file. ```yaml services: llm-vllm-dev: image: vllm/vllm-openai:cpu container_name: llm-vllm-dev restart: unless-stopped environment: HUGGING_FACE_HUB_TOKEN: ${HF_TOKEN} ports: - "8007:8007" deploy: resources: limits: cpus: "24" memory: 32GB ipc: host volumes: - ~/.cache/huggingface:/root/.cache/huggingface - ./models:/models networks: - ai-assistant command: > --host 0.0.0.0 --port 8007 --api-key --max-model-len 4096 --tensor-parallel-size 1 --served-model-name gpt-4o --seed 42 --disable-log-requests --quantization gguf --model /models/Llama-3.1-Storm-8B.Q4_K_M.gguf networks: ai-assistant: external: true ``` My running script: ```python import openai BASE_URL="http://localhost:8007/v1" # port 8000 or 8005 API_KEY= openai_client = openai.OpenAI( base_url=BASE_URL, api_key=API_KEY ) chat_template = "{% if not add_generation_prompt is defined %}{% set add_generation_pro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: vllm-cpu docker gguf: AttributeError: '_OpNamespace' '_C' object has no attribute 'ggml_dequantize' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug First, I followed [t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: no attribute 'ggml_dequantize' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug First, I followed [this instruction](https://docs.vllm.ai/en/latest/getting_started/cpu-installa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#cpu-backend-quick-start-dockerfile) and built my docker image. Then I started my container with the below `docker-compose.yml` file. ```yaml services:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: gguf: AttributeError: '_OpNamespace' '_C' object has no attribute 'ggml_dequantize' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug First, I followed [this instruction](https:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
