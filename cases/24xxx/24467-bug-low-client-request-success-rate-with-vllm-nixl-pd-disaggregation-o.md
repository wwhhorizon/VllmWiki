# vllm-project/vllm#24467: [Bug]: low client request success rate with vllm+nixl PD disaggregation on 2-node H100

| 字段 | 值 |
| --- | --- |
| Issue | [#24467](https://github.com/vllm-project/vllm/issues/24467) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: low client request success rate with vllm+nixl PD disaggregation on 2-node H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have tested vllm+nixl PD disaggregation on 2 H100 node, with both llama3.1-8B and llama3.3-70B model. The successful request rate is super low with some configurations (longer input or output length). I am using docker image: vllm/vllm-openai:v0.10.1.1, the command I am using is as below: prefill: VLLM_DISAGG_PREFILL_ROLE=prefill CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 VLLM_NIXL_SIDE_CHANNEL_HOST=10.10.38.12 VLLM_NIXL_SIDE_CHANNEL_PORT=5575 UCX_TLS=rc,sm,self,cuda_copy,cuda_ipc,gdr_copy UCX_NET_DEVICES=mlx5_0:1 UCX_SOCKADDR_TLS_PRIORITY=rdmacm,tcp UCX_RDMA_CM_ENABLED=y UCX_MEMTYPE_CACHE=y UCX_IB_GPU_DIRECT_RDMA=y UCX_RNDV_SCHEME=get_zcopy UCX_RNDV_THRESH=4k UCX_LOG_LEVEL=info VLLM_USE_V1=1 vllm serve /data/Llama-3.1-8B-Instruct --tensor_parallel_size 8 --max-model-len 8192 --enforce-eager --trust-remote-code --disable-log-requests --gpu-memory-utilization 0.85 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_rank":0,"kv_parallel_size":8,"kv_buffer_device":"cuda"}' --host 0.0.0.0 --port 8000 decode: VLLM_DISAGG_PREFILL_ROLE=decode CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 UCX_TLS=rc,sm,self,cuda_copy,cuda_ip...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: w with some configurations (longer input or output length). I am using docker image: vllm/vllm-openai:v0.10.1.1, the command I am using is as below: prefill: VLLM_DISAGG_PREFILL_ROLE=prefill CUDA_VISIBLE_DEVICES=0,1,2,3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: w client request success rate with vllm+nixl PD disaggregation on 2-node H100 bug ### Your current environment ### 🐛 Describe the bug I have tested vllm+nixl PD disaggregation on 2 H100 node, with both llama3.1-8B and l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug I have tested vllm+nixl PD disaggregation on 2 H100 node, with both llama3.1-8B and llama3.3-70B model. The successful request rate is super low with some configurations (longer input or output length). I am using d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: low client request success rate with vllm+nixl PD disaggregation on 2-node H100 bug ### Your current environment ### 🐛 Describe the bug I have tested vllm+nixl PD disaggregation on 2 H100 node, with both llama3.1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: H100 bug ### Your current environment ### 🐛 Describe the bug I have tested vllm+nixl PD disaggregation on 2 H100 node, with both llama3.1-8B and llama3.3-70B model. The successful request rate is super low with some con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
