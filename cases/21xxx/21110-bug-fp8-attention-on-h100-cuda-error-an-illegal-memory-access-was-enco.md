# vllm-project/vllm#21110: [Bug]: FP8 Attention on H100 - CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#21110](https://github.com/vllm-project/vllm/issues/21110) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: FP8 Attention on H100 - CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running multiple variants of Llama 3 models with different quantization setups on H100. While on most settings it runs stable, I realized that when using `--kv-cache-dtype "fp8"` sometimes I get `CUDA error: an illegal memory access was encountered` and the server crashes. I am unable to share an explicit reproducible example currently, but will update when I am able to extract a specific combination of model+config+prompt that fails. Crucially, the server works fine if I just skip faulty prompts. All the other prompts (longer/shorter inputs work just fine). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: FP8 Attention on H100 - CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug I am running multiple variants of Llama 3 models with different quantizat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ss was encountered` and the server crashes. I am unable to share an explicit reproducible example currently, but will update when I am able to extract a specific combination of model+config+prompt that fails. Crucially,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 Attention on H100 - CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug I am running multiple variants of Llama 3 models with different quantizat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nvironment ### 🐛 Describe the bug I am running multiple variants of Llama 3 models with different quantization setups on H100. While on most settings it runs stable, I realized that when using `--kv-cache-dtype "fp8"` s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ntion on H100 - CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug I am running multiple variants of Llama 3 models with different quantization setups on H...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | n function> + 0xe7764 (0x7f975c0e7764 in /lib64/libstdc++.so.6) frame #4: <unknown function> + 0x9f832 (0x7f97e9e9f832 in /lib64/libc.so.6) frame #5: <unknown function> + 0x3f480… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | irvenv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f976bd91e8d in workdirvenv/lib/python3.12/site-pac… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | irvenv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xe7764 (0x7f975c0e7764 in /lib64/libstdc++.so.6) frame #8: <unknown function> + 0x9… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
