# vllm-project/vllm#21840: [Bug]: [v0.10.0][Critical] Tools not invoked with `tool_choice="auto"` despite relevant prompt and valid schema (xgrammar)

| 字段 | 值 |
| --- | --- |
| Issue | [#21840](https://github.com/vllm-project/vllm/issues/21840) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [v0.10.0][Critical] Tools not invoked with `tool_choice="auto"` despite relevant prompt and valid schema (xgrammar)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is a follow-up to [issue #16880] which originally tracked *minItems* rejection in xgrammar. That part is now fixed in vLLM 0.9. However, in vLLM 0.10.0, when using `tool_choice="auto"` with the same setup, the model never emits tool_calls, even when a function is clearly relevant (e.g., weather question with matching schema). This leads to IndexError when accessing tool_calls[0]. ```dockerfile FROM vllm/vllm-openai:v0.10.0 RUN apt-get update && apt-get install -y git \ && pip install --upgrade pip \ && pip install vllm[audio] \ && pip install vllm[video] RUN apt-get clean && rm -rf /var/lib/apt/lists/* ``` ```bash docker build -t vllm/vllm-openai:v0.10.full \ -f /path/to/Dockerfile.vllm_full_v0.10 \ /other/path ``` ```bash docker run -d \ --rm \ --runtime nvidia \ --shm-size=1g \ --gpus ${GPU_VLLM} \ -v "${VLLM_CACHE}:${VLLM_CACHE}" \ -p "${VLLM_PORT}:${VLLM_PORT}" \ -e HF_HUB_DOWNLOAD_TIMEOUT=120 \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGINGFACE_TOKEN}" \ --name "${CONTAINER_VLLM}" \ vllm/vllm-openai:v0.10.full \ --model RedHatAI/Qwen2.5-VL-72B-Instruct-quantized.w4a16 \ --port "${VLLM_PORT}" \ --gpu_memory_utilization 0.9 \ --...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: hing schema). This leads to IndexError when accessing tool_calls[0]. ```dockerfile FROM vllm/vllm-openai:v0.10.0 RUN apt-get update && apt-get install -y git \ && pip install --upgrade pip \ && pip install vllm[audio] \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: l_choice="auto"` despite relevant prompt and valid schema (xgrammar) bug;stale ### Your current environment ### 🐛 Describe the bug This is a follow-up to [issue #16880] which originally tracked *minItems* rejection in x...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: in vLLM 0.10.0, when using `tool_choice="auto"` with the same setup, the model never emits tool_calls, even when a function is clearly relevant (e.g., weather question with matching schema). This leads to IndexError whe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: oken-abc123 \ --download-dir "${VLLM_CACHE}" \ --guided-decoding-backend xgrammar \ --limit_mm_per_prompt '{"images": 3}' \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --trust-remote-code ``` ```python from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
