# vllm-project/vllm#35477: [Usage]: How to test the performance of a encoder-only BertModel using `vllm bench serve`

| 字段 | 值 |
| --- | --- |
| Issue | [#35477](https://github.com/vllm-project/vllm/issues/35477) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to test the performance of a encoder-only BertModel using `vllm bench serve`

### Issue 正文摘录

### Your current environment ### How would you like to use vllm I can launch the `BAAI/bge-reranker-v2-m3` model using the following command: ``` model_name="bge-reranker-v2-m3" model_path=BAAI/$model_name vllm serve $model_path \ --port 8018 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --served-model-name $model_name \ --host 0.0.0.0 \ --trust-remote-code \ --max-model-len 512 \ --enable_prefix_caching \ --max_num_seqs=256 \ --dtype=bfloat16 ``` Then I can test the `request throughput(req/s)` with the following command: ``` vllm bench serve \ --backend openai-embeddings \ --endpoint /v1/embeddings \ --model $model_path \ --served-model-name $model_name \ --port 8018 \ --dataset-name random \ --random-input-len 256\ --random-output-len 256\ --ignore-eos \ --max-concurrency 32 \ --num-prompts 32 ``` Howerver, I don't know how to test the `request throughput(req/s)` of `BAAI/bge-large-zh-v1.5` model because when I changed the `model_name` to `bge-large-zh-v1.5`, I got the following output: ``` Waiting for endpoint to become up in 600 seconds | | 00:00 elapsed, ? remaining | | 00:00 elapsed, 00:07 remaining | | 00:05 elapsed, 09:54 remaining | | 00:05 elapsed, 09:54 re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: \ --max-model-len 512 \ --enable_prefix_caching \ --max_num_seqs=256 \ --dtype=bfloat16 ``` Then I can test the `request throughput(req/s)` with the following command: ``` vllm bench serve \ --backend openai-embeddings...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: caching \ --max_num_seqs=256 \ --dtype=bfloat16 ``` Then I can test the `request throughput(req/s)` with the following command: ``` vllm bench serve \ --backend openai-embeddings \ --endpoint /v1/embeddings \ --model $m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: throughput(req/s)` with the following command: ``` vllm bench serve \ --backend openai-embeddings \ --endpoint /v1/embeddings \ --model $model_path \ --served-model-name $model_name \ --port 8018 \ --dataset-name random...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
