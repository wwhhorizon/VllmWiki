# vllm-project/vllm#5273: [Bug]: chatglm3 with lora adapter

| 字段 | 值 |
| --- | --- |
| Issue | [#5273](https://github.com/vllm-project/vllm/issues/5273) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: chatglm3 with lora adapter

### Issue 正文摘录

### Your current environment ```text vllm 0.4.2 transformers 4.40.0 ``` ### 🐛 Describe the bug ```shell python -m vllm.entrypoints.openai.api_server --model /LLM/basemodels/chatglm/chatglm3-6b/ --enable-lora --lora-modules lora_1=/llama-factory/results/checkpoint-2410 --gpu-memory-utilization 0.6 --served-model-name chatglm3 --port 10025 --trust-remote-code ``` ```shell curl http://localhost:10025/v1/completions -H "Content-Type: application/json" -d '{ "model": "lora_1", "prompt": "你好", "max_tokens": 500, "temperature": 0 }' ``` ## AttributeError ``` File "/data/liqy-a/miniconda3/envs/vllm042/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 271, in add_request_async return self.add_request(request_id, File "/data/liqy-a/miniconda3/envs/vllm042/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 427, in add_request eos_token_id = self.tokenizer.get_lora_tokenizer( File "/data/liqy-a/miniconda3/envs/vllm042/lib/python3.10/site-packages/vllm/transformers_utils/tokenizer_group/tokenizer_group.py", line 59, in get_lora_tokenizer tokenizer = (get_lora_tokenizer( File "/data/liqy-a/miniconda3/envs/vllm042/lib/python3.10/site-packages/vllm/transformers_utils/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: escribe the bug ```shell python -m vllm.entrypoints.openai.api_server --model /LLM/basemodels/chatglm/chatglm3-6b/ --enable-lora --lora-modules lora_1=/llama-factory/results/checkpoint-2410 --gpu-memory-utilization 0.6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hon3.10/site-packages/vllm/engine/async_llm_engine.py", line 271, in add_request_async return self.add_request(request_id, File "/data/liqy-a/miniconda3/envs/vllm042/lib/python3.10/site-packages/vllm/engine/llm_engine.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
