# vllm-project/vllm#23954: [Bug]: CUDA error when serving MiniCPM-V model

| 字段 | 值 |
| --- | --- |
| Issue | [#23954](https://github.com/vllm-project/vllm/issues/23954) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA error when serving MiniCPM-V model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug How to reproduce ``` vllm serve /data/datasets/models-hf/MiniCPM-V-4_5/ --trust-remote-code --served-model-name minicpm vllm bench serve \ --endpoint-type openai-chat \ --endpoint /v1/chat/completions \ --model minicpm \ --dataset-name random-mm \ --random-mm-base-items-per-request 3 \ --tokenizer /data/datasets/models-hf/MiniCPM-V-4_5 --trust-remote-code \ --num-prompts 70 \ --max-concurrency 10``` part of error log ``` (VllmWorker TP1 pid=1035574) ERROR 08-30 01:28:29 [multiproc_executor.py:611] File "/home/zjy/code/vllm-src/vllm/compilation/cuda_graph.py", line 119, in __call__ (VllmWorker TP1 pid=1035574) ERROR 08-30 01:28:29 [multiproc_executor.py:611] return self.runnable(*args, **kwargs) (VllmWorker TP1 pid=1035574) ERROR 08-30 01:28:29 [multiproc_executor.py:611] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker TP1 pid=1035574) ERROR 08-30 01:28:29 [multiproc_executor.py:611] File "/home/zjy/code/vllm-src/vllm/compilation/cuda_piecewise_backend.py", line 96, in __call__ (VllmWorker TP1 pid=1035574) ERROR 08-30 01:28:29 [multiproc_executor.py:611] return self.compiled_graph_for_general_shape(*args) (VllmWorker TP1 pid=1035574) E...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #16229 [Bugfix] Merge MM embeddings by index instead of token IDs

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: CUDA error when serving MiniCPM-V model bug ### Your current environment ### 🐛 Describe the bug How to reproduce ``` vllm serve /data/datasets/models-hf/MiniCPM-V-4_5/ --trust-remote-code --served-model-name mini...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 035574) ERROR 08-30 01:28:29 [multiproc_executor.py:611] return self.compiled_graph_for_general_shape(*args) (VllmWorker TP1 pid=1035574) ERROR 08-30 01:28:29 [multiproc_executor.py:611] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: .py:611] File "/home/zjy/code/vllm-src/vllm/compilation/cuda_piecewise_backend.py", line 96, in __call__ (VllmWorker TP1 pid=1035574) ERROR 08-30 01:28:29 [multiproc_executor.py:611] return self.compiled_graph_for_gener...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA error when serving MiniCPM-V model bug ### Your current environment ### 🐛 Describe the bug How to reproduce ``` vllm serve /data/datasets/models-hf/MiniCPM-V-4_5/ --trust-remote-code --served-model-name mini...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --model minicpm \ --dataset-name random-mm \ --random-mm-base-items-per-request 3 \ --tokenizer /data/datasets/models-hf/MiniCPM-V-4_5 --trust-remote-code \ --num-prompts 70 \ --max-concurrency 10``` part of error log `...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | xecdb4 (0x7f6a3b4ecdb4 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x9caa4 (0x7f6ab5e9caa4 in /lib/x86_64-linux-gnu/libc.so.6) frame #5: <unknown funct… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /.venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xecdb4 (0x7f6a3b4ecdb4 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | xecdb4 (0x7f6a3b4ecdb4 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x9caa4 (0x7f6ab5e9caa4 in /lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown funct… |
| [#16229](https://github.com/vllm-project/vllm/pull/16229) | closes_keyword | 0.95 | [Bugfix] Merge MM embeddings by index instead of token IDs | FIX #23954 FIX #24456 ## Breaking change for model developers This PR has updated `SupportsMultiModal.get_input_embeddings` to support passing `is_multimodal` mask and added a de |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
