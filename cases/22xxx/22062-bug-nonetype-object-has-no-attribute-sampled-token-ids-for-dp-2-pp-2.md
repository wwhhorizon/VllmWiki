# vllm-project/vllm#22062: [Bug]: 'NoneType' object has no attribute 'sampled_token_ids' for DP 2 PP 2

| 字段 | 值 |
| --- | --- |
| Issue | [#22062](https://github.com/vllm-project/vllm/issues/22062) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;triton |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'NoneType' object has no attribute 'sampled_token_ids' for DP 2 PP 2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug one side` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model /mnt/jfs/models/Llama-2-7b-chat-hf --seed 42 -pp 2 -dp 2 --gpu_memory_utilization 0.8 --dtype bfloat16 --enforce-eager` the other side ` python3 benchmarks/benchmark_serving.py --backend vllm --model model/Llama-2-7b-chat-hf --dataset-name sharegpt --dataset-path benchmarks/ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 128 --request-rate inf` there will be It will only happen when the number of prompts is high, and between the call from the execute model to the return from the execute model, a new prompt arrives. It is over CUDA. ### Before submitting a new issue... - [x] Make sure you have already searched for relevant issues and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton nan_inf dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Llama-2-7b-chat-hf --seed 42 -pp 2 -dp 2 --gpu_memory_utilization 0.8 --dtype bfloat16 --enforce-eager` the other side ` python3 benchmarks/benchmark_serving.py --backend vllm --model model/Llama-2-7b-chat-hf --dataset-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: thon3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model /mnt/jfs/models/Llama-2-7b-chat-hf --seed 42 -pp 2 -dp 2 --gpu_memory_utilization 0.8 --dtype bfloat16 --enforce-eager` the other side ` pyt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ce-eager` the other side ` python3 benchmarks/benchmark_serving.py --backend vllm --model model/Llama-2-7b-chat-hf --dataset-name sharegpt --dataset-path benchmarks/ShareGPT_V3_unfiltered_cleaned_split.json --num-prompt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l to the return from the execute model, a new prompt arrives. It is over CUDA. ### Before submitting a new issue... - [x] Make sure you have already searched for relevant issues and asked the chatbot living at the botto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
