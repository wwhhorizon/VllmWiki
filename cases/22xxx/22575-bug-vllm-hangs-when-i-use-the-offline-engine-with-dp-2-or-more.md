# vllm-project/vllm#22575: [Bug]: Vllm hangs when I use the offline engine with dp = 2 or more

| 字段 | 值 |
| --- | --- |
| Issue | [#22575](https://github.com/vllm-project/vllm/issues/22575) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Vllm hangs when I use the offline engine with dp = 2 or more

### Issue 正文摘录

### Your current environment Vllm hangs when I use the offline engine with dp = 2 or more example from vllm import LLM llm = LLM( model="mistralai/Mistral-Small-3.1-24B-Instruct-2503", quantization="fp8", kv_cache_dtype="fp8", data_parallel_size=2, tensor_parallel_size=1, max_num_seqs=256, enforce_eager=True, tokenizer_mode="mistral", config_format="mistral", load_format="mistral", # If DP stalls in your setup, uncomment the two lines below: ) ### 🐛 Describe the bug Vllm hangs when I use the offline engine with dp = 2 or more example from vllm import LLM llm = LLM( model="mistralai/Mistral-Small-3.1-24B-Instruct-2503", quantization="fp8", kv_cache_dtype="fp8", data_parallel_size=2, tensor_parallel_size=1, max_num_seqs=256, enforce_eager=True, tokenizer_mode="mistral", config_format="mistral", load_format="mistral", # If DP stalls in your setup, uncomment the two lines below: ) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lm = LLM( model="mistralai/Mistral-Small-3.1-24B-Instruct-2503", quantization="fp8", kv_cache_dtype="fp8", data_parallel_size=2, tensor_parallel_size=1, max_num_seqs=256, enforce_eager=True, tokenizer_mode="mistral", co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ngine with dp = 2 or more example from vllm import LLM llm = LLM( model="mistralai/Mistral-Small-3.1-24B-Instruct-2503", quantization="fp8", kv_cache_dtype="fp8", data_parallel_size=2, tensor_parallel_size=1, max_num_se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: example from vllm import LLM llm = LLM( model="mistralai/Mistral-Small-3.1-24B-Instruct-2503", quantization="fp8", kv_cache_dtype="fp8", data_parallel_size=2, tensor_parallel_size=1, max_num_seqs=256, enforce_eager=True...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s when I use the offline engine with dp = 2 or more example from vllm import LLM llm = LLM( model="mistralai/Mistral-Small-3.1-24B-Instruct-2503", quantization="fp8", kv_cache_dtype="fp8", data_parallel_size=2, tensor_p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Vllm hangs when I use the offline engine with dp = 2 or more bug;stale ### Your current environment Vllm hangs when I use the offline engine with dp = 2 or more example from vllm import LLM llm = LLM( model="mist...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
