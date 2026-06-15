# vllm-project/vllm#11178: [Bug]: ARM vLLM container build failing due to outlines v0.1.9

| 字段 | 值 |
| --- | --- |
| Issue | [#11178](https://github.com/vllm-project/vllm/issues/11178) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ARM vLLM container build failing due to outlines v0.1.9

### Issue 正文摘录

### Your current environment M2 Mac with Docker Desktop ### Model Input Dumps _No response_ ### 🐛 Describe the bug Building ARM vLLM Docker image with `docker build -f Dockerfile.arm -t vllm-cpu-env --shm-size=4g .` leads to the following error: ``` 24.95 copying python/outlines_core/fsm/regex.py -> build/lib.linux-aarch64-cpython-310/outlines_core/fsm 24.95 running build_ext 24.95 running build_rust 24.95 error: can't find Rust compiler 24.95 24.95 If you are using an outdated pip version, it is possible a prebuilt wheel is available for this package but pip is not able to install from it. Installing from the wheel would avoid the need for a Rust compiler. 24.95 24.95 To update pip, run: 24.95 24.95 pip install --upgrade pip 24.95 24.95 and then retry package installation. 24.95 24.95 If you did intend to build this package from source, try installing a Rust compiler from your system package manager and ensure it is on the PATH during installation. Alternatively, rustup (available at https://rustup.rs) is the recommended way to download and update the Rust compiler toolchain. 24.97 error: subprocess-exited-with-error 24.97 24.97 × Building wheel for outlines_core (pyproject.toml)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: ARM vLLM container build failing due to outlines v0.1.9 bug ### Your current environment M2 Mac with Docker Desktop ### Model Input Dumps _No response_ ### 🐛 Describe the bug Building ARM vLLM Docker image with `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: leads to the following error: ``` 24.95 copying python/outlines_core/fsm/regex.py -> build/lib.linux-aarch64-cpython-310/outlines_core/fsm 24.95 running build_ext 24.95 running build_rust 24.95 error: can't find Rust co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: v0.1.9 bug ### Your current environment M2 Mac with Docker Desktop ### Model Input Dumps _No response_ ### 🐛 Describe the bug Building ARM vLLM Docker image with `docker build -f Dockerfile.arm -t vllm-cpu-env --shm-siz...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
