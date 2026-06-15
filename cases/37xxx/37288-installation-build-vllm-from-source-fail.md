# vllm-project/vllm#37288: [Installation]: Build vllm from source fail

| 字段 | 值 |
| --- | --- |
| Issue | [#37288](https://github.com/vllm-project/vllm/issues/37288) |
| 状态 | open |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Build vllm from source fail

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` /Users/wyattwong/GitHub/vllm/vllm/__init__.py:7: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from .version import __version__, __version_tuple__ # isort:skip Traceback (most recent call last): File "/Users/wyattwong/GitHub/vllm/collect_env.py", line 20, in from vllm.envs import environment_variables File "/Users/wyattwong/GitHub/vllm/vllm/__init__.py", line 14, in import vllm.env_override # noqa: F401 ^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/wyattwong/GitHub/vllm/vllm/env_override.py", line 87, in import torch ModuleNotFoundError: No module named 'torch' ### How you are installing vllm I followed the [vLLM Developing Guide](https://docs.vllm.ai/en/latest/contributing/) and got the following error messages: ``` git clone https://github.com/vllm-project/vllm.git cd vllm uv venv --python 3.12 --seed --managed-python source .venv/bin/activate VLLM_USE_PRECOMPILED=1 uv pip install -e . × Failed to build `vllm @ file:///Users/wyattwong/GitHub/vllm` ├─▶ Failed to resolve requirements from `build-system.requires` ├─▶ No solution found when resolving: `cmake>=3.26.1`, `ninja`, `packa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Build vllm from source fail installation ### Your current environment ```text The output of `python collect_env.py` ``` /Users/wyattwong/GitHub/vllm/vllm/__init__.py:7: RuntimeWarning: Failed to read com
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed to build `vllm @ file:///Users/wyattwong/GitHub/vllm` ├─▶ The build backend returned an error ╰─▶ Call to `setuptools.build_meta.prepare_metadata_for_build_editable` failed (exit status: 1) [stderr] Traceback (most r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lable for `torch` (v2.10.0) on the following platforms: `manylinux_2_28_aarch64`, `manylinux_2_28_x86_64`, `macosx_11_0_arm64`, `win_amd64` grep -v '^torch==' requirements/build.txt | uv pip install -r - Resolved 12 pac...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: d backend returned an error ╰─▶ Call to `setuptools.build_meta.prepare_metadata_for_build_editable` failed (exit status: 1) [stderr] Traceback (most recent call last): File " ", line 14, in File "/Users/wyattwong/GitHub...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: g vllm I followed the [vLLM Developing Guide](https://docs.vllm.ai/en/latest/contributing/) and got the following error messages: ``` git clone https://github.com/vllm-project/vllm.git cd vllm uv venv --python 3.12 --se...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
