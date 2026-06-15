# vllm-project/vllm#13129: [Bug]: IndexError: pop from empty list For Jamba

| 字段 | 值 |
| --- | --- |
| Issue | [#13129](https://github.com/vllm-project/vllm/issues/13129) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: IndexError: pop from empty list For Jamba

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Similar to https://github.com/vllm-project/vllm/issues/10693 In the current implementation of `MambaCacheManager._assign_seq_id_to_cache_index`, if `cur_id` is not amongst the finished requests, it will try to pop a free_cache_index. I think there are still corner cases where `free_cache_indices` can be empty. One possibilities is that: 1. All requests to async_llm_eng are aborted, aborted requests are added to [_finished_requests_ids](https://github.com/vllm-project/vllm/blob/72c2b68dc9d4fb20eb135c22ee8c86caca48d28b/vllm/core/scheduler.py#L482); 2. In [step_async](https://github.com/vllm-project/vllm/blob/e92694b6fe264a85371317295bca6643508034ef/vllm/engine/async_llm_engine.py#L306), _finished_requests_ids are put in to a `finished_requests_ids` temp var and cleared; 3. However, there is no guarantee `finished_requests_ids` will be passed into [execute_model_async](https://github.com/vllm-project/vllm/blob/main/vllm/engine/async_llm_engine.py#L353-L354), because [`scheduler_output.is_empty`](https://github.com/vllm-project/vllm/blob/e92694b6fe264a85371317295bca6643508034ef/vllm/engine/async_llm_engine.py#L326) 4. As a result, we...

## 现有链接修复摘要

#41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory cuda;operator;quantization...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: IndexError: pop from empty list For Jamba bug;stale ### Your current environment ### 🐛 Describe the bug Similar to https://github.com/vllm-project/vllm/issues/10693 In the current implementation of `MambaCacheMan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0b4 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ion;sampling_logits;scheduler_memory cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update gr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: lt, we never get back these cache index; For this theory, I was able to reproduce. Below stack trace is another one we found from our prod environment. Full stacktrace: https://gist.github.com/sfc-gh-zhwang/3ab28417edbb...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13129">#13129</a></li> </ul> <h2>v2.13.3 (2026-04-20)</h2> <p><a href="https://github.com/pydantic/pydantic/releases… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13129">#13129</a></li> </ul> <h2>v2.13.3 (2026-04-20)</h2> <p><a href="https://github.com/pydantic/pydantic/releases… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13129">#13129</a></li> </ul> <h2>v2.13.3 (2026-04-20)</h2> <p><a href="https://github.com/pydantic/pydantic/releases… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13129">#13129</a></li> </ul> <h2>v2.13.3 (2026-04-20)</h2> <p><a href="https://github.com/pydantic/pydantic/releases… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13129">#13129</a></li> </ul> <h2>v2.13.3 (2026-04-20)</h2> <p><a href="https://github.com/pydantic/pydantic/releases… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
