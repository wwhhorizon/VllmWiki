# vllm-project/vllm#29765: [Bug]: Server launch fails on vLLM 0.11.1 / 0.11.2 when loading AWQ or GPTQ MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#29765](https://github.com/vllm-project/vllm/issues/29765) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Server launch fails on vLLM 0.11.1 / 0.11.2 when loading AWQ or GPTQ MoE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On vLLM 0.11.1 or 0.11.2, server launch failed when try to launch AWQ / GPTQ MoE Model. The problem is introduced by this PR: https://github.com/vllm-project/vllm/pull/27291 The PR added SPLIT_K for`fused_moe_kernel_gptq_awq`, but ensured its presence only when using `get_default_config`. In other code paths, the Triton config may not contain "SPLIT_K", leading to a failure during kernel selection. The issue can be resolved by explicitly adding `config["SPLIT_K"] = 1` when constructing the Triton config. Reproduce: `python3 -m vllm.entrypoints.openai.api_server --trust-remote-code --host 0.0.0.0 --port 8999 --model QuixiAI/Qwen3-30B-A3B-AWQ --tensor-parallel-size 1 --distributed-executor-backend=mp --no-enable-prefix-caching` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Server launch fails on vLLM 0.11.1 / 0.11.2 when loading AWQ or GPTQ MoE models bug ### Your current environment ### 🐛 Describe the bug On vLLM 0.11.1 or 0.11.2, server launch failed when try to launch AWQ / GPTQ MoE Mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: presence only when using `get_default_config`. In other code paths, the Triton config may not contain "SPLIT_K", leading to a failure during kernel selection. The issue can be resolved by explicitly adding `config["SPLI...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tly adding `config["SPLIT_K"] = 1` when constructing the Triton config. Reproduce: `python3 -m vllm.entrypoints.openai.api_server --trust-remote-code --host 0.0.0.0 --port 8999 --model QuixiAI/Qwen3-30B-A3B-AWQ --tensor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: to a failure during kernel selection. The issue can be resolved by explicitly adding `config["SPLIT_K"] = 1` when constructing the Triton config. Reproduce: `python3 -m vllm.entrypoints.openai.api_server --trust-remote-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
