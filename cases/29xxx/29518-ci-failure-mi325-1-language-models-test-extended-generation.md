# vllm-project/vllm#29518: [CI Failure]: mi325_1: Language Models Test (Extended Generation)

| 字段 | 值 |
| --- | --- |
| Issue | [#29518](https://github.com/vllm-project/vllm/issues/29518) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Language Models Test (Extended Generation)

### Issue 正文摘录

### Name of failing test `uv pip install --system --no-build-isolation 'git+https://github.com/state-spaces/mamba@v2.2.5' && uv pip install --system --no-build-isolation 'git+https://github.com/Dao-AILab/causal-conv1d@v1.5.2' && pytest -v -s models/language/generation -m '(not core_model) and (not hybrid_model)'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Installation Failure - mamba/causal-conv1d Build** **Failure Type:** Build-time compilation error during dependency installation **Error:** RuntimeError during extension compilation - Location: Building mamba@v2.2.5 or causal-conv1d@v1.5.2 from source - Details: ninja build command returned non-zero exit status 1 - Additional context: urllib HTTP error (403 Forbidden) when attempting to download build dependencies **Configuration:** - Attempted pip install with --no-build-isolation flag - Building from git source: mamba@v2.2.5 and causal-conv1d@v1.5.2 **Likely cause:** The compilation of C++/CUDA extensions for mamba or causal-conv1d failed. The urllib 403 error suggests network/download issues fetching build-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [CI Failure]: mi325_1: Language Models Test (Extended Generation) ci-failure ### Name of failing test `uv pip install --system --no-build-isolation 'git+https://github.com/state-spaces/mamba@v2.2.5' && uv pip install --s
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi325_1: Language Models Test (Extended Generation) ci-failure ### Name of failing test `uv pip install --system --no-build-isolation 'git+https://github.com/state-spaces/mamba@v2.2.5' && uv pip install --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2.2.5 and causal-conv1d@v1.5.2 **Likely cause:** The compilation of C++/CUDA extensions for mamba or causal-conv1d failed. The urllib 403 error suggests network/download issues fetching build-time dependencies (possibly...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: (not hybrid_model)'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Installation Failure - mamba/caus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Language Models Test (Extended Generation) ci-failure ### Name of failing test `uv pip install --system --no-build-isolation 'git+https://github.com/state-spaces/mamba@v2.2.5' && uv pip install --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
