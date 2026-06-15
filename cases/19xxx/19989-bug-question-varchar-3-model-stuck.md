# vllm-project/vllm#19989: [Bug]: question "VARCHAR(3" Model stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#19989](https://github.com/vllm-project/vllm/issues/19989) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: question "VARCHAR(3" Model stuck

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm docker 0.9.0: run command: > --served-model-name Qwen3-235B --model /host/models/hub/Qwen/Qwen3-235B-A22B --tensor-parallel-size 8 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser hermes --max-model-len 131072 --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' curl --data '{ "messages": [{ "content": "VARCHAR(3", "role": "user" }], "model": "Qwen3-235B", "stream":true }' Model stuck curl --data '{ "messages": [{ "content": "ARCHAR(3", "role": "user" }], "model": "Qwen3-235B", "stream":true }' Normal return curl --data '{ "messages": [{ "content": "VARCHAR(", "role": "user" }], "model": "Qwen3-235B", "stream":true }' Normal return ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: question "VARCHAR(3" Model stuck bug ### Your current environment ### 🐛 Describe the bug vllm docker 0.9.0: run command: > --served-model-name Qwen3-235B --model /host/models/hub/Qwen/Qwen3-235B-A22B --tensor-par...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stuck bug ### Your current environment ### 🐛 Describe the bug vllm docker 0.9.0: run command: > --served-model-name Qwen3-235B --model /host/models/hub/Qwen/Qwen3-235B-A22B --tensor-parallel-size 8 --reasoning-parser qw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: question "VARCHAR(3" Model stuck bug ### Your current environment ### 🐛 Describe the bug vllm docker 0.9.0: run command: > --served-model-name Qwen3-235B --model /host/models/hub/Qwen/Qwen3-235B-A22B --tensor
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
