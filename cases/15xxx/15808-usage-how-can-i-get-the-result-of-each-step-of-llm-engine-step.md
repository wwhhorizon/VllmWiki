# vllm-project/vllm#15808: [Usage]: How can I get the result of each step of llm_engine.step()

| 字段 | 值 |
| --- | --- |
| Issue | [#15808](https://github.com/vllm-project/vllm/issues/15808) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How can I get the result of each step of llm_engine.step()

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` vLLM version: v0.8.1 When I run benchmark_latency.py, I want to see the result of self.llm_engine.step(), but I can only see the complete result after finish. Why is that? The script is as follows: ```shell python3 benchmark_latency.py --model Qwen2-VL-7B-Instruct ``` and i add print() log in this place:https://github.com/vllm-project/vllm/blob/v0.8.1/vllm/entrypoints/llm.py#L1371 But I can only get all the output after finish. I can get the output results of each step, thank you～ ![Image](https://github.com/user-attachments/assets/22e891ae-c265-4a24-8d10-4fd8432661e3) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ent environment ```text The output of `python collect_env.py` ``` vLLM version: v0.8.1 When I run benchmark_latency.py, I want to see the result of self.llm_engine.step(), but I can only see the complete result after fi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: output of `python collect_env.py` ``` vLLM version: v0.8.1 When I run benchmark_latency.py, I want to see the result of self.llm_engine.step(), but I can only see the complete result after finish. Why is that? The scrip...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: that? The script is as follows: ```shell python3 benchmark_latency.py --model Qwen2-VL-7B-Instruct ``` and i add print() log in this place:https://github.com/vllm-project/vllm/blob/v0.8.1/vllm/entrypoints/llm.py#L1371 B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
