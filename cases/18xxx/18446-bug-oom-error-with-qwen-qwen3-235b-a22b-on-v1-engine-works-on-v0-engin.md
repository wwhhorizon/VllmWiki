# vllm-project/vllm#18446: [Bug]: OOM Error with `Qwen/Qwen3-235B-A22B` on V1 Engine, Works on V0 Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#18446](https://github.com/vllm-project/vllm/issues/18446) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM Error with `Qwen/Qwen3-235B-A22B` on V1 Engine, Works on V0 Engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to serve the Qwen/Qwen3-235B-A22B model, an Out of Memory (OOM) error occurs if the V1 engine is used. However, the model serves correctly when using the V0 engine. I used `--kwargs` as below (both of V0 and V1): ```bash --gpu-memory-utilization 0.90 --tensor-parallel-size=8 --enable-expert-parallel --max-model-len 32000 --seed 42 --enable-auto-tool-choice --tool-call-parser hermes ``` **Expected Behavior:** The model should serve correctly with the V1 engine without an OOM error, similar to its behavior with the V0 engine. **Actual Behavior:** An OOM error occurs when using the V1 engine. - related: #17327 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_erro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 327 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: OOM Error with `Qwen/Qwen3-235B-A22B` on V1 Engine, Works on V0 Engine bug ### Your current environment ### 🐛 Describe the bug When attempting to serve the Qwen/Qwen3-235B-A22B model, an Out of Memory (OOM) error...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: emory-utilization 0.90 --tensor-parallel-size=8 --enable-expert-parallel --max-model-len 32000 --seed 42 --enable-auto-tool-choice --tool-call-parser hermes ``` **Expected Behavior:** The model should serve correctly wi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;nan_inf;oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
