# vllm-project/vllm#552: Building wheel for vllm (pyproject.toml) did not run successfully.

| 字段 | 值 |
| --- | --- |
| Issue | [#552](https://github.com/vllm-project/vllm/issues/552) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | activation;attention;cuda;operator |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Building wheel for vllm (pyproject.toml) did not run successfully.

### Issue 正文摘录

I'm trying to build a vLLM image on docker, but I keep getting an error while installing vllm module. I've tried with the given Dockerfile and I also try to build it from source but I keep getting this error. I'm not sure to understand what is the cause. Also, the installation of vllm module takes an hour, while it says it should take around 5/10min. It might come from my slow internet connexion. I had to remove the beggining of the build log as it exceed max github length, but no error and no warning until building wheel.

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Building wheel for vllm (pyproject.toml) did not run successfully. installation I'm trying to build a vLLM image on docker, but I keep getting an error while installing vllm module. I've tried with the given Dockerfile a
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ;distributed_parallel;frontend_api;scheduler_memory activation;attention;cuda;operator build_error;crash;mismatch;slowdown env_dependency;memory_layout #4 Use FlashAttention for `multi_query_kv_attention` I'm trying to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: build_error;crash;mismatch;slowdown env_dependency;memory_layout #4 Use FlashAttention for `multi_query_kv_attention` I'm trying to build a vLLM image on docker, but I keep getting an error while installing vllm module....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pi;scheduler_memory activation;attention;cuda;operator build_error;crash;mismatch;slowdown env_dependency;memory_layout #4 Use FlashAttention for `multi_query_kv_attention` I'm trying to build a vLLM image on docker, bu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ;cuda;operator build_error;crash;mismatch;slowdown env_dependency;memory_layout #4 Use FlashAttention for `multi_query_kv_attention` I'm trying to build a vLLM image on docker, but I keep getting an error while installi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | y built ffmpy lit pathtools wavedrom #4 3573.0 failed to build vllm #4 3573.0 error: could not build wheels for vllm, which is required to install pyproject.toml-based projects -- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
