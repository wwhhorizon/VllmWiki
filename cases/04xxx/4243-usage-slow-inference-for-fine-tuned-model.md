# vllm-project/vllm#4243: [Usage]: slow inference for fine-tuned model

| 字段 | 值 |
| --- | --- |
| Issue | [#4243](https://github.com/vllm-project/vllm/issues/4243) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: slow inference for fine-tuned model

### Issue 正文摘录

### Your current environment I am using SFT of huggingface transformers to fine tune model mistral 7b. https://github.com/huggingface/trl/blob/main/examples/scripts/sft.py After fine-tuning, the model works well, by loading via langchain - vllm (vllm version: 0.4.0)(https://python.langchain.com/docs/integrations/llms/vllm/), ``` from langchain_community.llms import VLLM llm = VLLM( model="mistralai/Mistral-7B-Instruct-v0.2", # or drop-in replacement of fine-tuned model with local path trust_remote_code=True, # mandatory for hf models max_new_tokens=128, top_k=10, top_p=0.95, temperature=0.8, ) ``` However, the inference latency is round 2-3 times slower than the original "mistralai/Mistral-7B-Instruct-v0.2". May I ask is there any specific settings that i have missed for applying vllm on SFT model ? Thanks. ### How would you like to use vllm run vllm on fine-tuned model.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ine-tuning, the model works well, by loading via langchain - vllm (vllm version: 0.4.0)(https://python.langchain.com/docs/integrations/llms/vllm/), ``` from langchain_community.llms import VLLM llm = VLLM( model="mistra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: slow inference for fine-tuned model usage;stale ### Your current environment I am using SFT of huggingface transformers to fine tune model mistral 7b. https://github.com/huggingface/trl/blob/main/examples/scrip...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: slow inference for fine-tuned model usage;stale ### Your current environment I am using SFT of huggingface transformers to fine tune model mistral 7b. https://github.com/huggingface/trl/blob/main/examples/scrip...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: _k=10, top_p=0.95, temperature=0.8, ) ``` However, the inference latency is round 2-3 times slower than the original "mistralai/Mistral-7B-Instruct-v0.2". May I ask is there any specific settings that i have missed for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
