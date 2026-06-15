# vllm-project/vllm#30656: [Bug]: EngineCore crashes testing v1/embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#30656](https://github.com/vllm-project/vllm/issues/30656) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineCore crashes testing v1/embeddings

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug EngineCore crashes ```bash curl -X POST http://localhost:8000/v1/embeddings -H "Content-Type: application/json" -d '{ "model": "Qwen/Qwen3-Embedding-0.6B", "input": "The quick brown fox jumps over the lazy dog." }' {"error":{"message":"EngineCore encountered an issue. See stack trace (above) for the root cause.","type":"BadRequestError","param":null,"code":400} ``` ``` docker run -v ~/.cache/huggingface:/root/.cache/huggingface --env "HF_TOKEN=$HF_TOKEN" -p 8000:8000 --ipc=host public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.12.0 --model Qwen/Qwen3-Embedding-0.6B public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo v0.12.0 e0f05ebe3257 11 days ago 3.28GB ``` ``` {"error":{"message":"EngineCore encountered an issue. See stack trace (above) for the root cause.","type":"BadRequestError","param":null,"code":400}} ``` ``` es_config': {'type': }, 'local_cache_dir': None} (EngineCore_DP0 pid=25) INFO 12-14 20:43:07 [cpu_worker.py:192] auto thread-binding list (id, physical core): [(2, 0), (3, 1)] get_mempolicy: Operation not permitted [W1214 20:43:07.729406999 utils.cpp:82] Warning: numa_migrate_pages failed. errno: 1 (function init_cpu_threa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: alhost:8000/v1/embeddings -H "Content-Type: application/json" -d '{ "model": "Qwen/Qwen3-Embedding-0.6B", "input": "The quick brown fox jumps over the lazy dog." }' {"error":{"message":"EngineCore encountered an issue....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: root cause.","type":"BadRequestError","param":null,"code":400} ``` ``` docker run -v ~/.cache/huggingface:/root/.cache/huggingface --env "HF_TOKEN=$HF_TOKEN" -p 8000:8000 --ipc=host public.ecr.aws/q9t5s3a7/vllm-cpu-rele...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: EngineCore crashes testing v1/embeddings bug;stale ### Your current environment ### 🐛 Describe the bug EngineCore crashes ```bash curl -X POST http://localhost:8000/v1/embeddings -H "Content-Type: application/jso...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ize=1 rank=0 local_rank=0 distributed_init_method=tcp://172.17.0.2:57543 backend=gloo [Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0 [Gloo] Rank 0 is connected to 0 peer ranks...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
