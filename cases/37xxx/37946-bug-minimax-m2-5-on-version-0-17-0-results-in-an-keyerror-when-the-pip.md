# vllm-project/vllm#37946: [Bug]: Minimax-M2.5 on version 0.17.0 results in an keyerror when the pipeline parallelism (PP) is greater than or equal to 2

| 字段 | 值 |
| --- | --- |
| Issue | [#37946](https://github.com/vllm-project/vllm/issues/37946) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Minimax-M2.5 on version 0.17.0 results in an keyerror when the pipeline parallelism (PP) is greater than or equal to 2

### Issue 正文摘录

### Your current environment Four servers, each equipped with two 80GB A800 GPUs, running vLLM version 0.17.0. The image startup script is as follows: `# 1 docker run -itd --entrypoint /bin/bash --network host --ipc=host \ --name ray_vllm_node --shm-size 10.24g --gpus all \ -v /nfsai/ai:/mllm_models \ -e GLOO_SOCKET_IFNAME=bond0 -e NCCL_SOCKET_IFNAME=bond0 \ -e TP_SOCKET_IFNAME=bond0 -e NCCL_DEBUG=TRACE \ -e VLLM_LOG_LEVEL=DEBUG \ swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/vllm/vllm-openai:v0.17.0 # 2、header ray start --head --port=6379 --dashboard-host='0.0.0.0' --disable-usage-stats # 3、worker ray start --address=headerip:6379` vllm server script is as follows: `nohup python3 -m vllm.entrypoints.openai.api_server \ --model /mllm_models/MiniMax/MiniMax-M2.5 \ --served-model-name MiniMax-M2.5 \ --tensor-parallel-size 2 \ --pipeline-parallel-size 4 \ --enable-expert-parallel \ --enable-auto-tool-choice \ --max-model-len 32000 \ --max_num_seqs 32 \ --enable-chunked-prefill \ --enable-prefix-caching \ --trust-remote-code \ --host 0.0.0.0 \ --port 8001 \ --dtype bfloat16 \ --quantization fp8 \ --gpu-memory-utilization 0.87 \ --tool-call-parser minimax_m2 \ --chat-template /mll...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: caching \ --trust-remote-code \ --host 0.0.0.0 \ --port 8001 \ --dtype bfloat16 \ --quantization fp8 \ --gpu-memory-utilization 0.87 \ --tool-call-parser minimax_m2 \ --chat-template /mllm_models/MiniMax/MiniMax-M2.5/ch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Minimax-M2.5 on version 0.17.0 results in an keyerror when the pipeline parallelism (PP) is greater than or equal to 2 bug ### Your current environment Four servers, each equipped with two 80GB A800 GPUs, running...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: M2.5 on version 0.17.0 results in an keyerror when the pipeline parallelism (PP) is greater than or equal to 2 bug ### Your current environment Four servers, each equipped with two 80GB A800 GPUs, running vLLM version 0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: \ --reasoning-parser minimax_m2_append_think \ --distributed-executor-backend ray > ./minimax-m2.5-20260316.log 2>&1 &` ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/fabba25a-8dbf-44d0-855c-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -name ray_vllm_node --shm-size 10.24g --gpus all \ -v /nfsai/ai:/mllm_models \ -e GLOO_SOCKET_IFNAME=bond0 -e NCCL_SOCKET_IFNAME=bond0 \ -e TP_SOCKET_IFNAME=bond0 -e NCCL_DEBUG=TRACE \ -e VLLM_LOG_LEVEL=DEBUG \ swr.cn-n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
