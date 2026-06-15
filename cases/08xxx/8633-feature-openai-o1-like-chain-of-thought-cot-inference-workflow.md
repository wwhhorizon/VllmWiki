# vllm-project/vllm#8633: [Feature]: OpenAI o1-like Chain-of-thought (CoT) inference workflow

| 字段 | 值 |
| --- | --- |
| Issue | [#8633](https://github.com/vllm-project/vllm/issues/8633) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: OpenAI o1-like Chain-of-thought (CoT) inference workflow

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Well, I am surprised that the "main" and "great" new feature of the new OpenAI o1 model is actually doing say "more sophisticated" inference workflow while employing something like Chain-of-thought process. Basically I understand it that even a "dumb" model can perform much better when it "thinks more" during inference. The great news they are telling us is that by "thinking more" you can get smarter, which is probably very true also for humans. The o1 model is probably trained to come up with its own CoT workflow for any given prompt, but I think it could be interesting to try to even hardcode some kind of workflow which any standard LLM model may try to follow during inference. Basically let the model analyze the prompt from various perspectives first and then try to judge on what type of "inference workflow" it should employ. The hardcoded workflow could look like this: 1. Prompt is submitted to the model. 2. The model asks itself couple of hard-coded questions about the prompt, maybe: - is that some light conversation (needing soft-skills like empathy etc) - does it look like a science problem (math, physics etc.) - can I break the promp...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he great news they are telling us is that by "thinking more" you can get smarter, which is probably very true also for humans. The o1 model is probably trained to come up with its own CoT workflow for any given prompt,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m surprised that the "main" and "great" new feature of the new OpenAI o1 model is actually doing say "more sophisticated" inference workflow while employing something like Chain-of-thought process. Basically I understan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ature]: OpenAI o1-like Chain-of-thought (CoT) inference workflow feature request;stale ### 🚀 The feature, motivation and pitch Well, I am surprised that the "main" and "great" new feature of the new OpenAI o1 model is a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nversation (needing soft-skills like empathy etc) - does it look like a science problem (math, physics etc.) - can I break the prompt down to subtasks - if yes, the workflow will feed each subtask into the model separat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
