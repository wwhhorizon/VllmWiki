# vllm-project/vllm#14614: [Usage]: What's the best practice of deploying DeepSeekV3 using vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#14614](https://github.com/vllm-project/vllm/issues/14614) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What's the best practice of deploying DeepSeekV3 using vllm?

### Issue 正文摘录

### Your current environment For the environment, i simply use the official vllm v0.7.3 docker image. ### How would you like to use vllm I want to run inference of [DeepSeekV3](https://huggingface.co/deepseek-ai/DeepSeek-V3) on multi-node GPU clusters. I have followed the [vllm guide](https://docs.vllm.ai/en/latest/serving/distributed_serving.html) to setup the distributed serving environment with the vllm v0.7.3 docker image. More specifically: ``` NCCL_SOCKET_IFNAME=eth0 \ GLOO_SOCKET_IFNAME=eth0 \ HF_EVALUATE_OFFLINE=1 \ HF_DATASETS_OFFLINE=1 \ TRANSFORMERS_OFFLINE=1 \ vllm serve xxx \ --trust-remote-code \ --enforce-eager \ --tensor-parallel-size 16 2>&1 | tee api_serve.log ``` to start api serving. ``` for out_len in 1024 2048 4096 8192 16384 32768 do echo "running with output-len $out_len" TRANSFORMERS_OFFLINE=1 \ python3 -m sglang.bench_serving \ --model xxx \ --backend vllm \ --dataset-name random \ --random-input-len 2048 \ --random-output-len $out_len \ --num-prompts 2000 \ --output-file result-out$out_len.json \ --seed 42 \ --max-concurrency 1024 \ --port 8000 2>&1 | tee log_out$out_len.log done ``` to benchmark the vllm performance I want to ask 1. Any additional flags...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ld you like to use vllm I want to run inference of [DeepSeekV3](https://huggingface.co/deepseek-ai/DeepSeek-V3) on multi-node GPU clusters. I have followed the [vllm guide](https://docs.vllm.ai/en/latest/serving/distrib...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: GPU clusters. I have followed the [vllm guide](https://docs.vllm.ai/en/latest/serving/distributed_serving.html) to setup the distributed serving environment with the vllm v0.7.3 docker image. More specifically: ``` NCCL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### Your current environment For the environment, i simply use the official vllm v0.7.3 docker image. ### How would you like to use vllm I want to run inference of [DeepSeekV3](https://huggingface.co/deepseek-ai/DeepSee...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: \ python3 -m sglang.bench_serving \ --model xxx \ --backend vllm \ --dataset-name random \ --random-input-len 2048 \ --random-output-len $out_len \ --num-prompts 2000 \ --output-file result-out$out_len.json \ --seed 42 \
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
