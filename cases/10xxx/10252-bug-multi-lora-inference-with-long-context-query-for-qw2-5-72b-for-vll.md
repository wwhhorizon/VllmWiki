# vllm-project/vllm#10252: [Bug]: multi lora inference with long context query for qw2.5 72B for vllm version 0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#10252](https://github.com/vllm-project/vllm/issues/10252) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | throughput |
| Operator 关键词 | cuda |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: multi lora inference with long context query for qw2.5 72B for vllm version 0.6.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using version 0.6.3 of vllm, we encounter different behaviors between two deployment methods of the same base model (Qwen2.5-72B-Instruct). Here are the details: - Method 1 (with multi LoRA): `python -m vllm.entrypoints.openai.api_server --model Qwen2.5-72B-Instruct/ --served-model-name Qwen25-72B-Instruct --enable-lora --lora-modules qwen25_1111=epoch_0 --gpu-memory-utilization 0.70 --port 8089 --max-model-len 32000 --tensor-parallel-size 4 --seed 1024 --max-lora-rank 64` This method results is garbled/meaningless answers when the query length exceeds 15,000 tokens when we request the answers of the "Qwen25-72B-Instruct" or the "qwen25_1111" - Method 2 (without multi LoRA): `python -m vllm.entrypoints.openai.api_server --model Qwen2.5-72B-Instruct/ --served-model-name Qwen25-72B-Instruct --gpu-memory-utilization 0.70 --port 8089 --max-model-len 32000 --tensor-parallel-size 4 --seed 1024 ` This method performs normally under the same conditions. Additionally, when using version 0.6.2, the responses are normal but the performance is significantly slower: - Avg generation throughput: 6.5 tokens/s (compared to 43.5 tokens/s in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ug]: multi lora inference with long context query for qw2.5 72B for vllm version 0.6.3 bug ### Your current environment ### 🐛 Describe the bug When using version 0.6.3 of vllm, we encounter different behaviors between t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nter different behaviors between two deployment methods of the same base model (Qwen2.5-72B-Instruct). Here are the details: - Method 1 (with multi LoRA): `python -m vllm.entrypoints.openai.api_server --model Qwen2.5-72...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda build_error;slowdown env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /meaningless answers when the query length exceeds 15,000 tokens when we request the answers of the "Qwen25-72B-Instruct" or the "qwen25_1111" - Method 2 (without multi LoRA): `python -m vllm.entrypoints.openai.api_serv...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: re normal but the performance is significantly slower: - Avg generation throughput: 6.5 tokens/s (compared to 43.5 tokens/s in version 0.6.3). ### ❓ Question How can I fix the bug in version 0.6.3 while obtaining normal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
