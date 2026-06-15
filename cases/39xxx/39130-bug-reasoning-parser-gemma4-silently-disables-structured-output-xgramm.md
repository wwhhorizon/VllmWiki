# vllm-project/vllm#39130: [Bug]: `--reasoning-parser gemma4` silently disables structured output (xgrammar) when `enable_thinking=false`

| 字段 | 值 |
| --- | --- |
| Issue | [#39130](https://github.com/vllm-project/vllm/issues/39130) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `--reasoning-parser gemma4` silently disables structured output (xgrammar) when `enable_thinking=false`

### Issue 正文摘录

### Your current environment - vLLM version: v0.19.0 (`vllm/vllm-openai:v0.19.0-x86_64-cu130-ubuntu2404` with `transformers>=5.5.0`) - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB GDDR7, SM 12.0) - OS: Linux 5.15.0-171-generic - CUDA: 13.0 - Python: 3.12 ## Model `google/gemma-4-E4B-it` (dense 4B model, FP8 quantization) Also applies to any Gemma 4 variant (`google/gemma-4-26B-A4B-it`, `google/gemma-4-31B-it`) — and likely any model whose reasoning parser uses channel-style delimiters not present in the prompt. ## Command ```bash vllm serve google/gemma-4-E4B-it \ --quantization fp8 \ --max-model-len 25600 \ --max-num-seqs 32 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.92 \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ --default-chat-template-kwargs '{"enable_thinking": false}' \ --structured-outputs-config '{"backend":"xgrammar"}' ``` ### 🐛 Describe the bug When `--reasoning-parser gemma4` is specified together with `--default-chat-template-kwargs '{"enable_thinking": false}'`, the xgrammar structured output engine is **completely bypassed** for every request. Grammar constraints (JSON schema, BNF, etc.) are never enforced....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: `--reasoning-parser gemma4` silently disables structured output (xgrammar) when `enable_thinking=false` bug ### Your current environment - vLLM version: v0.19.0 (`vllm/vllm-openai:v0.19.0-x86_64-cu130-ubuntu2404`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: .19.0-x86_64-cu130-ubuntu2404` with `transformers>=5.5.0`) - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB GDDR7, SM 12.0) - OS: Linux 5.15.0-171-generic - CUDA: 13.0 - Python: 3.12 ## Model `google/gemma-4-E4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r) when `enable_thinking=false` bug ### Your current environment - vLLM version: v0.19.0 (`vllm/vllm-openai:v0.19.0-x86_64-cu130-ubuntu2404` with `transformers>=5.5.0`) - GPU: NVIDIA RTX PRO 6000 Blackwell Server Editio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 13.0 - Python: 3.12 ## Model `google/gemma-4-E4B-it` (dense 4B model, FP8 quantization) Also applies to any Gemma 4 variant (`google/gemma-4-26B-A4B-it`, `google/gemma-4-31B-it`) — and likely any model whose reasoning p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e xgrammar structured output engine is **completely bypassed** for every request. Grammar constraints (JSON schema, BNF, etc.) are never enforced. The model generates unconstrained text that happens to look valid becaus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
