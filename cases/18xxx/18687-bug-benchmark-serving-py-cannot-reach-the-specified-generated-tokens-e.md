# vllm-project/vllm#18687: [Bug]: benchmark_serving.py cannot reach the specified generated tokens even with the flag --ignore-eos

| 字段 | 值 |
| --- | --- |
| Issue | [#18687](https://github.com/vllm-project/vllm/issues/18687) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: benchmark_serving.py cannot reach the specified generated tokens even with the flag --ignore-eos

### Issue 正文摘录

### Your current environment nvidia L20 cuda 12.4 vllm 0.7.2 & 0.8.5 & 0.9.1 ### 🐛 Describe the bug （vllm 0.8.5post1 and 0.9.1）First of all, I launched the api server via: `vllm serve /telechat2/telechat2-35B-32K/ --dtype float16 -tp 4 --port 1122 --max-model-len 65536 --trust-remote-code` And then, I ran the benchmark_serving.py with the following command: `vllm bench serve --model /data/llm-models/telechat2/telechat2-35B-32K/ --num-prompts 1 --random-input-len 6144 --random-output-len 2048 --port 1122 --trust-remote-code --ignore-eos` The terminal returns: ![Image](https://github.com/user-attachments/assets/9a6708e5-d3ac-408c-9b45-21fe779a2e0a) **I also tried diffierent input-len such as input-len=6145 , but it cannot reach the right output-len either** **（vllm 0.7.2）Same process as above, but get** **the right output length** why?and how to solve this problem? ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: launched the api server via: `vllm serve /telechat2/telechat2-35B-32K/ --dtype float16 -tp 4 --port 1122 --max-model-len 65536 --trust-remote-code` And then, I ran the benchmark_serving.py with the following command: `v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the flag --ignore-eos bug;stale ### Your current environment nvidia L20 cuda 12.4 vllm 0.7.2 & 0.8.5 & 0.9.1 ### 🐛 Describe the bug （vllm 0.8.5post1 and 0.9.1）First of all, I launched the api server via: `vllm serve /te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: benchmark_serving.py cannot reach the specified generated tokens even with the flag --ignore-eos bug;stale ### Your current environment nvidia L20 cuda 12.4 vllm 0.7.2 & 0.8.5 & 0.9.1 ### 🐛 Describe the bug （vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: benchmark_serving.py cannot reach the specified generated tokens even with the flag --ignore-eos bug;stale ### Your current environment nvidia L20 cuda 12.4 vllm 0.7.2 & 0.8.5 & 0.9.1 ### 🐛 Describe the bug （vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ve /telechat2/telechat2-35B-32K/ --dtype float16 -tp 4 --port 1122 --max-model-len 65536 --trust-remote-code` And then, I ran the benchmark_serving.py with the following command: `vllm bench serve --model /data/llm-mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
