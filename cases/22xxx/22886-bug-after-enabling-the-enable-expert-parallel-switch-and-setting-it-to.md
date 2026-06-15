# vllm-project/vllm#22886: [Bug]: After enabling the '--enable-expert-parallel' switch and setting it to 'deepep_high_throughput' mode, an error occurred during inference

| 字段 | 值 |
| --- | --- |
| Issue | [#22886](https://github.com/vllm-project/vllm/issues/22886) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After enabling the '--enable-expert-parallel' switch and setting it to 'deepep_high_throughput' mode, an error occurred during inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I was testing the DeepEP feature of vLLM 0.10.0 using two 8-GPU H100 servers, the API server started normally, but vLLM crashed with an error when running inference. The script is as follows, where the primary node runs `./test.sh 1` and the secondary node runs `./test.sh 2`. ```shell #!/bin/bash # model_path=/data/model/deepseek_V3/DeepSeek-V3-Chat model_path=/data/models/DeepSeek-V3-prune ip_1=172.30.87.177 rpc_port=30000 port=5000 node=$1 gpu_memory_utilization=0.9 max_model_len=4096 data_parallel_size=16 tensor_parallel_size=1 ###################################################### # Node 1 (Primary - handles incoming requests) if [ $node == 1 ] ; then data_parallel_size_local=8 data_parallel_start_rank=0 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 \ CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" \ vllm serve ${model_path} \ --host 0.0.0.0 \ --port ${port} \ --tensor-parallel-size ${tensor_parallel_size} \ --enable-expert-parallel \ --data-parallel-size ${data_parallel_size} \ --data-parallel-size-local ${data_parallel_size_local} \ --data-parallel-start-rank 0 \ --data-parallel-address ${ip_1} \ --data-paral...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe cuda;moe;operator;triton build_error;crash env_dependency Your curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ug When I was testing the DeepEP feature of vLLM 0.10.0 using two 8-GPU H100 servers, the API server started normally, but vLLM crashed with an error when running inference. The script is as follows, where the primary n...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: After enabling the '--enable-expert-parallel' switch and setting it to 'deepep_high_throughput' mode, an error occurred during inference bug;stale ### Your current environment ### 🐛 Describe the bug When I was te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: arallel_size_local=8 data_parallel_start_rank=0 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 \ CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" \ vllm serve ${model_path} \ --host 0.0.0.0 \ --port ${port} \ --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: to 'deepep_high_throughput' mode, an error occurred during inference bug;stale ### Your current environment ### 🐛 Describe the bug When I was testing the DeepEP feature of vLLM 0.10.0 using two 8-GPU H100 servers, the A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
