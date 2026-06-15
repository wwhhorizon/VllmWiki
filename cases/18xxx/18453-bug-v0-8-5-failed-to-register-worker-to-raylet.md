# vllm-project/vllm#18453: [Bug]: v0.8.5 Failed to register worker to Raylet

| 字段 | 值 |
| --- | --- |
| Issue | [#18453](https://github.com/vllm-project/vllm/issues/18453) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.8.5 Failed to register worker to Raylet

### Issue 正文摘录

vllm-v0.8.5 I try to deploy DeepSeek R1 on 2 nodes(8*H20 for each), this is my steps: 1. Pick a node as the head node, and run the following command: ``` ray start --head --port=6379 ``` 2. On the rest of the worker nodes, run the following command: ``` ray start --address=${HEAD_NODE_ADDRESS}:6379 ``` 3. on the head node: ``` vllm serve /model_path_to/DeepSeek-R1 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --trust-remote-code \ --max-model-len 40000 \ --gpu-memory-utilization 0.85 \ --port 8080 ``` after the 3rd step, It ocurrs : core_worker.cc:514: Failed to register worker to Raylet: IOError: [RayletClient] Unable to register worker with raylet. Failed to read data from the socket: End of file worker_id=01000000ffffffffffffffffffffffffffffffffffffffffffffffff I use the same steps for vLLM-v0.7.0, It works fine!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dress=${HEAD_NODE_ADDRESS}:6379 ``` 3. on the head node: ``` vllm serve /model_path_to/DeepSeek-R1 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --trust-remote-code \ --max-model-len 40000 \ --gpu-memory-uti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: v0.8.5 Failed to register worker to Raylet bug;stale vllm-v0.8.5 I try to deploy DeepSeek R1 on 2 nodes(8*H20 for each), this is my steps: 1. Pick a node as the head node, and run the following command: ``` ray s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
