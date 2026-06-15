# vllm-project/vllm#16928: [Bug]: SharedStorageConnector only see first batch of tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#16928](https://github.com/vllm-project/vllm/issues/16928) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SharedStorageConnector only see first batch of tokens

### Issue 正文摘录

Ccurrent environment: @robertgshaw2-redhat @ApostaC I am using a recent vLLM (`da818353321d`), and when trying a ~20,000 token prompt with `mistralai/Mistral-7B-Instruct-v0.3` I only see parts of the KVCache being saved. I think only about 2,000 tokens saved. I've attach the relevant output. Here's how I executed it: ``` PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm serve mistralai/Mistral-7B-Instruct-v0.3 \ --cpu-offload-gb 15 --enforce-eager --kv-transfer-config \ '{"kv_connector":"SharedStorageConnector","kv_role":"kv_both","kv_connector_extra_config": {"shared_storage_path": "local_storage"}}' ``` Execution log in: https://pastebin.com/KPnPUv5m Is it enough or should I run with more tracing?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: https://pastebin.com/KPnPUv5m Is it enough or should I run with more tracing? correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton bui...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: l-7B-Instruct-v0.3 \ --cpu-offload-gb 15 --enforce-eager --kv-transfer-config \ '{"kv_connector":"SharedStorageConnector","kv_role":"kv_both","kv_connector_extra_config": {"shared_storage_path": "local_storage"}}' ``` E...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape Ccurrent environment:
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: upport;sampling_logits cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape Ccurrent environment:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: I've attach the relevant output. Here's how I executed it: ``` PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm serve mistralai/Mistral-7B-Instruct-v0.3 \ --cpu-offload-gb 15 --enforce-eager --kv-transfer-config...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
