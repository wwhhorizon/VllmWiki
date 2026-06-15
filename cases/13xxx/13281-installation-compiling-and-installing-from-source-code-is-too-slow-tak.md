# vllm-project/vllm#13281: [Installation]: Compiling and installing from source code is too slow, taking at least 3 hours.

| 字段 | 值 |
| --- | --- |
| Issue | [#13281](https://github.com/vllm-project/vllm/issues/13281) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Compiling and installing from source code is too slow, taking at least 3 hours.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh cd vllm docker build --pull --build-arg torch_cuda_arch_list=9.0+PTX --build-arg max_jobs=32 --build-arg vllm_fa_cmake_gpu_arches=90-real -t vllm:0.7.2 --target vllm-base -f Dockerfile . ``` Compiling and installing from source code is too slow, taking at least 3 hours on A100. **How to speed up the compilation of vllm-flash-attn？** ![Image](https://github.com/user-attachments/assets/2f84aa90-a6c1-4294-a71f-3aed6c828b38) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Compiling and installing from source code is too slow, taking at least 3 hours. installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: re installing vllm ```sh cd vllm docker build --pull --build-arg torch_cuda_arch_list=9.0+PTX --build-arg max_jobs=32 --build-arg vllm_fa_cmake_gpu_arches=90-real -t vllm:0.7.2 --target vllm-base -f Dockerfile . ``` Com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
