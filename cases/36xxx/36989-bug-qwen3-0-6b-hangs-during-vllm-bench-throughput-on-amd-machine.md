# vllm-project/vllm#36989: [Bug]: Qwen3-0.6B hangs during `vllm bench throughput` on amd machine

| 字段 | 值 |
| --- | --- |
| Issue | [#36989](https://github.com/vllm-project/vllm/issues/36989) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-0.6B hangs during `vllm bench throughput` on amd machine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running `vllm bench throughput --model Qwen/Qwen3-0.6B --enforce-eager` consistently hangs around processed prompts: 52%. This hangs until the benchmark eventually times out This works fine for me with other models e.g. --model Qwen/Qwen2.5-0.5B ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#39111 [ROCm] Set HSA_NO_SCRATCH_RECLAIM=1 in platform init for non-Docker users

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: test/), which can answer lots of frequently asked questions. performance ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;slowdow...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Bug]: Qwen3-0.6B hangs during `vllm bench throughput` on amd machine bug;rocm ### Your current environment ### 🐛 Describe the bug Running `vllm bench throughput --model Qwen/Qwen3-0.6B --enforce-eager` consistently hang...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Qwen3-0.6B hangs during `vllm bench throughput` on amd machine bug;rocm ### Your current environment ### 🐛 Describe the bug Running `vllm bench throughput --model Qwen/Qwen3-0.6B --enforce-eager` consistently han...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-0.6B hangs during `vllm bench throughput` on amd machine bug;rocm ### Your current environment ### 🐛 Describe the bug Running `vllm bench throughput --model Qwen/Qwen3-0.6B --enforce-eager` consistently han...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;slowdown env_dependency #39111 [ROCm] Set HSA_NO_SCRATCH_RECLAIM=1 in platform init for non-Docker users Your current environme...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39111](https://github.com/vllm-project/vllm/pull/39111) | closes_keyword | 0.95 | [ROCm] Set HSA_NO_SCRATCH_RECLAIM=1 in platform init for non-Docker users | Fixes #36989 Signed-off-by: Bortlesboat <bortlesboat@users.noreply.github.com> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
