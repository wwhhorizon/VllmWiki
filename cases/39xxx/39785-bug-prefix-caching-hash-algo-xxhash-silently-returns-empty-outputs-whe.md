# vllm-project/vllm#39785: [Bug]: prefix_caching_hash_algo="xxhash" silently returns empty outputs when xxhash not installed

| 字段 | 值 |
| --- | --- |
| Issue | [#39785](https://github.com/vllm-project/vllm/issues/39785) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: prefix_caching_hash_algo="xxhash" silently returns empty outputs when xxhash not installed

### Issue 正文摘录

$(cat <<'EOF' ## Your current environment vLLM main branch (latest) ## 🐛 Describe the bug When `prefix_caching_hash_algo` is set to `"xxhash"` or `"xxhash_cbor"` but the `xxhash` package is not installed, `LLM.generate()` silently returns empty outputs for requests that trigger prefix caching — no exception is raised to the caller. **Root cause:** The `ModuleNotFoundError` in `vllm/utils/hashing.py` is raised at hash-computation time during request preprocessing, where it gets caught as a preprocessing failure and silently converted to an empty output. **Expected behavior:** An `ImportError` should be raised at engine construction time (in `CacheConfig.__post_init__`) when xxhash is required but not installed, consistent with how other optional-dependency configs (e.g. mamba stochastic rounding) are validated. ## How to reproduce ```bash pip uninstall xxhash -y python -c " from vllm import LLM llm = LLM(model='facebook/opt-125m', prefix_caching_hash_algo='xxhash') print(llm.generate(['Hello world'])) # silently returns empty " ``` Originally reported as #39338. EOF )

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: aching_hash_algo="xxhash" silently returns empty outputs when xxhash not installed $(cat <<'EOF' ## Your current environment vLLM main branch (latest) ## 🐛 Describe the bug When `prefix_caching_hash_algo` is set to `"xx...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: An `ImportError` should be raised at engine construction time (in `CacheConfig.__post_init__`) when xxhash is required but not installed, consistent with how other optional-dependency configs (e.g. mamba stochastic roun...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dency configs (e.g. mamba stochastic rounding) are validated. ## How to reproduce ```bash pip uninstall xxhash -y python -c " from vllm import LLM llm = LLM(model='facebook/opt-125m', prefix_caching_hash_algo='xxhash')...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ge is not installed, `LLM.generate()` silently returns empty outputs for requests that trigger prefix caching — no exception is raised to the caller. **Root cause:** The `ModuleNotFoundError` in `vllm/utils/hashing.py`...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: installed $(cat <<'EOF' ## Your current environment vLLM main branch (latest) ## 🐛 Describe the bug When `prefix_caching_hash_algo` is set to `"xxhash"` or `"xxhash_cbor"` but the `xxhash` package is not installed, `LLM...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
