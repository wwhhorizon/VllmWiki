# vllm-project/vllm#36654: [Bug]: Frequent Tool Call Parsing Failures with DeepSeek-V3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#36654](https://github.com/vllm-project/vllm/issues/36654) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Frequent Tool Call Parsing Failures with DeepSeek-V3.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Background: Long Context & Multi-turn Interactions This issue is particularly prevalent in **complex agentic workflows** characterized by: 1. **Long Context:** As the conversation history grows (e.g., 20k+ tokens), the parser's reliability in detecting DeepSeek-specific protocol tags seems to degrade. 2. **Multi-turn Tool Calling:** In scenarios where the model needs to call multiple tools sequentially (e.g., `Search` -> `Process Results` -> `Search again`), the vLLM server fails to maintain a clean separation between "Thinking" and "Acting." --- ### Description When using **DeepSeek-V3.2** with both **Tool Calling** and the **Thinking (Reasoning)** feature enabled, the vLLM server fails to intercept and parse DeepSeek-specific tool-calling tags (` `). **Current Problem:** Instead of generating a structured `tool_calls` list, the raw DSML XML-like tags are leaked into either the `reasoning` field or the `content` field. Consequently, the `tool_calls` attribute remains an empty list `[]`. --- ### Environment & Deployment * **Model:** `DeepSeek-V3.2` (or compatible variant) * **vLLM Launch Script:** ```bash PROC_PER_NODE=8 NODE...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s (e.g., 20k+ tokens), the parser's reliability in detecting DeepSeek-specific protocol tags seems to degrade. 2. **Multi-turn Tool Calling:** In scenarios where the model needs to call multiple tools sequentially (e.g....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rios where the model needs to call multiple tools sequentially (e.g., `Search` -> `Process Results` -> `Search again`), the vLLM server fails to maintain a clean separation between "Thinking" and "Acting." --- ### Descr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 0.0.0.0 \ --port 20010 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --data-parallel-size 1 \ --tokenizer-mode deepseek_v32 \ --tool-call-parser deepseek_v32 \ --enable-auto-tool-choice \ --reasoning-parser de...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: und: Long Context & Multi-turn Interactions This issue is particularly prevalent in **complex agentic workflows** characterized by: 1. **Long Context:** As the conversation history grows (e.g., 20k+ tokens), the parser'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: arser deepseek_v3 \ --trust-remote-code \ --distributed-executor-backend ray \ --max-model-len 65536 \ --max-num-seqs 64 \ --all2all-backend deepep_low_latency \ --seed 42 ``` --- ### Actual Behavior (The Bug) In a mult...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
