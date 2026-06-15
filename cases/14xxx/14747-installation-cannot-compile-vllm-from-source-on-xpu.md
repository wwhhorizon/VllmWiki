# vllm-project/vllm#14747: [Installation]: Cannot compile vLLM from source on XPU

| 字段 | 值 |
| --- | --- |
| Issue | [#14747](https://github.com/vllm-project/vllm/issues/14747) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;import_error;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Cannot compile vLLM from source on XPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Compiling vLLM from source for XPU or building the dockerfile results in failure each time you attempt to run vLLM. ``` python3 -m vllm.entrypoints.openai.api_server --model /llm/models/qwen2.5-1.5b-instruct --device xpu --max_model_len 1024 ``` ``` [W313 09:42:19.085066709 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator and the same dispatch key operator: aten::_validate_compressed_sparse_indices(bool is_crow, Tensor compressed_idx, Tensor plain_idx, int cdim, int dim, int nnz) -> () registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: XPU previous kernel: registered at /pytorch/build/aten/src/ATen/RegisterCPU.cpp:30477 new kernel: registered at /build/intel-pytorch-extension/build/Release/csrc/gpu/csrc/aten/generated/ATen/RegisterXPU.cpp:468 (function operator()) INFO 03-13 09:42:21 [__init__.py:256] Automatically detected platform xpu. [W313 09:42:22.469965695 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Cannot compile vLLM from source on XPU installation;stale ### Your current environment ### 🐛 Describe the bug Compiling vLLM from source for XPU or building the dockerfile results in failure each time
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Installation]: Cannot compile vLLM from source on XPU installation;stale ### Your current environment ### 🐛 Describe the bug Compiling vLLM from source for XPU or building the dockerfile results in failure each time yo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=1024, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ttempt to run vLLM. ``` python3 -m vllm.entrypoints.openai.api_server --model /llm/models/qwen2.5-1.5b-instruct --device xpu --max_model_len 1024 ``` ``` [W313 09:42:19.085066709 OperatorEntry.cpp:154] Warning: Warning...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: riding a previously registered kernel for the same operator and the same dispatch key operator: aten::_validate_compressed_sparse_indices(bool is_crow, Tensor compressed_idx, Tensor plain_idx, int cdim, int dim, int nnz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
