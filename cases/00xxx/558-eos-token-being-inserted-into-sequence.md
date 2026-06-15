# vllm-project/vllm#558: EOS token being inserted into sequence. 

| 字段 | 值 |
| --- | --- |
| Issue | [#558](https://github.com/vllm-project/vllm/issues/558) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> EOS token being inserted into sequence. 

### Issue 正文摘录

Hey guys, first thanks for VLLM, its insanely good!! When ignore EOS token is used, it inserts it into the sentence and it is not ignored by the model. So although the model keeps generating the EOS token is no part of the sequence, which causes issues. I have found this when using this model: When using https://huggingface.co/ehartford/Wizard-Vicuna-13B-Uncensored. Usually when generating using HF. If a special token was encountered it would not be included in the generated text. However here it appears ` ` is placed into the generations often, causing degradation. Thank you!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: en is used, it inserts it into the sentence and it is not ignored by the model. So although the model keeps generating the EOS token is no part of the sequence, which causes issues. I have found this when using this mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Wizard-Vicuna-13B-Uncensored. Usually when generating using HF. If a special token was encountered it would not be included in the generated text. However here it appears ` ` is placed into the generations often, causin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
