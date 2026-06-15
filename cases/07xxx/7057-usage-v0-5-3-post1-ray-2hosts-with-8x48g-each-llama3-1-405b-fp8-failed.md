# vllm-project/vllm#7057: [Usage]: v0.5.3.post1, ray, 2Hosts with 8x48G each, Llama3.1-405B-FP8, failed

| 字段 | 值 |
| --- | --- |
| Issue | [#7057](https://github.com/vllm-project/vllm/issues/7057) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Usage]: v0.5.3.post1, ray, 2Hosts with 8x48G each, Llama3.1-405B-FP8, failed

### Issue 正文摘录

### Your current environment ``` root@cy-ah85026:/vllm-workspace# ray status ======== Autoscaler status: 2024-08-02 02:04:32.248220 ======== Node status --------------------------------------------------------------- Active: 1 node_a689bb663bd4154a54614777bcc40f9c44b7dbd5c83f6cd7862b09cd 1 node_b07cdf56b532f9dfd446b08e9ddb2f1c9f4c46ab600779999807e482 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/256.0 CPU 0.0/16.0 GPU 0B/695.32GiB memory 0B/301.99GiB object_store_memory Demands: (no resource demands) ``` ### How would you like to use vllm `root@cy-ah85026:/vllm-workspace# vllm serve /mnt/cpn-pod/models/meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 --served-model-name meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 -tp 16 --distributed-executor-backend=ray --max-model-len 4096 ` ``` INFO 08-02 01:42:35 api_server.py:219] vLLM API server version 0.5.3.post1 INFO 08-02 01:42:35 api_server.py:220] args: Namespace(model_tag='/mnt/cpn-pod/models/meta-llama/Meta-Llama-3.1-405B-Instruct-FP8', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_met...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: .5.3.post1, ray, 2Hosts with 8x48G each, Llama3.1-405B-FP8, failed usage;stale ### Your current environment ``` root@cy-ah85026:/vllm-workspace# ray status ======== Autoscaler status: 2024-08-02 02:04:32.248220 ========...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Usage]: v0.5.3.post1, ray, 2Hosts with 8x48G each, Llama3.1-405B-FP8, failed usage;stale ### Your current environment ``` root@cy-ah85026:/vllm-workspace# ray status ======== Autoscaler status: 2024-08-02 02:04:32.2482...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: ta-llama/Meta-Llama-3.1-405B-Instruct-FP8 -tp 16 --distributed-executor-backend=ray --max-model-len 4096 ` ``` INFO 08-02 01:42:35 api_server.py:219] vLLM API server version 0.5.3.post1 INFO 08-02 01:42:35 api_server.py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en 4096 ` ``` INFO 08-02 01:42:35 api_server.py:219] vLLM API server version 0.5.3.post1 INFO 08-02 01:42:35 api_server.py:220] args: Namespace(model_tag='/mnt/cpn-pod/models/meta-llama/Meta-Llama-3.1-405B-Instruct-FP8'...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: P8', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | (0x7f4890913609 in /usr/lib/x86_64-linux-gnu/libpthread.so.0) frame #4: clone + 0x43 (0x7f4890a4d353 in /usr/lib/x86_64-linux-gnu/libc.so.6) (rayworkerwrapper pid=4062, ip=192.1 |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7f4843d9adcc in /usr/local/lib/python3.10/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xd6df4 (0x7f488f851df4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknow |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
