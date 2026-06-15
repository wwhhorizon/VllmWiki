# vllm-project/vllm#32400: [Bug]: Ray cluster(5 Node), Deploy DP=2, Creating too many placement groups

| 字段 | 值 |
| --- | --- |
| Issue | [#32400](https://github.com/vllm-project/vllm/issues/32400) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Ray cluster(5 Node), Deploy DP=2, Creating too many placement groups

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/4fd9d6a85c00ac0186aa9abbeff73fc2ac6c721e/vllm/v1/engine/utils.py#L511 Environment: 5*Node * 8NPU Deploy Parameters: vllm serve /home/models/Qwen3-VL-235B-A22B-Instruct --host 0.0.0.0 --port 8000 --data-parallel-backend ray --data-parallel-size-local 1 --data-parallel-size 2 --api-server-count 1 --seed 1024 --served-model-name qwen3vl --tensor-parallel-size 8 --max-num-seqs 4 --max-model-len 10000 --max-num-batched-tokens 1024 --trust-remote-code --no-enable-prefix-caching --gpu-memory-utilization 0.8 --swap-space 64 Errors: (APIServer pid=600860) File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 120, in make_async_mp_client (APIServer pid=600860) return DPLBAsyncMPClient(*client_args) (APIServer pid=600860) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=600860) File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 1182, in init (APIServer pid=600860) super().__init__( (APIServer pid=600860) File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 1023, in init (APIServer pid=600860) super().__init__( (APIServer pid=600860) File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 810, in init (APIServer...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: #L511 Environment: 5*Node * 8NPU Deploy Parameters: vllm serve /home/models/Qwen3-VL-235B-A22B-Instruct --host 0.0.0.0 --port 8000 --data-parallel-backend ray --data-parallel-size-local 1 --data-parallel-size 2 --api-se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: wen3-VL-235B-A22B-Instruct --host 0.0.0.0 --port 8000 --data-parallel-backend ray --data-parallel-size-local 1 --data-parallel-size 2 --api-server-count 1 --seed 1024 --served-model-name qwen3vl --tensor-parallel-size 8...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: Ray cluster(5 Node), Deploy DP=2, Creating too many placement groups stale https://github.com/vllm-project/vllm/blob/4fd9d6a85c00ac0186aa9abbeff73fc2ac6c721e/vllm/v1/engine/utils.py#L511 Environment: 5*Node * 8NPU D...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
