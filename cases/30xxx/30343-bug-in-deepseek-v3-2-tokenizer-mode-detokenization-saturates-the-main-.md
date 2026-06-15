# vllm-project/vllm#30343: [Bug]: In DeepSeek-V3.2 tokenizer mode, detokenization saturates the main thread, causing the server to hang

| 字段 | 值 |
| --- | --- |
| Issue | [#30343](https://github.com/vllm-project/vllm/issues/30343) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In DeepSeek-V3.2 tokenizer mode, detokenization saturates the main thread, causing the server to hang

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #### Summary `/health` requests hang or take extremely long when serving DeepSeek-V3.2 in tokenizer-mode ; main thread is busy in detokenization. When deployed with TP8, the vLLM API server process shows very high CPU usage; with DP8 + EP deployments, it’s even worse—after serving for a while, the API server process hangs and can no longer accept new HTTP requests, `/health `requests hang or take extremely long . #### Repro Steps Command: `vllm serve /path/to/DeepSeek-V3.2-Speciale --served-model-name dsv3p2-dp8 --max-model-len 163840 --max-num-seqs 256 --enable-chunked-prefill --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.9 --tool-call-parser deepseek_v32 --reasoning-parser deepseek_v3 --enable-auto-tool-choice --tokenizer-mode deepseek_v32` - Start server with the command above. - Trigger generation in high load. - Call `/health` while generation is active. - Observe `/health` either never returns or takes a very long time. #### Findings - `py-spy dump --native` shows main thread hot path: `detokenize_incrementally` → `decode_next` → `__len__ (tokenizer) `→ `get_added_vocab` → `added_tokens_decoder`...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: current environment ### 🐛 Describe the bug #### Summary `/health` requests hang or take extremely long when serving DeepSeek-V3.2 in tokenizer-mode ; main thread is busy in detokenization. When deployed with TP8, the vL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ong . #### Repro Steps Command: `vllm serve /path/to/DeepSeek-V3.2-Speciale --served-model-name dsv3p2-dp8 --max-model-len 163840 --max-num-seqs 256 --enable-chunked-prefill --data-parallel-size 8 --enable-expert-parall...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ax-num-seqs 256 --enable-chunked-prefill --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.9 --tool-call-parser deepseek_v32 --reasoning-parser deepseek_v3 --enable-auto-tool-choice --tokenizer-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ted_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
