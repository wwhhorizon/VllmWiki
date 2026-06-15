# vllm-project/vllm#26584: [Bug]: gpt-oss-20B output quality issues (I suspect a bug)

| 字段 | 值 |
| --- | --- |
| Issue | [#26584](https://github.com/vllm-project/vllm/issues/26584) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: gpt-oss-20B output quality issues (I suspect a bug)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As usual with this kind of issue, there is no easy way to reproduce this. Let's look at the symptoms first: **Example 1: Invented word ("wementeilen")** The word does not exist, but "sounds" correct. **Example 2: Sudden script change** A completely out-of-context word in another script appears in the output. I have observed similar outputs in many examples in the last days, running the original gpt-oss-20b on vLLM 0.11.0. I find it very unlikely that gpt-oss-20b actually would generate these tokens in these situations. This is why I suspect that the issue might be a bug in the inference code. Any ideas what could be causing this? If someone can suggest what code to inspect, I could maybe help finding the issue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gpt-oss-20B output quality issues (I suspect a bug) bug;stale ### Your current environment ### 🐛 Describe the bug As usual with this kind of issue, there is no easy way to reproduce this. Let's look at the sympto...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: gpt-oss-20B output quality issues (I suspect a bug) bug;stale ### Your current environment ### 🐛 Describe the bug As usual with this kind of issue, there is no easy way to reproduce this. Let's look at the sympto...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
