# vllm-project/vllm#19468: [Bug]: Failed to run dpsk r1 when enforcing eager mode on vLLM 0.9.0

| 字段 | 值 |
| --- | --- |
| Issue | [#19468](https://github.com/vllm-project/vllm/issues/19468) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run dpsk r1 when enforcing eager mode on vLLM 0.9.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Failed to run dpsk r1 when enforcing eager mode. The issue occured when enabling `enforce-eager`, not when it was disabled. Running the following script: ``` python examples/offline_inference/data_parallel.py \ --model /datasets/deepseek-r1/ \ --dp-size 8 \ --tp-size 1 \ --enforce-eager \ --trust-remote-code ``` Specifically the error is: ``` Traceback (most recent call last): output = func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl return self._call_impl(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1762, in _call_impl return forward_call(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 713, in forward hidden_states = self.model(input_ids, positions, intermediate_tensors, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Failed to run dpsk r1 when enforcing eager mode on vLLM 0.9.0 bug;stale ### Your current environment ### 🐛 Describe the bug Failed to run dpsk r1 when enforcing eager mode. The issue occured when enabling `enforc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Failed to run dpsk r1 when enforcing eager mode on vLLM 0.9.0 bug;stale ### Your current environment ### 🐛 Describe the bug Failed to run dpsk r1 when enforcing eager mode. The issue occured when enabling `enforc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: (self, File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/mla/common.py", line 908, in forward output[num_decode_tokens:] = self._forward_prefill( ^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: attn_interface.py", line 228, in flash_attn_varlen_func out, softmax_lse = torch.ops._vllm_fa2_C.varlen_fwd( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1158, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
