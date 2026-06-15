# vllm-project/vllm#16547: [Bug]: running DeepSeek V3 on vllm0.8.3 v1 Engine, but ray exception got

| 字段 | 值 |
| --- | --- |
| Issue | [#16547](https://github.com/vllm-project/vllm/issues/16547) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: running DeepSeek V3 on vllm0.8.3 v1 Engine, but ray exception got

### Issue 正文摘录

### Your current environment H20 docker image: NGC 24.12 docker image with `pip install vllm==0.8.3` to install vllm==0.8.3 Ray: 2.43.0 torch: 2.6.0 vllm: 0.8.3 ### 🐛 Describe the bug I established the ray connections for two nodes H20: ```bash export NUMEXPR_MAX_THREADS=192 export NCCL_SOCKET_IFNAME=eth0 export GLOO_SOCKET_IFNAME=eth0 export VLLM_ATTENTION_BACKEND=FLASHMLA ray start --head --port=8199 ray start --address=${HEAD_NODE_ADDRESS}:8199 ``` After ray started normally, I started the vllm server, ``` python3 -m vllm.entrypoints.openai.api_server --port 30001 --max_model_len 10000 --max_num_seqs 128 --gpu_memory_utilization 0.8 -tp 16 --model /mnt/data ``` after long time loading model weights, I started the testing client: ``` python3 vllm/benchmarks/benchmark_serving.py --port 30001 --dataset-name random --random-input-len 500 --random-output-len 500 --random-range-ratio 0.6 --model /mnt/data --num-prompts 1000 --max-concurrency 128 ``` It could work for a little time, but soon I got this error, which is rather annoying: It looks like ray meets some errors when compiling dag, that experimental things may not be robust enough! ![Image](https://github.com/user-attachments/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: but ray exception got bug;ray;stale ### Your current environment H20 docker image: NGC 24.12 docker image with `pip install vllm==0.8.3` to install vllm==0.8.3 Ray: 2.43.0 torch: 2.6.0 vllm: 0.8.3 ### 🐛 Describe the bug...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: odel /mnt/data ``` after long time loading model weights, I started the testing client: ``` python3 vllm/benchmarks/benchmark_serving.py --port 30001 --dataset-name random --random-input-len 500 --random-output-len 500...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _SOCKET_IFNAME=eth0 export GLOO_SOCKET_IFNAME=eth0 export VLLM_ATTENTION_BACKEND=FLASHMLA ray start --head --port=8199 ray start --address=${HEAD_NODE_ADDRESS}:8199 ``` After ray started normally, I started the vllm ser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 95) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r, ``` python3 -m vllm.entrypoints.openai.api_server --port 30001 --max_model_len 10000 --max_num_seqs 128 --gpu_memory_utilization 0.8 -tp 16 --model /mnt/data ``` after long time loading model weights, I started the t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
