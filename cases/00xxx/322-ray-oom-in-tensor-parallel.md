# vllm-project/vllm#322: ray OOM in tensor parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#322](https://github.com/vllm-project/vllm/issues/322) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | crash;import_error;mismatch;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ray OOM in tensor parallel

### Issue 正文摘录

In my case , I can deploy the vllm service on single GPU. but when I use multi gpu, I meet the ray OOM error. Could you please help solve this problem? my model is yahma/llama-7b-hf my transformers version is 4.28.0 my cuda version is 11.4 -------- 2023-06-30 09:24:53,455 WARNING utils.py:593 -- Detecting docker specified CPUs. In previous versions of Ray, CPU detection in containers was incorrect. Please ensure that Ray has enough CPUs allocated. As a temporary workaround to revert to the prior behavior, set `RAY_USE_MULTIPROCESSING_CPU_COUNT=1` as an env var before starting Ray. Set the env var: `RAY_DISABLE_DOCKER_CPU_WARNING=1` to mute this warning. 2023-06-30 09:24:53,459 WARNING services.py:1826 -- WARNING: The object store is using /tmp instead of /dev/shm because /dev/shm has only 67108864 bytes available. This will harm performance! You may be able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by passing '--shm-size=6.12gb' to 'docker run' (or add it to the run_options list in a Ray cluster config). Make sure to set this to more than 30% of available RAM. 2023-06-30 09:24:53,584 INFO worker.py:1636 --...

## 现有链接修复摘要

#1395 fix RAM OOM when load large models in tensor parallel mode.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: e help solve this problem? my model is yahma/llama-7b-hf my transformers version is 4.28.0 my cuda version is 11.4 -------- 2023-06-30 09:24:53,455 WARNING utils.py:593 -- Detecting docker specified CPUs. In previous ve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: , I meet the ray OOM error. Could you please help solve this problem? my model is yahma/llama-7b-hf my transformers version is 4.28.0 my cuda version is 11.4 -------- 2023-06-30 09:24:53,455 WARNING utils.py:593 -- Dete...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: itializing an LLM engine with config: model='/opt/app/yahma-llama-lora', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=4, seed=0) WARNING 06-30 09:24:54 conf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: blem? my model is yahma/llama-7b-hf my transformers version is 4.28.0 my cuda version is 11.4 -------- 2023-06-30 09:24:53,455 WARNING utils.py:593 -- Detecting docker specified CPUs. In previous versions of Ray, CPU de...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: el='/opt/app/yahma-llama-lora', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=4, seed=0) WARNING 06-30 09:24:54 config.py:131] Possibly too large swap space....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1395](https://github.com/vllm-project/vllm/pull/1395) | closes_keyword | 0.95 | fix RAM OOM when load large models in tensor parallel mode. | fix bug: #322 #872 ## Test log： ``` (vllm-boydfd) root:~/projects# python -m vllm.entrypoints.api_server --model /root/WizardLM--WizardCoder-15B-V1.0/ --tensor-parallel-size |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
