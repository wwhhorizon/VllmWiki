# vllm-project/vllm#8179: [Bug]: Frequent Errors:async_llm_engine.py:158] Aborted request

| 字段 | 值 |
| --- | --- |
| Issue | [#8179](https://github.com/vllm-project/vllm/issues/8179) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Frequent Errors:async_llm_engine.py:158] Aborted request

### Issue 正文摘录

### Your current environment ```text File "/data/tangjiakai/agentscope/src/agentscope/models/openai_model.py", line 268, in __call__ response = self.client.chat.completions.create(**kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/envs/agentscope/lib/python3.11/site-packages/openai/_utils/_utils.py", line 274, in wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/envs/agentscope/lib/python3.11/site-packages/openai/resources/chat/completions.py", line 668, in create return self._post( ^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/envs/agentscope/lib/python3.11/site-packages/openai/_base_client.py", line 1260, in post return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/envs/agentscope/lib/python3.11/site-packages/openai/_base_client.py", line 937, in request return self._request( ^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/envs/agentscope/lib/python3.11/site-packages/openai/_base_client.py", line 1026, in _request return self._retry_request( ^^^^^^^^^^^^^^^^^^^^ File...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt environment ```text File "/data/tangjiakai/agentscope/src/agentscope/models/openai_model.py", line 268, in __call__ response = self.client.chat.completions.create(**kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: --enable-lora \ --disable-frontend-multiprocessing ``` The vllm version = 0.6.0, Some prompts will encounter this problem. The same prompt sometimes succeeds and sometimes fails. ### Before submitting a new issue... - [...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nstruct \ --trust-remote-code \ --port $port \ --dtype auto \ --pipeline-parallel-size 1 \ --enforce-eager \ --enable-prefix-caching \ --enable-lora \ --disable-frontend-multiprocessing ``` The vllm version = 0.6.0, Som...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: f._make_status_error_from_response(err.response) from None openai.InternalServerError: Error code: 500 - {'detail': ''} ``` ### 🐛 Describe the bug The cmd is ``` python -m vllm.entrypoints.openai.api_server \ --model /d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
