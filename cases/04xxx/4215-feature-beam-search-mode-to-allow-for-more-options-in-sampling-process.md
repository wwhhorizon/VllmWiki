# vllm-project/vllm#4215: [Feature]: beam search mode to allow for more options in sampling process

| 字段 | 值 |
| --- | --- |
| Issue | [#4215](https://github.com/vllm-project/vllm/issues/4215) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: beam search mode to allow for more options in sampling process

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current implementation of beam search is a very simplified version, which seems to follow the description in the paper "Sequence to Sequence Learning with Neural Networks": > a simple left-to-right beam search decoder which maintains a small number B of partial hypotheses, where a partial hypothesis is a prefix of some translation. At each timestep we extend each partial hypothesis in the beam with every possible word in the vocabulary. This greatly increases the number of the hypotheses so we discard all but the B most likely hypotheses according to the model’s log probability. As soon as the“ ” symbol is appended to a hypothesis, it is removed from the beam and is added to the set of complete hypotheses. The beam search outcomes is predominantly influenced by the beam width when responding to a specific prompt, which can significantly constrain the creativity of the generated outputs. Creativity is a critical component in many LLM applications. I would like to support more options in beam search, i.e., be able to set non-zero temperature, top_k and top_p in the sampling parameter. It is currently denied by the function: ``` def _verify...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : beam search mode to allow for more options in sampling process feature request;stale ### 🚀 The feature, motivation and pitch The current implementation of beam search is a very simplified version, which seems to follo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nd pitch The current implementation of beam search is a very simplified version, which seems to follow the description in the paper "Sequence to Sequence Learning with Neural Networks": > a simple left-to-right beam sea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: beam search mode to allow for more options in sampling process feature request;stale ### 🚀 The feature, motivation and pitch The current implementation of beam search is a very simplified version, which seems...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eses so we discard all but the B most likely hypotheses according to the model’s log probability. As soon as the“ ” symbol is appended to a hypothesis, it is removed from the beam and is added to the set of complete hyp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
