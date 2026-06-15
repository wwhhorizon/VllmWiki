# vllm-project/vllm#14090: [Installation]:  ValueError: No supported config format found in meta-llama/Llama-3.3-70B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#14090](https://github.com/vllm-project/vllm/issues/14090) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]:  ValueError: No supported config format found in meta-llama/Llama-3.3-70B-Instruct

### Issue 正文摘录

### Your current environment Im trying to run vLLM on my machine with two gfx90a GPUs (ROCm). However, I keep getting no config supported for all the models I have tried including Llama3, Llama3.3, Mistral, etc. Note that my HF key is appropriately set and it has access to the models. I am using the `rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6` Docker Image. Any idea what's going on here? Dockerfile: ``` FROM rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6 RUN apt-get update && apt-get install -y \ curl \ wget \ && rm -rf /var/lib/apt/lists/* COPY entrypoint.sh /entrypoint.sh RUN chmod +x /entrypoint.sh ENTRYPOINT ["/entrypoint.sh"] ``` entrypoint.sh: ``` #!/bin/bash set -e # Default values MODEL=${MODEL:-"meta-llama/Llama-3.3-70B-Instruct"} TENSOR_PARALLEL_SIZE=${TENSOR_PARALLEL_SIZE:-2} HOST=${HOST:-"0.0.0.0"} PORT=${PORT:-8000} if [ -z "$HF_API_KEY" ]; then echo "Error. HF_API_KEY is not set." exit 1 fi export HUGGING_FACE_HUB_TOKEN=$HF_API_KEY # Any custom setup you need echo "Starting vLLM server with model: $MODEL" # Execute the vLLM server exec vllm serve $MODEL \ --trust-remote-code \ --tensor-parallel-size $TENSOR_PARALLEL_SIZE \ --host $HOST \ --port...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Installation]: ValueError: No supported config format found in meta-llama/Llama-3.3-70B-Instruct installation ### Your current environment Im trying to run vLLM on my machine with two gfx90a GPUs (ROCm). However, I kee...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t environment Im trying to run vLLM on my machine with two gfx90a GPUs (ROCm). However, I keep getting no config supported for all the models I have tried including Llama3, Llama3.3, Mistral, etc. Note that my HF key is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: ValueError: No supported config format found in meta-llama/Llama-3.3-70B-Instruct installation ### Your current environment Im trying to run vLLM on my machine with two gfx90a GPUs (ROCm). However, I kee
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
