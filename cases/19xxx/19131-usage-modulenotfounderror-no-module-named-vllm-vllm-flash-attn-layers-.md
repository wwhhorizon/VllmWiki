# vllm-project/vllm#19131: [Usage]: ModuleNotFoundError: No module named 'vllm.vllm_flash_attn.layers' vllm@0.9.0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#19131](https://github.com/vllm-project/vllm/issues/19131) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ModuleNotFoundError: No module named 'vllm.vllm_flash_attn.layers' vllm@0.9.0.1

### Issue 正文摘录

### Your current environment ### Your current environment Trying to install vllm, got installed and then got this error. ``` torch : 2.7.0+cu128 cuda : 12.8 python: 3.12.9 Linux-6.8.0-1013-nvidia-64k-aarch64-with-glibc2.35 ``` Error: ``` INFO 06-04 05:47:32 [__init__.py:243] Automatically detected platform cuda. INFO 06-04 05:47:33 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 06-04 05:47:33 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 06-04 05:47:33 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. INFO 06-04 05:47:40 [config.py:793] This model supports multiple tasks: {'classify', 'embed', 'score', 'reward', 'generate'}. Defaulting to 'generate'. INFO 06-04 05:47:40 [config.py:2118] Chunked prefill is enabled with max_num_batched_tokens=16384. [/home/ubuntu/OS-NotebookLM/.conda/lib/python3.12/site-packages/vllm/transformers_utils/tokenizer_group.py:23](https://vscode-remote+ssh-002dremote-002b192-002e222-002e59-002e147.vscode-resource.vscode-cdn.net/home/ubuntu/OS-NotebookLM/.conda/lib/python3.12/site-packages...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: le ### Your current environment ### Your current environment Trying to install vllm, got installed and then got this error. ``` torch : 2.7.0+cu128 cuda : 12.8 python: 3.12.9 Linux-6.8.0-1013-nvidia-64k-aarch64-with-gli...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: dError: No module named 'vllm.vllm_flash_attn.layers' vllm@0.9.0.1 usage;stale ### Your current environment ### Your current environment Trying to install vllm, got installed and then got this error. ``` torch : 2.7.0+c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: et `VLLM_PLUGINS` to control which plugins to load. INFO 06-04 05:47:40 [config.py:793] This model supports multiple tasks: {'classify', 'embed', 'score', 'reward', 'generate'}. Defaulting to 'generate'. INFO 06-04 05:4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disabl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
