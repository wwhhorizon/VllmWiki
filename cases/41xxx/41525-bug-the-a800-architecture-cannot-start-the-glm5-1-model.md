# vllm-project/vllm#41525: [Bug]: the A800 architecture cannot start the glm5.1 model.

| 字段 | 值 |
| --- | --- |
| Issue | [#41525](https://github.com/vllm-project/vllm/issues/41525) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: the A800 architecture cannot start the glm5.1 model.

### Issue 正文摘录

### Your current environment vLLM version: docker vllm/vllm-openai:v0.19.1 or vllm/vllm-openai:v0.20.0-cu130-ubuntu2404 GPU: 8x NVIDIA A800-SXM4-80GB (sm80, Ampere) OS: Ubuntu 22.04, Linux 5.15.0 ### 🐛 Describe the bug I currently plan to deploy the glm5.1 model using 8 A800 servers, but I found the deployment failed. Could you please help me figure out how to solve this problem? > In addition, I can successfully build the minimax m2.7 and kimi k2.6 models. However, glm5.1 and deepseek v4 both failed. start vllm container command. eg. ```bash HEAD_IP=100.64.10.10 docker rm -f vllm-glm5.1 docker run -it --gpus all \ --net=host \ --name vllm-glm5.1 \ --privileged --ipc=host \ -v /mnt/public-storage/model/ZhipuAI:/models \ -v /dev/infiniband:/dev/infiniband \ -e NCCL_DEBUG=INFO \ -e NCCL_IB_HCA=mlx5_10,mlx5_11,mlx5_12,mlx5_13 \ -e NCCL_SOCKET_IFNAME=bond0 \ -e GLOO_SOCKET_IFNAME=bond0 \ -e NCCL_IB_DISABLE=0 \ -e NCCL_NET_GDR_LEVEL=5 \ harbor-pro.xxx.net/library/vllm/vllm-openai:v0.19.1 \ --served-model-name GLM-5.1 \ --model /models/GLM-5.1 \ --trust-remote-code \ --chat-template-content-format=string \ --tensor-parallel-size 8 \ --pipeline-parallel-size 8 \ --nnodes 8 \ --node-rank...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug]: the A800 architecture cannot start the glm5.1 model. bug ### Your current environment vLLM version: docker vllm/vllm-openai:v0.19.1 or vllm/vllm-openai:v0.20.0-cu130-ubuntu2404 GPU: 8x NVIDIA A800-SXM4-80GB (sm80...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: re cannot start the glm5.1 model. bug ### Your current environment vLLM version: docker vllm/vllm-openai:v0.19.1 or vllm/vllm-openai:v0.20.0-cu130-ubuntu2404 GPU: 8x NVIDIA A800-SXM4-80GB (sm80, Ampere) OS: Ubuntu 22.04...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ntion backend found for cuda with AttentionSelectorConfig(head_size=576, dtype=torch.bfloat16, kv_cache_dtype=auto, block_size=None, use_mla=True, has_sink=False, use_sparse=True, use_mm_prefix=False, use_per_head_quant...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 5-02 13:02:22 [multiproc_executor.py:857] ValueError: No valid attention backend found for cuda with AttentionSelectorConfig(head_size=576, dtype=torch.bfloat16, kv_cache_dtype=auto, block_size=None, use_mla=True, has_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: the A800 architecture cannot start the glm5.1 model. bug ### Your current environment vLLM version: docker vllm/vllm-openai:v0.19.1 or vllm/vllm-openai:v0.20.0-cu130-ubuntu2404 GPU: 8x NVIDIA A800-SXM4-80GB (sm80...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
