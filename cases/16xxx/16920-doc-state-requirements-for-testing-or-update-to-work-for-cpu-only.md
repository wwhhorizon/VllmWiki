# vllm-project/vllm#16920: [Doc]: state requirements for testing or update to work for CPU-only

| 字段 | 值 |
| --- | --- |
| Issue | [#16920](https://github.com/vllm-project/vllm/issues/16920) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: state requirements for testing or update to work for CPU-only

### Issue 正文摘录

### 📚 The doc issue On https://docs.vllm.ai/en/latest/contributing/overview.html#testing, `pip install -r requirements/dev.txt` tries to install [mamba-ssm](https://github.com/vllm-project/vllm/blob/d41faaf9df6d1a741d5fdd4a282b16783cace888/requirements/test.txt#L273) whose [requirements are stated here](https://github.com/state-spaces/mamba/?tab=readme-ov-file#installation). > * Linux > * NVIDIA GPU > * PyTorch 1.12+ > * CUDA 11.6+ The `pip install` command fails otherwise with errors like `NameError: name 'bare_metal_version' is not defined`. ```bash $ pip install -r requirements/dev.txt ... Collecting mamba-ssm==2.2.4 (from -r /home/dxia/src/github.com/vllm-project/vllm/requirements/test.txt (line 273)) Downloading mamba_ssm-2.2.4.tar.gz (91 kB) Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> [26 lines of output] /tmp/pip-build-env-w7l3g7ku/overlay/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:275: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/cs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: https://docs.vllm.ai/en/latest/contributing/overview.html#testing, `pip install -r requirements/dev.txt` tries to install [mamba-ssm](https://github.com/vllm-project/vllm/blob/d41faaf9df6d1a741d5fdd4a282b16783cace888/re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: #testing, `pip install -r requirements/dev.txt` tries to install [mamba-ssm](https://github.com/vllm-project/vllm/blob/d41faaf9df6d1a741d5fdd4a282b16783cace888/requirements/test.txt#L273) whose [requirements are stated...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: te requirements for testing or update to work for CPU-only documentation;stale ### 📚 The doc issue On https://docs.vllm.ai/en/latest/contributing/overview.html#testing, `pip install -r requirements/dev.txt` tries to ins...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ess.py", line 143, in get_requires_for_build_wheel return hook(config_settings) ^^^^^^^^^^^^^^^^^^^^^ File "/tmp/pip-build-env-w7l3g7ku/overlay/lib/python3.12/site-packages/setuptools/build_meta.py", line 331, in get_re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Doc]: state requirements for testing or update to work for CPU-only documentation;stale ### 📚 The doc issue On https://docs.vllm.ai/en/latest/contributing/overview.html#testing, `pip install -r requirements/dev.txt` tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
