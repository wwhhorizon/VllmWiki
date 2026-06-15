# vllm-project/vllm#36861: [Bug]: Why does setting `--pipeline-parallel-size > 1` result in an OOM error, but `--tensor-parallel-size> 1` does not?

| 字段 | 值 |
| --- | --- |
| Issue | [#36861](https://github.com/vllm-project/vllm/issues/36861) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;moe;quantization;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Why does setting `--pipeline-parallel-size > 1` result in an OOM error, but `--tensor-parallel-size> 1` does not?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have four nodes, each with one A10 graphics card(run with ray cluster） If I switch to --tensor-parallel-size 4 --pipeline-parallel-size 1, it works fine. vllm serve bash ```bash python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen3.5-35B-A3B --model /athena/Qwen3.5-35B-A3B --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --pipeline-parallel-size 1 --max-model-len 160000 --max-num-batched-tokens 4096 --max-num-seqs 32 --distributed-executor-backend ray --enable-log-requests --enable-log-outputs --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-prefix-caching --reasoning-parser qwen3 ``` output log ``` root@xuanwu-text-safety-qwen3-5-1358612-cfrh7:/data# python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen3.5-35B-A3B --model /athena/Qwen3.5-35B-A3B --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --pipeline-parallel-size 1 --max-model-len 160000 --max-num-batched-tokens 4096 --max-num-seqs 32 --distributed-executor-backend ray --enable-log-requests --enable-log-outputs --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-prefix-caching --reasoning-parser q...

## 现有链接修复摘要

#36904 [WIP][BugFix] Fix PP OOM for Qwen3Next/Qwen3_5 by guarding embed_tokens and lm_head

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: 0 --max-num-batched-tokens 4096 --max-num-seqs 32 --distributed-executor-backend ray --enable-log-requests --enable-log-outputs --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-prefix-caching --reasonin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: erve bash ```bash python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen3.5-35B-A3B --model /athena/Qwen3.5-35B-A3B --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --pipeline-parallel-size 1 --max-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: id=45912) INFO 03-11 12:21:59 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0 (APIServer pid=45912) INFO 03-11 12:21:59 [utils.py:302] █▄█▀ █ █ █ █ model /athena/Qwen3.5-35B-A3B (APIServer pid=45912) INFO 03-11 12:21:59...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=160000, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: True} (APIServer pid=45912) INFO 03-11 12:21:59 [model.py:531] Resolved architecture: Qwen3_5MoeForConditionalGeneration (APIServer pid=45912) INFO 03-11 12:21:59 [model.py:1554] Using max model len 160000 (APIServer pi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36904](https://github.com/vllm-project/vllm/pull/36904) | closes_keyword | 0.95 | [WIP][BugFix] Fix PP OOM for Qwen3Next/Qwen3_5 by guarding embed_tokens and lm_head | Fixes #36861. When using pipeline parallelism (PP > 1), `embed_tokens` (`VocabParallelEmbedding`) is allocated on **all** PP ranks instead of only the first rank. Similarly, `Qwen |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
