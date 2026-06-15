# vllm-project/vllm#26292: [Bug]: FSM broken for Qwen3-VL-30B-A3B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#26292](https://github.com/vllm-project/vllm/issues/26292) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FSM broken for Qwen3-VL-30B-A3B-Instruct

### Issue 正文摘录

### Your current environment Running official Docker image: ``` vllm: image: vllm/vllm-openai:v0.11.0 volumes: - ./cache/huggingface:/root/.cache/huggingface ports: - 0.0.0.0:${VLLM_PORT}:8000 environment: HUGGING_FACE_HUB_TOKEN: ${HF_HUB_TOKEN} NCCL_DEBUG: INFO #VLLM_LOGGING_LEVEL: DEBUG shm_size: '2gb' entrypoint: python3 command: -m vllm.entrypoints.openai.api_server --port=8000 --host=0.0.0.0 --model=Qwen/Qwen3-VL-30B-A3B-Instruct --limit-mm-per-prompt '{"video":0}' --tensor-parallel-size 4 --async-scheduling deploy: resources: limits: cpus: "16" memory: 128GB reservations: devices: - driver: nvidia device_ids: ['0', '1', '2', '3'] capabilities: [gpu] ``` ### 🐛 Describe the bug I'm always getting an error like this pasky-vllm-1 | (EngineCore_DP0 pid=269) ERROR 10-06 04:51:05 [backend_xgrammar.py:165] Failed to advance FSM for request chatcmpl-cc8b486e7b81431886e0bd5b820860b8 for tokens 1. Please file an issue. when issuing a generate with `"guided_json"` parameter with Qwen/Qwen3-VL-30B-A3B-Instruct. Actual output eventually generated is something like this (with a jsonschema with root object having "_note" as the first attribute). ``` {'role': 'assistant', 'content': '{\n{\n...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: en3-VL-30B-A3B-Instruct bug ### Your current environment Running official Docker image: ``` vllm: image: vllm/vllm-openai:v0.11.0 volumes: - ./cache/huggingface:/root/.cache/huggingface ports: - 0.0.0.0:${VLLM_PORT}:800...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: FSM broken for Qwen3-VL-30B-A3B-Instruct bug ### Your current environment Running official Docker image: ``` vllm: image: vllm/vllm-openai:v0.11.0 volumes: - ./cache/huggingface:/root/.cache/huggingface ports:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: FSM broken for Qwen3-VL-30B-A3B-Instruct bug ### Your current environment Running official Docker image: ``` vllm: image: vllm/vllm-openai:v0.11.0 volumes: - ./cache/huggingface:/root/.cache/huggingfac
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ERROR 10-06 04:51:05 [backend_xgrammar.py:165] Failed to advance FSM for request chatcmpl-cc8b486e7b81431886e0bd5b820860b8 for tokens 1. Please file an issue. when issuing a generate with `"guided_json"` parameter with...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ike this pasky-vllm-1 | (EngineCore_DP0 pid=269) ERROR 10-06 04:51:05 [backend_xgrammar.py:165] Failed to advance FSM for request chatcmpl-cc8b486e7b81431886e0bd5b820860b8 for tokens 1. Please file an issue. when issuin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
