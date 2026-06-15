# vllm-project/vllm#19245: [Bug]: qwq32b-128k accuracy loss compare with sglang ， with proprietory business benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#19245](https://github.com/vllm-project/vllm/issues/19245) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwq32b-128k accuracy loss compare with sglang ， with proprietory business benchmark

### Issue 正文摘录

### Your current environment python -m vllm.entrypoints.openai.api_server \ --model "${replaced_current_model_path:-QwQ-32B/}" \ --tensor-parallel-size "${INFERENCE_ENV_TP:-8}" \ --trust-remote-code \ --port "${INFERENCE_PORT:-8003}" \ --enable-auto-tool-choice \ --served-model-name QwQ32B\ --tool-call-parser "${TOOL_CALL_PARSER:-hermes}"\ --gpu-memory-utilization "${INFERENCE_ENV_GPU_MEMORY_UTIL:-0.75}" \ --host "${INFERENCE_ENV_IP:-0.0.0.0}" \ --max-num-batched-tokens "${INFERENCE_ENV_MAX_BATCH_TOKENS:-32768}" \ --max-model-len "${INFERENCE_ENV_MAX_MODEL_LEN:-32768}" python3 -m sglang.launch_server \ --model-path QwQ-32B/ \ --served-model-name QwQ32B \ --host 0.0.0.0 \ --port 8003 \ --dtype half \ --trust-remote-code \ --tp 8 \ --max-total-tokens 131000 \ --attention-backend flashinfer \ --device cuda \ --kv-cache-dtype auto \ --disable-cuda-graph-padding \ --enable-metrics \ --triton-attention-num-kv-splits 4 \ --reasoning-parser deepseek-r1 ### 🐛 Describe the bug python -m vllm.entrypoints.openai.api_server \ --model "${replaced_current_model_path:-QwQ-32B/}" \ --tensor-parallel-size "${INFERENCE_ENV_TP:-8}" \ --trust-remote-code \ --port "${INFERENCE_PORT:-8003}" \ --enable-a...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: --tp 8 \ --max-total-tokens 131000 \ --attention-backend flashinfer \ --device cuda \ --kv-cache-dtype auto \ --disable-cuda-graph-padding \ --enable-metrics \ --triton-attention-num-kv-splits 4 \ --reasoning-parser dee...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: qwq32b-128k accuracy loss compare with sglang ， with proprietory business benchmark bug;stale ### Your current environment python -m vllm.entrypoints.openai.api_server \ --model "${replaced_current_model_path:-Qw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: okens 131000 \ --attention-backend flashinfer \ --device cuda \ --kv-cache-dtype auto \ --disable-cuda-graph-padding \ --enable-metrics \ --triton-attention-num-kv-splits 4 \ --reasoning-parser deepseek-r1 ### 🐛 Describ...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: qwq32b-128k accuracy loss compare with sglang ， with proprietory business benchmark bug;stale ### Your current environment python -m vllm.entrypoints.openai.api_server \ --model "${replaced_current_model_path:-Qw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cache;distributed_parallel;model_support attention;cuda;triton dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
