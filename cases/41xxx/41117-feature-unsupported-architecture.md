# vllm-project/vllm#41117: [Feature]: unsupported architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#41117](https://github.com/vllm-project/vllm/issues/41117) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: unsupported architecture

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are using version v0.20.0 and encountering an "unsupported architecture" error (4090) during deployment. When should we begin adaptation, or is it already adapted? Is our startup command incorrect? The correct startup command is: `vllm serve /root/xinglin-data/api_model/DeepSeek-V4-Flash --trust-remote-code --tensor-parallel-size 8 --enable-expert-parallel --block-size 128 --max-model-len 8192 --gpu-memory-utilization 0.90 --max-num-seqs 8 --max-num-batched-tokens 4096 --tokenizer-mode deepseek_v4 --tool-call-parser deepseek_v4 --reasoning-parser deepseek_v4 --enable-auto-tool-choice --host 0.0.0.0 --port 12800 --kv-cache-dtype fp8` --enforce-eager ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: seek_v4 --enable-auto-tool-choice --host 0.0.0.0 --port 12800 --kv-cache-dtype fp8` --enforce-eager ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: re feature request ### 🚀 The feature, motivation and pitch We are using version v0.20.0 and encountering an "unsupported architecture" error (4090) during deployment. When should we begin adaptation, or is it already ad...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: unsupported architecture feature request ### 🚀 The feature, motivation and pitch We are using version v0.20.0 and encountering an "unsupported architecture" error (4090) during deployment. When should we begi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: rser deepseek_v4 --enable-auto-tool-choice --host 0.0.0.0 --port 12800 --kv-cache-dtype fp8` --enforce-eager ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x]...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: --trust-remote-code --tensor-parallel-size 8 --enable-expert-parallel --block-size 128 --max-model-len 8192 --gpu-memory-utilization 0.90 --max-num-seqs 8 --max-num-batched-tokens 4096 --tokenizer-mode deepseek_v4 --too...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
