# vllm-project/vllm#21298: [Usage]: How to test throughput of 2:4 sparse model?

| 字段 | 值 |
| --- | --- |
| Issue | [#21298](https://github.com/vllm-project/vllm/issues/21298) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to test throughput of 2:4 sparse model?

### Issue 正文摘录

### Your current environment ```text I am currently testing like this: ``` ```` vllm bench throughput --model "/home/geiger/gwb082/Jonathans_Thesis/LLMCBench/llm-compressor/Meta-Llama-3-8B-Instruct-W4A16-G128" --backend vllm --dataset-name random --input-len 32 --output-len 128 --num-prompts 1000 --max-num-batched-tokens 32768 --dtype auto --seed 42 --output-json llama3-8b_w4a16.json ``` but didn't find any flag like sparsity or sth. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: h. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to test throughput of 2:4 sparse model? usage;stale ### Your current environment ```text I am currently testing like this: ``` ```` vllm bench throughput --model "/home/geiger/gwb082/Jonathans_Thesis/LLMCBe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: How to test throughput of 2:4 sparse model? usage;stale ### Your current environment ```text I am currently testing like this: ``` ```` vllm bench throughput --model "/home/geiger/gwb082/Jonathans_Thesis/LLMCBe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Thesis/LLMCBench/llm-compressor/Meta-Llama-3-8B-Instruct-W4A16-G128" --backend vllm --dataset-name random --input-len 32 --output-len 128 --num-prompts 1000 --max-num-batched-tokens 32768 --dtype auto --seed 42 --output...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: output-len 128 --num-prompts 1000 --max-num-batched-tokens 32768 --dtype auto --seed 42 --output-json llama3-8b_w4a16.json ``` but didn't find any flag like sparsity or sth. ### How would you like to use vllm I want to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
