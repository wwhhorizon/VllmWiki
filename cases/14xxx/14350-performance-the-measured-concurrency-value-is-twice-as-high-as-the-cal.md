# vllm-project/vllm#14350: [Performance]: The measured concurrency value is twice as high as the calculated value in the formula, why?

| 字段 | 值 |
| --- | --- |
| Issue | [#14350](https://github.com/vllm-project/vllm/issues/14350) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: The measured concurrency value is twice as high as the calculated value in the formula, why?

### Issue 正文摘录

### Proposal to improve performance I want to calculate the concurrency that can be achieved from the kv cache usage. I use the following calculation method: ``` KVCache Size = 2×L×b×n×d×(Byte count per element) ``` where L, b. N and d are the number of hidden layers, concurrency value, sequence length, and hidden layer size, respectively. So for the following model, there will be a theoretical concurrency value: Model | Parameters (Billion) | Layers | Hidden size | 量化类型 | Total Mem (GB) | Reserved Mem(GB) | Sequence Length | Cocurrency （Theoretical） | Cocurrency （Measured ） -- | -- | -- | -- | -- | -- | -- | -- | -- | -- DeepSeek-R1-Distill-Qwen-1.5B | 1.5 | 28 | 1536 | fp16 | 16 | 2 | 4096 | 16.76 | / DeepSeek-R1-Distill-Qwen-7B | 7 | 28 | 3584 | fp16 | 32 | 2 | 4096 | 10.45 | / DeepSeek-R1-Distill-Llama-8B-q4 | 8 | 32 | 4096 | int4 | 32 | 2 | 4096 | 48.60 | / DeepSeek-R1-Distill-Qwen-14B | 14 | 48 | 5120 | fp16 | 48 | 2 | 4096 | 4.80 | 9.60 DeepSeek-R1-Distill-Qwen-32B | 32 | 64 | 5120 | fp16 | 96 | 4 | 4096 | 5.60 | 11.20 DeepSeek-R1-Distill-Llama-70B | 70 | 80 | 8192 | fp16 | 160 | 4 | 4096 | 1.60 | 3.20 DeepSeek-V3-q2 | 671 | 61 | 7168 | int2 | 220 | 4 | 4096 | 24.06 | / Dee...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ence length, and hidden layer size, respectively. So for the following model, there will be a theoretical concurrency value: Model | Parameters (Billion) | Layers | Hidden size | 量化类型 | Total Mem (GB) | Reserved Mem(GB)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: | 2 | 4096 | 10.45 | / DeepSeek-R1-Distill-Llama-8B-q4 | 8 | 32 | 4096 | int4 | 32 | 2 | 4096 | 48.60 | / DeepSeek-R1-Distill-Qwen-14B | 14 | 48 | 5120 | fp16 | 48 | 2 | 4096 | 4.80 | 9.60 DeepSeek-R1-Distill-Qwen-32B |...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: error? Or， vllm has special optimizations ? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The out...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lculated value. Where did I make a calculation error? Or， vllm has special optimizations ? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
