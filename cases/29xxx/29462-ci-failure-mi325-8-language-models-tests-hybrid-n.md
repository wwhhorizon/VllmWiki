# vllm-project/vllm#29462: [CI Failure]: mi325_8: Language Models Tests (Hybrid) %N

| 字段 | 值 |
| --- | --- |
| Issue | [#29462](https://github.com/vllm-project/vllm/issues/29462) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_8: Language Models Tests (Hybrid) %N

### Issue 正文摘录

### Name of failing test `uv pip install --system --no-build-isolation 'git+https://github.com/state-spaces/mamba@v2.2.5' && uv pip install --system --no-build-isolation 'git+https://github.com/Dao-AILab/causal-conv1d@v1.5.2' && pytest -v -s models/language/generation -m hybrid_model --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --shard-id=$BUILDKITE_PARALLEL_JOB` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Parallel test execution in Shard 4** - C++ extension compilation failure during test runtime **Failure:** RuntimeError during JIT compilation - "Error compiling objects for extension" **Stack trace highlights:** - `torch/utils/cpp_extension.py:2612` in `_run_ninja_build` - `_write_ninja_file_and_compile_objects` → ninja build process - Extension compilation through setuptools/Cython build_ext **Configuration:** Parallel pytest execution (shard 4 of multi-shard run) **Likely cause:** JIT compilation failure for PyTorch custom extensions on ROCm. When vLLM imports model code, PyTorch attempts to compile custom CUDA/ROCm kernels on-the-fly using ninja. The compilat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [CI Failure]: mi325_8: Language Models Tests (Hybrid) %N ci-failure ### Name of failing test `uv pip install --system --no-build-isolation 'git+https://github.com/state-spaces/mamba@v2.2.5' && uv pip install --system --n
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Likely cause:** JIT compilation failure for PyTorch custom extensions on ROCm. When vLLM imports model code, PyTorch attempts to compile custom CUDA/ROCm kernels on-the-fly using ninja. The compilation crashes on ROCm,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi325_8: Language Models Tests (Hybrid) %N ci-failure ### Name of failing test `uv pip install --system --no-build-isolation 'git+https://github.com/state-spaces/mamba@v2.2.5' && uv pip install --system --...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ILDKITE_PARALLEL_JOB` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Parallel test execution in Shard...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_8: Language Models Tests (Hybrid) %N ci-failure ### Name of failing test `uv pip install --system --no-build-isolation 'git+https://github.com/state-spaces/mamba@v2.2.5' && uv pip install --system --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
