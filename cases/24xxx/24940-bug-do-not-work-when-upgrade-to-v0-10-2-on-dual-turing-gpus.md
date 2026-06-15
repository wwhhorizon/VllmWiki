# vllm-project/vllm#24940: [Bug]: do not work when upgrade to v0.10.2 on dual turing GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#24940](https://github.com/vllm-project/vllm/issues/24940) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: do not work when upgrade to v0.10.2 on dual turing GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When upgrade to container image vllm/vllm-openai:v0.10.2 , vllm report error 'TopPSamplingFromProbs failed with error code too many resources requested for launch'. And container image vllm/vllm-openai:v0.10.1.1 works normal. The docker compose: ```yaml name: llm services: vllm-qwen3-32b: command: - --model - /Qwen3-32B - --served-model-name - Qwen3-32B - --pipeline-parallel-size - "2" - --reasoning-parser - qwen3 - --enable-auto-tool-choice - --tool-call-parser - hermes - --max-model-len - "1024" deploy: resources: reservations: devices: - capabilities: - compute - utility driver: nvidia device_ids: - GPU-uuid0 - GPU-uuid1 environment: PYTORCH_CUDA_ALLOC_CONF: expandable_segments:True VLLM_SLEEP_WHEN_IDLE: "1" image: vllm/vllm-openai:v0.10.2 networks: default: null shm_size: "1073741824" volumes: - type: bind source: /path/to/vllm/cache target: /root/.cache/vllm bind: create_host_path: true - type: bind source: /path/to/Qwen/Qwen3-32B-AWQ target: /Qwen3-32B read_only: true bind: create_host_path: true - type: bind source: /path/to/llm-benchmark target: /llm-benchmark read_only: true bind: create_host_path: true networks: default...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ch'. And container image vllm/vllm-openai:v0.10.1.1 works normal. The docker compose: ```yaml name: llm services: vllm-qwen3-32b: command: - --model - /Qwen3-32B - --served-model-name - Qwen3-32B - --pipeline-parallel-s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t error 'TopPSamplingFromProbs failed with error code too many resources requested for launch'. And container image vllm/vllm-openai:v0.10.1.1 works normal. The docker compose: ```yaml name: llm services: vllm-qwen3-32b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;operator;quantization;sampling;triton build_error;crash;import_error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - GPU-uuid0 - GPU-uuid1 environment: PYTORCH_CUDA_ALLOC_CONF: expandable_segments:True VLLM_SLEEP_WHEN_IDLE: "1" image: vllm/vllm-openai:v0.10.2 networks: default: null shm_size: "1073741824" volumes: - type: bind sourc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 1 works normal. The docker compose: ```yaml name: llm services: vllm-qwen3-32b: command: - --model - /Qwen3-32B - --served-model-name - Qwen3-32B - --pipeline-parallel-size - "2" - --reasoning-parser - qwen3 - --enable-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
