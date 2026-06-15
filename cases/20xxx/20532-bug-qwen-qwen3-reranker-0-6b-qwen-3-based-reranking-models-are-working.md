# vllm-project/vllm#20532: [Bug]: `Qwen/Qwen3-Reranker-0.6B` Qwen 3 based reranking models are working

| 字段 | 值 |
| --- | --- |
| Issue | [#20532](https://github.com/vllm-project/vllm/issues/20532) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `Qwen/Qwen3-Reranker-0.6B` Qwen 3 based reranking models are working

### Issue 正文摘录

### Your current environment vLLM Production Stack Helm chart K8s CUDA 12.8 Nvidia GPUs ### 🐛 Describe the bug Following #19260, I tried to implement reranking with [`Qwen/Qwen3-Reranker-0.6B`](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B), [`Qwen/Qwen3-Reranker-4B`](https://huggingface.co/Qwen/Qwen3-Reranker-4B), and [`tomaarsen/Qwen3-Reranker-0.6B-seq-cls`](https://huggingface.co/tomaarsen/Qwen3-Reranker-0.6B-seq-cls) in vLLM Product Stack Helm chart on k8s, but ended up facing these errors. This is my Helm setup: ```yaml servingEngineSpec: runtimeClassName: "" modelSpec: - name: qwen-qwen3-reranker-0-6-b repository: vllm/vllm-openai tag: v0.9.1 modelURL: Qwen/Qwen3-Reranker-0.6B replicaCount: 1 requestCPU: 8 requestMemory: 16Gi requestGPU: 1 vllmConfig: extraArgs: - >- --hf_overrides={"architectures":["Qwen3ForSequenceClassification"],"classifier_from_token":["no","yes"],"is_original_qwen3_reranker":true} - name: qwen-qwen3-reranker-4-b repository: vllm/vllm-openai tag: v0.9.1 modelURL: Qwen/Qwen3-Reranker-4B replicaCount: 1 requestCPU: 8 requestMemory: 16Gi requestGPU: 1 vllmConfig: extraArgs: - >- --hf_overrides={"architectures":["Qwen3ForSequenceClassification"],"classifi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: `Qwen/Qwen3-Reranker-0.6B` Qwen 3 based reranking models are working bug ### Your current environment vLLM Production Stack Helm chart K8s CUDA 12.8 Nvidia GPUs ### 🐛 Describe the bug Following #19260, I tried to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: er-0.6B-seq-cls) in vLLM Product Stack Helm chart on k8s, but ended up facing these errors. This is my Helm setup: ```yaml servingEngineSpec: runtimeClassName: "" modelSpec: - name: qwen-qwen3-reranker-0-6-b repository:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ng to 'generate'. INFO 07-06 15:25:33 [config.py:3268] Downcasting torch.float32 to torch.bfloat16. INFO 07-06 15:25:33 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 07-06 15:25:3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 9.1 modelURL: Qwen/Qwen3-Reranker-0.6B replicaCount: 1 requestCPU: 8 requestMemory: 16Gi requestGPU: 1 vllmConfig: extraArgs: - >- --hf_overrides={"architectures":["Qwen3ForSequenceClassification"],"classifier_from_toke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
