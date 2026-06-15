# vllm-project/vllm#301: Can not run vllm with docker

| 字段 | 值 |
| --- | --- |
| Issue | [#301](https://github.com/vllm-project/vllm/issues/301) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can not run vllm with docker

### Issue 正文摘录

I'm trying to run this project with the following Dockerfile: ```Dockerfile FROM nvcr.io/nvidia/pytorch:22.12-py3 RUN pip uninstall torch -y WORKDIR /workspace COPY /inference/vllm /workspace/inference/vllm WORKDIR /workspace/inference/vllm RUN pip install -e . ENV PYTHONPATH=/workspace/inference/vllm EXPOSE 8000 CMD ["python", "-m", "vllm.entrypoints.openai.api_server", "--host", "0.0.0.0"] ``` My directory structure: ```bash (api) srikanth@instance-1:~/api/inference$ ls Dockerfile main.py vllm (api) srikanth@instance-1:~/api/inference$ ls vllm/ CONTRIBUTING.md MANIFEST.in benchmarks docs mypy.ini requirements-dev.txt setup.py vllm LICENSE README.md csrc examples pyproject.toml requirements.txt tests ``` However when i run this container, I get: ` /usr/bin/python: Error while finding module specification for 'vllm.entrypoints.openai.api_server' (ImportError: cannot import name 'activation_ops' from partially initialized module 'vllm' (most likely due to a circular import) (/workspace/inference/vllm/vllm/__init__.py))` Any help is appreciated :)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Can not run vllm with docker I'm trying to run this project with the following Dockerfile: ```Dockerfile FROM nvcr.io/nvidia/pytorch:22.12-py3 RUN pip uninstall torch -y WORKDIR /workspace COPY /inference/vllm /workspac...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: kanth@instance-1:~/api/inference$ ls vllm/ CONTRIBUTING.md MANIFEST.in benchmarks docs mypy.ini requirements-dev.txt setup.py vllm LICENSE README.md csrc examples pyproject.toml requirements.txt tests ``` However when i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
