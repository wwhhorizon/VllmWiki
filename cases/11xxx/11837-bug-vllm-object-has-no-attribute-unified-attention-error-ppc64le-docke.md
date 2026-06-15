# vllm-project/vllm#11837: [Bug]: 'vllm' object has no attribute 'unified_attention' error - ppc64le docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#11837](https://github.com/vllm-project/vllm/issues/11837) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 'vllm' object has no attribute 'unified_attention' error - ppc64le docker image

### Issue 正文摘录

### Anything you want to discuss about vllm. I have built the vllm for ppc64le docker image from the latest code base. It was successful and I am able to run the image on a Power 10 server. But, when I use : _curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "mistralai/Mistral-7B-Instruct-v0.2", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": "Who are you?" } ] }'_ **I am getting 500 error from the server and the server gets shutdown. The main error is : AttributeError: '_OpNamespace' 'vllm' object has no attribute 'unified_attention'** **Full Error log is:** CRITICAL 01-08 09:20:26 launcher.py:99] MQLLMEngine is already dead, terminating server process INFO: 10.88.0.1:41888 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR 01-08 09:20:26 engine.py:135] AttributeError("'_OpNamespace' 'vllm' object has no attribute 'unified_attention'") ERROR 01-08 09:20:26 engine.py:135] Traceback (most recent call last): ERROR 01-08 09:20:26 engine.py:135] File "/opt/conda/lib/python3.10/site-packages/vllm-0.6.6.post2.dev124+gef68eb28.cpu-py3.10-linux-ppc64le.egg/vllm/e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 0/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "mistralai/Mistral-7B-Instruct-v0.2", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content":...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: y", line 196, in run_engine_loop ERROR 01-08 09:20:26 engine.py:135] request_outputs = self.engine_step() ERROR 01-08 09:20:26 engine.py:135] File "/opt/conda/lib/python3.10/site-packages/vllm-0.6.6.post2.dev124+gef68eb...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Bug]: 'vllm' object has no attribute 'unified_attention' error - ppc64le docker image ### Anything you want to discuss about vllm. I have built the vllm for ppc64le docker image from the latest code base. It was success...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 20:26 engine.py:135] attn_output = self.attn(q, k, v, kv_cache, attn_metadata) ERROR 01-08 09:20:26 engine.py:135] File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
