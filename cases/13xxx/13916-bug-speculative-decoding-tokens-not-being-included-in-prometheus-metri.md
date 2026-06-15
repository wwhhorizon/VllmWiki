# vllm-project/vllm#13916: [Bug]: Speculative Decoding Tokens not being included in Prometheus metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#13916](https://github.com/vllm-project/vllm/issues/13916) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding Tokens not being included in Prometheus metrics

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For then following metric ``` self.counter_generation_tokens = self._counter_cls( name="vllm:generation_tokens_total", documentation="Number of generation tokens processed.", labelnames=labelnames) ``` It does not get updated properly when doing speculative decoding (only half) Issue lies in the calculating of how much to increment by ``` # Number of generation tokens. # num_batched_tokens equals the number of prompt_tokens plus the # number of decode_tokens in a single iteration. So, # num_generation_tokens = num_batched_tokens - num_prompt_tokens # + num_generation_tokens_from_prefill_groups (since we generate # one token on prefills on iters where the prefill finishes). num_generation_tokens_iter = ( actual_num_batched_tokens - num_prompt_tokens_iter + num_generation_tokens_from_prefill_groups) num_tokens_iter = (num_generation_tokens_iter + num_prompt_tokens_iter)``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked question...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Speculative Decoding Tokens not being included in Prometheus metrics bug;stale ### Your current environment ### 🐛 Describe the bug For then following metric ``` self.counter_generation_tokens = self._counte
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
