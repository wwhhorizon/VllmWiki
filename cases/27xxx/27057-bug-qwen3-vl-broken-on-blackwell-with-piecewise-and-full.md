# vllm-project/vllm#27057: [Bug]: Qwen3-VL broken on Blackwell with `PIECEWISE_AND_FULL`

| 字段 | 值 |
| --- | --- |
| Issue | [#27057](https://github.com/vllm-project/vllm/issues/27057) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Qwen3-VL broken on Blackwell with `PIECEWISE_AND_FULL`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug All Qwen3-VL models have significant quality drops on B200 with default `PIECEWISE_AND_FULL` cuda graph settings. However, when launching with `-O.cudagraph_mode=PIECEWISE` the issue goes away. It's been also confirmed that this is a B200 issue in particular, as the default cuda graph setting works fine on L40s, A100 and H200. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Qwen3-VL broken on Blackwell with `PIECEWISE_AND_FULL` bug ### Your current environment ### 🐛 Describe the bug All Qwen3-VL models have significant quality drops on B200 with default `PIECEWISE_AND_FULL` cuda gra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-VL broken on Blackwell with `PIECEWISE_AND_FULL` bug ### Your current environment ### 🐛 Describe the bug All Qwen3-VL models have significant quality drops on B200 with default `PIECEWISE_AND_FULL` cuda gra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
