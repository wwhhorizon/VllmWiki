# vllm-project/vllm#16570: [Bug]: qwen2.5-vl-72b oom in 4 A100 in 0.8.3

| 字段 | 值 |
| --- | --- |
| Issue | [#16570](https://github.com/vllm-project/vllm/issues/16570) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 37; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen2.5-vl-72b oom in 4 A100 in 0.8.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server \ --dtype auto \ --port 8009 \ --trust-remote-code \ --served-model-name qwen2vl \ --model /home/ps/data/pretrained_model/Qwen/Qwen2.5-VL-72B-Instruct/ \ --tensor-parallel-size 4 \ --gpu_memory_utilization 0.95 \ --max_num_seqs 2 \ --max_model_len 8192 \ --mm_processor_kwargs '{"max_pixels":1280, "min_pixels":256}' above is my running code. I find that it caused 36GB memory each card, but i don't know the later process and vllm caused oom error. Can anyone know why? Thank you very much ```text (VllmWorker rank=1 pid=52940) INFO 04-14 14:23:05 [loader.py:447] Loading weights took 20.16 seconds (VllmWorker rank=2 pid=52983) INFO 04-14 14:23:05 [loader.py:447] Loading weights took 20.27 seconds (VllmWorker rank=1 pid=52940) INFO 04-14 14:23:05 [gpu_model_runner.py:1273] Model loading took 34.4340 GiB and 20.495027 seconds (VllmWorker rank=3 pid=53006) INFO 04-14 14:23:05 [loader.py:447] Loading weights took 20.42 seconds Loading safetensors checkpoint shards: 97% Completed | 37/38 [00:20<00:00, 1.98it/s] (VllmWorker rank=2 pid=52983) INFO 04-14 14:23:05...

## 现有链接修复摘要

#16704 [Doc] Improve OOM troubleshooting

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 4:23:29 [backends.py:416] Using cache directory: /root/.cache/vllm/torch_compile_cache/9cfb59d003/rank_2_0 for vLLM's torch.compile (VllmWorker rank=2 pid=52983) INFO 04-14 14:23:29 [backends.py:426] Dynamo bytecode tra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: qwen2.5-vl-72b oom in 4 A100 in 0.8.3 bug ### Your current environment ### 🐛 Describe the bug VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server \ --dtype auto \ --port 8009 \ --trust...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: qwen2.5-vl-72b oom in 4 A100 in 0.8.3 bug ### Your current environment ### 🐛 Describe the bug VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server \ --dtype auto \ --port 8009 \ --trust...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: _executor.py:383] return self.language_model.sample(logits, sampling_metadata) (VllmWorker rank=1 pid=52940) ERROR 04-14 14:24:52 [multiproc_executor.py:383] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen2.5-vl-72b oom in 4 A100 in 0.8.3 bug ### Your current environment ### 🐛 Describe the bug VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server \ --dtype auto \ --port 8009 \ --trust...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16704](https://github.com/vllm-project/vllm/pull/16704) | closes_keyword | 0.95 | [Doc] Improve OOM troubleshooting | FIX #16570 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
