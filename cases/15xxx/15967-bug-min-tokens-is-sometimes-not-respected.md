# vllm-project/vllm#15967: [Bug]: min_tokens is sometimes not respected

| 字段 | 值 |
| --- | --- |
| Issue | [#15967](https://github.com/vllm-project/vllm/issues/15967) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: min_tokens is sometimes not respected

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am setting `min_tokens` in my `SamplingParams` but I sometimes see requests that generate fewer than `min_tokens` tokens. Here is how I set up my `SamplingParams`: ```Python num_output_tokens = 128 # could be arbitrary sampling_params = SamplingParams( temperature=temperature, min_tokens=num_output_tokens, max_tokens=num_output_tokens, seed=seed, ignore_eos=True, stop_token_ids=[-1], ) ``` I have seen the same bug whether or not I set `ignore_eos` and `stop_token_ids`, but unfortunately I don't have a deterministic reproduction. I also saw that #15407 fixed an issue with `min_tokens` but I have this PR in my installation.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: aw that #15407 fixed an issue with `min_tokens` but I have this PR in my installation. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;sampling_logits cuda;triton build_error;nondeterministic env...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: set `ignore_eos` and `stop_token_ids`, but unfortunately I don't have a deterministic reproduction. I also saw that #15407 fixed an issue with `min_tokens` but I have this PR in my installation. correctness ci_build;dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: min_tokens is sometimes not respected bug;stale ### Your current environment ### 🐛 Describe the bug I am setting `min_tokens` in my `SamplingParams` but I sometimes see requests that generate fewer than `min_toke...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;distributed_parallel;frontend_api;hardware_porting;sampling_logits cuda;triton build_error;nondeterministic env_dependency;race_condition Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: build;distributed_parallel;frontend_api;hardware_porting;sampling_logits cuda;triton build_error;nondeterministic env_dependency;race_condition Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
