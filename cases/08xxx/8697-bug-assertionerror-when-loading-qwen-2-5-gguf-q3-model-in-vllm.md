# vllm-project/vllm#8697: [Bug]: AssertionError when loading Qwen 2.5 GGUF q3 model in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#8697](https://github.com/vllm-project/vllm/issues/8697) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError when loading Qwen 2.5 GGUF q3 model in vLLM

### Issue 正文摘录

### Your current environment I'm encountering an AssertionError when trying to load the Qwen 2.5 GGUF (Qwen-2.5-q3_gguf.bin) model using vLLM. The error occurs in the vocab_parallel_embedding.py file, where it asserts that the loaded weight's shape matches the expected vocabulary size. Below is the traceback of the error: ### Model Input Dumps _No response_ ### 🐛 Describe the bug python -m vllm.entrypoints.openai.api_server --model /data/models/Qwen2.5-32B-Instruct-GGUF-q3_k_m/qwen2.5-32b-instruct-q3_k_m.gguf --dtype float16 --api-key '' --tensor-parallel-size 1 --trust-remote-code --gpu-memory-utilization 0.8 --port 8000 --max_model_len 10000 --enforce-eager --quantization gguf gguf file It works fine in ollama ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: dels/Qwen2.5-32B-Instruct-GGUF-q3_k_m/qwen2.5-32b-instruct-q3_k_m.gguf --dtype float16 --api-key '' --tensor-parallel-size 1 --trust-remote-code --gpu-memory-utilization 0.8 --port 8000 --max_model_len 10000 --enforce-e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: AssertionError when loading Qwen 2.5 GGUF q3 model in vLLM bug ### Your current environment I'm encountering an AssertionError when trying to load the Qwen 2.5 GGUF (Qwen-2.5-q3_gguf.bin) model using vLLM. The er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ama ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
