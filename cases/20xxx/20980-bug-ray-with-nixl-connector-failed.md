# vllm-project/vllm#20980: [Bug]: ray with nixl connector failed

| 字段 | 值 |
| --- | --- |
| Issue | [#20980](https://github.com/vllm-project/vllm/issues/20980) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ray with nixl connector failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to use ray+tp16 (2 nodes) as one prefill instance and ray+tp16 (2 nodes) as one decode instance. Does the current NixL Connector support this? cli ``` RAY_DEDUP_LOGS=0 GLOO_SOCKET_IFNAME=eth0 NCCL_NET_GDR_LEVEL=SYS NCCL_IB_DISABLE=0 NCCL_CUMEM_ENABLE=0 NCCL_IC_HCA=mlx5 NCCL_DEBUG=TRACE VLLM_LOGGING_LEVEL=DEBUG VLLM_NIXL_SIDE_CHANNEL_HOST=10.18.2.19 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve /models/Qwen3-8B --served-model-name "qwen3" --port 8100 --enforce-eager --disable-log-requests --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --distributed-executor-backend ray --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ment ### 🐛 Describe the bug I want to use ray+tp16 (2 nodes) as one prefill instance and ray+tp16 (2 nodes) as one decode instance. Does the current NixL Connector support this? cli ``` RAY_DEDUP_LOGS=0 GLOO_SOCKET_IFNA...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: IDE_CHANNEL_HOST=10.18.2.19 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve /models/Qwen3-8B --served-model-name "qwen3" --port 8100 --enforce-eager --disable-log-requests --gpu-memory-utilization 0.9 --tensor-parallel-size...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u-memory-utilization 0.9 --tensor-parallel-size 2 --distributed-executor-backend ray --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' ``` ### Before submitting a new issue... - [x] Make sure y...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
