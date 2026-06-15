# vllm-project/vllm#2870: Trailing new lines "\n" with Qwen1.5-7B-Chat-AWQ and vllm v0.3.0

| 字段 | 值 |
| --- | --- |
| Issue | [#2870](https://github.com/vllm-project/vllm/issues/2870) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Trailing new lines "\n" with Qwen1.5-7B-Chat-AWQ and vllm v0.3.0

### Issue 正文摘录

I run vllm in a docker container with the following args: `["--quantization", "awq", "--enforce-eager", "--disable-custom-all-reduce", "--max-num-batched-tokens", "4096", "--max-model-len", "4096", "--model", "LoneStriker/Qwen1.5-7B-Chat-AWQ", "--host", "0.0.0.0", "--port", "8080", "--chat-template", "/chat_template/qwen1.5-7b-chat.jinja2"]` and chat template ``` {% for message in messages %}{{' ' + message['role'] + ' ' + message['content'] + ' ' + ' '}}{% endfor %}{% if add_generation_prompt %}{{ ' assistant ' }}{% endif %} ``` Every 2 or 3 queries I do, the model just fills up all remaining completion tokens with new lines ("\n"). It only happens if the messages I send to the model are > 1, i.e. if I add a history of messages. Does anyone else experience this? I tried without setting `--enforce-eager` and `--disable-custom-all-reduce`. I also noticed that with the v0.3.0 version, I get these outputs as if someone was calling the model: `INFO 02-14 15:30:16 llm_engine.py:877] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%` Might be unrelated, thoug...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ines "\n" with Qwen1.5-7B-Chat-AWQ and vllm v0.3.0 stale I run vllm in a docker container with the following args: `["--quantization", "awq", "--enforce-eager", "--disable-custom-all-reduce", "--max-num-batched-tokens",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Trailing new lines "\n" with Qwen1.5-7B-Chat-AWQ and vllm v0.3.0 stale I run vllm in a docker container with the following args: `["--quantization", "awq", "--enforce-eager", "--disable-custom-all-reduce", "--max-num-ba...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .0 stale I run vllm in a docker container with the following args: `["--quantization", "awq", "--enforce-eager", "--disable-custom-all-reduce", "--max-num-batched-tokens", "4096", "--max-model-len", "4096", "--model", "...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%` Might be unrelated, though **Update**: I use streaming and `vllm.entrypoints.openai.api_server`
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: to the model are > 1, i.e. if I add a history of messages. Does anyone else experience this? I tried without setting `--enforce-eager` and `--disable-custom-all-reduce`. I also noticed that with the v0.3.0 version, I ge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
