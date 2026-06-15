# vllm-project/vllm#13204: [Performance]: Why vllm infers slower when implemented with LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#13204](https://github.com/vllm-project/vllm/issues/13204) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Why vllm infers slower when implemented with LoRA

### Issue 正文摘录

### Proposal to improve performance My model is `Qwen2.5-72B-Instruct-AWQ`, vllm version is `0.7.0`, I use the LoRA adapter which is trained from Llama-factory, to run in vllm. # With LoRA Instructions is `vllm serve models/Qwen2.5-72B-Instruct-AWQ --port 8001 --trust-remote-code --tensor-parallel-size 1 --quantization awq --enforce-eager --gpu-memory-utilization 0.9 --enable-lora --lora-modules lora1=/LLaMA-Factory/saves/Qwen2.5-72B-Instruct-AWQ/lora/train_2025-02-12-11-57-47` model with LoRA: ```python llm = ChatOpenAI( model="lora1", openai_api_key="None", openai_api_base="http://localhost:8001/v1", ) ``` When with `LoRA`, vllm output `Avg generation throughput: 6.5 tokens/s` ---- # Without LoRA Instructions is `vllm serve models/Qwen2.5-72B-Instruct-AWQ --port 8001 --trust-remote-code --tensor-parallel-size 1 --quantization awq --enforce-eager --gpu-memory-utilization 0.9` model without LoRA: ```python llm = ChatOpenAI( model="Qwen2.5-72B-Instruct-AWQ", openai_api_key="None", openai_api_base="http://localhost:8001/v1", ) ``` When without `LoRA`, vllm output `Avg generation throughput: 17.6 tokens/s` ---- So, why this is different? Should quantify LoRA to int4? ### Report of pe...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mplemented with LoRA performance ### Proposal to improve performance My model is `Qwen2.5-72B-Instruct-AWQ`, vllm version is `0.7.0`, I use the LoRA adapter which is trained from Llama-factory, to run in vllm. # With Lo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: /localhost:8001/v1", ) ``` When with `LoRA`, vllm output `Avg generation throughput: 6.5 tokens/s` ---- # Without LoRA Instructions is `vllm serve models/Qwen2.5-72B-Instruct-AWQ --port 8001 --trust-remote-code --tensor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -Instruct-AWQ --port 8001 --trust-remote-code --tensor-parallel-size 1 --quantization awq --enforce-eager --gpu-memory-utilization 0.9 --enable-lora --lora-modules lora1=/LLaMA-Factory/saves/Qwen2.5-72B-Instruct-AWQ/lor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sal to improve performance My model is `Qwen2.5-72B-Instruct-AWQ`, vllm version is `0.7.0`, I use the LoRA adapter which is trained from Llama-factory, to run in vllm. # With LoRA Instructions is `vllm serve models/Qwen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
