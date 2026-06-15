# vllm-project/vllm#34326: [Bug]: --served-model-name causes model detection issues

| 字段 | 值 |
| --- | --- |
| Issue | [#34326](https://github.com/vllm-project/vllm/issues/34326) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --served-model-name causes model detection issues

### Issue 正文摘录

### Your current environment ```Dockerfile FROM vllm/vllm-openai:nightly AS audio RUN uv pip install --system --no-cache-dir mistral-common[soundfile] RUN uv pip install --system 'vllm[audio]' ``` ### 🐛 Describe the bug running `vllm serve Qwen/Qwen3-ASR-1.7B` sets the model correctly ``` (APIServer pid=839) INFO 02-11 09:08:42 [utils.py:287] (APIServer pid=839) INFO 02-11 09:08:42 [utils.py:287] █ █ █▄ ▄█ (APIServer pid=839) INFO 02-11 09:08:42 [utils.py:287] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.2rc1.dev119+g7c233dbb3 (APIServer pid=839) INFO 02-11 09:08:42 [utils.py:287] █▄█▀ █ █ █ █ model Qwen/Qwen3-ASR-1.7B (APIServer pid=839) INFO 02-11 09:08:42 [utils.py:287] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=839) INFO 02-11 09:08:42 [utils.py:287] ``` whereas running `vllm serve --served-model-name ASR Qwen/Qwen3-ASR-1.7B` doesn't ``` (APIServer pid=888) INFO 02-11 09:09:31 [utils.py:287] (APIServer pid=888) INFO 02-11 09:09:31 [utils.py:287] █ █ █▄ ▄█ (APIServer pid=888) INFO 02-11 09:09:31 [utils.py:287] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.2rc1.dev119+g7c233dbb3 (APIServer pid=888) INFO 02-11 09:09:31 [utils.py:287] █▄█▀ █ █ █ █ model Qwen/Qwen3-0.6B (APIServer pid=888) INFO 02-11 09:09:31 [utils.py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: -name causes model detection issues bug ### Your current environment ```Dockerfile FROM vllm/vllm-openai:nightly AS audio RUN uv pip install --system --no-cache-dir mistral-common[soundfile] RUN uv pip install --system...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ent ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: --served-model-name causes model detection issues bug ### Your current environment ```Dockerfile FROM vllm/vllm-openai:nightly AS audio RUN uv pip install --system --no-cache-dir mistral-common[soundfile] RUN uv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
