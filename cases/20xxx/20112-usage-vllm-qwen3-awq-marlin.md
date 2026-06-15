# vllm-project/vllm#20112: [Usage]: vllm + qwen3 + awq-marlin?

| 字段 | 值 |
| --- | --- |
| Issue | [#20112](https://github.com/vllm-project/vllm/issues/20112) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm + qwen3 + awq-marlin?

### Issue 正文摘录

Hi vLLM team, I'm currently running Qwen3.14B-AWQ with vLLM and noticed the following logs when starting the server: ``` INFO 06-17 13:04:11 [awq_marlin.py:120] Detected that the model can run with awq_marlin, however you specified quantization=awq explicitly, so forcing awq. Use quantization=awq_marlin for faster inference WARNING 06-17 13:04:11 [config.py:931] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. ``` It seems `awq_marlin` is a new quantization method that could offer faster inference compared to `awq`. Can you clarify what `awq_marlin` is and how it differs from standard `awq` quantization? Is it recommended to switch to `awq_marlin` for better performance with Qwen3.14B-AWQ, or are there specific considerations (e.g., compatibility, stability, or hardware requirements) to keep in mind? For reference, here's my current vLLM server command: ```bash python3 -m vllm.entrypoints.openai.api_server \ --model "${LLM_MODEL_NAME}" \ --served-model-name model \ --api-key "${LLM_API_KEY}" \ --max-model-len "${LLM_TOKEN_COUNT}" \ --tensor-parallel-size 1 \ --uvicorn-log-level error \ --gpu-memory-utilization 0.80 \ --max-num-seqs 32...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: vllm + qwen3 + awq-marlin? usage Hi vLLM team, I'm currently running Qwen3.14B-AWQ with vLLM and noticed the following logs when starting the server: ``` INFO 06-17 13:04:11 [awq_marlin.py:120] Detected that th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ] Detected that the model can run with awq_marlin, however you specified quantization=awq explicitly, so forcing awq. Use quantization=awq_marlin for faster inference WARNING 06-17 13:04:11 [config.py:931] awq quantizat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: .py:120] Detected that the model can run with awq_marlin, however you specified quantization=awq explicitly, so forcing awq. Use quantization=awq_marlin for faster inference WARNING 06-17 13:04:11 [config.py:931] awq qu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lp! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --gpu-memory-utilization 0.80 \ --max-num-seqs 32 \ --enable-chunked-prefill \ --max-num-batched-tokens 20480 \ --quantization awq \ --dtype half \ --enforce-eager ``` ### How would you like to use vllm Should I simply...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
