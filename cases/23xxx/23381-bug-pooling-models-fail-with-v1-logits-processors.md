# vllm-project/vllm#23381: [Bug]: Pooling models fail with V1 logits processors

| 字段 | 值 |
| --- | --- |
| Issue | [#23381](https://github.com/vllm-project/vllm/issues/23381) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pooling models fail with V1 logits processors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I was running MxBAI v2 Large and Qwen 3 0.6B rerankers with `--runner pooling`, the issue was triggered by having the first req_id be None, which cannot be handled in the loop as a dict key. To reproduce this issue, just load the models: ```sh CUDA_VISIBLE_DEVICES=0 vllm serve mixedbread-ai/mxbai-rerank-large-v2 --port 8004 --gpu_memory_utilization 0.9 --max_model_len 8192 --hf_overrides '{"architectures": ["Qwen2ForSequenceClassification"],"classifier_from_token": ["0", "1"], "method": "from_2_way_softmax"}' --runner pooling & CUDA_VISIBLE_DEVICES=1 vllm serve Qwen/Qwen3-Reranker-0.6B --port 8005 --gpu_memory_utilization 0.9 --max_model_len 32768 --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' --runner pooling & ``` and then request the `/score` endpoint with: ```python3 response = requests.post( f"http://127.0.0.1:8004/score", json={ "model": "mixedbread-ai/mxbai-rerank-large-v2", "text_1": queries, # list[str] "text_2": texts, # list[str] "truncate_prompt_tokens": 8192, } ) ``` Code for formatting queries and texts for Qwen 3...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Pooling models fail with V1 logits processors bug ### Your current environment ### 🐛 Describe the bug When I was running MxBAI v2 Large and Qwen 3 0.6B rerankers with `--runner pooling`, the issue was triggered b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ject/vllm/blob/main/examples/offline_inference/qwen3_reranker.py The specific commit that introduces the issue is https://github.com/vllm-project/vllm/commit/bf7f470b22e8bf26e1edb30b3bf465ab7dd69f0c, since its parent ht...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: as a dict key. To reproduce this issue, just load the models: ```sh CUDA_VISIBLE_DEVICES=0 vllm serve mixedbread-ai/mxbai-rerank-large-v2 --port 8004 --gpu_memory_utilization 0.9 --max_model_len 8192 --hf_overrides '{"a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: "],"is_original_qwen3_reranker": true}' --runner pooling & ``` and then request the `/score` endpoint with: ```python3 response = requests.post( f"http://127.0.0.1:8004/score", json={ "model": "mixedbread-ai/mxbai-reran...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
