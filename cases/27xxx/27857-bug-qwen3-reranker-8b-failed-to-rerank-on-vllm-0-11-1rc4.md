# vllm-project/vllm#27857: [Bug]: Qwen3-Reranker-8B failed to rerank on vllm 0.11.1rc4

| 字段 | 值 |
| --- | --- |
| Issue | [#27857](https://github.com/vllm-project/vllm/issues/27857) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Reranker-8B failed to rerank on vllm 0.11.1rc4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve Qwen/Qwen3-Reranker-8B --host 0.0.0.0 --port 10000 --tensor-parallel-size 4 --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": true}' ``` with curl ``` -H "Authorization: Bearer sk-" \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen/Qwen3-Reranker-8B", "query": "中国首都在哪", "documents": [ "北京", "西京", "南京", "东京","面筋" ],"return_documents":true }' {"id":"rerank-18dc216f35d64d458b54fe03d40549d3","model":"Qwen/Qwen3-Reranker-8B","usage":{"total_tokens":27},"results":[{"index":0,"document":{"text":"北京","multi_modal":null},"relevance_score":0.5},{"index":1,"document":{"text":"西京","multi_modal":null},"relevance_score":0.5},{"index":2,"document":{"text":"南京","multi_modal":null},"relevance_score":0.5},{"index":3,"document":{"text":"东京","multi_modal":null},"relevance_score":0.5},{"index":4,"document":{"text":"面筋","multi_modal":null},"relevance_score":0.5}]}# ``` Using the template will also yield the same result of 0.5 Even without using a template, it shouldn't be all 0.5 It works fine in 0.11.0, b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Reranker-8B failed to rerank on vllm 0.11.1rc4 bug ### Your current environment ### 🐛 Describe the bug ```bash CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve Qwen/Qwen3-Reranker-8B --host 0.0.0.0 --port 10000 --te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rc4 bug ### Your current environment ### 🐛 Describe the bug ```bash CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve Qwen/Qwen3-Reranker-8B --host 0.0.0.0 --port 10000 --tensor-parallel-size 4 --hf_overrides '{"architectures": [...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_depend...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
