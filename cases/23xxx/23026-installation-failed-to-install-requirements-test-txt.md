# vllm-project/vllm#23026: [Installation]: Failed to install requirements/test.txt

| 字段 | 值 |
| --- | --- |
| Issue | [#23026](https://github.com/vllm-project/vllm/issues/23026) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Failed to install requirements/test.txt

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip3 install -r ./requirements/build.txt pip3 install -r ./requirements/common.txt pip3 install -r ./requirements/cuda.txt pip3 install -r ./requirements/test.txt VLLM_COMMIT=6d8d0a24c02bfd84d46b3016b865a44f048ae84b VLLM_PRECOMPILED_WHEEL_LOCATION=https://wheels.vllm.ai/${VLLM_COMMIT}/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl pip3 install -e . pip3 install -U pynvml ``` I'm trying to build vLLM v0.10.0 on the docker image `nvcr.io/nvidia/pytorch:25.01-py3`. While installing the requirements from test.txt, it failed with the following error message. So I can run vLLM, but it's hard to run test codes with pytest. ``` ERROR: Ignored the following versions that require a different python version: 1.10.0 Requires-Python =3.8; 1.10.0rc1 Requires-Python =3.8; 1.10.0rc2 Requires-Python =3.8; 1.10.1 Requires-Python =3.8; 1.21.2 Requires-Python >=3.7, =3.7, =3.7, =3.7, =3.7, =3.7, =3.7, =3.7, =3.7, =3.7, =3.7, =3.8, =3.8, =3.8, =3.8, =3.8, =3.8, =3.8, =3.8, =3.8, =3.8, =3.8,<3.12 ERROR: Could not find a version that satisfies the requirement torch==2.7.1+cu128 (from vers...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Failed to install requirements/test.txt installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip3 install -r ./requirements/b
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pip3 install -r ./requirements/common.txt pip3 install -r ./requirements/cuda.txt pip3 install -r ./requirements/test.txt VLLM_COMMIT=6d8d0a24c02bfd84d46b3016b865a44f048ae84b VLLM_PRECOMPILED_WHEEL_LOCATION=https://whee...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Installation]: Failed to install requirements/test.txt installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip3 install -r ./requirements/bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
