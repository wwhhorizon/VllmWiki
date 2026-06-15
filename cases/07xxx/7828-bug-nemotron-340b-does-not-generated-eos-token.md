# vllm-project/vllm#7828: [Bug]: Nemotron 340B does not generated EOS token

| 字段 | 值 |
| --- | --- |
| Issue | [#7828](https://github.com/vllm-project/vllm/issues/7828) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Nemotron 340B does not generated EOS token

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Nemotron 340b models implemented in #6611 are not generating the EOS token correctly. Some more information. Parameters: ``` max_tokens: 4096 max_context_length: 4096 temperature: 0.1 top_k: 50 top_p: 1.0 ``` Basic code: ``` sampling_params = SamplingParams( n=1, # TODO: allow multiple outputs per input; will affect batching in a few places temperature=self._generate_config.temperature, top_k=self._generate_config.top_k, top_p=self._generate_config.top_p, max_tokens=max_tokens, detokenize=False, # we defer this since it can be CPU-intensive ) ``` Example: ``` "outputs": [{"index": 0, "text": "\n\n\n\n\n\n\n\n\n\nThe answer is \"beehive\" because this type of structure is known for housing what kind of animal?\n\nThe question is: \"What type of structure is known for housing bees?\" A beehive is the correct answer as it is designed to be the dwelling place for a colony of bees.\nAnswer: The question that would justify the answer \"beehive\" is \"What type of structure is known for housing bees?\" This is because a beehive is specifically designed and used as a home for a colony of bees, making it the most appropriate and accurate...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e of the earliest known pieces of literature, exploring themes of friendship, loss, and the human condition.\n\n2. **The Iliad and The Odyssey by Homer (circa 8th century BCE)**: These epic poems have significantly infl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e ### Your current environment ### 🐛 Describe the bug Nemotron 340b models implemented in #6611 are not generating the EOS token correctly. Some more information. Parameters: ``` max_tokens: 4096 max_context_length: 409...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: f structure is known for housing bees?\" This is because a beehive is specifically designed and used as a home for a colony of bees, making it the most appropriate and accurate answer to the question.\n\nWhat are some o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: self._generate_config.top_p, max_tokens=max_tokens, detokenize=False, # we defer this since it can be CPU-intensive ) ``` Example: ``` "outputs": [{"index": 0, "text": "\n\n\n\n\n\n\n\n\n\nThe answer is \"beehive\" beca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Nemotron 340B does not generated EOS token bug;stale ### Your current environment ### 🐛 Describe the bug Nemotron 340b models implemented in #6611 are not generating the EOS token correctly. Some more information...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
