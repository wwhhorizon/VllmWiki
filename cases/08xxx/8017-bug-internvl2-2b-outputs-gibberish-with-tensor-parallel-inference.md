# vllm-project/vllm#8017: [Bug]: InternVL2-2B outputs gibberish with tensor parallel inference

| 字段 | 值 |
| --- | --- |
| Issue | [#8017](https://github.com/vllm-project/vllm/issues/8017) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: InternVL2-2B outputs gibberish with tensor parallel inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Reproduce** - Just run `examples/offline_inference_vision_language.py` with `tensor_parallel_size=2`. - The inference with `tensor_parallel_size=1` works normally. **Outputs** ``` Processed prompts: 100%|████████████████████████████████████████| 1/1 [00:01<00:00, 1.52s/it, est. speed input: 1192.65 toks/s, output: 26.96 toks/s] 1. 1. 1/2 3/2 1 for example �2/定有了一个iSA诉快的队/纳厄/否化，4. INFO 08-30 03:22:42 multiproc_worker_utils.py:136] Terminating local vLLM worker processes (VllmWorkerProcess pid=9476) INFO 08-30 03:22:42 multiproc_worker_utils.py:237] Worker exiting ``` **The root issue** - This is broken by the `split_qkv` function for `internlm2` backbone introduced in #7187 to make compatible with awq model. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: InternVL2-2B outputs gibberish with tensor parallel inference bug ### Your current environment ### 🐛 Describe the bug **Reproduce** - Just run `examples/offline_inference_vision_language.py` with `tensor_parallel...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: inference bug ### Your current environment ### 🐛 Describe the bug **Reproduce** - Just run `examples/offline_inference_vision_language.py` with `tensor_parallel_size=2`. - The inference with `tensor_parallel_size=1` wor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
