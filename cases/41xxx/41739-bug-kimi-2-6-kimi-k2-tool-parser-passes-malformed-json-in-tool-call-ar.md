# vllm-project/vllm#41739: [Bug]: Kimi 2.6 + Kimi K2 tool parser passes malformed JSON in tool-call arguments to client without validation

| 字段 | 值 |
| --- | --- |
| Issue | [#41739](https://github.com/vllm-project/vllm/issues/41739) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi 2.6 + Kimi K2 tool parser passes malformed JSON in tool-call arguments to client without validation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - vLLM v0.19.1 - Model: moonshotai/Kimi-K2.6 `args: [ 'serve', 'moonshotai/Kimi-K2.6', '--host', '0.0.0.0', '--port', '8000', '--tensor-parallel-size', '8', '--max-model-len', '262144', '--kv-cache-dtype', 'auto', '--gpu-memory-utilization', '0.9', '--max-num-batched-tokens', '16384', '--chat-template', './chat_template.jinja', '--enable-prefix-caching', '--override-generation-config', '{"temperature": 1.0, "top_p": 0.95, "max_new_tokens": 131000, "repetition_penalty": 1.05}', '--served-model-name', '', '', '--decode-context-parallel-size', '8', '--mm-encoder-tp-mode', 'data', '--mm-processor-cache-type', 'shm', '--trust-remote-code', '--tokenizer-mode', 'hf', '--default-chat-template-kwargs', '{"thinking": true}', '--enable-chunked-prefill', '--max-num-seqs', '64', '--max-cudagraph-capture-size', '128', '--compilation-config', '{"cudagraph_mode": "FULL_AND_PIECEWISE"}', '--enable-auto-tool-choice', '--tool-call-parser', 'kimi_k2', '--reasoning-parser', 'kimi_k2', '--kv-cache-metrics', '--kv-cache-metrics-sample', '0.05' ]` ~~- Kimi 2.6 with The Kimi K2 tool parser (`vllm/tool_parsers/kimi_k2_tool_parser.py`) extracts tool-call a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;samp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ## Your current environment ### 🐛 Describe the bug - vLLM v0.19.1 - Model: moonshotai/Kimi-K2.6 `args: [ 'serve', 'moonshotai/Kimi-K2.6', '--host', '0.0.0.0', '--port', '8000', '--tensor-parallel-size', '8', '--max-mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: petition_penalty": 1.05}', '--served-model-name', '', '', '--decode-context-parallel-size', '8', '--mm-encoder-tp-mode', 'data', '--mm-processor-cache-type', 'shm', '--trust-remote-code', '--tokenizer-mode', 'hf', '--de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: '--enable-chunked-prefill', '--max-num-seqs', '64', '--max-cudagraph-capture-size', '128', '--compilation-config', '{"cudagraph_mode": "FULL_AND_PIECEWISE"}', '--enable-auto-tool-choice', '--tool-call-parser', 'kimi_k2'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
