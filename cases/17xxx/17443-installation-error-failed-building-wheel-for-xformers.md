# vllm-project/vllm#17443: [Installation]: ERROR: Failed building wheel for xformers

| 字段 | 值 |
| --- | --- |
| Issue | [#17443](https://github.com/vllm-project/vllm/issues/17443) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: ERROR: Failed building wheel for xformers

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Traceback (most recent call last): File "/home/u2024001049/collect_env.py", line 17, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm' ``` ### How you are installing vllm ```sh module load cuda/12.1.1 pip install -vvv vllm ``` When I was installing vllm, the displayed information was as follows ``` Building wheels for collected packages: xformers Created temporary directory: /tmp/pip-wheel-suvcw6uj DEPRECATION: Building 'xformers' using the legacy setup.py bdist_wheel mechanism, which will be removed in a future version. pip 25.3 will enforce this behaviour change. A possible replacement is to use the standardized build interface by setting the `--use-pep517` option, (possibly combined with `--no-build-isolation`), or adding a `pyproject.toml` file to the source tree of 'xformers'. Discussion can be found at https://github.com/pypa/pip/issues/6334 Building wheel for xformers (setup.py) ... Destination directory: /tmp/pip-wheel-suvcw6uj Running command python setup.py bdist_wheel Looks like we are using CUDA 12.1 which segfaults when provided with the -generate-line-i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: ERROR: Failed building wheel for xformers installation;stale ### Your current environment ```text The output of `python collect_env.py` Traceback (most recent call last): File "/home/u2024001049/collec
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ule named 'vllm' ``` ### How you are installing vllm ```sh module load cuda/12.1.1 pip install -vvv vllm ``` When I was installing vllm, the displayed information was as follows ``` Building wheels for collected package...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: with tokenize.open(__file__) as f: setup_py_code = f.read() else: filename = " " setup_py_code = "from setuptools import setup; setup()" exec(compile(setup_py_code, filename, "exec")) '"'"''"'"''"'"' % ('"'"'/tmp/pip-in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 1 pip install -vvv vllm ``` When I was installing vllm, the displayed information was as follows ``` Building wheels for collected packages: xformers Created temporary directory: /tmp/pip-wheel-suvcw6uj DEPRECATION: Bui...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: ERROR: Failed building wheel for xformers installation;stale ### Your current environment ```text The output of `python collect_env.py` Traceback (most recent call last): File "/home/u2024001049/collect_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
