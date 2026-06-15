# vllm-project/vllm#9314: [RFC]: Let every model be a reward model/embedding model for PRMs

| 字段 | 值 |
| --- | --- |
| Issue | [#9314](https://github.com/vllm-project/vllm/issues/9314) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Let every model be a reward model/embedding model for PRMs

### Issue 正文摘录

### Motivation. As the openai o1 series of models gave us a peek on the great potential of RL, the interest on reward model, as a core component of model RL algorithms, are rising. Recently, we have tried to introduce new reward models into vllm by reusing embedding APIs (https://github.com/vllm-project/vllm/pull/8896) and have ongoing RFC to discuss a better server API for reward model specifically (https://github.com/vllm-project/vllm/issues/8967). This RFC is trying to introduce a broader class of RMs by making all generation models be able to be served as embedding models. In this way, vllm could easily support process-supervised reward model (PRM). PRM is a kind of rewad model that will give reward score on the intermediate steps of an llm response. For example, in cot, when the model is thinking step by step, prm could make a judgement on each thinking step, which gives a finer granularity for RL optimization. Also, many are guessing that PRM is a cruial component to replicate o1, e.g. [GAIR-NLP/O1-Journey](https://github.com/GAIR-NLP/O1-Journey). A common way to train PRM is to add an special token after each step, and use the output logits of the special token, to be more...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Let every model be a reward model/embedding model for PRMs RFC ### Motivation. As the openai o1 series of models gave us a peek on the great potential of RL, the interest on reward model, as a core component of m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: estimation in PRM training (contrary to soft estimation, which will do a regression instead of a classfication) and is used in the famous Let's Verify Step by Step (https://arxiv.org/abs/2305.20050) by openai, who also...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and have ongoing RFC to discuss a better server API for reward model specifically (https://github.com/vllm-project/vllm/issues/8967). This RFC is trying to introduce a broader class of RMs by making all generation model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: C:) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: oler( self, hidden_states: torch.Tensor, pooling_metadata: PoolingMetadata, ) -> Optional[PoolerOutput]: # we can trim the lm_head by calculating the hidden_states @ lm_head # and doing pooling at the same time. return...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
