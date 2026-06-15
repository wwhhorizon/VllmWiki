# vllm-project/vllm#21991: [Bug]: [registry.py:410] ValueError: infer_schema(func): Parameter block_size has unsupported type list[int].

| 字段 | 值 |
| --- | --- |
| Issue | [#21991](https://github.com/vllm-project/vllm/issues/21991) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [registry.py:410] ValueError: infer_schema(func): Parameter block_size has unsupported type list[int].

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving the Qwen3 model on the vllm=0.10.1 version, it reports the following error. Command: vllm serve /models/Qwen3-8B/ INFO 07-31 05:30:20 [__init__.py:241] Automatically detected platform rocm. [1;36m(APIServer pid=670)[0;0m INFO 07-31 05:30:40 [api_server.py:1774] vLLM API server version 0.10.1.dev235+g055bd3978 [1;36m(APIServer pid=670)[0;0m INFO 07-31 05:30:40 [utils.py:326] non-default args: {'model_tag': '/models/Qwen3-0.6B-GPTQ-Int8/', 'port': 8080, 'api_key': ['4families'], 'model': '/models/Qwen3-0.6B-GPTQ-Int8/', 'max_model_len': 8192, 'served_model_name': ['zz-model']} [1;36m(APIServer pid=670)[0;0m ERROR 07-31 05:31:05 [registry.py:410] Error in inspecting model architecture 'Qwen3ForCausalLM' [1;36m(APIServer pid=670)[0;0m ERROR 07-31 05:31:05 [registry.py:410] Traceback (most recent call last): [1;36m(APIServer pid=670)[0;0m ERROR 07-31 05:31:05 [registry.py:410] File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line 820, in _run_in_subprocess [1;36m(APIServer pid=670)[0;0m ERROR 07-31 05:31:05 [registry.py:410] returned.check_returncode() [1;36m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug When serving the Qwen3 model on the vllm=0.10.1 version, it reports the following error. Command: vllm serve /models/Qwen3-8B/ INFO 07-31 05:30:20 [__init__.py:241] Automatically detected platform...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ROR 07-31 05:31:05 [registry.py:410] from vllm.model_executor.layers.quantization.utils.fp8_utils import ( [1;36m(APIServer pid=670)[0;0m ERROR 07-31 05:31:05 [registry.py:410] File "/opt/conda/envs/py_3.12/lib/python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: / INFO 07-31 05:30:20 [__init__.py:241] Automatically detected platform rocm. [1;36m(APIServer pid=670)[0;0m INFO 07-31 05:30:40 [api_server.py:1774] vLLM API server version 0.10.1.dev235+g055bd3978 [1;36m(APIServer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ## Your current environment ### 🐛 Describe the bug When serving the Qwen3 model on the vllm=0.10.1 version, it reports the following error. Command: vllm serve /models/Qwen3-8B/ INFO 07-31 05:30:20 [__init__.py:241] Aut...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: g_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
