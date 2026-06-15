# vllm-project/vllm#2021: ARM aarch-64 server build failed (host OS: Ubuntu22.04.3) 

| 字段 | 值 |
| --- | --- |
| Issue | [#2021](https://github.com/vllm-project/vllm/issues/2021) |
| 状态 | closed |
| 标签 |  |
| 评论 | 55; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ARM aarch-64 server build failed (host OS: Ubuntu22.04.3) 

### Issue 正文摘录

do as: https://docs.vllm.ai/en/latest/getting_started/installation.html 1. docker run --gpus all -it --rm --ipc=host nvcr.io/nvidia/pytorch:23.10-py3 2. git clone https://github.com/vllm-project/vllm.git 3. cd vllm 4. pip install -e . here is the details in side the docker instance: root@f8c2e06fbf8b:/mnt/vllm# pip install -e . Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com Obtaining file:///mnt/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [22 lines of output] /tmp/pip-build-env-4xoxai9j/overlay/local/lib/python3.10/dist-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' :142: UserWarning: Unsupported CUDA/ROCM architectures ({'6.1', '7.2', '8.7', '5.2...

## 现有链接修复摘要

#10499 [CI/Build] Dockerfile build for ARM64 / GH200 | #41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ARM aarch-64 server build failed (host OS: Ubuntu22.04.3) do as: https://docs.vllm.ai/en/latest/getting_started/installation.html 1. docker run --gpus all -it --rm --ipc=host nvcr.io/nvidia/pytorch:23.10-py3 2. git clon...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ARM aarch-64 server build failed (host OS: Ubuntu22.04.3) do as: https://docs.vllm.ai/en/latest/getting_started/installation.html 1. docker run --gpus all -it --rm --ipc=host nvcr.io/nvidia/pytorch:23.10-py3 2. git clon...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ///mnt/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 132, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-4xoxai9j/overlay/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 441, in get_requires_for_build...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: build failed (host OS: Ubuntu22.04.3) do as: https://docs.vllm.ai/en/latest/getting_started/installation.html 1. docker run --gpus all -it --rm --ipc=host nvcr.io/nvidia/pytorch:23.10-py3 2. git clone https://github.com...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10499](https://github.com/vllm-project/vllm/pull/10499) | closes_keyword | 0.95 | [CI/Build] Dockerfile build for ARM64 / GH200 | FIX #2021 ### Changes Overview: - Added an additional `requirements-cuda-arm64.txt` that uses the pytorch nightly modules that are compatible with ARM64+CUDA. This is temporary u |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 140 updates | fix: use uvx --with cairosvg instead of uv pip install --system (<a href="https://redirect.github.com/huggingface/tokenizers/issues/2021">#2021</a>)</li> <li><a href="https://githu |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 141 updates | fix: use uvx --with cairosvg instead of uv pip install --system (<a href="https://redirect.github.com/huggingface/tokenizers/issues/2021">#2021</a>)</li> <li><a href="https://githu |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 141 updates | fix: use uvx --with cairosvg instead of uv pip install --system (<a href="https://redirect.github.com/huggingface/tokenizers/issues/2021">#2021</a>)</li> <li><a href="https://githu |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 142 updates | fix: use uvx --with cairosvg instead of uv pip install --system (<a href="https://redirect.github.com/huggingface/tokenizers/issues/2021">#2021</a>)</li> <li><a href="https://githu |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 143 updates | fix: use uvx --with cairosvg instead of uv pip install --system (<a href="https://redirect.github.com/huggingface/tokenizers/issues/2021">#2021</a>)</li> <li><a href="https://githu |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 145 updates | fix: use uvx --with cairosvg instead of uv pip install --system (<a href="https://redirect.github.com/huggingface/tokenizers/issues/2021">#2021</a>)</li> <li><a href="https://githu |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 147 updates | fix: use uvx --with cairosvg instead of uv pip install --system (<a href="https://redirect.github.com/huggingface/tokenizers/issues/2021">#2021</a>)</li> <li><a href="https://githu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
