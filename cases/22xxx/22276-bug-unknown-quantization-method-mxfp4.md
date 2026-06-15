# vllm-project/vllm#22276: [Bug]:  Unknown quantization method: mxfp4

| 字段 | 值 |
| --- | --- |
| Issue | [#22276](https://github.com/vllm-project/vllm/issues/22276) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Unknown quantization method: mxfp4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash export VLLM_MODEL_NAME="openai/gpt-oss-20b" echo ">> Starting vLLM API server on 8001 in background (logs → vllm.log)…" nohup python -m vllm.entrypoints.openai.api_server \ --model "${VLLM_MODEL_NAME}" \ --served-model-name model \ --api-key "${LLM_API_KEY}" \ --max-model-len "${VLLM_TOKEN_COUNT}" \ --tensor-parallel-size 1 \ --uvicorn-log-level error \ --gpu-memory-utilization 0.80 \ --max-num-seqs 32 \ --enable-chunked-prefill \ --max-num-batched-tokens 20480 \ --quantization mxfp4 \ --dtype half \ --enforce-eager \ --port 8001 \ > vllm.log 2>&1 & ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Unknown quantization method: mxfp4 bug;stale ### Your current environment ### 🐛 Describe the bug ```bash export VLLM_MODEL_NAME="openai/gpt-oss-20b" echo ">> Starting vLLM API server on 8001 in background (logs →...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Your current environment ### 🐛 Describe the bug ```bash export VLLM_MODEL_NAME="openai/gpt-oss-20b" echo ">> Starting vLLM API server on 8001 in background (logs → vllm.log)…" nohup python -m vllm.entrypoints.openai.api...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Unknown quantization method: mxfp4 bug;stale ### Your current environment ### 🐛 Describe the bug ```bash export VLLM_MODEL_NAME="openai/gpt-oss-20b" echo ">> Starting vLLM API server on 8001 in background (logs →...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
