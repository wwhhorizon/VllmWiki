# vllm-project/vllm#12178: [Bug]: AMD GPU docker image build No matching distribution found for torch==2.6.0.dev20241113+rocm6.2

| 字段 | 值 |
| --- | --- |
| Issue | [#12178](https://github.com/vllm-project/vllm/issues/12178) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AMD GPU docker image build No matching distribution found for torch==2.6.0.dev20241113+rocm6.2

### Issue 正文摘录

### Your current environment Archlinux 13th Gen Intel(R) Core(TM) i9-13900HX environment to build the docker image ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to build the AMD GPU docker image: ``` git checkout v0.6.6.post1 DOCKER_BUILDKIT=1 docker build -f Dockerfile.rocm -t substratusai/vllm-rocm:v0.6.6.post1 . ``` Results in following error: ``` 1.147 Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/nightly/rocm6.2 1.717 ERROR: Could not find a version that satisfies the requirement torch==2.6.0.dev20241113+rocm6.2 (from versions: 1.7.1, 1.8.0, 1.8.1, 1.9.0, 1.9.1, 1.10.0, 1.10.1, 1.10.2, 1.11.0, 1.12.0, 1.12.1, 1.13.0, 1.13.1, 2.0.0, 2.0.1, 2.1.0, 2.1.1, 2.1.2, 2.2.0, 2.2.1, 2.2.2, 2.3.0, 2.3.1, 2.4.0, 2.4.1, 2.5.0, 2.5.1, 2.6.0.dev20241119+rocm6.2, 2.6.0.dev20241120+rocm6.2, 2.6.0.dev20241121+rocm6.2, 2.6.0.dev20241122+rocm6.2) 2.135 ERROR: No matching distribution found for torch==2.6.0.dev20241113+rocm6.2 ------ Dockerfile.rocm:49 -------------------- 48 | # Install torch == 2.6.0 on ROCm 49 | >>> RUN --mount=type=cache,target=/root/.cache/pip \ 50 | >>> case "$(ls /opt | grep -Po 'rocm-[0-9]\.[0-9]')" in \ 51 | >>> *"rocm-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: AMD GPU docker image build No matching distribution found for torch==2.6.0.dev20241113+rocm6.2 bug;rocm ### Your current environment Archlinux 13th Gen Intel(R) Core(TM) i9-13900HX environment to build the docker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: image build No matching distribution found for torch==2.6.0.dev20241113+rocm6.2 bug;rocm ### Your current environment Archlinux 13th Gen Intel(R) Core(TM) i9-13900HX environment to build the docker image ### Model Input...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Intel(R) Core(TM) i9-13900HX environment to build the docker image ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to build the AMD GPU docker image: ``` git checkout v0.6.6.post1 DOCKER_BUILDKIT=1 doc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
