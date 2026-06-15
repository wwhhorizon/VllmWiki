# vllm-project/vllm#8641: [Bug]: Using FlashInfer with FP8 model with FP8 KV cache produces an error

| 字段 | 值 |
| --- | --- |
| Issue | [#8641](https://github.com/vllm-project/vllm/issues/8641) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using FlashInfer with FP8 model with FP8 KV cache produces an error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When launching vLLM 0.6.1.post2 via docker for a FP8 quantized model containing k_scale and v_scale using the FlashInfer backend (set up with the corresponding env var), I get this error : ```ERROR 09-19 10:08:02 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 66 died, exit code: -15 INFO 09-19 10:08:02 multiproc_worker_utils.py:123] Killing local vLLM worker processes Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner_base.py", line 112, in _wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner.py", line 1546, in execute_model hidden_or_intermediate_states = model_executable( ^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1562, in _call_impl return forward_call(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/l...

## 现有链接修复摘要

#9861 [Bugfix/Core] Remove assertion for Flashinfer k_scale and v_scale

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: o response_ ### 🐛 Describe the bug When launching vLLM 0.6.1.post2 via docker for a FP8 quantized model containing k_scale and v_scale using the FlashInfer backend (set up with the corresponding env var), I get this err...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Using FlashInfer with FP8 model with FP8 KV cache produces an error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When launching vLLM 0.6.1.post2 via docker for a FP8...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: line 181, in forward attn_output = self.attn(q, k, v, kv_cache, attn_metadata) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1553, in _wrappe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Using FlashInfer with FP8 model with FP8 KV cache produces an error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When launching vLLM 0.6.1.post2 via docker for a FP8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: since PyTorch 2.4 (function operator()) [rank0]:[W919 10:08:03.186378249 CudaIPCTypes.cpp:16] Producer process has been terminated before all shared CUDA tensors released. See Note [Sharing CUDA tensors] ERROR 09-19 10:...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9861](https://github.com/vllm-project/vllm/pull/9861) | closes_keyword | 0.95 | [Bugfix/Core] Remove assertion for Flashinfer k_scale and v_scale | fixes: #8641 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
