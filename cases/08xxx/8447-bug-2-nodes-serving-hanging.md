# vllm-project/vllm#8447: [Bug]: 2 nodes serving hanging 

| 字段 | 值 |
| --- | --- |
| Issue | [#8447](https://github.com/vllm-project/vllm/issues/8447) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 2 nodes serving hanging 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug running command: export NCCL_DEBUG=INFO export CUDA_LAUNCH_BLOCKING=1 export VLLM_TRACE_FUNCTION=1 python3 api_server.py \ --model my_model \ -tp 8 \ -pp 2 \ --enforce-eager \ --max-num-seqs=32 \ --dtype=bfloat16 \ --worker-use-ray \ --gpu-memory-utilization 0.8 logs are hanging here: INFO 09-12 23:40:47 utils.py:977] Found nccl from library libnccl.so.2 INFO 09-12 23:40:47 pynccl.py:63] vLLM is using nccl==2.20.5 VM-160-69-tencentos:561:561 [0] NCCL INFO Using non-device net plugin version 0 VM-160-69-tencentos:561:561 [0] NCCL INFO Using network IB VM-160-69-tencentos:561:561 [0] NCCL INFO comm 0x1476dca0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 23000 commId 0xa015ae7e0a50005d - Init START (RayWorkerWrapper pid=248, ip=10.1.160.68) INFO 09-12 23:40:47 utils.py:977] Found nccl from library libnccl.so.2 (RayWorkerWrapper pid=248, ip=10.1.160.68) INFO 09-12 23:40:47 pynccl.py:63] vLLM is using nccl==2.20.5 VM-160-69-tencentos:561:561 [0] NCCL INFO Setting affinity for GPU 0 to 0f,ffffffff,ffffffff,ffffffff VM-160-69-tencentos:561:561 [0] NCCL INFO comm 0x1476dca0 rank 0 nRanks 2 nNodes 2 localR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .5 VM-160-69-tencentos:561:561 [0] NCCL INFO Using non-device net plugin version 0 VM-160-69-tencentos:561:561 [0] NCCL INFO Using network IB VM-160-69-tencentos:561:561 [0] NCCL INFO comm 0x1476dca0 rank 0 nranks 2 cud...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: model my_model \ -tp 8 \ -pp 2 \ --enforce-eager \ --max-num-seqs=32 \ --dtype=bfloat16 \ --worker-use-ray \ --gpu-memory-utilization 0.8 logs are hanging here: INFO 09-12 23:40:47 utils.py:977] Found nccl from library...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### 🐛 Describe the bug running command: export NCCL_DEBUG=INFO export CUDA_LAUNCH_BLOCKING=1 export VLLM_TRACE_FUNCTION=1 python3 api_server.py \ --model my_model \ -tp 8 \ -pp 2 \ --enforce-eager \ --max-num-seqs=32 \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error dtype;env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ibe the bug running command: export NCCL_DEBUG=INFO export CUDA_LAUNCH_BLOCKING=1 export VLLM_TRACE_FUNCTION=1 python3 api_server.py \ --model my_model \ -tp 8 \ -pp 2 \ --enforce-eager \ --max-num-seqs=32 \ --dtype=bfl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
