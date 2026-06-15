# vllm-project/vllm#37868: [Bug]: bge-m3 /pooling endpoint breaks in the latest main branch

| 字段 | 值 |
| --- | --- |
| Issue | [#37868](https://github.com/vllm-project/vllm/issues/37868) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: bge-m3 /pooling endpoint breaks in the latest main branch

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run vllm command: vllm serve BAAI/BAAI/bge-m3 --port 9001 --hf-overrides '{"architectures": ["BgeM3EmbeddingModel"]}' Then run ``` for i in $(seq 1 10000); do response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:9001/pooling \ -H "Content-Type: application/json" \ -d '{"model": "BAAI/BAAI/bge-m3", "task": "embed", "input": ["test sentence number '$i'"]}') if [ "$response" != "200" ]; then echo "FAILED at index $i (HTTP $response)" break else echo "OK: $i" fi done ``` It breaks at index 3999. (APIServer pid=67656) INFO: 127.0.0.1:51488 - "POST /pooling HTTP/1.1" 200 OK (APIServer pid=67656) INFO: 127.0.0.1:51500 - "POST /pooling HTTP/1.1" 200 OK (APIServer pid=67656) INFO: 127.0.0.1:51506 - "POST /pooling HTTP/1.1" 200 OK (APIServer pid=67656) INFO: 127.0.0.1:51514 - "POST /pooling HTTP/1.1" 200 OK (APIServer pid=67656) INFO: 127.0.0.1:51516 - "POST /pooling HTTP/1.1" 200 OK (APIServer pid=67656) INFO: 127.0.0.1:51532 - "POST /pooling HTTP/1.1" 200 OK (APIServer pid=67656) INFO: 127.0.0.1:51542 - "POST /pooling HTTP/1.1" 200 OK (APIServer pid=67656) INFO: 127.0.0.1:51550 - "POST /pooling HTTP/1.1" 200 OK (APIServer p...

## 现有链接修复摘要

#37873 [Bugfix] RoBERTa position_id accumulation in CUDA graph padding region | #37884 [Bugfix] Fix RoBERTa position_ids accumulation on CUDA graph padding | #37896 [Bugfix] Fix RoBERTa position_ids accumulation on CUDA graph padding

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: (EngineCore pid=67718) ERROR 03-23 15:40:54 [dump_input.py:79] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=pool-a697394010a73a4c-0-93050ebb,prompt_token_ids_le...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nds: 0 , 'debug_dump_path': None, 'cache_dir': '/root/.cache/vllm/torch_compile_cache/e44841742f', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['none'], 'splitting_ops': ['vllm::unified_a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: vllm command: vllm serve BAAI/BAAI/bge-m3 --port 9001 --hf-overrides '{"architectures": ["BgeM3EmbeddingModel"]}' Then run ``` for i in $(seq 1 10000); do response=$(curl -s -o /dev/null -w "%{http_code}" http://localho...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 200" ]; then echo "FAILED at index $i (HTTP $response)" break else echo "OK: $i" fi done ``` It breaks at index 3999. (APIServer pid=67656) INFO: 127.0.0.1:51488 - "POST /pooling HTTP/1.1" 200 OK (APIServer pid=67656) I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: be the bug Run vllm command: vllm serve BAAI/BAAI/bge-m3 --port 9001 --hf-overrides '{"architectures": ["BgeM3EmbeddingModel"]}' Then run ``` for i in $(seq 1 10000); do response=$(curl -s -o /dev/null -w "%{http_code}"...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37873](https://github.com/vllm-project/vllm/pull/37873) | closes_keyword | 0.95 | [Bugfix] RoBERTa position_id accumulation in CUDA graph padding region | Fixes #37868 Related #37648 #37868 ## Purpose ## Test Plan ### Reproduce the bug ```bash CUDA_LAUNCH_BLOCKING=1 vllm serve BAAI/bge-m3 --port 9001 \ --hf-overrides ' |
| [#37884](https://github.com/vllm-project/vllm/pull/37884) | closes_keyword | 0.95 | [Bugfix] Fix RoBERTa position_ids accumulation on CUDA graph padding | Fixes #37868 Related: #37873 (alternative fix that zeroes the padding region in `_preprocess`) ## Test Plan ### Reproduce the bug (before fix) ```bash vllm serve BAAI/bge-m3 -- |
| [#37896](https://github.com/vllm-project/vllm/pull/37896) | closes_keyword | 0.95 | [Bugfix] Fix RoBERTa position_ids accumulation on CUDA graph padding | Fixes #37868 ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
