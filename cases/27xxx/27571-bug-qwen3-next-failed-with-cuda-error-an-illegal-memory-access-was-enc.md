# vllm-project/vllm#27571: [Bug]: qwen3-next failed with CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#27571](https://github.com/vllm-project/vllm/issues/27571) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: qwen3-next failed with CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --enable-expert-parallel -tp 4 -dp 2 ``` ``` vllm bench serve \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --dataset-name random \ --tokenizer Qwen/Qwen3-Next-80B-A3B-Instruct \ --num-prompts 512 \ --random-input-len 2048 \ --random-output-len 1024 --request-rate 30 ``` And `--enable-expert-parallel -tp 8` will not fail ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory cache;cuda;kernel;moe;oper...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: qwen3-next failed with CUDA error: an illegal memory access was encountered bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --enable-expert-parallel -tp 4 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3-next failed with CUDA error: an illegal memory access was encountered bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --enable-expert-parallel -tp 4 -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: scribe the bug ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --enable-expert-parallel -tp 4 -dp 2 ``` ``` vllm bench serve \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --dataset-name random \ --tokenizer Qwen/Qwen3-Ne...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uantization;scheduler_memory cache;cuda;kernel;moe;operator;quantization;triton build_error;crash;mismatch;slowdown dtype;env_dependency;race_condition #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatic...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | c/.venv/lib/python3.12/site-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /.venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xd8b74 (0x7f20a54e8b74 in /lib64/libstdc++.so.6) frame #7: <unknown function> + 0x9… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | n function> + 0xd8b74 (0x7f20a54e8b74 in /lib64/libstdc++.so.6) frame #7: <unknown function> + 0x93fb (0x7f20bb0783fb in /lib64/libpthread.so.0) frame #8: clone + 0x43 (0x7f20bad7… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
