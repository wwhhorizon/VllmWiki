# vllm-project/vllm#11811: [Installation]: Installing vLLM 0.6.6.post1 fails on TPU

| 字段 | 值 |
| --- | --- |
| Issue | [#11811](https://github.com/vllm-project/vllm/issues/11811) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Installing vLLM 0.6.6.post1 fails on TPU

### Issue 正文摘录

### Your current environment My python environment is 3.11. ### How you are installing vllm I have a docker image with the following commands: ``` RUN cd /opt/vllm && curl -sLO "https://github.com/vllm-project/vllm/archive/refs/tags/v${VLLM_VERSION}.zip" && unzip v${VLLM_VERSION}.zip WORKDIR /opt/vllm/vllm-${VLLM_VERSION} RUN pip uninstall torch torch-xla -y RUN sudo apt-get install libopenblas-base libopenmpi-dev libomp-dev -y RUN pip install -r requirements-tpu.txt RUN VLLM_TARGET_DEVICE="tpu" python3 setup.py develop ``` I get the following error: ``` => ERROR [24/38] RUN pip install -r requirements-tpu.txt 1.2s ------ > [24/38] RUN pip install -r requirements-tpu.txt: #0 0.902 Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/nightly/cpu #0 0.902 Looking in links: https://storage.googleapis.com/libtpu-releases/index.html, https://storage.googleapis.com/jax-releases/jax_nightly_releases.html, https://storage.googleapis.com/jax-releases/jaxlib_nightly_releases.html #0 0.903 Ignoring fastapi: markers 'python_version "3.11"' don't match your environment #0 0.904 Ignoring setuptools: markers 'python_version > "3.11"' don't match your environment #0 0.910...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Installing vLLM 0.6.6.post1 fails on TPU installation ### Your current environment My python environment is 3.11. ### How you are installing vllm I have a docker image with the following commands: ```
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` RUN cd /opt/vllm && curl -sLO "https://github.com/vllm-project/vllm/archive/refs/tags/v${VLLM_VERSION}.zip" && unzip v${VLLM_VERSION}.zip WORKDIR /opt/vllm/vllm-${VLLM_VERSION} RUN pip uninstall torch torch-xla -y R...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
