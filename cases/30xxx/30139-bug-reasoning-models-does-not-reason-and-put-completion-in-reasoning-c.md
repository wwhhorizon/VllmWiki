# vllm-project/vllm#30139: [Bug]: Reasoning models does not reason and put completion in reasoning_content

| 字段 | 值 |
| --- | --- |
| Issue | [#30139](https://github.com/vllm-project/vllm/issues/30139) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Reasoning models does not reason and put completion in reasoning_content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deploy the model: ``` sh uv pip install vllm==0.11.2 # issue is still valid for ancient and recent versions of VLLM uv run vllm serve mistralai/Magistral-Small-2509 --reasoning-parser mistral --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --limit-mm-per-prompt '{"image":10}' --tensor-parallel-size 1 --host 0.0.0.0 --enable-prompt-tokens-details ``` See [deploying logs](https://gist.github.com/Rictus/dad1be8beff9f90a27c9d0355104146f) Send this payload to `/v1/chat/completions`: ``` json { "messages": [ { "content": "hello", "role": "user" } ], "model": "mistralai/Magistral-Small-2509", "max_completion_tokens": 2000, "seed": 0, "stop": [], "temperature": 0, "top_p": 0.4, "reasoning_effort": "low", "include_reasoning": true } ``` I get this response: ``` json { "id": "chatcmpl-a86ec69adc404dbe87800bdd7a269fad", "object": "chat.completion", "created": 1764947491, "model": "mistralai/Magistral-Small-2509", "choices": [ { "index": 0, "message": { "role": "assistant", "content": null, "refusal": null, "annotations": null, "audio": null, "function_call": null, "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: environment ### 🐛 Describe the bug Deploy the model: ``` sh uv pip install vllm==0.11.2 # issue is still valid for ancient and recent versions of VLLM uv run vllm serve mistralai/Magistral-Small-2509 --reasoning-parser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ncient and recent versions of VLLM uv run vllm serve mistralai/Magistral-Small-2509 --reasoning-parser mistral --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Reasoning models does not reason and put completion in reasoning_content bug ### Your current environment ### 🐛 Describe the bug Deploy the model: ``` sh uv pip install vllm==0.11.2 # issue is still valid for anc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
