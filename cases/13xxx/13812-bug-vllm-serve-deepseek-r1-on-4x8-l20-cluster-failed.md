# vllm-project/vllm#13812: [Bug]: vLLM serve Deepseek-R1 on 4x8*L20 cluster failed

| 字段 | 值 |
| --- | --- |
| Issue | [#13812](https://github.com/vllm-project/vllm/issues/13812) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM serve Deepseek-R1 on 4x8*L20 cluster failed

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` Sry current no network connection on the server The vllm docker version is v0.7.1 8 L20 on each node with 2 IB card, Driver Version: 550.54.14 ni cluster commend: bash run_cluster.sh vllm/vllm-openai:12.4 10.128.122.1 --worker /lustre/models/ --privileged -e VLLM_HOST_IP=10.128.125.1 -e NCCL_IB_HCA=mlx5_0,mlx5_3 -e GLOO_SOCKET_IFNAME=ens9f0np0 -e NCCL_SOCKET_IFNAME=ens9f0np0 And GPU P2P is supported on each node ### 🐛 Describe the bug I tried deploy the Deepseek-R1 671B on our 4x8*L20 cluster, and I comfirm that each node can be connected to each other. I followe the instruction of our officail vllm distributed deployment guide and get ray cluster done ![Image](https://github.com/user-attachments/assets/0b167cd1-8e83-4e26-8ad5-0273d271536d) Then I started to deploy the model, command "NCCL_DEBUG=INFO vllm serve /root/deepseek-671b --served-model-name deepseek-r1 --tensor-parallel- size 8 --pipeline-parallel-size 4 --trust_remote_code --max-num-seqs 4096" then It started to load the weight successfully but ends up with an error: ![Image](https://github.com/user-attachments/assets/d62e2aea-4098-42bb-ba60-2e8b31acfc6a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ollect_env.py` Sry current no network connection on the server The vllm docker version is v0.7.1 8 L20 on each node with 2 IB card, Driver Version: 550.54.14 ni cluster commend: bash run_cluster.sh vllm/vllm-openai:12.4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: m? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: un_cluster.sh vllm/vllm-openai:12.4 10.128.122.1 --worker /lustre/models/ --privileged -e VLLM_HOST_IP=10.128.125.1 -e NCCL_IB_HCA=mlx5_0,mlx5_3 -e GLOO_SOCKET_IFNAME=ens9f0np0 -e NCCL_SOCKET_IFNAME=ens9f0np0 And GPU P2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
