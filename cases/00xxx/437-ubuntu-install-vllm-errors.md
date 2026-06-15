# vllm-project/vllm#437: ubuntu install vllm errors

| 字段 | 值 |
| --- | --- |
| Issue | [#437](https://github.com/vllm-project/vllm/issues/437) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ubuntu install vllm errors

### Issue 正文摘录

Building wheels for collected packages: vllm Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [212 lines of output] running editable_wheel creating /tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm.egg-info writing /tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm.egg-info/PKG-INFO writing dependency_links to /tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm.egg-info/dependency_links.txt writing requirements to /tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm.egg-info/requires.txt writing top-level names to /tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm.egg-info/top_level.txt writing manifest file '/tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm.egg-info/SOURCES.txt' reading manifest file '/tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm.egg-info/SOURCES.txt' reading manifest template 'MANIFEST.in' adding license file 'LICENSE' writing manifest file '/tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm.egg-info/SOURCES.txt' creating '/tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm-0.1.2.dist-info' creating /tmp/pip-wheel-xaz048_1/.tmp-wr9v2r2_/vllm-0.1.2.dist-info/WHEEL running build_py running build_ext /t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ubuntu install vllm errors installation Building wheels for collected packages: vllm Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building editable for vllm (pyproject.toml)
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: nst c10::detail::integer_iterator > &) const [with I=size_t, one_sided=false, =0]" (61): here instantiation of "__nv_bool c10::detail::integer_iterator >::operator!=(const c10::detail::integer_iterator > &) const [with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ite-packages/torch/utils/cpp_extension.py:388: UserWarning: The detected CUDA version (11.5) has a minor version mismatch with the version that was used to compile PyTorch (11.7). Most likely this shouldn't be a problem...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: y:388: UserWarning: The detected CUDA version (11.5) has a minor version mismatch with the version that was used to compile PyTorch (11.7). Most likely this shouldn't be a problem. warnings.warn(CUDA_MISMATCH_WARN.forma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O2 -std=c++17 -D_GLIBCXX_USE_CX...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
