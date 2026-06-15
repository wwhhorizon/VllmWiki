# vllm-project/vllm#25060: [Bug]: Does not run embedding model sergeyzh/rubert-tiny-turbo

| 字段 | 值 |
| --- | --- |
| Issue | [#25060](https://github.com/vllm-project/vllm/issues/25060) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Does not run embedding model sergeyzh/rubert-tiny-turbo

### Issue 正文摘录

### 🐛 Describe the bug HI, I am using version vllm/vllm-openai:v0.10.2 in docker. I can't run embedding model sergeyzh/rubert-tiny-turbo (while sergeyzh/LaBSE-ru-turbo works successfully). Both BERT models that are supported by the architecture. ```text vllm-openai-3: image: vllm/vllm-openai:v0.10.2 container_name: vllm-openai-3.shark02.loc hostname: vllm-openai-3.shark02.loc ipc: host volumes: - vllm-openai-3:/root/.cache/huggingface command: --model sergeyzh/rubert-tiny-turbo deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] count: all ports: - 8085:8000 network_mode: bridge restart: always environment: - TORCHDYNAMO_VERBOSE=1 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: el sergeyzh/rubert-tiny-turbo bug ### 🐛 Describe the bug HI, I am using version vllm/vllm-openai:v0.10.2 in docker. I can't run embedding model sergeyzh/rubert-tiny-turbo (while sergeyzh/LaBSE-ru-turbo works successfull...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_depen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -turbo works successfully). Both BERT models that are supported by the architecture. ```text vllm-openai-3: image: vllm/vllm-openai:v0.10.2 container_name: vllm-openai-3.shark02.loc hostname: vllm-openai-3.shark02.loc i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Does not run embedding model sergeyzh/rubert-tiny-turbo bug ### 🐛 Describe the bug HI, I am using version vllm/vllm-openai:v0.10.2 in docker. I can't run embedding model sergeyzh/rubert-tiny-turbo (while sergeyzh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: its;scheduler_memory attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency;shape <details>

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
