# vllm-project/vllm#13521: [Bug]: Can't serve on ray cluster although passing VLLM_HOST_IP

| 字段 | 值 |
| --- | --- |
| Issue | [#13521](https://github.com/vllm-project/vllm/issues/13521) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't serve on ray cluster although passing VLLM_HOST_IP

### Issue 正文摘录

### Your current environment `vLLM API server version 0.7.2` ### 🐛 Describe the bug I create a cluster with two instance each with 1 GPU. - head ``` RAY_num_heartbeats_timeout=600 ray start --head --node-ip-address HEAD-IP \ --port 6379 \ --ray-client-server-port 10001 \ --object-manager-port=8076 \ --node-manager-port=8077 -------------------- Ray runtime started. -------------------- Next steps To add another node to this Ray cluster, run ray start --address='HEAD-IP:6379' ``` - worker ``` ray start --object-manager-port=8076 \ --address='HEAD-IP:6379' \ --node-manager-port=8077 ``` - serve model with two option, first only send `--tensor-parallel-size 1 --pipeline-parallel-size 2` and second time with ` --tensor-parallel-size 2` and with both I have the following error: - Error: ``` 2025-02-19 07:41:17,494 INFO worker.py:1654 -- Connecting to existing Ray cluster at address: HEAD-IP:6379... 2025-02-19 07:41:17,507 INFO worker.py:1832 -- Connected to Ray cluster. View the dashboard at 127.0.0.1:8265 (autoscaler +18s) Tip: use `ray status` to view detailed cluster status. To disable these messages, set RAY_SCHEDULER_EVENTS=0. (autoscaler +18s) Error: No available node types can f...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Can't serve on ray cluster although passing VLLM_HOST_IP bug;ray;stale ### Your current environment `vLLM API server version 0.7.2` ### 🐛 Describe the bug I create a cluster with two instance each with 1 GPU. - h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ress='HEAD-IP:6379' \ --node-manager-port=8077 ``` - serve model with two option, first only send `--tensor-parallel-size 1 --pipeline-parallel-size 2` and second time with ` --tensor-parallel-size 2` and with both I ha...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tensor-parallel-size 1 --pipeline-parallel-size 2 --distributed-executor-backend ray ``` - ``` VLLM_HOST_IP=HEAD-IP:6379 vllm serve NousResearch/Meta-Llama-3.1-8B-Instruct --max-model-len 8192 --gpu-memory-utilization 0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: LLM_HOST_IP bug;ray;stale ### Your current environment `vLLM API server version 0.7.2` ### 🐛 Describe the bug I create a cluster with two instance each with 1 GPU. - head ``` RAY_num_heartbeats_timeout=600 ray start --h...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -- Connected to Ray cluster. View the dashboard at 127.0.0.1:8265 (autoscaler +18s) Tip: use `ray status` to view detailed cluster status. To disable these messages, set RAY_SCHEDULER_EVENTS=0. (autoscaler +18s) Error:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
