# vllm-project/vllm#872: Taking too much memory on multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#872](https://github.com/vllm-project/vllm/issues/872) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | kernel |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Taking too much memory on multiple GPUs

### Issue 正文摘录

I am trying to load a llama13b model on a machine with 4 16GB V100 GPUs (Combined 64 GB GPU memory), 64 GB memory and 16 CPUs. This is the command I am using: ``` llm = LLM(model = 'meta-llama/Llama-2-13b-chat-hf', trust_remote_code=True, tensor_parallel_size = 4, dtype = "float16" ) ``` However I am running into OutOfMemoryError: ``` 2023-08-25 12:31:27,423 WARNING utils.py:597 -- Ray currently does not support initializing Ray with fractional cpus. Your num_cpus will be truncated from 19.2 to 19. 2023-08-25 12:31:27,634 INFO worker.py:1612 -- Started a local Ray instance. View the dashboard at 127.0.0.1:8265 INFO 08-25 12:31:29 llm_engine.py:70] Initializing an LLM engine with config: model=''meta-llama/Llama-2-13b-chat-hf'', tokenizer=''meta-llama/Llama-2-13b-chat-hf'', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=4, seed=0) INFO 08-25 12:31:29 tokenizer.py:29] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. -----...

## 现有链接修复摘要

#1395 fix RAM OOM when load large models in tensor parallel mode.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Taking too much memory on multiple GPUs I am trying to load a llama13b model on a machine with 4 16GB V100 GPUs (Combined 64 GB GPU memory), 64 GB memory and 16 CPUs. This is the command I am using: ``` llm = LLM(model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: m-prevention.html. Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. Set max_restarts and max_task_retries to enable retry when the task crashes due to OOM. To...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: trust_remote_code=True, tensor_parallel_size = 4, dtype = "float16" ) ``` However I am running into OutOfMemoryError: ``` 2023-08-25 12:31:27,423 WARNING utils.py:597 -- Ray currently does not support initializing Ray w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. Set max_restarts and max_task_retries to enable retry when the task crashes due to OOM. To adjust the kill th...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: load a llama13b model on a machine with 4 16GB V100 GPUs (Combined 64 GB GPU memory), 64 GB memory and 16 CPUs. This is the command I am using: ``` llm = LLM(model = 'meta-llama/Llama-2-13b-chat-hf', trust_remote_code=T...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1395](https://github.com/vllm-project/vllm/pull/1395) | closes_keyword | 0.95 | fix RAM OOM when load large models in tensor parallel mode. | fix bug: #322 #872 ## Test log： ``` (vllm-boydfd) root:~/projects# python -m vllm.entrypoints.api_server --model /root/WizardLM--WizardCoder-15B-V1.0/ --tensor-parallel-size |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
