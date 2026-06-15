# vllm-project/vllm#8455: [Usage]:  There is a significant difference in memory usage between vllm and sglang when deploying deepseek-v2 fp8.

| 字段 | 值 |
| --- | --- |
| Issue | [#8455](https://github.com/vllm-project/vllm/issues/8455) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  There is a significant difference in memory usage between vllm and sglang when deploying deepseek-v2 fp8.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I deployed the fp8 quantized model of deepseek-v2.5 using vllm and sglang respectively, and found that vllm's memory consumption is significantly higher than sglang's (especially the memory available for kv cache). Is this mainly due to the differences between MHA and MLA? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rence in memory usage between vllm and sglang when deploying deepseek-v2 fp8. usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I deployed the fp8 qu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hat vllm's memory consumption is significantly higher than sglang's (especially the memory available for kv cache). Is this mainly due to the differences between MHA and MLA? ### Before submitting a new issue... - [X] M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: LA? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: significantly higher than sglang's (especially the memory available for kv cache). Is this mainly due to the differences between MHA and MLA? ### Before submitting a new issue... - [X] Make sure you already searched for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y` ``` ### How would you like to use vllm I deployed the fp8 quantized model of deepseek-v2.5 using vllm and sglang respectively, and found that vllm's memory consumption is significantly higher than sglang's (especiall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
