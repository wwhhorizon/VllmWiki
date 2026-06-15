# vllm-project/vllm#43189: [Usage]: DeepSeek-V4 startup takes ~8 min — guidance on reducing initialization time

| 字段 | 值 |
| --- | --- |
| Issue | [#43189](https://github.com/vllm-project/vllm/issues/43189) |
| 状态 | open |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: DeepSeek-V4 startup takes ~8 min — guidance on reducing initialization time

### Issue 正文摘录

### Your current environment node: h20 ### How would you like to use vllm node: h20 When serving **DeepSeek-V4-Flash** with the following command, the time from process start to "service ready" is approximately **8 minutes**. I would like to understand whether this is expected and what are the recommended ways to speed up the startup phase. Do you have any documentation on startup speed optimization? ``` vllm serve /models/deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: els/deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: DeepSeek-V4 startup takes ~8 min — guidance on reducing initialization time usage ### Your current environment node: h20 ### How would you like to use vllm node: h20 When serving **DeepSeek-V4-Flash** with the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: erve /models/deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepse...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-too...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
