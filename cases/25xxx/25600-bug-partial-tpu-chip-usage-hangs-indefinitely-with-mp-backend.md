# vllm-project/vllm#25600: [Bug]: Partial TPU chip usage hangs indefinitely with MP backend

| 字段 | 值 |
| --- | --- |
| Issue | [#25600](https://github.com/vllm-project/vllm/issues/25600) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Partial TPU chip usage hangs indefinitely with MP backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serving with partial number of TPU chips (say TP=4 out of 8 in a v6e-8) hangs indefinitely without a message on mp backend for the distributed-executor-backend. With ray, it does complain of this and immediately terminates. mp backend needs some validation to avoid running into this. Additionally some documentation regarding the need to use the full set of TPU chips on a node would be great Command to serve: ``` vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --max-model-len 8192 --disable-log-requests -tp 4 --no-enable-prefix-caching --distributed-executor-backend ``` [mp_launch.log](https://github.com/user-attachments/files/22521264/mp_launch.log) ``` [Gloo] Rank 0 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3 [Gloo] Rank 1 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3 [Gloo] Rank 3 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3 [Gloo] Rank 3 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3 [Gloo] Rank 0 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3 [Gloo] Rank 1 is connect...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: py:718] RuntimeError: TPU initialization failed: Invalid --2a886c8_slice_builder_worker_addresses specified. Expected 8 worker addresses, got 4. ``` ### Before submitting a new issue... - [x] Make sure you already searc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Partial TPU chip usage hangs indefinitely with MP backend bug;stale ### Your current environment ### 🐛 Describe the bug vllm serving with partial number of TPU chips (say TP=4 out of 8 in a v6e-8) hangs indefinit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Partial TPU chip usage hangs indefinitely with MP backend bug;stale ### Your current environment ### 🐛 Describe the bug vllm serving with partial number of TPU chips (say TP=4 out of 8 in a v6e-8) hangs indefinit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Partial TPU chip usage hangs indefinitely with MP backend bug;stale ### Your current environment ### 🐛 Describe the bug vllm serving with partial number of TPU chips (say TP=4 out of 8 in a v6e-8) hangs indefinit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: PU chips on a node would be great Command to serve: ``` vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --max-model-len 8192 --disable-log-requests -tp 4 --no-enable-prefix-caching --distributed-executor-backend ``` [m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
