# vllm-project/vllm#27209: [Bug]: VLLM Hang when DP=2, USE_EP=TRUE, backend = pplx

| 字段 | 值 |
| --- | --- |
| Issue | [#27209](https://github.com/vllm-project/vllm/issues/27209) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM Hang when DP=2, USE_EP=TRUE, backend = pplx

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is a very simple script to reproduce this error: sever: ``` export CUDA_VISIBLE_DEVICES=0,1 # 让 vLLM 走新版执行路径 export VLLM_USE_V1=1 # 强制 vLLM 的 all-to-all 用 PPLX export VLLM_ALL2ALL_BACKEND=pplx # 单机测试：让 NVSHMEM 不走远程传输 export NVSHMEM_REMOTE_TRANSPORT=none # 避免 NCCL 去探测 IB/RDMA，单机更稳 export NCCL_IB_DISABLE=1 # 开启 NCCL 日志，若卡住便于看 AllGather/AllToAll 进度 export NCCL_DEBUG=INFO python -m vllm.entrypoints.openai.api_server \ --model allenai/OLMoE-1B-7B-0924-Instruct \ --enable-expert-parallel \ --tensor-parallel-size 1 \ --data-parallel-size 2 \ --enforce-eager \ --max-model-len 1024 \ --gpu-memory-utilization 0.30 ``` client: run this python file: ``` from openai import OpenAI cli = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="EMPTY") resp = cli.chat.completions.create( model="allenai/OLMoE-1B-7B-0924-Instruct", messages=[{"role": "user", "content": "Ping! 只要快速回一句话即可。"}], temperature=0.0, max_tokens=8, ) print("OK:", resp.choices[0].message.content.strip()) ``` Client get no response and server jam (but util is 100%), when i use other backends "naive" or "allgather_reducescatter", it work smoothly. I think there is sth wrong w...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: This is a very simple script to reproduce this error: sever: ``` export CUDA_VISIBLE_DEVICES=0,1 # 让 vLLM 走新版执行路径 export VLLM_USE_V1=1 # 强制 vLLM 的 all-to-all 用 PPLX export VLLM_ALL2ALL_BACKEND=pplx # 单机测试：让 NVSHMEM 不走远程...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: mory-utilization 0.30 ``` client: run this python file: ``` from openai import OpenAI cli = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="EMPTY") resp = cli.chat.completions.create( model="allenai/OLMoE-1B-7B-092...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: =INFO python -m vllm.entrypoints.openai.api_server \ --model allenai/OLMoE-1B-7B-0924-Instruct \ --enable-expert-parallel \ --tensor-parallel-size 1 \ --data-parallel-size 2 \ --enforce-eager \ --max-model-len 1024 \ --...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: VLLM Hang when DP=2, USE_EP=TRUE, backend = pplx bug;stale ### Your current environment ### 🐛 Describe the bug This is a very simple script to reproduce this error: sever: ``` export CUDA_VISIBLE_DEVICES=0,1 # 让...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: environment ### 🐛 Describe the bug This is a very simple script to reproduce this error: sever: ``` export CUDA_VISIBLE_DEVICES=0,1 # 让 vLLM 走新版执行路径 export VLLM_USE_V1=1 # 强制 vLLM 的 all-to-all 用 PPLX export VLLM_ALL2ALL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
