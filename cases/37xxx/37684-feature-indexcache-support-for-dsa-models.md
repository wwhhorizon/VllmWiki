# vllm-project/vllm#37684: [Feature]: IndexCache support for DSA models

| 字段 | 值 |
| --- | --- |
| Issue | [#37684](https://github.com/vllm-project/vllm/issues/37684) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: IndexCache support for DSA models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Z.ai released IndexCache based on their research with a claim of 1.2-1.8.x performance increase for DSA models. At least some providers seem to have already included them with some success (see below). It'd be great to have this patch included natively, though I'm not exactly sure if it would need to be a bit more defensive/optional than what's provided in the research repository. I guess if the upcoming DeepSeek V4 retains the DSA architecture, vLLM might also benefit from a native performance boost. ### Alternatives Manually maintaining the vLLM patch from https://github.com/THUDM/IndexCache/blob/main/indexcache_vllm.patch - not a fun prospect. ### Additional context Sources: * arxiv: https://arxiv.org/abs/2603.12201 * HF: https://huggingface.co/papers/2603.12201 * GitHub patches (vLLM + sglang): https://github.com/THUDM/IndexCache/ * x.com thread: https://x.com/realYushiBai/status/2032299919999189107 Existing implementations: * chutes.ai sglang fork: https://github.com/chutesai/sglang/pull/12 * omlx: https://github.com/jundot/omlx/pull/214 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: IndexCache support for DSA models feature request ### 🚀 The feature, motivation and pitch Z.ai released IndexCache based on their research with a claim of 1.2-1.8.x performance increase for DSA models. At lea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ature, motivation and pitch Z.ai released IndexCache based on their research with a claim of 1.2-1.8.x performance increase for DSA models. At least some providers seem to have already included them with some success (s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: IndexCache support for DSA models feature request ### 🚀 The feature, motivation and pitch Z.ai released IndexCache based on their research with a claim of 1.2-1.8.x performance increase for DSA models. At lea...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
