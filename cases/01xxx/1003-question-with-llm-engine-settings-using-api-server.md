# vllm-project/vllm#1003: question with llm engine settings using api_server.

| 字段 | 值 |
| --- | --- |
| Issue | [#1003](https://github.com/vllm-project/vllm/issues/1003) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;sampling |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> question with llm engine settings using api_server.

### Issue 正文摘录

Hi, I am using OpenAI API python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen-7B --host 0.0.0.0 --port 8001 --trust-remote-code to post a quest like: { "model":"Qwen/Qwen-7B", "messages":[{"role":"user","content":"Tell me a story"}], "stream":false, "temperature":0.7, "max_tokens":500 } the server side stats shows: Received request cmpl-bd26ae24cc03420994e9cf497e3b4530: prompt: ' system\nYou are a helpful assistant. \n user\nTell me a story \n assistant\n', sampling params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, temperature=0.7, top_p=1.0, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=False, max_tokens=500, logprobs=None), prompt token ids: [151644, 8948, 198, 2610, 525, 264, 10950, 17847, 13, 151645, 198, 151644, 872, 198, 40451, 752, 264, 3364, 151645, 198, 151644, 77091, 198]. INFO 09-10 12:13:24 llm_engine.py:613] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.5%, CPU KV cache usage: 0.0% INFO 09-10 12:13:29 llm_engine.py:613] Avg prompt throughput: 0.0 tokens/s, Avg generation t...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: frequency_penalty=0.0, temperature=0.7, top_p=1.0, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=False, max_tokens=500, logprobs=None), prompt token ids: [151644, 8948, 1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: doing wrong? thanks. gpu params are: NVIDIA-SMI 515.48.07 Driver Version: 515.48.07 CUDA Version: 11.7 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id D...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: I am using OpenAI API python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen-7B --host 0.0.0.0 --port 8001 --trust-remote-code to post a quest like: { "model":"Qwen/Qwen-7B", "messages":[{"role":"user","content"...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.5%, CPU KV cache usage: 0.0% INFO 09-10 12:13:29 llm_engine.py:613] Avg prompt throughput: 0.0 tokens/s, Avg generation throughp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: B", "messages":[{"role":"user","content":"Tell me a story"}], "stream":false, "temperature":0.7, "max_tokens":500 } the server side stats shows: Received request cmpl-bd26ae24cc03420994e9cf497e3b4530: prompt: ' system\n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
