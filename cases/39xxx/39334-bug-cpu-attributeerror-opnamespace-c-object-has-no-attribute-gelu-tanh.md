# vllm-project/vllm#39334: [Bug]: [CPU] AttributeError: '_OpNamespace' '_C' object has no attribute 'gelu_tanh_and_mul'

| 字段 | 值 |
| --- | --- |
| Issue | [#39334](https://github.com/vllm-project/vllm/issues/39334) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [CPU] AttributeError: '_OpNamespace' '_C' object has no attribute 'gelu_tanh_and_mul'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### 1. Build the vllm from the source against the main branch (as of 04/07/2026) ``` uv pip install -r requirements/cpu-build.txt --torch-backend cpu uv pip install -r requirements/cpu.txt --torch-backend cpu VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation ``` ### 2. Serve Gemma4 ``` (gemma4) (base) bash-4.4$ vllm serve google/gemma-4-E2B-it ... (APIServer pid=674180) pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig (APIServer pid=674180) Value error, The checkpoint you are trying to load has model type `gemma4` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. (APIServer pid=674180) (APIServer pid=674180) You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transform...

## 现有链接修复摘要

#39342 [CPU] Fix AttributeError when loading GeluAndMul and similar activations

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: mul' bug ### Your current environment ### 🐛 Describe the bug ### 1. Build the vllm from the source against the main branch (as of 04/07/2026) ``` uv pip install -r requirements/cpu-build.txt --torch-backend cpu uv pip i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: TARGET_DEVICE=cpu uv pip install . --no-build-isolation ``` ### 2. Serve Gemma4 ``` (gemma4) (base) bash-4.4$ vllm serve google/gemma-4-E2B-it ... (APIServer pid=674180) pydantic_core._pydantic_core.ValidationError: 1 v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: of 04/07/2026) ``` uv pip install -r requirements/cpu-build.txt --torch-backend cpu uv pip install -r requirements/cpu.txt --torch-backend cpu VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation ``` ### 2. Serv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: to load has model type `gemma4` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. (APIServer pid=674180...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 4:37:57 [cpu.py:139] VLLM_CPU_KVCACHE_SPACE not set. Using 62.64 GiB for KV cache. ... (Worker pid=670627) ERROR 04-06 14:39:30 [multiproc_executor.py:871] WorkerProc failed to start. (Worker pid=670627) ERROR 04-06 14:...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39342](https://github.com/vllm-project/vllm/pull/39342) | closes_keyword | 0.95 | [CPU] Fix AttributeError when loading GeluAndMul and similar activations | Fixes #39334 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
