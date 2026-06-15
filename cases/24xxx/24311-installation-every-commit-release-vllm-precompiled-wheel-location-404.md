# vllm-project/vllm#24311: [Installation]: every commit release (VLLM_PRECOMPILED_WHEEL_LOCATION): 404

| 字段 | 值 |
| --- | --- |
| Issue | [#24311](https://github.com/vllm-project/vllm/issues/24311) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: every commit release (VLLM_PRECOMPILED_WHEEL_LOCATION): 404

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm Follow the installation instructions in the [document](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#build-wheel-from-source). ```sh export VLLM_COMMIT=e599e2c65ee32abcc986733ab0a55becea158bb4 # use full commit hash from the main branch export VLLM_PRECOMPILED_WHEEL_LOCATION=https://wheels.vllm.ai/${VLLM_COMMIT}/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl uv pip install -vvv --editable . ``` ``` DEBUG urllib.error.HTTPError: HTTP Error 404: Not Found DEBUG Downloading wheel from https://wheels.vllm.ai/e599e2c65ee32abcc986733ab0a55becea158bb4/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl to /tmp/vllm-wheelsj_b7omwc/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl ``` Did I miss any important changes, or is the documentation not updated, or is there a problem with the every commit release pipeline? *** This can be used normally ``` VLLM_USE_PRECOMPILED=1 uv pip install -v --editable . ``` DEBUG Downloading wheel from https://wheels.vllm.ai/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl to /tmp/vllm-wheels8biy82yo/vllm-1.0.0.dev-cp38-abi3-man...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: every commit release (VLLM_PRECOMPILED_WHEEL_LOCATION): 404 installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm Follow the install
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: he installation instructions in the [document](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#build-wheel-from-source). ```sh export VLLM_COMMIT=e599e2c65ee32abcc986733ab0a55becea158bb4 # use full...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
