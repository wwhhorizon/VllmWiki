# vllm-project/vllm#8836: [Bug]: TimeoutError: MQLLMEngine didn't reply within 10000ms

| 字段 | 值 |
| --- | --- |
| Issue | [#8836](https://github.com/vllm-project/vllm/issues/8836) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TimeoutError: MQLLMEngine didn't reply within 10000ms

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```yaml # docker-compose.yml services: llm-vllm-cpu: image: vllm/vllm-openai:cpu container_name: llm-vllm-cpu restart: unless-stopped environment: HUGGING_FACE_HUB_TOKEN: ports: - "8007:8007" deploy: resources: limits: cpus: "28" memory: 24GB ipc: host volumes: - ~/.cache/huggingface:/root/.cache/huggingface command: > --host 0.0.0.0 --port 8007 --api-key --max-model-len 2048 --served-model-name llama3.2 --seed 42 --device cpu --dtype bfloat16 --disable-log-requests --model meta-llama/Llama-3.2-1B-Instruct ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```yaml # docker-compose.yml services: llm-vllm-cpu: image: vllm/vllm-openai:cpu container_name: llm-vllm-cpu restart: unless-stopped environment: HUGGING_FACE_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --served-model-name llama3.2 --seed 42 --device cpu --dtype bfloat16 --disable-log-requests --model meta-llama/Llama-3.2-1B-Instruct ``` ### Before submitting a new issue... - [X] Make sure you already searched for rele...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ine didn't reply within 10000ms bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```yaml # docker-compose.yml services: llm-vllm-cpu: image: vllm/vllm-openai:cpu container_name...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: --seed 42 --device cpu --dtype bfloat16 --disable-log-requests --model meta-llama/Llama-3.2-1B-Instruct ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
