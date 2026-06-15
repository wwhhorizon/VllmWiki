# vllm-project/vllm#11709: [Usage]: Getting shape mismatch for multimodal input with task="embed"

| 字段 | 值 |
| --- | --- |
| Issue | [#11709](https://github.com/vllm-project/vllm/issues/11709) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Getting shape mismatch for multimodal input with task="embed"

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I am running the following code, I getting a shape mismatch error ``` llm = LLM(model="Qwen/Qwen2-VL-2B-Instruct", download_dir="/root/cache", enable_lora=True, task="embed") message = f"{req['input_text']} " (output,) = llm.encode({ "prompt": message, "multi_modal_data": {"image": image} }) ``` Error: `RuntimeError: shape mismatch: value tensor of shape [324, 1536] cannot be broadcast to indexing result of shape [0, 1536]` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Getting shape mismatch for multimodal input with task="embed" usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I am running the follow...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Getting shape mismatch for multimodal input with task="embed" usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I am running the follow...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Usage]: Getting shape mismatch for multimodal input with task="embed" usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I am running the follow...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
