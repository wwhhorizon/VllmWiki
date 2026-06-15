# vllm-project/vllm#16853: [Bug]: Two BOS when using chat

| 字段 | 值 |
| --- | --- |
| Issue | [#16853](https://github.com/vllm-project/vllm/issues/16853) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Two BOS when using chat

### Issue 正文摘录

### Your current environment vllm 0.8.4 ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM("meta-llama/Llama-3.2-1B-Instruct", gpu_memory_utilization=0.3) prompt = [{"role": "user", "content": "Are you ok?"}] out = llm.chat(prompt) print(out[0].prompt_token_ids[:2], llm.get_tokenizer().bos_token_id) ``` ``` ([128000, 128000], 128000) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ent environment vllm 0.8.4 ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM("meta-llama/Llama-3.2-1B-Instruct", gpu_memory_utilization=0.3) prompt = [{"role": "user", "content": "Are you ok?"}] out = llm....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM("meta-llama/Llama-3.2-1B-Instruct", gpu_memory_utilization=0.3) prompt = [{"role": "user", "content": "Are you ok?"}] out = llm.chat(prompt) print(out[0].p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
