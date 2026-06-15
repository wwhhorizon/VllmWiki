# vllm-project/vllm#19723: [Bug]: vllm running on new H20-3e Nvidia card has occasional garbled bug using Qwen 2.5 VL 72B

| 字段 | 值 |
| --- | --- |
| Issue | [#19723](https://github.com/vllm-project/vllm/issues/19723) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm running on new H20-3e Nvidia card has occasional garbled bug using Qwen 2.5 VL 72B

### Issue 正文摘录

### Your current environment current environment H20-3e Nvidia with 2 Cuda 12.6 vllm version 0.9.1 current ### 🐛 Describe the bug vllm serve /data01/vllm/llm_qwenvl25/ --served-model-name qwen2vl --api-key mr-98765 --tensor-parallel-size 2 --trust-remote-code --host 0.0.0.0 --port 8001 --gpu-memory-utilization 0.95 --no-enable-prefix-caching --generation-config /data01/vllm/llm_qwenvl25/generation_config.json The model VL can be loaded successful, but when in the chating, it has some strange characters like 📐⚗️ Sometimes, it stops before all the answer shows. IN A WORD , the answer is not correct with abnormal characters. Does anyone meet the same problem ? Thanks ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm running on new H20-3e Nvidia card has occasional garbled bug using Qwen 2.5 VL 72B bug ### Your current environment current environment H20-3e Nvidia with 2 Cuda 12.6 vllm version 0.9.1 current ### 🐛 Describe the b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g ### Your current environment current environment H20-3e Nvidia with 2 Cuda 12.6 vllm version 0.9.1 current ### 🐛 Describe the bug vllm serve /data01/vllm/llm_qwenvl25/ --served-model-name qwen2vl --api-key mr-98765 --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nt environment current environment H20-3e Nvidia with 2 Cuda 12.6 vllm version 0.9.1 current ### 🐛 Describe the bug vllm serve /data01/vllm/llm_qwenvl25/ --served-model-name qwen2vl --api-key mr-98765 --tensor-parallel-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;frontend_api;model_support cuda Your current environ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
