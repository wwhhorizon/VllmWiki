# vllm-project/vllm#43559: [Bug]: Accuracy drops ~20% when `--enable-prefix-caching` is used together with MTP speculative decoding (Qwen3.6 35B-A3B)

| 字段 | 值 |
| --- | --- |
| Issue | [#43559](https://github.com/vllm-project/vllm/issues/43559) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Accuracy drops ~20% when `--enable-prefix-caching` is used together with MTP speculative decoding (Qwen3.6 35B-A3B)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug **Model:** an SFT-finetuned **Qwen3.6 35B-A3B** (MoE) checkpoint. When serving this model with **MTP speculative decoding** (`--speculative-config '{"method": "mtp", "num_speculative_tokens": 2}'`) **together with** `--enable-prefix-caching`, the model's output quality drops dramatically. On an internal classification benchmark, accuracy degrades by **~20%** compared to the exact same setup without prefix caching. I ran four configurations on the same checkpoint, with the same client requests (`temperature=0.1`), and **only the last one degrades**: | # | Configuration | Prefix Caching | Accuracy | Speed | |---|---|---|---|---| | 1 | base (plain decoding) | off | baseline | baseline | | 2 | base + prefix caching | **on** | **unchanged** ✅ | faster ✅ | | 3 | MTP (`num_speculative_tokens=2`) | off | unchanged ✅ | faster ✅ | | 4 | MTP + prefix caching | **on** | **drops ~20%** ❌ | faster | So prefix caching alone is fine (group 2), MTP alone is fine (group 3), but **MTP + prefix caching** (group 4) consistently loses ~20% accuracy on the classification task. This strongly suggests an interaction bug between the...

## 现有链接修复摘要

#43650 [Bugfix][Core] MTP + enable prefix caching + mamba accuracy fix

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: works).** A minimal reproducer: ```python # repro_client.py from openai import OpenAI client = OpenAI(base_url="http://0.0.0.0:30002/v1", api_key="EMPTY") # A classification-style prompt with a long, shared system prefi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: racy drops ~20% when `--enable-prefix-caching` is used together with MTP speculative decoding (Qwen3.6 35B-A3B) bug ### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug **Model:** an SFT-finetuned *...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Accuracy drops ~20% when `--enable-prefix-caching` is used together with MTP speculative decoding (Qwen3.6 35B-A3B) bug ### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug **Model:** an SFT-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: MODEL=/path/to/qwen3-checkpoint export VLLM_ENGINE_READY_TIMEOUT_S=3600 CUDA_VISIBLE_DEVICES=0 \ vllm serve $MODEL \ --host 0.0.0.0 \ --port 30000 \ --tensor-parallel-size 1 \ --reasoning-parser qwen3 \ --gpu-memory-uti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: --enable-prefix-caching` is used together with MTP speculative decoding (Qwen3.6 35B-A3B) bug ### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug **Model:** an SFT-finetuned **Qwen3.6 35B-A3B** (Mo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43650](https://github.com/vllm-project/vllm/pull/43650) | closes_keyword | 0.95 | [Bugfix][Core] MTP + enable prefix caching + mamba accuracy fix | fix ## Purpose #43559 In full attention, with speculative decoding the final block is dropped since it contains only part of accepted tokens. Mamba currently does not drop the fi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
