# vllm-project/vllm#1888: Throughput issues with Tensor Parallelism (Mistral 7B + FP16)

| 字段 | 值 |
| --- | --- |
| Issue | [#1888](https://github.com/vllm-project/vllm/issues/1888) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Throughput issues with Tensor Parallelism (Mistral 7B + FP16)

### Issue 正文摘录

Today, I was testing on a node with 8x A100. I used a fine-tuned Mistral 7B, no quantization and just running FP16. The specific use-case is to summarize long documents and eventually chatting with them. Settings: ```bash python benchmark_throughput.py \ --backend vllm \ --model mistralai/Mistral-7B-Instruct-v0.1 \ --tensor-parallel-size 8 \ --dtype float16 \ --input-len 10240 \ --output-len 1024 \ --num-prompts 100 ``` Setup: Python 3.10, PyTorch 2.1.0, CUDA 12.1. Throughput: - 1x A100 (TP=1): 0.575 requests/second, 6464 tokens/second - 8x A100 (TP=8): 0.27 requests/second, 2957 tokens/second - Note: I did not get to try 2x, 3x, 4x, etc. as these tests were taking a long time to finish because I started out with 1000 prompts. Questions: - Is this the expected performance? - Why does TP not scale well, is there a bug? - Is the expected way to scale to more requests/second to use Ray/KubeRay to create replicas of vLLM with TP=1? I found similar problems described in #1838 #1707 #1435 but unsure if it has been determined there is a bug.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: I was testing on a node with 8x A100. I used a fine-tuned Mistral 7B, no quantization and just running FP16. The specific use-case is to summarize long documents and eventually chatting with them. Settings: ```bash pyth...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Throughput issues with Tensor Parallelism (Mistral 7B + FP16) Today, I was testing on a node with 8x A100. I used a fine-tuned Mistral 7B, no quantization and just running FP16. The specific use-case is to summarize lon...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Throughput issues with Tensor Parallelism (Mistral 7B + FP16) Today, I was testing on a node with 8x A100. I used a fine-tuned Mistral 7B, no quantization and just running FP16. The specific use-case is to summarize long
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d a fine-tuned Mistral 7B, no quantization and just running FP16. The specific use-case is to summarize long documents and eventually chatting with them. Settings: ```bash python benchmark_throughput.py \ --backend vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ng with them. Settings: ```bash python benchmark_throughput.py \ --backend vllm \ --model mistralai/Mistral-7B-Instruct-v0.1 \ --tensor-parallel-size 8 \ --dtype float16 \ --input-len 10240 \ --output-len 1024 \ --num-p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
