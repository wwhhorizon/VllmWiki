# vllm-project/vllm#1597: Docker build fails due to CUDA version mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#1597](https://github.com/vllm-project/vllm/issues/1597) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Docker build fails due to CUDA version mismatch

### Issue 正文摘录

I attempted to build vllm with docker, using this command: ``` docker build -t vllm-v0.2.1-8efe23f . ``` But it fails like this: ``` ------ > [build 6/6] RUN python3 setup.py build_ext --inplace: 2.168 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' 2.192 running build_ext 2.229 Traceback (most recent call last): 2.229 File "/workspace/setup.py", line 257, in 2.229 setuptools.setup( 2.229 File "/usr/lib/python3/dist-packages/setuptools/__init__.py", line 153, in setup 2.229 return distutils.core.setup(**attrs) 2.229 File "/usr/lib/python3.10/distutils/core.py", line 148, in setup 2.229 dist.run_commands() 2.229 File "/usr/lib/python3.10/distutils/dist.py", line 966, in run_commands 2.229 self.run_command(cmd) 2.229 File "/usr/lib/python3.10/distutils/dist.py", line 985, in run_command 2.229 cmd_obj.run() 2.229 File "/usr/lib/python3/dist-packages/setuptools/command/build_ext.py", line 79, in run 2.230 _build_ext.run(self) 2.230 File "/usr/lib/python3.10/distutils/command/build_ext.py", line 340, in run 2.230 self.build_extensions() 2.230 File "/usr/local/lib/python3.10/dist-packages/torch/utils/cpp_extension.py", line 525, in build_extensions 2.230 _check_cuda_version(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Docker build fails due to CUDA version mismatch I attempted to build vllm with docker, using this command: ``` docker build -t vllm-v0.2.1-8efe23f . ``` But it fails like this: ``` ------ > [build 6/6] RUN python3 se
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Docker build fails due to CUDA version mismatch I attempted to build vllm with docker, using this command: ``` docker build -t vllm-v0.2.1-8efe23f . ``` But it fails like this: ``` ------ > [build 6/6] RUN python3 setup...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Docker build fails due to CUDA version mismatch I attempted to build vllm with docker, using this command: ``` docker build -t vllm-v0.2.1-8efe23f . ``` But it fails like this: ``` ------ > [build 6/6] RUN python3 setup...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n _check_cuda_version 2.230 raise RuntimeError(CUDA_MISMATCH_MESSAGE.format(cuda_str_version, torch.version.cuda)) 2.230 RuntimeError: 2.230 The detected CUDA version (11.8) mismatches the version that was used to compi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: uld there be a mismatch with the current dockerfile? Is this build being tested with CI? correctness ci_build cuda build_error;crash;mismatch env_dependency I attempted to build vllm with docker, using this command:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
