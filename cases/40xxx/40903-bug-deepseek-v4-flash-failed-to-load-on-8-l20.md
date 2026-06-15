# vllm-project/vllm#40903: [Bug]: Deepseek-V4-Flash failed to load on 8*L20

| 字段 | 值 |
| --- | --- |
| Issue | [#40903](https://github.com/vllm-project/vllm/issues/40903) |
| 状态 | open |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek-V4-Flash failed to load on 8*L20

### Issue 正文摘录

### Your current environment CUDA version：13.0 docker：vllm/vllm-openai:deepseekv4-cu129 ### 🐛 Describe the bug vllm serve /workdir/model/deepseek-v4-flash/ --served-model-name dpsk --port 8082 --host 0.0.0.0 --tensor-parallel-size 8 --max-model-len 32000 --gpu-memory-utilization 0.8 --enforce-eager --kv-cache-dtype fp8 log: [log.txt](https://github.com/user-attachments/files/27095559/log.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -V4-Flash failed to load on 8*L20 bug ### Your current environment CUDA version：13.0 docker：vllm/vllm-openai:deepseekv4-cu129 ### 🐛 Describe the bug vllm serve /workdir/model/deepseek-v4-flash/ --served-model-name dpsk...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -model-len 32000 --gpu-memory-utilization 0.8 --enforce-eager --kv-cache-dtype fp8 log: [log.txt](https://github.com/user-attachments/files/27095559/log.txt) ### Before submitting a new issue... - [x] Make sure you alre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pseek-V4-Flash failed to load on 8*L20 bug ### Your current environment CUDA version：13.0 docker：vllm/vllm-openai:deepseekv4-cu129 ### 🐛 Describe the bug vllm serve /workdir/model/deepseek-v4-flash/ --served-model-name...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e 8 --max-model-len 32000 --gpu-memory-utilization 0.8 --enforce-eager --kv-cache-dtype fp8 log: [log.txt](https://github.com/user-attachments/files/27095559/log.txt) ### Before submitting a new issue... - [x] Make sure...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: llm-openai:deepseekv4-cu129 ### 🐛 Describe the bug vllm serve /workdir/model/deepseek-v4-flash/ --served-model-name dpsk --port 8082 --host 0.0.0.0 --tensor-parallel-size 8 --max-model-len 32000 --gpu-memory-utilization...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
