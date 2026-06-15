# vllm-project/vllm#17346: [Bug]: [v0.8.5] Qwen3 returned reasoning content, but --enable-reasoning was not enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#17346](https://github.com/vllm-project/vllm/issues/17346) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [v0.8.5] Qwen3 returned reasoning content, but --enable-reasoning was not enabled.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Deployment ```yaml services: llm-vllm: image: vllm/vllm-openai:latest container_name: llm-vllm restart: unless-stopped environment: HUGGING_FACE_HUB_TOKEN: ${HF_TOKEN} # VLLM_TRACE_FUNCTION: 1 # VLLM_LOGGING_LEVEL: DEBUG # CUDA_LAUNCH_BLOCKING: 1 ports: - "${PORT}:${PORT}" deploy: resources: reservations: devices: - driver: nvidia device_ids: ['0', '1'] capabilities: [gpu] ipc: host volumes: - ~/.cache/huggingface:/root/.cache/huggingface env_file: - .env command: > --host 0.0.0.0 --port ${PORT} --api-key ${API_KEY} --max-model-len ${MAX_MODEL_LEN} --tensor-parallel-size ${TP} --gpu-memory-utilization ${GMU} --served-model-name ${SERVED_MODEL_NAME} --seed 42 --disable-log-requests --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser hermes --model ${MODEL} ``` ```shell HF_TOKEN= PORT=8012 MAX_MODEL_LEN=32768 TP=2 GMU=0.8 SERVED_MODEL_NAME=gpt-4o-mini MODEL=Qwen/Qwen3-8B API_KEY=Lizai@54321 ``` # Usage ```python from langchain_openai import ChatOpenAI model = ChatOpenAI( model="gpt-4o-mini", base_url="http://localhost:8012/v1", api_key="Lizai@54321", temperature=0.7, top_p=0.8, max_completion_tokens=1024, seed=42...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: wen3-8B API_KEY=Lizai@54321 ``` # Usage ```python from langchain_openai import ChatOpenAI model = ChatOpenAI( model="gpt-4o-mini", base_url="http://localhost:8012/v1", api_key="Lizai@54321", temperature=0.7, top_p=0.8,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: [v0.8.5] Qwen3 returned reasoning content, but --enable-reasoning was not enabled. bug;stale ### Your current environment ### 🐛 Describe the bug # Deployment ```yaml services: llm-vllm: image: vllm/vllm-openai:la...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: # VLLM_TRACE_FUNCTION: 1 # VLLM_LOGGING_LEVEL: DEBUG # CUDA_LAUNCH_BLOCKING: 1 ports: - "${PORT}:${PORT}" deploy: resources: reservations: devices: - driver: nvidia device_ids: ['0', '1'] capabilities: [
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: returned reasoning content, but --enable-reasoning was not enabled. bug;stale ### Your current environment ### 🐛 Describe the bug # Deployment ```yaml services: llm-vllm: image: vllm/vllm-openai:latest container_name: l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: # Deployment ```yaml services: llm-vllm: image: vllm/vllm-openai:latest container_name: llm-vllm restart: unless-stopped environment: HUGGING_FACE_HUB_TOKEN: ${HF_TOKEN} # VLLM_TRACE_FUNCTION: 1 # VLLM_LOGGING_LEVEL: DE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
