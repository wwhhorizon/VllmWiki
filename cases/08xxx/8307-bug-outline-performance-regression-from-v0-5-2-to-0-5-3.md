# vllm-project/vllm#8307: [BUG]: Outline performance regression from v0.5.2 to 0.5.3

| 字段 | 值 |
| --- | --- |
| Issue | [#8307](https://github.com/vllm-project/vllm/issues/8307) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUG]: Outline performance regression from v0.5.2 to 0.5.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In our setup, vLLM's structured generation became 2x slower from 0.5.2 to 0.5.3. The regression was introduced with this [commit](https://github.com/vllm-project/vllm/commit/185ad31f37541ac205b55f446bfd71542f83075). It mainly replaced the LRUCache annotation on the `_get_guide` function of the LogitsProcessor in favor of the `@cache` implementation from Outlines, so the cache function outputs can be reused across startup. However, this seems to have a significant impact on performance. Not totally sure why, one hypothesis is that Outlines' diskcache-based implementation is not as efficient. Adding back the LRUCache on top of the Outlines one seems to fix this performance issue. This [PR](https://github.com/vllm-project/vllm/pull/8308) contains those changes. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#8308 [Bugfix] Reenable LRU cache on Outlines' guide getters

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ypothesis is that Outlines' diskcache-based implementation is not as efficient. Adding back the LRUCache on top of the Outlines one seems to fix this performance issue. This [PR](https://github.com/vllm-project/vllm/pul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [BUG]: Outline performance regression from v0.5.2 to 0.5.3 bug;stale ### Your current environment ### 🐛 Describe the bug In our setup, vLLM's structured generation became 2x slower from 0.5.2 to 0.5.3. The regression wa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ots of frequently asked questions. performance ci_build;hardware_porting;model_support cuda;operator build_error;slowdown env_dependency #8308 [Bugfix] Reenable LRU cache on Outlines' guide getters Your current environm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [BUG]: Outline performance regression from v0.5.2 to 0.5.3 bug;stale ### Your current environment ### 🐛 Describe the bug In our setup, vLLM's structured generation became 2x slower from 0.5.2 to 0.5.3. The regression wa...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8308](https://github.com/vllm-project/vllm/pull/8308) | closes_keyword | 0.95 | [Bugfix] Reenable LRU cache on Outlines' guide getters | FIX #8307 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
