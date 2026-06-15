# vllm-project/vllm#4282: [Bug]: When will vllm support P-Tuning_V2 fine-tuning models

| 字段 | 值 |
| --- | --- |
| Issue | [#4282](https://github.com/vllm-project/vllm/issues/4282) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When will vllm support P-Tuning_V2 fine-tuning models

### Issue 正文摘录

### Your current environment llm = LLM(model="checkpoint-3000", trust_remote_code=True, gpu_memory_utilization=0.5, tokenizer_mode="auto", tensor_parallel_size=1, dtype="float16") ### 🐛 Describe the bug File "/home/zj/.conda/envs/ChatGLM3/lib/python3.11/site-packages/vllm/model_executor/models/chatglm.py", line 389, in load_weights param = params_dict[name] ~~~~~~~~~~~^^^^^^ KeyError: 'transformer.prefix_encoder.embedding.weight'

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: u_memory_utilization=0.5, tokenizer_mode="auto", tensor_parallel_size=1, dtype="float16") ### 🐛 Describe the bug File "/home/zj/.conda/envs/ChatGLM3/lib/python3.11/site-packages/vllm/model_executor/models/chatglm.py", l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: When will vllm support P-Tuning_V2 fine-tuning models bug;stale ### Your current environment llm = LLM(model="checkpoint-3000", trust_remote_code=True, gpu_memory_utilization=0.5, tokenizer_mode="auto", tensor_pa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: When will vllm support P-Tuning_V2 fine-tuning models bug;stale ### Your current environment llm = LLM(model="checkpoint-3000", trust_remote_code=True, gpu_memory_utilization=0.5, tokenizer_mode="auto", tensor_pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
