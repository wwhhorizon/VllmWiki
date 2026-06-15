# vllm-project/vllm#20976: [Usage]: How to turn off thinking using OpenAI client?

| 字段 | 值 |
| --- | --- |
| Issue | [#20976](https://github.com/vllm-project/vllm/issues/20976) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to turn off thinking using OpenAI client?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, i deployed Qwen3-30B-A3B-AWQ with reasoning enable using below command ``` vllm serve cognitivecomputations/Qwen3-30B-A3B-AWQ --enable-reasoning --reasoning-parser deepseek_r1 --port 8001 --tensor-parallel-size 2 --trust-remote-code --max-num-seqs 64 --gpu-memory-utilization 0.85 ``` Then, I found this python script that may help me turn on and turn off the thinking mode ``` extra_body={"chat_template_kwargs": {"thinking": True}} ``` https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_with_reasoning_streaming.py However when i trying to disable the thinking like below but it didn't work ``` stream = client.chat.completions.create( model="cognitivecomputations/Qwen3-30B-A3B-AWQ ", messages=messages, stream=True, extra_body={"chat_template_kwargs": {"thinking": False}} ) ``` Could anyone guide me how to on/off the thinking mode ? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: collect_env.py` ``` ### How would you like to use vllm Hi, i deployed Qwen3-30B-A3B-AWQ with reasoning enable using below command ``` vllm serve cognitivecomputations/Qwen3-30B-A3B-AWQ --enable-reasoning --reasoning-par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e ? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: stream=True, extra_body={"chat_template_kwargs": {"thinking": False}} ) ``` Could anyone guide me how to on/off the thinking mode ? ### Before submitting a new issue... - [x] Make sure you already searched for relevant...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
