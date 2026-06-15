# vllm-project/vllm#30722: [Bug]: llama4_pythonic tool parser fails with SyntaxError on nested list parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#30722](https://github.com/vllm-project/vllm/issues/30722) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization;sampling_logits |
| 子分类 | install |
| Operator 关键词 | cuda;fp8;gemm;moe;sampling |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llama4_pythonic tool parser fails with SyntaxError on nested list parameters

### Issue 正文摘录

### Your current environment I don't have direct access to the cluster the model is running in. But it's running on 8x H100 GPUs using TP 8, expert parallel. This is the fp8 model from Huggingface. These are the vllm serve args I'm using: VLLM Version: 0.11.0 ``` --port 8002 --model /config/models/maverick --device cuda --tensor-parallel-size 8 --disable-log-requests --max-num-batched-tokens 16000 --served-model-name 'llama-4-maverick-17b-128e-instruct' --limit-mm-per-prompt image=50 --kv-cache-dtype fp8 --trust-remote-code --enable-auto-tool-choice --enable-chunked-prefill true --enable-prefix-caching --tool-call-parser llama4_pythonic --enable-expert-parallel --chat-template examples/tool_chat_template_llama4_pythonic.jinja --override-generation-config '{\"attn_temperature_tuning\": true}' --max-model-len 1000000 ``` ### 🐛 Describe the bug ### Description The `llama4_pythonic` tool parser intermittently fails to parse valid tool calls, resulting in: 1. `SyntaxError` from `ast.parse()` when model output is malformed (missing closing `]`) 2. Valid pythonic syntax returned as `content` instead of being parsed into `tool_calls` ### Reproduction **Minimal curl (run 10+ times to obser...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: llama4_pythonic tool parser fails with SyntaxError on nested list parameters bug;stale ### Your current environment I don't have direct access to the cluster the model is running in. But it's running on 8x H100 G...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: it's running on 8x H100 GPUs using TP 8, expert parallel. This is the fp8 model from Huggingface. These are the vllm serve args I'm using: VLLM Version: 0.11.0 ``` --port 8002 --model /config/models/maverick --device cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ct access to the cluster the model is running in. But it's running on 8x H100 GPUs using TP 8, expert parallel. This is the fp8 model from Huggingface. These are the vllm serve args I'm using: VLLM Version: 0.11.0 ``` -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: er the model is running in. But it's running on 8x H100 GPUs using TP 8, expert parallel. This is the fp8 model from Huggingface. These are the vllm serve args I'm using: VLLM Version: 0.11.0 ``` --port 8002 --model /co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ythonic tool parser fails with SyntaxError on nested list parameters bug;stale ### Your current environment I don't have direct access to the cluster the model is running in. But it's running on 8x H100 GPUs using TP 8,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
