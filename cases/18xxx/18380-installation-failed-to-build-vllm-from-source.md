# vllm-project/vllm#18380: [Installation]: Failed to build vLLM from source

| 字段 | 值 |
| --- | --- |
| Issue | [#18380](https://github.com/vllm-project/vllm/issues/18380) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Failed to build vLLM from source

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Traceback (most recent call last): File "/users/congcongchen/code/vllm/vllm/collect_env.py", line 17, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm' ### How you are installing vllm ```sh conda create -n vllm python=3.12 -y conda activate vllm git clone https://github.com/vllm-project/vllm.git cd vllm conda install -y ccache pip install --user -e . -vvv # This may take 5-10 minutes. ``` Full log ``` ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.3/37.3 MB 222.3 MB/s eta 0:00:00 Downloading link https://files.pythonhosted.org/packages/0b/1f/03f52c282437a168ee2c7c14a1a0d0781a9a4a8962d84ac05c06b4c5b555/scipy-1.15.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (from https://pypi.org/simple/scipy/) (requires-python:>=3.10) to /tmp/pip-unpack-wjt1pvqh/scipy-1.15.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl Building wheels for collected packages: vllm Created temporary directory: /tmp/pip-wheel-4yvtdwd5 Destination directory: /tmp/pip-wheel-4yvtdwd5 Running command Building editable for vllm (pyproject.toml) /tmp/pip-build-env-0fmd0nj7/overl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: Failed to build vLLM from source installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Traceback (most recent call last): File "/users/congcongchen/code/vllm/
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: pile features - done -- Build type: RelWithDebInfo -- Target device: cuda -- Found Python: /home/aiscuser/.conda/envs/vllm/bin/python3.12 (found version "3.12.9") found components: Interpreter Development.Module Develop...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: command/editable_wheel.py", line 340, in _create_wheel_file files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/tmp/pip-build-env-0fmd0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 0nj7/overlay/lib/python3.12/site-packages/torch/share/cmake/Caffe2/Caffe2Config.cmake:86 (include) /tmp/pip-build-env-0fmd0nj7/overlay/lib/python3.12/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:68 (find_pack...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Installation]: Failed to build vLLM from source installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Traceback (most recent call last): File "/users/congcongchen/code/vllm/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
