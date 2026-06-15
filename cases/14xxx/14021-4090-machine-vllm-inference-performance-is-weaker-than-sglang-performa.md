# vllm-project/vllm#14021: 4090 machine vllm inference performance is weaker than sglang performance！

| 字段 | 值 |
| --- | --- |
| Issue | [#14021](https://github.com/vllm-project/vllm/issues/14021) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 4090 machine vllm inference performance is weaker than sglang performance！

### Issue 正文摘录

### Your current environment Testing Machine：8x4090x24GiB Testing Model: DeepSeek-R1-Distill-Qwen-32B 1.vllm(0.7.3) v1 test： ``` VLLM_USE_V1=1 vllm serve /models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --served-model-name deepseek-r1-distill-qwen-32b --dtype=float16 --gpu-memory-utilization 0.80 --tensor-parallel-size 8 --trust-remote-code --port 8001 python3 benchmarks/benchmark_serving.py \ --backend vllm \ --model /models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \ --num-prompts 512 \ --dataset-name random \ --dataset-path /data/ShareGPT_V3_unfiltered_cleaned_split.json \ --random-input-len 1024 \ --random-output-len 1024 \ --seed 42 \ --port 8001 \ --host 0.0.0.0 \ --max-concurrency 32 ``` 2.sglang(v0.4.3) test: ``` python3 -m sglang.launch_server --model /models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --trust-remote-code --tp 8 --mem-fraction-static 0.80 python3 -m sglang.bench_serving --backend sglang --num-prompts 512 --random-input-len 1024 --random-output-len 1024 --dataset-name random --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json --max-concurrency 32 --seed 42 --host 127.0.0.1 --port 30000 ``` 3.result: ![Image](https://github.com/user-attachments/assets/2e3d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: v1 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -R1-Distill-Qwen-32B --served-model-name deepseek-r1-distill-qwen-32b --dtype=float16 --gpu-memory-utilization 0.80 --tensor-parallel-size 8 --trust-remote-code --port 8001 python3 benchmarks/benchmark_serving.py \ --ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: stale ### Your current environment Testing Machine：8x4090x24GiB Testing Model: DeepSeek-R1-Distill-Qwen-32B 1.vllm(0.7.3) v1 test： ``` VLLM_USE_V1=1 vllm serve /models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --served-m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: eaker than sglang performance！ usage;stale ### Your current environment Testing Machine：8x4090x24GiB Testing Model: DeepSeek-R1-Distill-Qwen-32B 1.vllm(0.7.3) v1 test： ``` VLLM_USE_V1=1 vllm serve /models/deepseek-ai/De...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ust-remote-code --port 8001 python3 benchmarks/benchmark_serving.py \ --backend vllm \ --model /models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \ --num-prompts 512 \ --dataset-name random \ --dataset-path /data/ShareGPT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
