# vllm-project/vllm#35507: [Bug]: Assertionerror when using OffloadingConnector: assert len(req.block_hashes) >= num_gpu_blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#35507](https://github.com/vllm-project/vllm/issues/35507) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Assertionerror when using OffloadingConnector: assert len(req.block_hashes) >= num_gpu_blocks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run the ``` vllm serve /home/models/MiMo-7B-Base --host 0.0.0.0 --port 8206 --block_size=16 --max_model_len=6144 --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' --tensor-parallel-size 1 --gpu_memory_utilization=0.85 --no-enable-prefix-caching --trust_remote_code --kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"num_cpu_blocks": 10000}}' ``` to start the online service and run the ``` vllm bench serve --backend vllm --model /home/models/MiMo-7B-Base --host 0.0.0.0 --port 8206 --dataset-name random --random-input-len 4096 --random-output-len 1024 --ignore-eos --request-rate 1 --num-prompts 1 ``` to test the performance. However, I got the Assertionerror ```(EngineCore_DP0 pid=20437) ERROR 02-27 20:04:46 [core.py:710] EngineCore encountered a fatal error. (EngineCore_DP0 pid=20437) ERROR 02-27 20:04:46 [core.py:710] Traceback (most recent call last): (EngineCore_DP0 pid=20437) ERROR 02-27 20:04:46 [core.py:710] File "/home/r00813794/vllm/vllm/vllm/v1/engine/core.py", line 701, in run_engine_core (EngineCore_DP0 pid=20437) ERROR 02-27 20:04:46 [core.p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: OffloadingConnector: assert len(req.block_hashes) >= num_gpu_blocks bug;stale ### Your current environment ### 🐛 Describe the bug I run the ``` vllm serve /home/models/MiMo-7B-Base --host 0.0.0.0 --port 8206 --block_siz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: pid=20437) ERROR 02-27 20:04:46 [core.py:710] meta = self.connector.build_connector_meta(scheduler_output) (EngineCore_DP0 pid=20437) ERROR 02-27 20:04:46 [core.py:710] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: environment ### 🐛 Describe the bug I run the ``` vllm serve /home/models/MiMo-7B-Base --host 0.0.0.0 --port 8206 --block_size=16 --max_model_len=6144 --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 0}}' ``` to start the online service and run the ``` vllm bench serve --backend vllm --model /home/models/MiMo-7B-Base --host 0.0.0.0 --port 8206 --dataset-name random --random-input-len 4096 --random-output-len 1024 --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
