# vllm-project/vllm#20247: [Bug]: Scheduler and GPUModelRunner have inconsistent output_token_ids when speculative decoding is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#20247](https://github.com/vllm-project/vllm/issues/20247) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Scheduler and GPUModelRunner have inconsistent output_token_ids when speculative decoding is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With vLLM v1, there's an inconsistency between the `output_token_ids` maintained by the scheduler and the GPU model runner when speculative decoding is enabled. The scheduler contains more tokens than the GPU model runner. ## Root Cause Analysis ### GPU Model Runner Side (`v1/worker/gpu_model_runner.py`) The GPU model runner updates its token list using `CachedRequestData.new_token_ids`: ```python def _update_states(self, scheduler_output: "SchedulerOutput") -> None: ... if num_new_tokens == 1: # Avoid slicing list in most common case. req_state.output_token_ids.append(req_data.new_token_ids[-1]) elif num_new_tokens > 0: req_state.output_token_ids.extend( req_data.new_token_ids[-num_new_tokens:]) ``` ### Scheduler Side (`v1/core/sched/scheduler.py`) However, the scheduler's `_make_cached_request_data` method determines `new_token_ids` based on **currently scheduled spec tokens**, which fails to account for tokens that were accepted from speculative decoding in **previous steps**: ```python def _make_cached_request_data( self, request: Request, num_scheduled_tokens: int, num_scheduled_spec_tokens: int, new_block_ids: tuple[list[in...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Scheduler and GPUModelRunner have inconsistent output_token_ids when speculative decoding is enabled bug;stale ### Your current environment ### 🐛 Describe the bug With vLLM v1, there's an inconsistency between th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Output") -> None: ... if num_new_tokens == 1: # Avoid slicing list in most common case. req_state.output_token_ids.append(req_data.new_token_ids[-1]) elif num_new_tokens > 0: req_state.output_token_ids.extend( req_data....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ner ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: num_scheduled_tokens: int, num_scheduled_spec_tokens: int, new_block_ids: tuple[list[int], ...], resumed_from_preemption: bool, ) -> CachedRequestData: num_computed_tokens = request.num_computed_tokens num_regular_token...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
