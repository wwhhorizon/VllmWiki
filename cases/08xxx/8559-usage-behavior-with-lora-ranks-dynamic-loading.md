# vllm-project/vllm#8559: [Usage]:   Behavior with LoRA Ranks dynamic loading

| 字段 | 值 |
| --- | --- |
| Issue | [#8559](https://github.com/vllm-project/vllm/issues/8559) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:   Behavior with LoRA Ranks dynamic loading

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, I’ve encountered a couple of issues while trying the new [feat](https://github.com/vllm-project/vllm/pull/6566), and I’m hoping to get clarification or assistance. VLLM container: vllm/vllm-openai:latest lora rank 8 weight: https://huggingface.co/Akchacha/meta-llama-Meta-Llama-3-8B-Instruct-1726391523/blob/main/adapter_config.json lora rank 16 weight: https://huggingface.co/Akchacha/meta-llama-Meta-Llama-3-8B-Instruct-1725954636/blob/main/adapter_config.json server launch cmd ``` python3 -m vllm.entrypoints.openai.api_server --port 8080 \ --model /mnt/inference/models/Meta-Llama-3-8B-Instruct \ --served-model-name base-model --enable-lora --max-lora-rank=64 --max-loras=60 ``` ## First inference request took too long between LoRA ranks: 1. Load/unload lora adaptors is working fine. ``` curl -X POST http://localhost:8080/v1/load_lora_adapter \ -H "Content-Type: application/json" \ -d '{"lora_name": "lora8", "lora_path": "/mnt/test/test-lora8"}' ``` 2. First forward pass is taking too much time. ``` curl -X POST localhost8080/v1/chat/completions \ -H "Content-Type: ap...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ce. VLLM container: vllm/vllm-openai:latest lora rank 8 weight: https://huggingface.co/Akchacha/meta-llama-Meta-Llama-3-8B-Instruct-1726391523/blob/main/adapter_config.json lora rank 16 weight: https://huggingface.co/Ak...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=100, min...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Behavior with LoRA Ranks dynamic loading usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, I’ve encountered a couple of issues whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: to get clarification or assistance. VLLM container: vllm/vllm-openai:latest lora rank 8 weight: https://huggingface.co/Akchacha/meta-llama-Meta-Llama-3-8B-Instruct-1726391523/blob/main/adapter_config.json lora rank 16 w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: x_tokens=100, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [128000, 128006, 882, 128007, 271, 15339, 12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
