# vllm-project/vllm#956: 15% less speed after rotary_embedding_neox_kernel update in #592

| 字段 | 值 |
| --- | --- |
| Issue | [#956](https://github.com/vllm-project/vllm/issues/956) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 15% less speed after rotary_embedding_neox_kernel update in #592

### Issue 正文摘录

After this loop was introduced in #592, the speed of execution of my 7B LLaMa model decreased by roughly 15%. This is due to the extra for-loop that is executed. I believe there is a **low-hanging fruit** in implementing an if-else for when to run this extra loop versus just updating the key values as you did in the old version. @zhuohan123 @WoosukKwon This loop is not needed for all models: https://github.com/vllm-project/vllm/blob/8ce9c50d4034de3c557b520935fac1d6dac585a0/csrc/pos_encoding_kernels.cu#L48-L66 This worked well for LLaMa models and was faster: https://github.com/vllm-project/vllm/blob/0b98ba15c744f1dfb0ea4f2135e85ca23d572ae1/csrc/pos_encoding_kernels.cu#L42-L45

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: After this loop was introduced in #592, the speed of execution of my 7B LLaMa model decreased by roughly 15%. This is due to the extra for-loop that is executed. I believe there is a **low-hanging fruit** in implementin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: his extra loop versus just updating the key values as you did in the old version. @zhuohan123 @WoosukKwon This loop is not needed for all models: https://github.com/vllm-project/vllm/blob/8ce9c50d4034de3c557b520935fac1d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cuted. I believe there is a **low-hanging fruit** in implementing an if-else for when to run this extra loop versus just updating the key values as you did in the old version. @zhuohan123 @WoosukKwon This loop is not ne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
