# vllm-project/vllm#39574: [Bug]: glm4_moe_tool_parser._is_string_type crashes on /v1/responses streaming with 'FunctionTool' object has no attribute 'function' (affects GLM-4.5/4.7/5.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#39574](https://github.com/vllm-project/vllm/issues/39574) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | fp8 |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: glm4_moe_tool_parser._is_string_type crashes on /v1/responses streaming with 'FunctionTool' object has no attribute 'function' (affects GLM-4.5/4.7/5.1)

### Issue 正文摘录

### Your current environment ``` vllm version: 0.19.0 OS: Ubuntu 22.04 GPU: 8 x NVIDIA H20-3e Model: GLM-5.1-FP8 (zai-org/GLM-5.1) Serve cmd: vllm serve /path/to/GLM-5.1-FP8 \ --tensor-parallel-size 8 \ --served-model-name GLM-5.1 \ --reasoning-parser glm45 \ --tool-call-parser glm47 \ --enable-auto-tool-choice \ --trust-remote-code ``` Per the official vLLM recipe for GLM-5 (`docs.vllm.ai/projects/recipes/en/latest/GLM/GLM5.html`), `--tool-call-parser glm47` is the recommended parser for GLM-5.1 — so this path is the canonical way to use GLM-5.1 with vLLM 0.19. ### 🐛 Describe the bug `Glm4MoeModelToolParser._is_string_type` (inherited by `Glm47MoeModelToolParser`) crashes with `AttributeError: 'FunctionTool' object has no attribute 'function'` during streaming tool calls on the `/v1/responses` endpoint. The SSE stream ends silently after `response.output_item.added` for the `function_call` item, never emitting `response.function_call_arguments.delta` / `.done` / `response.completed`, causing downstream clients (e.g., OpenAI Codex CLI) to disconnect with "stream closed before response.completed". **Root cause**: the parser assumes tools arrive in the `/v1/chat/completions` shape (...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nction' (affects GLM-4.5/4.7/5.1) ### Your current environment ``` vllm version: 0.19.0 OS: Ubuntu 22.04 GPU: 8 x NVIDIA H20-3e Model: GLM-5.1-FP8 (zai-org/GLM-5.1) Serve cmd: vllm serve /path/to/GLM-5.1-FP8 \ --tensor-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m version: 0.19.0 OS: Ubuntu 22.04 GPU: 8 x NVIDIA H20-3e Model: GLM-5.1-FP8 (zai-org/GLM-5.1) Serve cmd: vllm serve /path/to/GLM-5.1-FP8 \ --tensor-parallel-size 8 \ --served-model-name GLM-5.1 \ --reasoning-parser glm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tem.done` → `response.completed`. Happy to submit a PR with the fix + a small test covering the `/v1/responses` tool shape if that helps. ### Before submitting a new issue... - [x] Make sure you already searched for rel...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: glm4_moe_tool_parser._is_string_type crashes on /v1/responses streaming with 'FunctionTool' object has no attribute 'function' (affects GLM-4.5/4.7/5.1) ### Your current environment ``` vllm version: 0.19.0 OS: U...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: llm/blob/main/vllm/tool_parsers/glm4_moe_tool_parser.py#L120-L142 ### 🔁 Reproduce ```bash vllm serve zai-org/GLM-5.1 \ --tensor-parallel-size 8 \ --reasoning-parser glm45 \ --tool-call-parser glm47 \ --enable-auto-tool-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
