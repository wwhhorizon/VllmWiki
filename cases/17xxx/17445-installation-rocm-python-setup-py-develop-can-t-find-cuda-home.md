# vllm-project/vllm#17445: [Installation]: rocm `python setup.py develop` can't find CUDA_HOME

| 字段 | 值 |
| --- | --- |
| Issue | [#17445](https://github.com/vllm-project/vllm/issues/17445) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: rocm `python setup.py develop` can't find CUDA_HOME

### Issue 正文摘录

### Your current environment ```text (venv) ubuntu@qwertyuiop-server:~/vllm$ python vllm/collect_env.py Traceback (most recent call last): File "/home/ubuntu/vllm/vllm/collect_env.py", line 17, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm' ``` ### How you are installing vllm ```sh pip install --upgrade pip pip install /opt/rocm/share/amd_smi pip install --upgrade numba scipy huggingface-hub[cli,hf_transfer] setuptools_scm pip install "numpy [25 lines of output] /tmp/pip-build-env-i4bnwtmc/overlay/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:275: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.) cpu = _conversion_method_template(device=torch.device("cpu")) No ROCm runtime is found, using ROCM_HOME='/opt/rocm' Traceback (most recent call last): File "/home/ubuntu/vllm/venv/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/home/ubuntu/vllm/venv/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main json_out['return_val']...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: rocm `python setup.py develop` can't find CUDA_HOME installation ### Your current environment ```text (venv) ubuntu@qwertyuiop-server:~/vllm$ python vllm/collect_env.py Traceback (most recent call last):
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Installation]: rocm `python setup.py develop` can't find CUDA_HOME installation ### Your current environment ```text (venv) ubuntu@qwertyuiop-server:~/vllm$ python vllm/collect_env.py Traceback (most recent call last):...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: pip install /opt/rocm/share/amd_smi pip install --upgrade numba scipy huggingface-hub[cli,hf_transfer] setuptools_scm pip install "numpy [25 lines of output] /tmp/pip-build-env-i4bnwtmc/overlay/lib/python3.12/site-packa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
