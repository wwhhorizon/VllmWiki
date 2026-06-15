# vllm-project/vllm#3291: v0.3.3 api server can't startup with neuron sdk 

| 字段 | 值 |
| --- | --- |
| Issue | [#3291](https://github.com/vllm-project/vllm/issues/3291) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> v0.3.3 api server can't startup with neuron sdk 

### Issue 正文摘录

————————env lib detail:—————————————— inf2.24xlarge ubuntu@ip-172-31-12-212:~/vllm$ pip list|grep -i neuron aws-neuronx-runtime-discovery 2.9 libneuronxla 2.0.755 neuronx-cc 2.12.68.0+4480452af neuronx-hwm 2.12.0.0+422c9037c torch-neuronx 2.1.1.2.0.0b0 transformers-neuronx 0.9.474 ————————startup cli: ———————————————— nohup python3 -m vllm.entrypoints.api_server --device neuron --model openlm-research/open_llama_3b --tensor-parallel-size 24 & ————————error message:—————————————— INFO 03-09 02:13:19 llm_engine.py:88] Initializing an LLM engine (v0.3.3) with config: model='mistralai/Mistral-7B-Instruct-v0.2', tokenizer='mistralai/Mistral-7B-Instruct-v0.2', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cpu, seed=0) Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globa...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantizatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ————————— nohup python3 -m vllm.entrypoints.api_server --device neuron --model openlm-research/open_llama_3b --tensor-parallel-size 24 & ————————error message:—————————————— INFO 03-09 02:13:19 llm_engine.py:88] Initial...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ython3 -m vllm.entrypoints.api_server --device neuron --model openlm-research/open_llama_3b --tensor-parallel-size 24 & ————————error message:—————————————— INFO 03-09 02:13:19 llm_engine.py:88] Initializing an LLM engi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rontend_api;model_support;quantization cuda;quantization crash dtype;env_dependency ————————env lib detail:——————————————
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quanti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
