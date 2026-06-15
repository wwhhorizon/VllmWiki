# vllm-project/vllm#3325: Cannot server StarCoder 2 with `vllm/vllm-openai:v0.3.3` image?

| 字段 | 值 |
| --- | --- |
| Issue | [#3325](https://github.com/vllm-project/vllm/issues/3325) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Cannot server StarCoder 2 with `vllm/vllm-openai:v0.3.3` image?

### Issue 正文摘录

Hi all, When I was trying to test the newly released StarCoder2 model with 0.3.3, I noticed the following error being thrown: ```ValueError: The checkpoint you are trying to load has model type `starcoder2` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.``` From my understanding this is due to `transformers` not releasing support for SC2 in the current released version but only in the master branch? Lmk if I am understanding correctly, and if so, is there anyway to fix the image? Thanks!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.``` From my understanding this is due to `transformers` not releasing support for SC2 in the current releas...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: oad has model type `starcoder2` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.``` From my understand...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: image? Hi all, When I was trying to test the newly released StarCoder2 model with 0.3.3, I noticed the following error being thrown: ```ValueError: The checkpoint you are trying to load has model type `starcoder2` but T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: er 2 with `vllm/vllm-openai:v0.3.3` image? Hi all, When I was trying to test the newly released StarCoder2 model with 0.3.3, I noticed the following error being thrown: ```ValueError: The checkpoint you are trying to lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
