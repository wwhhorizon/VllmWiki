# vllm-project/vllm#39043: [Bug]: Vllm + Gemma 4 + claude code: tool calling problems

| 字段 | 值 |
| --- | --- |
| Issue | [#39043](https://github.com/vllm-project/vllm/issues/39043) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm + Gemma 4 + claude code: tool calling problems

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to use claude code with gemma 4 (31B) but for some reason this didn't work well - if thinking is enabled the reasoning tags are leaking to chat. If I turn off reasoning with `--default-chat-template-kwargs '{"enable_thinking": false}'` it starts to leak tool calls to chat. Here is some examples: reasoning on (command to run: `vllm serve /mnt/nfs-esxi/LLM/gemma-4-31B-it-NVFP4/ --tensor-parallel-size 2 --host 0.0.0.0 --port 30000 --max-model-len $((200*1024)) --gpu-memory-utilization 0.9 --max-num-seqs 4 --enable-auto-tool-choice --reasoning-parser gemma4 --tool-call-parser gemma4 --served-model-name qwen3.5-397b-ud-q4-k-xl:thinking-coding-vision --kv-cache-dtype fp8` NB: alias is just to quickly return to using qwen as main model via llama.cpp ``` ╭─── Claude Code v2.1.92 ────────────────────────────────────────────────────────────────────────────────────────────────╮ │ Tips for getting started │ │ Welcome back Роман! Run /init to create a CLAUDE.md file with instructions for Claude │ │ ───────────────────────────────────────────────────────────────── │ │ ▐▛███▜▌ Recent activity │ │ ▝▜█████▛▘ No recent activity │ │ ▘▘ ▝▝ │...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: asoning on (command to run: `vllm serve /mnt/nfs-esxi/LLM/gemma-4-31B-it-NVFP4/ --tensor-parallel-size 2 --host 0.0.0.0 --port 30000 --max-model-len $((200*1024)) --gpu-memory-utilization 0.9 --max-num-seqs 4 --enable-a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Vllm + Gemma 4 + claude code: tool calling problems bug ### Your current environment ### 🐛 Describe the bug Trying to use claude code with gemma 4 (31B) but for some reason this didn't work well - if thinking is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: by exploring the project structure and key files. Since this is a broad request, I'll use the Explore agent to map out the system.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ● Since you didn't specify a further request, I will assume you are satisfied with the architectural explanation.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ma4 --served-model-name qwen3.5-397b-ud-q4-k-xl:thinking-coding-vision --kv-cache-dtype fp8` NB: alias is just to quickly return to using qwen as main model via llama.cpp ``` ╭─── Claude Code v2.1.92 ───────────────────...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
