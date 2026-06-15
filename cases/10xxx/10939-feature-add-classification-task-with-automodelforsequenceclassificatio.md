# vllm-project/vllm#10939: [Feature]: Add classification Task with AutoModelForSequenceClassification and BertForSequenceClassification

| 字段 | 值 |
| --- | --- |
| Issue | [#10939](https://github.com/vllm-project/vllm/issues/10939) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add classification Task with AutoModelForSequenceClassification and BertForSequenceClassification

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Latest Version: `v0.6.4.post1` **Summary:** I would like to request support for using BERT and DistilBERT models for **classification tasks**. As of `v0.6.4.post1`, `BertForSequenceClassification` is only available for Sentence Pair Scoring tasks via the Score API. **Detail:** With a recent Pull Request, #9704 `Qwen2ForSequenceClassification` became available for text classification tasks. This is a fantastic improvement! However, in text multi-classification tasks, models other than Qwen2 are often preferred due to the following reasons: - Limited multilingual support in Qwen2. - A larger number of parameters in Qwen2, leading to longer inference times. BERT and DistilBERT, which have been extensively researched and fine-tuned for a wide range of languages, often achieve better classification accuracy and faster inference times. These models are frequently integrated into applications as local LLMs, making them an excellent fit for vLLM's role as a high-speed inference accelerator. Currently, if we try to execute code for text classification using BERT or DistilBERT models in the same manner as the sample code for Qwen2, the following error...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Feature]: Add classification Task with AutoModelForSequenceClassification and BertForSequenceClassification feature request;stale ### 🚀 The feature, motivation and pitch Latest Version: `v0.6.4.post1` **Summary:** I wo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: on feature request;stale ### 🚀 The feature, motivation and pitch Latest Version: `v0.6.4.post1` **Summary:** I would like to request support for using BERT and DistilBERT models for **classification tasks**. As of `v0.6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: inference times. BERT and DistilBERT, which have been extensively researched and fine-tuned for a wide range of languages, often achieve better classification accuracy and faster inference times. These models are freque...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ModelForSequenceClassification and BertForSequenceClassification feature request;stale ### 🚀 The feature, motivation and pitch Latest Version: `v0.6.4.post1` **Summary:** I would like to request support for using BERT a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
