# vllm-project/vllm#29448: [Bug]: DeepSeek R1 MTP Model Loading Broken on H200

| 字段 | 值 |
| --- | --- |
| Issue | [#29448](https://github.com/vllm-project/vllm/issues/29448) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: DeepSeek R1 MTP Model Loading Broken on H200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Via bisection, #27563 appears to have broken MTP model loading for DeepSeek R1 (tested on H200): ```python vllm serve deepseek-ai/DeepSeek-R1 --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' -dp 8 --enable-expert-parallel ``` result: * on commit `68dfe28ea` (immediately prior): server starts successfully * on commit `8005e606` (PR commit): server crashes during startup, yielding: ``` KeyError: 'model.layers.61.mtp_block.mlp.experts.195.down_proj.weight' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#27563 [Bugfix][Rocm] Fix shared expert weight loading failure in DeepSeek-MTP | #29545 [Bugfix] Fix DeepSeek R1 MTP weight loading

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: e-config '{"method": "mtp", "num_speculative_tokens": 1}' -dp 8 --enable-expert-parallel ``` result: * on commit `68dfe28ea` (immediately prior): server starts successfully * on commit `8005e606` (PR commit): server cra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: DeepSeek R1 MTP Model Loading Broken on H200 bug ### Your current environment ### 🐛 Describe the bug Via bisection, #27563 appears to have broken MTP model loading for DeepSeek R1 (tested on H200): ```python vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;crash;nan_inf env_dependency #27563 [Bugfix][Rocm] Fix shared expert weight loading failure in DeepSeek-MTP | #29545 [Bugfix] F...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27563](https://github.com/vllm-project/vllm/pull/27563) | mentioned | 0.45 | [Bugfix][Rocm] Fix shared expert weight loading failure in DeepSeek-MTP | le_threads=1 ``` </details> ### 🐛 describe the bug via bisection, #27563 appears to have broken mtp model loading for deepseek r1 (tested on h200): ```python vllm serve deepseek-a… |
| [#29545](https://github.com/vllm-project/vllm/pull/29545) | closes_keyword | 0.95 | [Bugfix] Fix DeepSeek R1 MTP weight loading | Fixes #29448 by adding some logic from `deepseek_v2.py` that was missing in `deepseek_mtp.py` ## Test Plan ``` vllm serve deepseek-ai/DeepSeek-R1 \ --speculative-config '{"met |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
