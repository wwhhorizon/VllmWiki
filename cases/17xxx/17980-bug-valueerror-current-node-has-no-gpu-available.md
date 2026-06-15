# vllm-project/vllm#17980: [Bug]: ValueError: Current node has no GPU available

| 字段 | 值 |
| --- | --- |
| Issue | [#17980](https://github.com/vllm-project/vllm/issues/17980) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Current node has no GPU available

### Issue 正文摘录

### Your current environment the command line of ray GLOO_SOCKET_IFNAME=bond0 NCCL_SOCKET_IFNAME=bond0 ray start --head --port=6379 the output of ray status ``` ======== Autoscaler status: 2025-05-12 13:56:11.534834 ======== Node status --------------------------------------------------------------- Active: 1 node_62fbf2e9fa2b727c9da8c4c875d8a158197b1400d4845364594071c4 1 node_841b8f4a6a5122881cce5f9cbe246bad6af8c4675e4368e8195faa31 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/128.0 CPU 0.0/16.0 GPU 0B/3.56TiB memory 0B/372.53GiB object_store_memory Constraints: (no request_resources() constraints) Demands: (no resource demands) ``` ### 🐛 Describe the bug The output of vllm serve models/DeepSeek-V2-Lite --tensor-parallel-size 8 --data-parallel-size 2 --enable-expert-parallel --trust-remote-code --gpu-memory-utilization 0.97 --max-model-len 512 --max-num-seqs 1 --max-num-batched-tokens 512 --enforce-eager --distributed-executor-backend ray ```text INFO 05-12 13:45:42 [__init__.py:239] Automatically detected platform cuda. INFO 05-12 13:45:43 [api_server.py:1034] vLLM API server versio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 05-12 13:45:43 [api_server.py:1034] vLLM API server version 0.8.3rc2.dev179+gdc1b4a6f1.d20250423 INFO 05-12 13:45:43 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='/home/models/De...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: d --port=6379 the output of ray status ``` ======== Autoscaler status: 2025-05-12 13:56:11.534834 ======== Node status --------------------------------------------------------------- Active: 1 node_62fbf2e9fa2b727c9da8c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: ValueError: Current node has no GPU available bug;stale ### Your current environment the command line of ray GLOO_SOCKET_IFNAME=bond0 NCCL_SOCKET_IFNAME=bond0 ray start --head --port=6379 the output of ray status...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: urce demands) ``` ### 🐛 Describe the bug The output of vllm serve models/DeepSeek-V2-Lite --tensor-parallel-size 8 --data-parallel-size 2 --enable-expert-parallel --trust-remote-code --gpu-memory-utilization 0.97 --max-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: s 1 --max-num-batched-tokens 512 --enforce-eager --distributed-executor-backend ray ```text INFO 05-12 13:45:42 [__init__.py:239] Automatically detected platform cuda. INFO 05-12 13:45:43 [api_server.py:1034] vLLM API s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
