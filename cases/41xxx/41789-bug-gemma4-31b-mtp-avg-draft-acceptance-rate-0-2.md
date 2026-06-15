# vllm-project/vllm#41789: [Bug]: gemma4 31B MTP Avg Draft acceptance rate: 0.2%

| 字段 | 值 |
| --- | --- |
| Issue | [#41789](https://github.com/vllm-project/vllm/issues/41789) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma4 31B MTP Avg Draft acceptance rate: 0.2%

### Issue 正文摘录

### Your current environment 5090 32G cyankiwi/gemma-4-31B-it-AWQ-4bit docker run -itd --name gemma4 \ --ipc=host \ --network host \ --shm-size 16G \ --gpus '"device=0"' \ -v /home/ma/work/models/gemma-4-31B-it-AWQ-4bit:/model \ -v /home/ma/.cache/huggingface:/root/.cache/huggingface \ -e HF_HOME=/root/.cache/huggingface \ -e HF_ENDPOINT=https://hf-mirror.com/ \ vllm/vllm-openai:gemma4-0505-cu130 \ --model /model \ --served-model-name gpt \ --tensor-parallel-size 1 \ --max-num-seqs 32 \ --max-model-len 65536 \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ --gpu-memory-utilization 0.93 \ --async-scheduling \ --performance-mode throughput \ --enable-chunked-prefill \ --host 0.0.0.0 \ --enable-prefix-caching \ --kv-cache-dtype fp8 \ --limit-mm-per-prompt '{"video":0,"image":0,"audio":0}' \ --port 8000 \ --speculative-config '{"model": "google/gemma-4-31B-it-assistant", "num_speculative_tokens": 4}' ### 🐛 Describe the bug Avg Draft acceptance rate: 0.2% ``` WARNING 05-06 06:05:03 [argparse_utils.py:257] With `vllm serve`, you should provide the model as a positional argument or in a config file instead of via the `--model` option. The `--model` op...

## 现有链接修复摘要

#42069 [Spec Decode] Allow DFlash drafter to autoselect non-causal-capable backend on Gemma 4

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: gemma4 31B MTP Avg Draft acceptance rate: 0.2% bug ### Your current environment 5090 32G cyankiwi/gemma-4-31B-it-AWQ-4bit docker run -itd --name gemma4 \ --ipc=host \ --network host \ --shm-size 16G \
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: gemma4 31B MTP Avg Draft acceptance rate: 0.2% bug ### Your current environment 5090 32G cyankiwi/gemma-4-31B-it-AWQ-4bit docker run -itd --name gemma4 \ --ipc=host \ --network host \ --shm-size 16G \ --gpus '"de...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 8: ilization 0.93 \ --async-scheduling \ --performance-mode throughput \ --enable-chunked-prefill \ --host 0.0.0.0 \ --enable-prefix-caching \ --kv-cache-dtype fp8 \ --limit-mm-per-prompt '{"video":0,"image":0,"audio":0}'...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ## Your current environment 5090 32G cyankiwi/gemma-4-31B-it-AWQ-4bit docker run -itd --name gemma4 \ --ipc=host \ --network host \ --shm-size 16G \ --gpus '"device=0"' \ -v /home/ma/work/models/gemma-4-31B-it-AWQ-4bit:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: --host 0.0.0.0 \ --enable-prefix-caching \ --kv-cache-dtype fp8 \ --limit-mm-per-prompt '{"video":0,"image":0,"audio":0}' \ --port 8000 \ --speculative-config '{"model": "google/gemma-4-31B-it-assistant", "num_speculati...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42069](https://github.com/vllm-project/vllm/pull/42069) | mentioned | 0.6 | [Spec Decode] Allow DFlash drafter to autoselect non-causal-capable backend on Gemma 4 | 068 - #38887 — Gemma 4 E4B slow on TRITON_ATTN (open since v0.19.0) - #41789 — Gemma 4 31B MTP draft acceptance 0.2% (different bug, same area) - #41745 — Gemma4 MTP speculative d… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
