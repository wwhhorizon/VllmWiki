# vllm-project/vllm#12670: [Bug]: DeepSeek multinode inference - Error: No available node types can fulfill resource request

| 字段 | 值 |
| --- | --- |
| Issue | [#12670](https://github.com/vllm-project/vllm/issues/12670) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek multinode inference - Error: No available node types can fulfill resource request

### Issue 正文摘录

### Your current environment I have issue as indicated by the title when I try to run multi-node inference for DeepSeek V3 with two 8*H100. After I setup the ray cluster, I am able to see following by `ray status`. ``` ======== Autoscaler status: 2025-02-02 19:52:24.223188 ======== Node status --------------------------------------------------------------- Active: 1 node_e6107ebf05bbc00 1 node_4c9baf725a0e654 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/384.0 CPU 0.0/16.0 GPU 0B/3.88TiB memory 0B/19.46GiB object_store_memory Demands: {'node:ec2- .us-west-2.compute.amazonaws.com': 0.001, 'GPU': 1.0} * 1, {'GPU': 1.0} * 15 (PACK): 1+ pending placement groups ``` I used the lastest docker of vllm and followed the latest instruction [here](https://github.com/vllm-project/vllm/blob/main/docs/source/serving/distributed_serving.md#troubleshooting-incorrect-hardware-driver) to include `-e VLLM_HOST_IP` in running `run_cluster.sh` file but still, I have those type of error ``` (autoscaler +10m11s, ip=172.31.42.4) Error: No available node types can fulfill resource request {'node:ec2- .us-west...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: title when I try to run multi-node inference for DeepSeek V3 with two 8*H100. After I setup the ray cluster, I am able to see following by `ray status`. ``` ======== Autoscaler status: 2025-02-02 19:52:24.223188 =======...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ultinode inference - Error: No available node types can fulfill resource request bug;ray ### Your current environment I have issue as indicated by the title when I try to run multi-node inference for DeepSeek V3 with tw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ': 1.0} * 15 (PACK): 1+ pending placement groups ``` I used the lastest docker of vllm and followed the latest instruction [here](https://github.com/vllm-project/vllm/blob/main/docs/source/serving/distributed_serving.md...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: y cluster, I am able to see following by `ray status`. ``` ======== Autoscaler status: 2025-02-02 19:52:24.223188 ======== Node status --------------------------------------------------------------- Active: 1 node_e6107...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ://github.com/vllm-project/vllm/issues/7815#issuecomment-2569684364 ### Model Input Dumps Same as above. ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
