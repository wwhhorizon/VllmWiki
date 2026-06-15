# vllm-project/vllm#1801: Nvidia drivers 545.29.02 broken --tensor-parallel-size

| 字段 | 值 |
| --- | --- |
| Issue | [#1801](https://github.com/vllm-project/vllm/issues/1801) |
| 状态 | closed |
| 标签 |  |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Nvidia drivers 545.29.02 broken --tensor-parallel-size

### Issue 正文摘录

I just upgraded my drivers to 545.29.02 and it has broken being able to run models larger than a single GPU ram for me with vLLM. If I pass in `--tensor-parallel-size 2`, things just hang when trying to create the engine. Without it, the model loads just fine (if it will fit in a single GPU's ram) ``` (venv) user@pop-os:/media/user/Data/IdeaProjects/vllm$ python3 -m vllm.entrypoints.openai.api_server --model teknium/OpenHermes-2.5-Mistral-7B --tensor-parallel-size 2 INFO 11-27 12:46:10 api_server.py:648] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', model='teknium/OpenHermes-2.5-Mistral-7B', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Special tokens have been added i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ust upgraded my drivers to 545.29.02 and it has broken being able to run models larger than a single GPU ram for me with vLLM. If I pass in `--tensor-parallel-size 2`, things just hang when trying to create the engine....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: p-os:/media/user/Data/IdeaProjects/vllm$ nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilation tools, release 12.1, V12.1....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:648] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
