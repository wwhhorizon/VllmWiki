# vllm-project/vllm#1831: ValueError: setuptools>=49.4.0 is required when build docker

| 字段 | 值 |
| --- | --- |
| Issue | [#1831](https://github.com/vllm-project/vllm/issues/1831) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
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

> ValueError: setuptools>=49.4.0 is required when build docker

### Issue 正文摘录

docker build -t vllm:main . ``` => CACHED [build 3/6] COPY requirements.txt requirements.txt 0.0s => CACHED [build 4/6] COPY pyproject.toml pyproject.toml 0.0s => CACHED [build 5/6] COPY vllm/__init__.py vllm/__init__.py 0.0s => ERROR [build 6/6] RUN python3 setup.py build_ext --inplace 5.5s ------ > [build 6/6] RUN python3 setup.py build_ext --inplace: #0 4.323 running build_ext #0 4.462 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' #0 4.464 Traceback (most recent call last): #0 4.464 File "setup.py", line 208, in #0 4.464 setuptools.setup( #0 4.464 File "/usr/lib/python3/dist-packages/setuptools/__init__.py", line 144, in setup #0 4.464 return distutils.core.setup(**attrs) #0 4.464 File "/usr/lib/python3.8/distutils/core.py", line 148, in setup #0 4.464 dist.run_commands() #0 4.464 File "/usr/lib/python3.8/distutils/dist.py", line 966, in run_commands #0 4.464 self.run_command(cmd) #0 4.464 File "/usr/lib/python3.8/distutils/dist.py", line 985, in run_command #0 4.464 cmd_obj.run() #0 4.464 File "/usr/lib/python3/dist-packages/setuptools/command/build_ext.py", line 87, in run #0 4.464 _build_ext.run(self) #0 4.464 File "/usr/lib/python3.8/distutils/command/build_ex...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ValueError: setuptools>=49.4.0 is required when build docker docker build -t vllm:main . ``` => CACHED [build 3/6] COPY requirements.txt requirements.txt 0.0s => CACHED [build 4/
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: #0 4.462 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' #0 4.464 Traceback (most recent call last):

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
