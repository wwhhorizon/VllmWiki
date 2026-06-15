# vllm-project/vllm#27971: [Bug]: ibm-granite/granite-4.0-h-tiny model fails for CPU on vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#27971](https://github.com/vllm-project/vllm/issues/27971) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ibm-granite/granite-4.0-h-tiny model fails for CPU on vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run `ibm-granite/granite-4.0-h-tiny` on a IBM Power 10 system with the below script ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) def main(): model_path = "ibm-granite/granite-4.0-h-tiny" llm = LLM(model=model_path, max_model_len=4096) # Build chat-style prompts from the simple prompts list using the # tokenizer's chat template (adds model-specific system/instruction text # and generation prompt if supported by the tokenizer). chat_prompts = [] for p in prompts: chat = [{"role": "user", "content": p}] chat_prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True) chat_prompts.append(chat_prompt) print("Chat-formatted Prompts:\n" + "-" * 60) for chat_prompt in chat_prompts: print(repr(chat_prompt)) print("-" * 60) # Generate texts from the chat-formatted prompts. outputs = llm.generate(chat_prompts, sampling_...

## 现有链接修复摘要

#39157 [CPU] Enable Granite 4 / Mamba models on CPU backend

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ny` on a IBM Power 10 system with the below script ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer # Sample prompts. prompts = [ "Hello, my name is", "The president of the United St...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Using max model len 4096 INFO 10-21 03:56:02 [arg_utils.py:1301] Chunked prefill is not supported for ARM and POWER, S390X and RISC-V CPUs; disabling it for V1 backend. INFO 10-21 03:56:02 [config.py:323] Disabling casc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: tomatically detected platform cpu. INFO 10-21 03:55:58 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. INFO 10-21 03:56:01 [utils.py:243] non-default args:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: p}] chat_prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True) chat_prompts.append(chat_prompt) print("Chat-formatted Prompts:\n" + "-" * 60) for chat_prompt in chat_prompts: print(rep...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39157](https://github.com/vllm-project/vllm/pull/39157) | closes_keyword | 0.95 | [CPU] Enable Granite 4 / Mamba models on CPU backend  | Fixes: #27971 This PR enables execution for Granite 4 / Mamba architecture models on CPU backends which were previously crashing due to tightly coupled Triton kernel dependencie |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
