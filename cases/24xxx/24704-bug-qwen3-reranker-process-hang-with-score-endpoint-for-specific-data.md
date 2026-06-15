# vllm-project/vllm#24704: [Bug]: Qwen3-Reranker: Process Hang with `/score` Endpoint for Specific Data

| 字段 | 值 |
| --- | --- |
| Issue | [#24704](https://github.com/vllm-project/vllm/issues/24704) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Reranker: Process Hang with `/score` Endpoint for Specific Data

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## The issue When I was running `Qwen/Qwen3-Reranker-8B`, calling the `/score` endpoint, vLLM freezes with no log for that endpoint call and no response. When the next request comes, the previous task is cancelled with an exception; otherwise, it hangs forever. I did not have this issue in European languages such as English and Spanish, but I have encountered it multiple times stably on datasets of other languages, such as Arabic and Hindi. Tested on 0.10.1.dev714+g4fc722eca and 0.10.2rc2.dev1+g15de5ff9e.cu129, but neither works. ## To reproduce Run the model server: ```sh vllm serve Qwen/Qwen3-Reranker-8B --port 8007 --gpu_memory_utilization 0.9 --max_model_len 8192 --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' --runner pooling ``` Then run the following request: ```python import requests import json if __name__ == "__main__": with open('queries.json', 'r') as f: queries = json.load(f) with open('docs.json', 'r') as f: docs = json.load(f) response = requests.post( f"http://127.0.0.1:8007/score", json={ "model": "Qwen/Qwen3-Reranker...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Qwen3-Reranker: Process Hang with `/score` Endpoint for Specific Data bug;stale ### Your current environment ### 🐛 Describe the bug ## The issue When I was running `Qwen/Qwen3-Reranker-8B`, calling the `/score` e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: wen3-Reranker: Process Hang with `/score` Endpoint for Specific Data bug;stale ### Your current environment ### 🐛 Describe the bug ## The issue When I was running `Qwen/Qwen3-Reranker-8B`, calling the `/score` endpoint,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Reranker: Process Hang with `/score` Endpoint for Specific Data bug;stale ### Your current environment ### 🐛 Describe the bug ## The issue When I was running `Qwen/Qwen3-Reranker-8B`, calling the `/score` e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 8007 --gpu_memory_utilization 0.9 --max_model_len 8192 --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' --runner pooling ``...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ogits;scheduler_memory;speculative_decoding cache;cuda;operator;sampling;triton build_error;crash;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
