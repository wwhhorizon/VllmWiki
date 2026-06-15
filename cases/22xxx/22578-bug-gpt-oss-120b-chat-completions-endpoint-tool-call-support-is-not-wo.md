# vllm-project/vllm#22578: [Bug]: [gpt-oss-120b] Chat Completions endpoint tool_call support is not working

| 字段 | 值 |
| --- | --- |
| Issue | [#22578](https://github.com/vllm-project/vllm/issues/22578) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [gpt-oss-120b] Chat Completions endpoint tool_call support is not working

### Issue 正文摘录

### Your current environment version: '3.8' services: vllm: container_name: vllm-gpt image: vllm/vllm-openai:gptoss restart: unless-stopped runtime: nvidia env_file: .env command: > --model ${MODEL_NAME} --tensor-parallel-size ${TENSOR_PARALLEL_SIZE} --dtype auto --max-model-len ${MAX_MODEL_LEN} --gpu-memory-utilization ${GPU_MEMORY_UTILIZATION} --swap-space ${SWAP_SPACE} --max-num-batched-tokens ${MAX_MODEL_LEN} --served-model-name ${SERVED_MODEL_NAME} --api-key ${VLLM_API_KEY} --async-scheduling environment: - HUGGING_FACE_HUB_TOKEN=${HF_TOKEN} - VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 - NVIDIA_VISIBLE_DEVICES=0,1 - OMP_NUM_THREADS=48 # OpenMP线程数匹配CPU核心数 - MKL_NUM_THREADS=48 # MKL线程数匹配CPU核心数 - VLLM_ATTENTION_BACKEND=${ATTENTION_BACKEND} cpuset: "0-63" volumes: - ${MODEL_CACHE}:/root/.cache/huggingface - ./logs:/logs ports: - "${API_PORT}:8000" ipc: host ulimits: memlock: -1 stack: 67108864 networks: - ai-network networks: ai-network: external: true ### 🐛 Describe the bug When using the `gpt-oss-120b` model with vLLM via the `/v1/chat/completions` endpoint, enabling tool calling (`--enable-auto-tool-choice` with any `--tool-call-parser`) does not work properly: - Using `--tool-call-parse...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: [gpt-oss-120b] Chat Completions endpoint tool_call support is not working bug;stale;gpt-oss ### Your current environment version: '3.8' services: vllm: container_name: vllm-gpt image: vllm/vllm-openai:gptoss
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l support is not working bug;stale;gpt-oss ### Your current environment version: '3.8' services: vllm: container_name: vllm-gpt image: vllm/vllm-openai:gptoss restart: unless-stopped runtime: nvidia env_file: .env comma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: - MKL_NUM_THREADS=48 # MKL线程数匹配CPU核心数 - VLLM_ATTENTION_BACKEND=${ATTENTION_BACKEND} cpuset: "0-63" volumes: - ${MODEL_CACHE}:/root/.cache/huggingface - ./logs:/logs ports: - "${API_PORT}:8000" ipc: host ulimits: memlock...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: MODEL_NAME} --tensor-parallel-size ${TENSOR_PARALLEL_SIZE} --dtype auto --max-model-len ${MAX_MODEL_LEN} --gpu-memory-utilization ${GPU_MEMORY_UTILIZATION} --swap-space ${SWAP_SPACE} --max-num-batched-tokens ${MAX_MODEL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mes ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
