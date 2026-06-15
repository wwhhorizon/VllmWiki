# vllm-project/vllm#981: install from source failed

| 字段 | 值 |
| --- | --- |
| Issue | [#981](https://github.com/vllm-project/vllm/issues/981) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | activation;attention;cuda |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> install from source failed

### Issue 正文摘录

pip install vllm is ok but pip install -e . failed error: ``` Building wheel for vllm (pyproject.toml): started Building wheel for vllm (pyproject.toml): finished with status 'error' error: subprocess-exited-with-error × Building wheel for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [221 lines of output] No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' running bdist_wheel running build running build_py creating build creating build/lib.linux-x86_64-cpython-39 creating build/lib.linux-x86_64-cpython-39/vllm copying vllm/__init__.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/block.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/config.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/logger.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/outputs.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/sampling_params.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/sequence.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/utils.py -> build/lib.linux-x86_64-cpython-39/vllm creating build/lib.linux-x86_64-cpython-39/vllm/core copying vllm/core/__init__.py -> build/lib.linux-x86_64-cpython-39/v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: install from source failed pip install vllm is ok but pip install -e . failed error: ``` Building wheel for vllm (pyproject.toml): started Building wheel for vllm (pyproject.toml): finished with status 'error' er
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: lm/block.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/config.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/logger.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/outputs.py -> build/li...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: __init__.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/block.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/config.py -> build/lib.linux-x86_64-cpython-39/vllm copying vllm/logger.py -> build/lib....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: run successfully. │ exit code: 1 ╰─> [221 lines of output] No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' running bdist_wheel running build running build_py creating build creating build/lib.linux-x86_64-cp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O2 -std=c++17 -D_GLIBCXX_USE_CX...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
