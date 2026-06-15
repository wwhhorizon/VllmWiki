# vllm-project/vllm#27823: [Doc]: Multi-node distributed guide issues

| 字段 | 值 |
| --- | --- |
| Issue | [#27823](https://github.com/vllm-project/vllm/issues/27823) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Multi-node distributed guide issues

### Issue 正文摘录

### 📚 The doc issue For context, see a recent issue (https://github.com/ROCm/ROCm/issues/5567) where a user was trying to set up distributed inference with `ray` by following guidance at https://docs.vllm.ai/en/v0.8.0/serving/distributed_serving.html#running-vllm-on-multiple-nodes. I ran into several issues setting this up on AMD GPUs that I believe might be deficiencies in the vLLM docs: - The `run_cluster.sh` script passes `--gpus all` which I believe is NVIDIA-only, needed to remove this from the script - I had to add `--distributed_executor_backend="ray"` to the `vllm serve` command to get vLLM to use the `ray` cluster that the script sets up - I had to set NCCL_SOCKET_IFNAME and GLOO_SOCKET_IFNAME to the appropriate network interfaces, otherwise ran into a NCCL connection error - Relevant environment variables (NCCL_SOCKET_IFNAME, GLOO_SOCKET_IFNAME, NCCL_DEBUG) are not propagated to the Docker containers that the script creates; I worked around this by adding them to the `ray` invocation in `run_cluster.sh`, but I don't see a reason why the script shouldn't pass these to the container automatically I also needed to set `--enforce-eager` but I believe that is an issue specifi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: o several issues setting this up on AMD GPUs that I believe might be deficiencies in the vLLM docs: - The `run_cluster.sh` script passes `--gpus all` which I believe is NVIDIA-only, needed to remove this from the script...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### 📚 The doc issue For context, see a recent issue (https://github.com/ROCm/ROCm/issues/5567) where a user was trying to set up distributed inference with `ray` by following guidance at https://docs.vllm.ai/en/v0.8.0/s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed to remove this from the script - I had to add `--distributed_executor_backend="ray"` to the `vllm serve` command to get vLLM to use the `ray` cluster that the script sets up - I had to set NCCL_SOCKET_IFNAME and GLOO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Multi-node distributed guide issues documentation;stale ### 📚 The doc issue For context, see a recent issue (https://github.com/ROCm/ROCm/issues/5567) where a user was trying to set up distributed inference with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rom our Docker images. The image I used and got working was `rocm/vllm:latest` which at the time had vLLM 0.11. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
