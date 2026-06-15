# vllm-project/vllm#8565: [Bug]: INTEL GPU ARC 770 import vllm error 

| 字段 | 值 |
| --- | --- |
| Issue | [#8565](https://github.com/vllm-project/vllm/issues/8565) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: INTEL GPU ARC 770 import vllm error 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Working on intel arc 770. vllm is not being imported, after building it using docker with the following commands ``` podman build -f Dockerfile.xpu -t vllm-xpu-env . podman run --device /dev/dri/ -it --rm vllm-xpu-env bash root@b1500aef7c39:/workspace/vllm# ls CMakeLists.txt Dockerfile.ppc64le benchmarks dist requirements-cpu.txt requirements-test.txt CODE_OF_CONDUCT.md Dockerfile.rocm build docs requirements-cuda.txt requirements-tpu.txt CONTRIBUTING.md Dockerfile.tpu cmake examples requirements-dev.txt requirements-xpu.txt Dockerfile Dockerfile.xpu collect_env.py format.sh requirements-lint.txt setup.py Dockerfile.cpu LICENSE collect_env.py.1 pyproject.toml requirements-neuron.txt tests Dockerfile.neuron MANIFEST.in collect_env.py.2 requirements-build.txt requirements-openvino.txt vllm Dockerfile.openvino README.md csrc requirements-common.txt requirements-rocm.txt vllm.egg-info root@b1500aef7c39:/workspace/vllm# cd root@b1500aef7c39:~# vllm Traceback (most recent call last): File "/usr/local/bin/vllm", line 33, in sys.exit(load_entry_point('vllm==0.6.1.post2+xpu', 'console_scripts', 'vllm')(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: INTEL GPU ARC 770 import vllm error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Working on intel arc 770. vllm is not being imported, after building it using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ents-cpu.txt requirements-test.txt CODE_OF_CONDUCT.md Dockerfile.rocm build docs requirements-cuda.txt requirements-tpu.txt CONTRIBUTING.md Dockerfile.tpu cmake examples requirements-dev.txt requireme
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: RC 770 import vllm error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Working on intel arc 770. vllm is not being imported, after building it using docker with the fo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 1500aef7c39:/workspace/vllm# ls CMakeLists.txt Dockerfile.ppc64le benchmarks dist requirements-cpu.txt requirements-test.txt CODE_OF_CONDUCT.md Dockerfile.rocm build docs requirements-cuda.txt requirements-tpu.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 0.egg/vllm/config.py", line 12, in from vllm.model_executor.layers.quantization import QUANTIZATION_METHODS File "/usr/local/lib/python3.10/dist-packages/vllm-0.6.1.post2+xpu-py3.10.egg/vllm/model_executor/__init__.py",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
