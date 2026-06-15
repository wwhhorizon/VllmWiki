# vllm-project/vllm#37343: [Bug]: n_completions + logprobs Causes Significant TTFT Spike for Co-Scheduled Requests on Cold Cache

| 字段 | 值 |
| --- | --- |
| Issue | [#37343](https://github.com/vllm-project/vllm/issues/37343) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: n_completions + logprobs Causes Significant TTFT Spike for Co-Scheduled Requests on Cold Cache

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## My current environment in short ``` Model: Qwen/Qwen2.5-0.5B-Instruct vLLM version: (tested on current main) GPU: NVIDIA RTX A6000 CUDA version: 12.x Python: 3.10 ``` Launch command: ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen2.5-0.5B-Instruct \ --port 8000 \ --gpu-memory-utilization 0.95 \ --max-model-len 32768 \ --enable-prefix-caching \ --disable-log-requests ``` This is found in the same round of 12 hours fuzzing done to vLLM as in #37308 and #37076 We found that a single request carrying `n_completions=8` and `logprobs=20` causes a **76–423× TTFT regression** for every other request co-scheduled in the same batch, confirmed across 10 independent runs. The expensive request itself is not the victim, it only generates 16 tokens and completes within its own budget. The victims are the plain co-scheduled requests that are forced to share every decode iteration with it. Their TTFT goes from an expected ~46ms to **3524ms p99** (76×), with worst-case single samples reaching **19678ms** (423×) in one reproduction. This was found via automated fuzzing (finding_01758, seed 199991774) and confirmed acros...

## 现有链接修复摘要

#37594 [Bugfix] fixd issue#37343: prevent TTFT regression by adding batched logprobs budget to scheduler

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment in short ``` Model: Qwen/Qwen2.5-0.5B-Instruct vLLM version: (tested on current main) GPU: NVIDIA RTX A6000 CUDA version: 12.x Python: 3.10 ``` Launch command: ```bash python -m vllm.entrypoints.open...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Qwen2.5-0.5B-Instruct vLLM version: (tested on current main) GPU: NVIDIA RTX A6000 CUDA version: 12.x Python: 3.10 ``` Launch command: ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen2.5-0.5B-Ins...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: n_completions + logprobs Causes Significant TTFT Spike for Co-Scheduled Requests on Cold Cache bug ### Your current environment ### 🐛 Describe the bug ## My current environment in short ``` Model: Qwen/Qwen2.5-0.5B-Inst...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: **This is a different root cause from the chunked-prefill head-of-line blocking bug #37308 .** Enabling `--enable-chunked-prefill` does not help here. The regression occurs entirely in the decode phase and is caused by...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ment ### 🐛 Describe the bug ## My current environment in short ``` Model: Qwen/Qwen2.5-0.5B-Instruct vLLM version: (tested on current main) GPU: NVIDIA RTX A6000 CUDA version: 12.x Python: 3.10 ``` Launch command: ```ba...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37594](https://github.com/vllm-project/vllm/pull/37594) | closes_keyword | 0.95 | [Bugfix] fixd issue#37343: prevent TTFT regression by adding batched logprobs budget to scheduler | Fixes #37343 ## Test Plan 1. **Environment:** NVIDIA RTX A40, CUDA 12.2, Model: `Qwen/Qwen2.5-0.5B-Instruct`. 2. **Reproduction:** Run the fuzzing reproduction script (`rep |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
